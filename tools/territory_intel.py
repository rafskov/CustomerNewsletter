#!/usr/bin/env python3
"""
Territory Intelligence Pipeline

Loads sales data exports, applies bot detection, corrected scoring,
revenue trend analysis, PR adoption mapping, and full-book adoption
gap analysis. Outputs a structured JSON artifact and a markdown briefing.

Usage:
    python territory_intel.py \\
        --prospects   ~/Downloads/Prospects.csv \\
        --copilot-rev ~/Downloads/CopilotRevenue.csv \\
        --actions-rev ~/Downloads/ActionsRevenue.csv \\
        --pr-data     ~/Downloads/PRData.csv \\
        --book        ~/Downloads/SuperSummary.csv \\
        --output-dir  ~/Documents/Projects/

All flags are optional. The script processes whichever files are provided.
"""

import argparse
import csv
import json
import os
import sys
from collections import defaultdict
from datetime import datetime, timedelta

NOW = datetime.utcnow()

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def num(val):
    """Parse a string like '$6,861' or '35.5%' into a float."""
    if not val:
        return 0.0
    v = val.replace('$', '').replace(',', '').replace('%', '').strip()
    try:
        return float(v)
    except ValueError:
        return 0.0


def parse_ts(ts):
    """Parse 'YYYY-MM-DD HH:MM:SS UTC' into a datetime, or None."""
    if not ts:
        return None
    try:
        return datetime.strptime(ts.strip()[:19], '%Y-%m-%d %H:%M:%S')
    except (ValueError, IndexError):
        return None


def days_ago(dt):
    """Return how many days ago a datetime was, or None."""
    if not dt:
        return None
    return (NOW - dt).total_seconds() / 86400


# ---------------------------------------------------------------------------
# Step 1: Load & score prospects (bot detection + corrected scoring)
# ---------------------------------------------------------------------------

def load_prospects(path):
    prospects = []
    with open(path, 'r', encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):
            touched = parse_ts(row.get('Touched At', ''))
            engaged = parse_ts(row.get('Engaged At', ''))
            raw_score = num(row.get('Engaged Score', ''))

            delta = None
            is_bot = False
            bot_reason = ''
            if touched and engaged:
                delta = abs((engaged - touched).total_seconds())
                if delta <= 10:
                    is_bot = True
                    bot_reason = f'engaged {delta:.0f}s after touch'

            recency = days_ago(engaged)
            stage = row.get('Stage Name', '') or ''

            # Corrected score
            if is_bot:
                corrected = 0.0
            else:
                decay = 1.0 / (1.0 + ((recency or 365) / 30.0))
                stage_bonus = (
                    3.0 if stage in ('Working', 'Qualified') else
                    1.5 if stage == 'Contacted' else 0.0
                )
                phone = row.get('Work Phone', '') or row.get('Mobile Phone', '')
                phone_bonus = 0.5 if phone else 0.0
                corrected = raw_score * decay + stage_bonus + phone_bonus

            prospects.append({
                'name': f"{row.get('First Name', '')} {row.get('Last Name', '')}".strip(),
                'title': row.get('Title', '') or '',
                'company': row.get('Company', '') or '',
                'email': row.get('Email', '') or '',
                'phone': row.get('Work Phone', '') or row.get('Mobile Phone', '') or '',
                'linkedin': row.get('LinkedIn', '') or '',
                'stage': stage,
                'raw_score': raw_score,
                'corrected_score': round(corrected, 2),
                'is_bot': is_bot,
                'bot_reason': bot_reason,
                'delta_seconds': delta,
                'touched_at': row.get('Touched At', ''),
                'engaged_at': row.get('Engaged At', ''),
                'finished_sequences': row.get('Finished Sequences', ''),
                'active_sequences': row.get('Active Sequences', ''),
                'tags': row.get('Tags', ''),
                'company_size': row.get('Company Size', ''),
                'company_industry': row.get('Company Industry', ''),
            })
    return prospects


# ---------------------------------------------------------------------------
# Step 2: Revenue trends (Copilot and/or Actions)
# ---------------------------------------------------------------------------

def load_revenue(path):
    """Return {account_name: {month: amount}}."""
    rev = defaultdict(lambda: defaultdict(float))
    with open(path, 'r', encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):
            name = row.get('name', '').strip()
            amt = num(row.get('charge_amt', ''))
            month = (row.get('date_month', '') or '')[:7]
            if name and month:
                rev[name][month] = amt
    return dict(rev)


