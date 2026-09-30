# Workshop Topics & Content — Implementation Plan

**Overall Progress:** `12%`
**Revision:** v2 (2026-09-30) — graded against a rubric and rewritten. See `## Grading record`.

## TLDR

The routine currently picks the **newest unused episode** and builds a workshop from it. That
guarantees two workshops a month but not two *good* ones — it makes topic quality a function of
what Rachael happened to listen to last.

This plan changes the unit of selection from **episode** to **theme**, gives the quality bar
teeth, and fixes the problem v1 of this plan missed entirely: the input supply is thin, narrow,
and partly unusable.

## What the pool actually looks like

Measured 2026-09-30 across all five archived episodes. These numbers drive every decision below.

| Fact | Number | Consequence |
| --- | --- | --- |
| Total snips archived | 87 | Finite. At ~8 snips per workshop, roughly 10 workshops of raw material. |
| Snips tagged with a theme | 56 | 31 untagged (loops, Grok Bot) — tagging is incomplete, so no track claim is trustworthy yet. |
| Tagged snips that are **not** owner-actionable | 19 of 56 (34%) | A third of the material cannot be taught to this audience. Mostly the Sam Altman episode. |
| Distinct shows | 3 | Lenny's supplies 3 of 5 episodes. The input is one podcast's worldview. |
| Largest single theme | 7 snips (The Demo) | Most themes hold 1–4. Very few clear a meaningful bar on their own. |

Two conclusions v1 of this plan got wrong:

1. **Supply is the binding constraint, not selection.** 10 workshops of material is five months at
   two a month, and a third of what arrives is unusable. Better selection on a shrinking pool
   still runs out. The plan now includes broadening the input.
2. **The four-track spine was asserted, not derived.** The themes that actually emerged are a
   sales funnel (Discovery Call → Demo → Paid Pilot → Price It → Close It, 18 snips across five
   stages) plus scattered singletons. Tracks get derived from the pool after tagging is complete,
   not declared in advance.

## Critical Decisions

- **Topic unit is a theme, not an episode** — one episode can yield two workshops or half of one.
  The loops episode proved it: 8 of 14 snips built workshop 01, and three leftovers are a pricing
  workshop with nothing to do with loops.
- **Score snips, not episodes** — an episode averaging poorly can still hold the single best snip
  in the pool. Snip-level scoring is the only way to find it.
- **Three axes, scored 1–3: owner-actionable, teachable, demo-able** — a snip scoring 1 on
  owner-actionable is excluded outright, however interesting it is. That axis is what rejects the
  34% of the pool that is frontier-lab strategy and energy policy.
- **Theme quality is the *mean* score, not the sum** — v1 used a sum threshold, which rewarded
  volume: a 7-snip mediocre theme cleared the bar while a tight 3-snip excellent theme failed.
  A theme qualifies at **3+ snips with mean score ≥ 2.2 per axis**. Size and quality are judged
  separately.
- **The quality gate blocks the Slack post** — v1 wrote a `gate.md` and posted regardless, which
  is not a gate. A failed gate now commits the workshop as a draft, skips Slack, and reports which
  checks failed. Rachael decides whether to ship it.
- **Tracks are derived after tagging, not before** — see the table above.
- **Broaden the input** — three shows, one dominant, is a single worldview and a finite pool.
  Adding shows is a Rachael action, not an agent action, and it is on the critical path.
- **`CLAUDE.md` gets a rollback copy before Step 7** — it is the file that makes the routine work.
  If theme selection turns out worse than episode selection, reverting must take one command.
- **The two-a-month floor is never traded away** — every change below preserves it.
- **Owners are explicit on every step** — `[agent]` the cloud routine, `[claude]` an interactive
  session, `[rachael]` her call or her access. v1 named no owners, which is why three of its steps
  were unexecutable.

## Tasks:

