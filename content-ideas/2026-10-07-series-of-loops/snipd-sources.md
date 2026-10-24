# Snipd sources inventory

Checked Wed Oct 7, 2026, ~5:40 AM PT. All access was read-only.

## Where the captures live

| Place | What's there | Status today |
|---|---|---|
| **GitHub `RachaelQuisel/Automate-Your-Business`** (private), folder `sources/snips/` | Verbatim Snipd snips, one markdown file per episode. A scheduled cloud agent (runs on the 1st and 15th, 9:00 AM PT) turns them into workshops. Ledger: `state/processed-episodes.md`. | **The connected GitHub account can't see this repo today** (`scm_repo_not_accessible`). Another agent could read it on Oct 6, so the Cursor GitHub App probably lost access to it, or never had it. Rachael needs to grant the app access to this repo before the full archive can be read. |
| **Gmail `rachael.quisel@gmail.com`** | The source emails. Sender `hello@snipd.com`, subject `✨ Your snips for: <episode>`. Each snip is a labeled block (INSIGHT / ADVICE / ANECDOTE) with two bullets and a `share.snipd.com` link. | **No connector for this inbox.** The two connected inboxes don't have it. |
| Gmail `maisonsantabarbara@gmail.com` (user-Gmail) | No Snipd emails. Has Lenny's Newsletter / Lenny's Podcast / How I AI episode emails (lenny@substack.com), Jun 26 – Aug 2, 2026, plus a Sep 4 "Grok Bot to do" email: "take my snips from podcasts and turn them into linkedin and x posts." | Connected, searched |
| Gmail `rachael@xray.tech` (user-Gmail--work) | No Snipd emails. Has 5 Lenny's newsletter emails (Jul 13–22, 2026) and an Oct 2 email with the attachments for "Workshop 04 — The Skills Loop", which was built from AI Tools Daily snips (paraphrased, not verbatim). | Connected, searched |
| A cached audit file on the shared work computer | A cached copy of the first commit of Automate-Your-Business (Sep 30, 2026), with **one full verbatim snips file** | Extracted to a working `_src/` folder. Not committed here, since the same snips are in `sources/snips/2026-09-22-series-of-loops.md`. |

## Captures I could read verbatim

- `sources/snips/2026-09-22-series-of-loops.md` (in this repo): **Lenny's Podcast**, "Why companies are becoming a series of loops | Anish Acharya (a16z)". Snipd email dated 2026-09-22. **14 snips.** All 5 content ideas come from this file.

## Known from the repo ledger and earlier notes (titles only, not readable today)

From `state/processed-episodes.md` (snapshot as of 2026-09-30) and the Oct 6 workspace notes:
- 2026-09-22 · Lenny's Podcast · How we built Grok Bot in a month | Roman Ugarte (SpaceXAI)
- 2026-09-14 · Super Data Science · 1024: In Case You Missed It in August 2026
- 2026-09-04 · Lenny's Podcast · How to close $100K+ enterprise deals, step by step | Jen Abel
- 2026-08-13 · The a16z Show · Sam Altman on Sora, Energy, and Building an AI Empire
- 2026-10-01 · AI Tools Daily · `sources/snips/2026-10-01-ai-tools-trending.md` (13 snips)

**Known date range of the Snipd emails: 2026-08-13 → 2026-10-01** (at least 6 episodes). Only 1 episode (14 snips) was readable verbatim today.

## What I searched
- GitHub: `get_me` (RachaelQuisel); `search_repositories user:RachaelQuisel` returned 27 repos and missed Automate-Your-Business; `search_code` for `snipd`, `Lenny`, `podcast` (0 hits, index incomplete); `search_commits snipd`; recursive trees of RachaelQuisel, Skills, la-maison, airbnbai, skillsforyou, cited-research-assistant, contact-follow-up-tracker, humanize-output; `get_git_tree` on Automate-Your-Business, which was denied.
- Gmail (both connected inboxes): `from:snipd OR snipd OR "Lenny's Podcast"`; `snipd OR snips OR "snipd.com" OR from:snipd.com in:anywhere`; `"share.snipd.com" OR "Your snips for" OR` the workshop names.

## To unlock the full archive
1. Grant the Cursor GitHub App access to `RachaelQuisel/Automate-Your-Business`, **or**
2. Connect `rachael.quisel@gmail.com` as a Gmail connector, **or**
3. Forward `hello@snipd.com` emails to rachael@xray.tech or maisonsantabarbara@gmail.com.