def compute_revenue_trends(rev):
    """For each account, compute latest, prev, delta, growth streak."""
    trends = {}
    for name, months in rev.items():
        s = sorted(months.keys())
        latest_m = s[-1]
        latest_v = months[latest_m]
        prev_v = months[s[-2]] if len(s) >= 2 else 0
        delta = latest_v - prev_v
        pct = ((delta / prev_v) * 100) if prev_v > 0 else (100 if delta > 0 else 0)

        streak = 0
        for i in range(len(s) - 1, 0, -1):
            if months[s[i]] > months[s[i - 1]]:
                streak += 1
            else:
                break

        trends[name] = {
            'latest_month': latest_m,
            'latest': round(latest_v, 2),
            'previous': round(prev_v, 2),
            'delta': round(delta, 2),
            'pct_change': round(pct, 1),
            'growth_streak': streak,
            'months_active': len(s),
            'first_month': s[0],
        }
    return trends


# ---------------------------------------------------------------------------
# Step 3: PR / Code Review adoption
# ---------------------------------------------------------------------------

def load_pr_data(path):
    orgs = defaultdict(lambda: defaultdict(dict))
    with open(path, 'r', encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):
            acct = row.get('Salesforce Account Name', '').strip()
            org = row.get('Organization Name', '').strip()
            month = (row.get('Month', '') or '')[:7]
            total = int(num(row.get('No. of Pull Requests', '0')))
            with_cr = int(num(row.get('No. of Pull Requests with Copilot Code Review', '0')))
            users = int(num(row.get('No. of Users Receiving Reviews from Copilot Code Review', '0')))
            key = f"{acct}|{org}"
            orgs[key][month] = {
                'total_prs': total,
                'with_copilot': with_cr,
                'users': users,
                'ratio': round((with_cr / total * 100), 1) if total > 0 else 0,
            }
    # Aggregate to account level
    accounts = defaultdict(lambda: {'total_prs': 0, 'with_copilot': 0, 'users': 0})
    for key, months in orgs.items():
        acct = key.split('|')[0]
        latest = sorted(months.keys())[-1]
        d = months[latest]
        accounts[acct]['total_prs'] += d['total_prs']
        accounts[acct]['with_copilot'] += d['with_copilot']
        accounts[acct]['users'] += d['users']
    for acct in accounts:
        a = accounts[acct]
        a['ratio'] = round((a['with_copilot'] / a['total_prs'] * 100), 1) if a['total_prs'] > 0 else 0
    return dict(accounts)


# ---------------------------------------------------------------------------
# Step 4: Full book (Super Summary)
# ---------------------------------------------------------------------------

def load_book(path):
    accounts = []
    with open(path, 'r', encoding='utf-8-sig') as f:
        for row in csv.DictReader(f):
            renewal = (row.get('Next Renewal Date (GH)', '') or '')[:10]
            days_to_renewal = None
            if renewal:
                try:
                    rd = datetime.strptime(renewal, '%Y-%m-%d')
                    days_to_renewal = (rd - NOW).days
                except ValueError:
                    pass

            ghe = num(row.get('Total GHE Seats (Vol and Metered)', ''))
            cfb = num(row.get('Current CfB Seats (incl. CE & CS)', ''))
            ghas = num(row.get('GHAS total volume and metered', ''))

            accounts.append({
                'name': row.get('salesforce_name', '').strip(),
                'owner': row.get('Account Owner', '').strip(),
                'arr': num(row.get('Total ARR (Vol + Metered)', '')),
                'ghe_seats': ghe,
                'teams_seats': num(row.get('# Teams seats', '')),
                'cfb_seats': cfb,
                'cfb_30d_change': num(row.get('30D CfB +/-', '')),
                'cfb_potential': num(row.get('GHE/VS to CfB Potential', '')),
                'cfb_penetration': row.get('CfB Penetration vs GHE+VS', '').strip(),
                'active_committers': num(row.get('Active Committers L90d (Cloud Users)', '')),
                'ghas_total': ghas,
                'ghas_90d_change': num(row.get('L90d GHAS Seats +/-', '')),
                'ghazdo_seats': num(row.get('GHAzDO Seats', '')),
                'consumption': num(row.get('LM Consumption $', '')),
                'renewal_date': renewal,
                'days_to_renewal': days_to_renewal,
                'cfb_attach_pct': round((cfb / ghe * 100), 1) if ghe > 0 else 0,
                'ghas_attach_pct': round((ghas / ghe * 100), 1) if ghe > 0 else 0,
            })
    return accounts


