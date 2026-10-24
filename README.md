# Automate Your Business

Workshop material for the twice-monthly **Automate Your Business** workshop, generated from
Rachael's Snipd podcast highlights.

Taught twice a month. Each run of the cloud routine produces one workshop, so the repo gains
at least two new workshops per month.

## How a workshop gets made

1. Rachael listens to a podcast in Snipd and saves snips (highlights).
2. Snipd emails the snips to `rachael.quisel@gmail.com`, subject `✨ Your snips for: <episode>`,
   sender `hello@snipd.com`. The body contains every snip as a labeled block
   (`INSIGHT`, `ADVICE`, `ANECDOTE`) with two bullets and a share link.
3. A scheduled cloud agent runs on the 1st and 15th of each month. It searches Gmail for snip
   emails, picks one episode that has not been used yet, archives the raw snips, writes a
   workshop from them, and commits everything to this repo.
4. The agent posts the full curriculum as a Slack Canvas in `#automate_your_business`
   (private, `xraytech` workspace) with a summary message linking the canvas and the repo.
5. Rachael pulls the new files down: `git pull`.

## Layout

| Path | What lives there |
| --- | --- |
| `workshops/<YYYY-MM-DD>-<slug>/workshop.md` | The teaching plan — agenda, script beats, timings |
| `workshops/<YYYY-MM-DD>-<slug>/handout.md` | The one-page worksheet attendees fill in |
| `sources/snips/<YYYY-MM-DD>-<slug>.md` | Raw snips from one episode, verbatim, with links |
| `state/processed-episodes.md` | Ledger of episodes already turned into workshops |
| `templates/workshop-template.md` | The fixed structure every workshop follows |
| `content-ideas/brand-plan.md` | Draft brand plan for Rachael's posts and short videos (added Oct 7, 2026; waiting on her decisions) |
| `CLAUDE.md` | Instructions the cloud agent follows on each run |

## Working on this locally

```sh
cd "$HOME/Projects/personal/Automate Your Business"
git pull            # bring down workshops the cloud routine wrote
```

The cloud routine runs in Anthropic's cloud. It cannot see this machine. GitHub is the
handoff point in both directions: anything Rachael edits locally needs a push before the
next run, or the routine will not know about it.

## The routine

Managed at https://claude.ai/code/routines — schedule, prompt, and connectors live there.
Schedule: 1st and 15th of the month, 9:00 AM Pacific.
Connectors required: Gmail (read-only search of the Snipd emails) and Slack (post the workshop
to `#automate_your_business`, channel ID `C0C5UAT6ER2`).

### Schedule and daylight saving

The cron expression is `7 16 1,15 * *` — UTC, because routines run on UTC. That is 9:07 AM Pacific
from March to November and 8:07 AM Pacific from November to March. The hour drifts by one; the day
does not. Left as-is on purpose rather than maintained twice a year.
