#!/usr/bin/env python3
"""
Extract ZEXTRAINCOME from a Daily Budget SQLite backup and produce a
patch JSON for importing into Pocket Ledger.

Usage:
    python3 extract_extra_incomes.py <sqlite_path>

Output:
    extra-incomes-patch.json  (distributions + daily child transactions)

Import via: Pocket Ledger → Settings → Import data (select the patch file)
"""

import sys
import json
import sqlite3
from datetime import datetime, timedelta

APPLE_EPOCH = datetime(2001, 1, 1)

def apple_ts(v):
    if v is None:
        return None
    try:
        dt = APPLE_EPOCH + timedelta(seconds=float(v))
        if dt.year > 4001:
            return '4001-01-01'
        return dt.strftime('%Y-%m-%d')
    except:
        return None

def date_range(start_str, end_str):
    """Yield ISO date strings from start to end inclusive."""
    start = datetime.strptime(start_str, '%Y-%m-%d')
    end   = datetime.strptime(end_str,   '%Y-%m-%d')
    d = start
    while d <= end:
        yield d.strftime('%Y-%m-%d')
        d += timedelta(days=1)

# Map new-backup ZCATEGORY Z_PK → Pocket Ledger income category ID
CAT_MAP = {
    10: 27,  # Bonus     → Pocket Ledger Bonus      (id=27)
    15: 13,  # ExtraIncome → Pocket Ledger Extra income (id=13)
    18: 20,  # Sale      → Pocket Ledger Sale       (id=20)
    27: 21,  # Investment→ Pocket Ledger Investment  (id=21)
    28: 14,  # Expenses  → Pocket Ledger Expenses reimbursement (id=14)
}

def main():
    sqlite_path = sys.argv[1] if len(sys.argv) > 1 else '../DailyBudgetBackup3.sqlite'
    conn = sqlite3.connect(sqlite_path)

    rows = conn.execute(
        'SELECT Z_PK, ZAMOUNT, ZDESC, ZSTARTDATE, ZENDDATE, ZCATEGORY '
        'FROM ZEXTRAINCOME ORDER BY ZSTARTDATE'
    ).fetchall()

    print(f'Found {len(rows)} extra income entries')

    distributions = []
    transactions  = []
    now_str = datetime.utcnow().isoformat() + 'Z'
    today   = datetime.utcnow().strftime('%Y-%m-%d')

    # Use IDs well above existing data to avoid collisions
    dist_id_base = 5000
    txn_id_base  = 100000

    txn_id = txn_id_base

    for row in rows:
        pk, amount, desc, start_ts, end_ts, cat_legacy = row
        start = apple_ts(start_ts)
        end   = apple_ts(end_ts)
        if not start or not end or amount is None:
            continue

        cat_id = CAT_MAP.get(cat_legacy, 13)  # default → Extra income
        dist_id = dist_id_base + pk

        # Clamp end date to today for 'isFinished' check
        is_finished = (end <= today)

        dist = {
            'id':          dist_id,
            'description': (desc or 'Extra income').strip(),
            'totalAmount': round(float(amount), 2),
            'startDate':   start,
            'endDate':     end,
            'categoryId':  cat_id,
            'isIncome':    True,
            'isFinished':  is_finished,
            'createdAt':   now_str,
            'updatedAt':   now_str,
            'syncStatus':  'pending',
        }
        distributions.append(dist)

        # Generate daily child transactions
        days = list(date_range(start, end))
        day_count = max(1, len(days))
        daily_amount = round(float(amount) / day_count, 4)

        for d in days:
            transactions.append({
                'id':             txn_id,
                'date':           d,
                'amount':         daily_amount,
                'categoryId':     cat_id,
                'note':           (desc or '').strip(),
                'type':           'distributed_income',
                'distributionId': dist_id,
                'createdAt':      now_str,
                'updatedAt':      now_str,
                'syncStatus':     'pending',
            })
            txn_id += 1

    conn.close()

    output = {
        'distributions': distributions,
        'transactions':  transactions,
    }

    out_path = 'extra-incomes-patch.json'
    with open(out_path, 'w') as f:
        json.dump(output, f, indent=2)

    print(f'\nPatch written: {out_path}')
    print(f'  {len(distributions)} distributions')
    print(f'  {len(transactions)} daily child transactions')
    print(f'\nImport via: Pocket Ledger → Settings → Import data')

if __name__ == '__main__':
    main()