# ---------------------------------------------------------------------------
# Step 5: Multi-threading / persona mapping
# ---------------------------------------------------------------------------

PERSONA_RULES = [
    (['ceo', 'cto', 'cio', 'ciso', 'chief', 'president', 'evp', 'vp ', 'vice president'], 'Economic Buyer'),
    (['director', 'head of', 'principal', 'fellow', 'distinguished'], 'Technical Champion'),
    (['security', 'secops', 'devsecops', 'appsec', 'infosec'], 'Security'),
    (['devops', 'platform', 'sre', 'reliability', 'infrastructure'], 'DevOps/Platform'),
    (['manager', 'lead', 'architect', 'staff'], 'Manager/Lead'),
]


def classify_persona(title):
    if not title:
        return 'Unknown'
    t = title.lower()
    for keywords, persona in PERSONA_RULES:
        if any(k in t for k in keywords):
            return persona
    return 'IC'


def build_threading_map(prospects):
    companies = defaultdict(lambda: defaultdict(int))
    for p in prospects:
        if p['is_bot'] or not p['company']:
            continue
        persona = classify_persona(p['title'])
        companies[p['company']][persona] += 1

    results = {}
    for co, personas in companies.items():
        total = sum(personas.values())
        if total < 3:
            continue
        gaps = []
        if not personas.get('Economic Buyer'):
            gaps.append('VP Eng / CTO')
        if not personas.get('Technical Champion'):
            gaps.append('Director / Head of Eng')
        if not personas.get('Security'):
            gaps.append('CISO / Security Lead')
        if not personas.get('DevOps/Platform'):
            gaps.append('DevOps Mgr / Platform Eng')
        results[co] = {
            'total_contacts': total,
            'personas': dict(personas),
            'gaps': gaps,
            'full_coverage': len(gaps) == 0,
        }
    return results


# ---------------------------------------------------------------------------
# Step 6: Sequence effectiveness
# ---------------------------------------------------------------------------

def analyze_sequences(prospects):
    seq_stats = defaultdict(lambda: {
        'total': 0, 'no_response': 0, 'contacted': 0, 'working': 0,
        'qualified': 0, 'real_engaged': 0, 'bot_engaged': 0,
        'total_corrected_score': 0,
    })

    for p in prospects:
        finished = p.get('finished_sequences', '')
        if not finished:
            continue
        for seq in (s.strip() for s in finished.split(',') if s.strip()):
            s = seq_stats[seq]
            s['total'] += 1
            stage = p['stage'].lower()
            if 'no response' in stage:
                s['no_response'] += 1
            elif 'contacted' in stage:
                s['contacted'] += 1
            elif 'working' in stage:
                s['working'] += 1
            elif 'qualified' in stage:
                s['qualified'] += 1
            if p['raw_score'] > 0:
                if p['is_bot']:
                    s['bot_engaged'] += 1
                else:
                    s['real_engaged'] += 1
            s['total_corrected_score'] += p['corrected_score']

    results = {}
    for seq, s in seq_stats.items():
        if s['total'] < 5:
            continue
        advanced = s['contacted'] + s['working'] + s['qualified']
        results[seq] = {
            **s,
            'advance_pct': round((advanced / s['total'] * 100), 1) if s['total'] > 0 else 0,
            'avg_score': round(s['total_corrected_score'] / s['total'], 2) if s['total'] > 0 else 0,
        }
    return results


# ---------------------------------------------------------------------------
# Step 7: Combine into account scorecard
# ---------------------------------------------------------------------------

