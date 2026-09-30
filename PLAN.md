# Workshop Topics & Content — Implementation Plan

**Overall Progress:** `0%`

## TLDR

Right now the routine picks the **newest unused episode** and builds a workshop from it. That
guarantees two workshops a month but not two *good* ones — it makes topic quality a function of
what Rachael happened to listen to last.

This plan changes the unit of selection from **episode** to **theme**. All snips from all episodes
go into one pool, get scored for how useful they are to a small business owner, and cluster into
themes. A workshop gets built from the best-scoring cluster, drawing snips across episodes when
that makes a stronger hour. It also adds the two things missing entirely: a quality gate before a
workshop is published, and a record of what actually happened in the room.

## Critical Decisions

- **Topic unit is a theme, not an episode** — one episode can yield two workshops, or half of one.
  The loops episode already proved this: 8 of 14 snips built workshop 01, and 3 of the leftovers
  are a pricing workshop that has nothing to do with loops.
- **Score snips, not episodes** — an episode averaging poorly can still contain the single best
  snip in the pool. Scoring at the snip level is the only way to find it.
- **Three-axis score: owner-actionable, teachable, demo-able** — a snip that fails owner-actionable
  is out regardless of how interesting it is. Most VC-podcast macro commentary fails this axis, and
  it is exactly the material that feels smart and teaches nothing.
- **A curriculum spine, not 24 standalone hours** — attendees repeat. Four tracks
  (Find the Work, Build the Loop, Prove It Paid, Sell What You Built) so a regular has a path
  instead of a shuffle.
- **Translation is the product, not the snips** — the source is Silicon Valley product talk; the
  audience runs a 10-person business. Every teaching point states the small-business translation
  explicitly. This is already the rule in `CLAUDE.md`; the rubric makes it scoreable.
- **The routine still never skips a run** — theme selection replaces episode selection, but the
  two-a-month floor is unchanged.
- **Quality gate is a checklist in the repo, not a judgment call** — so the cloud agent can apply
  it and a failed check is a visible artifact, not a silent pass.

## Tasks:

- [ ] 🟥 **Step 1: Build the snip pool**
  - [ ] 🟥 Extract all snips from the 4 remaining Snipd emails into `sources/snips/` (Grok Bot, Super Data Science Aug recap, Jen Abel enterprise deals, Sam Altman on Sora), verbatim, matching the existing file format
  - [ ] 🟥 Add a `Theme` column alongside the existing `Used in` column in every snips file
  - [ ] 🟥 Write `sources/snip-pool.md` — one row per snip across all episodes: snip title, episode, type, theme, score, used-in

- [ ] 🟥 **Step 2: Write the scoring rubric**
  - [ ] 🟥 Create `templates/topic-selection.md` with the three axes, scored 1–3 each: owner-actionable (can a 10-person business act on this Monday), teachable (can it be taught in 10 minutes to non-engineers), demo-able (can Rachael show it on screen)
  - [ ] 🟥 Set the thresholds: a snip scoring 1 on owner-actionable is excluded; a theme needs 3+ snips totaling 18+ to become a workshop
  - [ ] 🟥 Score every snip in the pool and record it in `sources/snip-pool.md`

- [ ] 🟥 **Step 3: Cluster into themes and pick the spine**
  - [ ] 🟥 Group the scored pool into named themes; record which episodes feed each theme
  - [ ] 🟥 Assign each theme to one of four tracks: Find the Work, Build the Loop, Prove It Paid, Sell What You Built
  - [ ] 🟥 Write `state/curriculum.md` — the ranked queue of buildable themes with their track, feeder snips, and total score
  - [ ] 🟥 Flag themes that are below threshold and name what snip would unblock them

- [ ] 🟥 **Step 4: Backfill workshops from the top themes**
  - [ ] 🟥 Build the next 3 workshops from the top 3 themes in the queue (workshop 02 from the Grok Bot run already in flight counts as one if its theme ranks)
  - [ ] 🟥 Each gets `workshop.md` + `handout.md` against the existing template, matching workshop 01's depth
  - [ ] 🟥 Update `Used in` and `Theme` in every snips file touched, and update `state/processed-episodes.md`
  - [ ] 🟥 Post each to `#automate_your_business` as canvas + summary message

- [ ] 🟥 **Step 5: Add the quality gate**
  - [ ] 🟥 Create `templates/quality-gate.md` — the checks a workshop must pass before it posts: every teaching point cites a real snip link, minutes sum to 60, 15+ minutes are the room working, every objection has an honest answer, the live build has a break-glass fallback, no filler words from the banned list, handout is a form and not a summary
  - [ ] 🟥 Add a step to `CLAUDE.md` requiring the gate be run and its result written to the workshop folder as `gate.md`
  - [ ] 🟥 Run the gate against workshop 01 retroactively and record the result

- [ ] 🟥 **Step 6: Close the feedback loop**
  - [ ] 🟥 Create `state/taught.md` — one row per session taught: date, workshop, headcount, what landed, what died, what to cut next time
  - [ ] 🟥 Add a `## What happened when taught` section to the workshop template, empty until Rachael fills it
  - [ ] 🟥 Add a rule to `CLAUDE.md`: read `state/taught.md` before writing, and avoid segments recorded as having died

- [ ] 🟥 **Step 7: Switch the routine from newest-episode to best-theme**
  - [ ] 🟥 Rewrite `CLAUDE.md` steps 1–3 to read `state/curriculum.md` and build the top-ranked unbuilt theme instead of the newest unused episode
  - [ ] 🟥 Keep the never-skip rule: if no theme meets threshold, build the highest-scoring sub-threshold theme and say so at the top of the workshop
  - [ ] 🟥 Add a step that re-scores newly arrived snips into the pool at the start of each run, so new episodes feed the queue instead of jumping it
  - [ ] 🟥 Test with one manual `RemoteTrigger` run and confirm the commit, the canvas, and the channel message

## Out of scope

Named so it does not creep in: slides, video recording, attendee registration, pricing the
workshop, a public landing page, and anything that turns this into a course product. This plan
covers topic selection and content quality only.
