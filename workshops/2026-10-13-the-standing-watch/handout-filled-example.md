# The Standing Watch — filled example

**Automate Your Business** · This is a worked example, not a real client's data. Every name,
invoice, and number below is invented for illustration.

---

## Part 1 — Name the watch

**What are you watching?** The `Invoices` table, specifically unpaid ones.

**How often does it check?** Every morning at 7am.

**What counts as worth mentioning?** An invoice has just crossed 14 days since it was sent, and
is still marked `Sent` (not `Paid`).

## Part 2 — Build it

**Step 1 — Find the candidates.** `Status = Sent` AND `Days Since Sent > 14`.

**Step 2 — Remember what it already said.** A checkbox field, `Flagged`, set to true the first
time an invoice is included in a digest. Future checks skip anything already `Flagged`.

**Step 3 — Say it once.** One Slack message to the owner, once a day, naming every
newly-crossed invoice together — never one message per invoice.

## Part 3 — The stop condition

**What is it never allowed to do without a person checking first?** It never emails or contacts
the client directly. It only ever notifies a person internally. If it can't tell whether an
invoice counts as "new" (e.g., the `Days Since Sent` field is blank or broken), it skips that
invoice and waits for a person — it does not guess.

**How many times a day can it speak up, at most?** Once. One digest, maximum, no matter how many
invoices qualify.

---

## Context example — what the automation reads

A sample of what's actually in the `Invoices` table the morning this runs:

| Client | Status | Sent date | Days Since Sent | Flagged |
| --- | --- | --- | --- | --- |
| Acme Co | Sent | 2026-09-29 | 14 | — |
| Bolt LLC | Sent | 2026-09-28 | 15 | — |
| Carver Design | Sent | 2026-10-10 | 3 | — |
| Delta Supplies | Paid | 2026-09-20 | 23 | — |
| Everwell Clinic | Sent | 2026-09-15 | 28 | ✓ (already flagged 9/30) |

Only Acme Co and Bolt LLC qualify today: both just crossed 14 days, both still unpaid, neither
flagged yet. Carver Design isn't old enough. Delta Supplies is paid. Everwell Clinic already got
mentioned two weeks ago, so it stays quiet — the watch doesn't repeat itself.

## Definition of done — what success looks like

A single Slack message, delivered once, by 7:05am:

> **Standing Watch — Invoices, 2026-10-13**
> 2 invoices just crossed 14 days unpaid:
> • Acme Co — $1,200 (14 days)
> • Bolt LLC — $430 (15 days)
> Everwell Clinic is still unpaid at 28 days but was already flagged on 9/30 — no new action
> needed unless you want to escalate it yourself.

If a run produces this — one message, only the genuinely new items, nothing repeated — the watch
worked. If it produces five separate pings for five invoices, or re-mentions Everwell Clinic
every morning, the build isn't done yet, even if the underlying data is correct.