def build_account_scorecard(book, copilot_trends, actions_trends, pr_data, threading, prospects):
    """Cross-reference all signals into a single account-level scorecard."""
    # Index prospects by company
    prospect_index = defaultdict(list)
    for p in prospects:
        if not p['is_bot'] and p['company']:
            prospect_index[p['company']].append(p)

    def fuzzy_match(name, index):
        """Simple first-word match against a dict."""
        token = name.lower().split()[0] if name else ''
        if len(token) < 4:
            return None
        for key in index:
            if token in key.lower():
                return index[key]
        return None

    scorecards = []
    for acct in book:
        name = acct['name']

        # Revenue signals
        cp_trend = fuzzy_match(name, copilot_trends)
        ac_trend = fuzzy_match(name, actions_trends)

        # PR data
        pr = None
        for pr_name, pr_val in (pr_data or {}).items():
            if name.lower().split()[0] in pr_name.lower():
                pr = pr_val
                break

        # Threading
        thread = None
        for co, th in (threading or {}).items():
            if name.lower().split()[0] in co.lower():
                thread = th
                break

        # Contacts
        contacts = []
        for co, plist in prospect_index.items():
            if name.lower().split()[0] in co.lower():
                contacts = plist
                break

        engaged_contacts = [c for c in contacts if c['corrected_score'] > 0]
        best_contact = max(contacts, key=lambda c: c['corrected_score']) if contacts else None

        # Build flags
        flags = []
        if acct['days_to_renewal'] is not None and 0 <= acct['days_to_renewal'] <= 90:
            flags.append(f"RENEWAL in {acct['days_to_renewal']}d")
        if acct['cfb_seats'] == 0 and acct['ghe_seats'] > 20:
            flags.append('NO COPILOT')
        elif acct['cfb_attach_pct'] < 20 and acct['ghe_seats'] > 50:
            flags.append(f"CfB low ({acct['cfb_attach_pct']:.0f}%)")
        if acct['cfb_30d_change'] < -5:
            flags.append(f"CfB shrinking ({acct['cfb_30d_change']:+.0f})")
        if acct['cfb_30d_change'] > 10:
            flags.append(f"CfB growing ({acct['cfb_30d_change']:+.0f})")
        if acct['ghas_total'] == 0 and acct['ghe_seats'] > 20:
            flags.append('NO GHAS')
        if acct['ghas_90d_change'] < -10:
            flags.append(f"GHAS shrinking ({acct['ghas_90d_change']:+.0f})")
        if acct['ghas_90d_change'] > 10:
            flags.append(f"GHAS growing ({acct['ghas_90d_change']:+.0f})")
        if acct['teams_seats'] > 0 and acct['ghe_seats'] == 0:
            flags.append('TEAMS ONLY')
        if not contacts:
            flags.append('NO CONTACTS')
        if cp_trend and cp_trend['delta'] < -200:
            flags.append(f"Rev declining (${cp_trend['delta']:+,.0f}/mo)")
        if pr and pr['total_prs'] > 500 and pr['ratio'] < 5:
            flags.append(f"Low CR ({pr['ratio']}% of {pr['total_prs']} PRs)")
        if thread and not thread['full_coverage']:
            flags.append(f"Persona gaps: {', '.join(thread['gaps'][:2])}")

        scorecards.append({
            'name': name,
            'arr': acct['arr'],
            'ghe_seats': acct['ghe_seats'],
            'cfb_seats': acct['cfb_seats'],
            'cfb_attach_pct': acct['cfb_attach_pct'],
            'cfb_30d_change': acct['cfb_30d_change'],
            'cfb_potential': acct['cfb_potential'],
            'ghas_total': acct['ghas_total'],
            'ghas_90d_change': acct['ghas_90d_change'],
            'teams_seats': acct['teams_seats'],
            'renewal_date': acct['renewal_date'],
            'days_to_renewal': acct['days_to_renewal'],
            'copilot_rev_trend': cp_trend,
            'actions_rev_trend': ac_trend,
            'pr_adoption': pr,
            'threading': thread,
            'contact_count': len(contacts),
            'engaged_count': len(engaged_contacts),
            'best_contact': {
                'name': best_contact['name'],
                'title': best_contact['title'],
                'score': best_contact['corrected_score'],
                'stage': best_contact['stage'],
            } if best_contact else None,
            'flags': flags,
            'flag_count': len(flags),
        })

    scorecards.sort(key=lambda x: (-x['flag_count'], -x['arr']))
    return scorecards


# ---------------------------------------------------------------------------
# Output: Markdown briefing
# ---------------------------------------------------------------------------