- [ ] 🟨 **Step 1: Finish the snip pool** `[claude]`
  - [x] 🟩 Archive all 5 episodes verbatim from Gmail — 87 snips, links intact
  - [x] 🟩 Add a `Theme` column to the three backfilled episodes — 56 snips tagged
  - [ ] 🟥 Tag the remaining 31 snips (loops, Grok Bot) so the pool is complete
  - [ ] 🟥 Write `sources/snip-pool.md` — one row per snip: title, episode, type, theme, three axis scores, used-in
  - **Done when:** all 87 snips appear in `snip-pool.md` with a theme and three scores, and the count reconciles against the per-episode files.

- [ ] 🟥 **Step 2: Write and calibrate the scoring rubric** `[claude]`
  - [ ] 🟥 Create `templates/topic-selection.md`: the three axes, what 1 / 2 / 3 means on each, and a worked example at each level
  - [ ] 🟥 Set the gates: any snip scoring 1 on owner-actionable is excluded; a theme qualifies at 3+ surviving snips with mean ≥ 2.2 per axis
  - [ ] 🟥 Calibrate against known-good ground truth: the 8 snips that built workshop 01 must all score ≥ 2 on owner-actionable, and the 13 macro snips must all score 1. If they don't, the rubric is wrong, not the snips
  - [ ] 🟥 Score all 87 snips and record in `sources/snip-pool.md`
  - **Done when:** the calibration check passes and every snip has three scores.

- [ ] 🟥 **Step 3: Derive the tracks and build the queue** `[claude]`
  - [ ] 🟥 Group surviving snips into themes; count each theme's size and mean score
  - [ ] 🟥 Derive the track names from the clusters that actually exist — do not force the pool into four predetermined tracks
  - [ ] 🟥 Write `state/curriculum.md`: ranked queue of qualifying themes with track, feeder snips, size, mean score, and source-show spread
  - [ ] 🟥 List sub-threshold themes separately with what would unblock each one, so Step 4b knows what to listen for
  - **Done when:** the queue holds at least 4 qualifying themes, or says plainly that it does not and names the shortfall.

- [ ] 🟥 **Step 4a: Broaden the input** `[rachael]`
  - [ ] 🟥 Add 2–3 shows in Snipd aimed at operators rather than founders and investors — the current pool is 3 shows and one worldview
  - [ ] 🟥 Snip at least 2 episodes from the new shows before the 15th
  - **Why this is on the critical path:** 10 workshops of material, a third of it unusable, is five months. Selection cannot fix supply.
  - **Done when:** `sources/snips/` holds an episode from a show that is not Lenny's, a16z, or Super Data Science.

- [ ] 🟥 **Step 4b: Backfill workshops from the top themes** `[claude]`
  - [ ] 🟥 Disable the routine for the duration so the ledger does not race a live run
  - [ ] 🟥 Build workshops from the top 3 themes in the queue (workshops 01 and 02 already exist; check whether their themes rank, and do not rebuild them)
  - [ ] 🟥 `workshop.md` + `handout.md` against the template, matching workshop 01's depth — note workshop 02's handout came in at 201 words against workshop 01's 402, and is missing the verification checklist
  - [ ] 🟥 Update `Used in` and `Theme` in every snips file touched, plus `state/processed-episodes.md`
  - [ ] 🟥 Re-enable the routine
  - **Done when:** each new workshop passes the Step 5 gate and is posted.

- [ ] 🟥 **Step 5: Add a gate with teeth** `[claude]`
  - [ ] 🟥 Create `templates/quality-gate.md` — every check mechanically checkable: minutes sum to exactly 60; ≥15 minutes are the room working; every teaching point carries a `share.snipd.com` link; **every cited link resolves to a snip in `sources/snips/`**; every objection has an answer; the live build has a break-glass fallback; no word from the banned filler list; the handout contains blank fields and a verification checklist
  - [ ] 🟥 Add the link-resolution check as a script so it cannot be eyeballed — the current pass rate is 16/16 across both workshops and that is the baseline to hold
  - [ ] 🟥 Wire the gate into `CLAUDE.md` as a **blocking** step: on failure, commit the workshop to `workshops/<slug>/DRAFT-` and skip the Slack post, then report the failed checks
  - [ ] 🟥 Run the gate retroactively against workshops 01 and 02; record results; fix workshop 02's handout
  - **Done when:** a deliberately broken workshop is refused by the gate in a test run.

- [ ] 🟥 **Step 6: Close the feedback loop** `[claude]` + `[rachael]`
  - [ ] 🟥 Create `state/taught.md`: date, workshop, headcount, what landed, what died, what to cut next time
  - [ ] 🟥 Add an empty `## What happened when taught` section to the workshop template
  - [ ] 🟥 Add the nudge — v1 assumed Rachael would fill this unprompted, which means it would stay empty. The routine's Slack message asks, by name, for the debrief on any workshop with a `Teach date` in the past and an empty section
  - [ ] 🟥 Add a `CLAUDE.md` rule: read `state/taught.md` before writing, and do not rebuild a segment recorded as having died
  - **Done when:** one real session is recorded and the next workshop demonstrably avoids something the record flagged.

- [ ] 🟥 **Step 7: Switch the routine from newest-episode to best-theme** `[claude]`
  - [ ] 🟥 Copy the working `CLAUDE.md` to `templates/CLAUDE-episode-mode.md` first, so reverting is one command
  - [ ] 🟥 Rewrite steps 1–3 to read `state/curriculum.md` and build the top-ranked unbuilt theme
  - [ ] 🟥 Add a step that scores newly arrived snips into the pool at the start of each run, so new episodes **feed** the queue rather than jump it
  - [ ] 🟥 Keep the never-skip rule: if no theme qualifies, build the highest-scoring sub-threshold theme and say so at the top of the workshop
  - [ ] 🟥 Test with one manual run; confirm commit, canvas, and channel message
  - **Rollback:** if two consecutive theme-mode workshops fail the gate, restore `templates/CLAUDE-episode-mode.md` and say so in the channel.
  - **Done when:** one theme-mode run completes all seven of its own steps unattended.

## Out of scope

Named so it does not creep in: slides, video recording, attendee registration, pricing the
workshop, a public landing page, and anything that turns this into a course product. This plan
covers topic selection and content quality only.

## Grading record

v1 of this plan was graded against the rubric in `templates/plan-rubric.md` and scored **62/100**.
What changed in v2:

| Criterion | v1 | Why it lost points | Fix in v2 |
| --- | --- | --- | --- |
| Diagnoses the real failure mode | 9/10 | — | — |
| Decisions decided, not deferred | 8/10 | — | — |
| Executable unattended | 6/15 | No owners on any step; "score every snip" never said by whom | `[agent]` / `[claude]` / `[rachael]` on every step |
| Measurable quality bar | 7/15 | Gate wrote a file and posted anyway; sum threshold rewarded volume over quality | Gate blocks the post; threshold is mean ≥ 2.2, size judged separately; link-resolution is a script |
| Closes the feedback loop | 5/10 | Assumed Rachael fills `taught.md` unprompted, so it would stay empty forever | Routine asks her by name when a taught workshop has an empty debrief |
| Scope discipline | 10/10 | — | — |
| Handles the supply problem | 3/10 | Biggest miss. 87 finite snips, 34% unusable, 3 shows, one dominant — no broadening step | Step 4a, on the critical path, owned by Rachael |
| Sequencing correctness | 5/10 | Step 4 raced the live routine; themes were tagged before the rubric that defines them existed | Routine disabled during backfill; tagging now completes under the calibrated rubric |
| Preserves the 2/month floor | 9/10 | — | — |
| **Total** | **62/100** | | |

Two things the grading surfaced that are worth stating plainly rather than burying in a table.
First, the largest hole was not in how topics get picked but in whether there will be topics to
pick — a selection plan on a five-month pool is solving the wrong problem. Second, the theme tags
already in the snip files were assigned by eye before the scoring rubric existed, which is the
plan's own steps run backwards; they are provisional and Step 2's calibration check is what makes
them trustworthy.