def generate_briefing(scorecards, book, sequences, output_dir):
    date_str = NOW.strftime('%Y-%m-%d')

    # Book-level aggregates
    total_arr = sum(a['arr'] for a in book)
    total_ghe = sum(a['ghe_seats'] for a in book)
    total_cfb = sum(a['cfb_seats'] for a in book)
    total_ghas = sum(a['ghas_total'] for a in book)
    total_teams = sum(a['teams_seats'] for a in book)
    cfb_potential = sum(a['cfb_potential'] for a in book)

    lines = [
        f'# Territory Intelligence Briefing — {date_str}',
        '',
        '## Book Snapshot',
        '',
        f'| Metric | Value |',
        f'|--------|-------|',
        f'| Accounts | {len(book)} |',
        f'| Total ARR | ${total_arr:,.0f} |',
        f'| GHE Seats | {total_ghe:,.0f} |',
        f'| Copilot Seats | {total_cfb:,.0f} ({total_cfb/total_ghe*100:.0f}% attach) |' if total_ghe else f'| Copilot Seats | {total_cfb:,.0f} |',
        f'| Copilot Whitespace | {cfb_potential:,.0f} seats |',
        f'| GHAS Seats | {total_ghas:,.0f} ({total_ghas/total_ghe*100:.0f}% attach) |' if total_ghe else f'| GHAS Seats | {total_ghas:,.0f} |',
        f'| Teams Seats | {total_teams:,.0f} |',
        '',
        '---',
        '',
        '## Priority Accounts (most flags)',
        '',
    ]

    for sc in scorecards[:15]:
        lines.append(f"### {sc['name']} — ${sc['arr']:,.0f} ARR")
        lines.append(f"- **GHE:** {sc['ghe_seats']:.0f}  **CfB:** {sc['cfb_seats']:.0f} ({sc['cfb_attach_pct']:.0f}%, {sc['cfb_30d_change']:+.0f} 30d)  **GHAS:** {sc['ghas_total']:.0f} ({sc['ghas_90d_change']:+.0f} 90d)")
        if sc['renewal_date']:
            lines.append(f"- **Renewal:** {sc['renewal_date']} ({sc['days_to_renewal']}d)")
        if sc['best_contact']:
            bc = sc['best_contact']
            lines.append(f"- **Best contact:** {bc['name']} ({bc['title']}) — score {bc['score']}, {bc['stage']}")
        elif 'NO CONTACTS' in sc['flags']:
            lines.append('- **Contacts:** ⚠️ NONE in Outreach')
        if sc['pr_adoption']:
            pr = sc['pr_adoption']
            lines.append(f"- **PRs:** {pr['total_prs']:,}/mo, {pr['ratio']}% Code Review, {pr['users']} users")
        lines.append(f"- **Flags:** {' | '.join(sc['flags'])}")
        lines.append('')

    # Renewals
    renewals = [sc for sc in scorecards if sc['days_to_renewal'] is not None and 0 <= sc['days_to_renewal'] <= 90]
    renewals.sort(key=lambda x: x['days_to_renewal'])
    if renewals:
        lines += ['---', '', '## Upcoming Renewals (90 days)', '',
                   '| Account | Days | ARR | CfB% | GHAS | Flags |',
                   '|---------|------|-----|------|------|-------|']
        for r in renewals:
            lines.append(f"| {r['name'][:30]} | {r['days_to_renewal']} | ${r['arr']:,.0f} | {r['cfb_attach_pct']:.0f}% | {r['ghas_total']:.0f} | {', '.join(r['flags'][:3])} |")
        lines.append('')

    # Copilot whitespace
    ws = [sc for sc in scorecards if sc['cfb_potential'] > 20]
    ws.sort(key=lambda x: -x['cfb_potential'])
    if ws:
        lines += ['---', '', '## Copilot Whitespace (top 15)', '',
                   '| Account | Open Seats | Current | GHE | Attach% | ARR |',
                   '|---------|-----------|---------|-----|---------|-----|']
        for w in ws[:15]:
            lines.append(f"| {w['name'][:30]} | {w['cfb_potential']:.0f} | {w['cfb_seats']:.0f} | {w['ghe_seats']:.0f} | {w['cfb_attach_pct']:.0f}% | ${w['arr']:,.0f} |")
        lines.append('')

    # Sequences
    if sequences:
        top = sorted(sequences.items(), key=lambda x: -x[1]['advance_pct'])[:10]
        bottom = sorted(sequences.items(), key=lambda x: x[1]['advance_pct'])[:10]
        lines += ['---', '', '## Sequence Effectiveness', '',
                   '### Top performers', '',
                   '| Sequence | n | Advance% | Avg Score |',
                   '|----------|---|----------|-----------|']
        for name, s in top:
            lines.append(f"| {name[:45]} | {s['total']} | {s['advance_pct']}% | {s['avg_score']} |")
        lines += ['', '### Underperformers', '',
                   '| Sequence | n | Advance% | Bot Engaged |',
                   '|----------|---|----------|-------------|']
        for name, s in bottom:
            if s['advance_pct'] < 10:
                lines.append(f"| {name[:45]} | {s['total']} | {s['advance_pct']}% | {s['bot_engaged']} |")
        lines.append('')

    lines += ['---', '', f'*Generated {date_str} by territory_intel.py*', '']

    md_path = os.path.join(output_dir, f'territory_briefing_{date_str}.md')
    with open(md_path, 'w') as f:
        f.write('\n'.join(lines))
    return md_path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='Territory Intelligence Pipeline')
    parser.add_argument('--prospects', help='Outreach prospects CSV')
    parser.add_argument('--copilot-rev', help='Copilot billed revenue CSV')
    parser.add_argument('--actions-rev', help='Actions billed revenue CSV')
    parser.add_argument('--pr-data', help='PR / Code Review adoption CSV')
    parser.add_argument('--book', help='Super Summary (full book) CSV')
    parser.add_argument('--output-dir', default='.', help='Output directory')
    args = parser.parse_args()

    date_str = NOW.strftime('%Y-%m-%d')
    os.makedirs(args.output_dir, exist_ok=True)

    result = {'generated': date_str, 'sources': []}

    # --- Prospects ---
    prospects = []
    sequences = {}
    threading = {}
    if args.prospects:
        print(f'Loading prospects from {args.prospects}...')
        prospects = load_prospects(args.prospects)
        total = len(prospects)
        bots = sum(1 for p in prospects if p['is_bot'])
        engaged = sum(1 for p in prospects if p['raw_score'] > 0 and not p['is_bot'])
        print(f'  {total} prospects, {bots} bots filtered, {engaged} genuinely engaged')
        result['sources'].append('prospects')
        result['prospect_summary'] = {
            'total': total, 'bots_filtered': bots, 'genuinely_engaged': engaged,
        }
        sequences = analyze_sequences(prospects)
        threading = build_threading_map(prospects)

    # --- Revenue ---
    copilot_trends = {}
    actions_trends = {}
    if args.copilot_rev:
        print(f'Loading Copilot revenue from {args.copilot_rev}...')
        copilot_trends = compute_revenue_trends(load_revenue(args.copilot_rev))
        result['sources'].append('copilot_revenue')
        growing = sum(1 for t in copilot_trends.values() if t['delta'] > 0)
        declining = sum(1 for t in copilot_trends.values() if t['delta'] < 0)
        print(f'  {len(copilot_trends)} accounts: {growing} growing, {declining} declining')

    if args.actions_rev:
        print(f'Loading Actions revenue from {args.actions_rev}...')
        actions_trends = compute_revenue_trends(load_revenue(args.actions_rev))
        result['sources'].append('actions_revenue')
        print(f'  {len(actions_trends)} accounts')

    # --- PR Data ---
    pr_data = {}
    if args.pr_data:
        print(f'Loading PR data from {args.pr_data}...')
        pr_data = load_pr_data(args.pr_data)
        result['sources'].append('pr_data')
        low_adoption = sum(1 for p in pr_data.values() if p['ratio'] < 5 and p['total_prs'] > 100)
        print(f'  {len(pr_data)} accounts, {low_adoption} with <5% Code Review adoption')

    # --- Book ---
    book = []
    scorecards = []
    if args.book:
        print(f'Loading book from {args.book}...')
        book = load_book(args.book)
        result['sources'].append('book')
        total_arr = sum(a['arr'] for a in book)
        print(f'  {len(book)} accounts, ${total_arr:,.0f} total ARR')

        # Build combined scorecard
        scorecards = build_account_scorecard(
            book, copilot_trends, actions_trends, pr_data, threading, prospects
        )

    # --- Output JSON ---
    result['scorecards'] = scorecards[:50]  # top 50 by flag count
    result['copilot_trends'] = copilot_trends
    result['actions_trends'] = actions_trends
    result['pr_adoption'] = pr_data
    result['threading'] = threading
    result['sequences'] = sequences

    json_path = os.path.join(args.output_dir, f'territory_intel_{date_str}.json')
    with open(json_path, 'w') as f:
        json.dump(result, f, indent=2, default=str)
    print(f'\nJSON artifact: {json_path}')

    # --- Output Markdown ---
    if book:
        md_path = generate_briefing(scorecards, book, sequences, args.output_dir)
        print(f'Markdown briefing: {md_path}')

    print('\nDone.')


if __name__ == '__main__':
    main()
