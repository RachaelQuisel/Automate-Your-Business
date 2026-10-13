# The Standing Watch: Give One Automation a Permanent Job, With a Leash

**Source:** Lenny's Podcast: Product | Career | Growth — OpenAI's Head of ChatGPT: We're entering a new era of AI (again) | Tibo Sottiaux
**Concept:** Standing Watch — 1 of an estimated 6 from this episode
**Snips file:** ../../sources/snips/2026-10-05-chatgpt-new-era-of-ai.md — snips used: Specialist Agents Could Become A Virtual Team, Persistent Agents Require Memory And Coherence, A Dot Spotted An Outage Before The Demo
**Built:** 2026-10-13
**Teach date:** TBD
**Length:** 60 minutes (30 teach / 30 open build + questions)
**Audience:** Small business owners and operators

---

## 1. The promise

By 3:30 you'll know how to give one automation a permanent job — watching one thing in your
business, continuously, instead of running once and forgetting it existed. By 4:00 you'll have
built (or started building) that exact thing, with a built-in limit on what it's allowed to do
without you.

## 2. What they leave with

- One "standing watch" automation, built or half-built, pointed at a real recurring thing in
  their business.
- A written stop condition for it — the rule that caps what it can do before a person steps in.
- A filled handout showing the exact input it reads and the exact output that counts as success.

## 3. Agenda — 30 minutes teach, 30 minutes open

| Minutes | Segment |
| --- | --- |
| 0–3 | Hook — the automation that only works once |
| 3–10 | The concept + where it comes from |
| 10–15 | What it means for a 10-person business + the example |
| 15–19 | The receipts — two real stories, with links |
| 19–25 | The honest objection + FAQ |
| 25–30 | Bridge to the build: what we're building for the next 30 minutes |
| 30–55 | Open build — Rachael builds live, the room builds alongside, questions anytime |
| 55–60 | Close and the one-week assignment |

## 4. The concept

**The idea.** Most automations run once and stop. A standing watch is different: it has one
job, it keeps doing that job on a schedule, it remembers what it already told you so it doesn't
repeat itself, and it has a hard limit on what it's allowed to do before a person has to look.

**Where it comes from.** [snip: Specialist Agents Could Become A Virtual Team](https://share.snipd.com/snip/fb853160-7cc3-4e1e-960b-c7146297d5f0),
[snip: Persistent Agents Require Memory And Coherence](https://share.snipd.com/snip/062f4f6d-02f4-4ac6-be56-d73d4b2a22b0),
and [snip: A Dot Spotted An Outage Before The Demo](https://share.snipd.com/snip/ffd1206d-8083-49d4-a968-722a5b487852).

**What it means for a 10-person business.** The podcast's example is an engineer who keeps a
dedicated AI "Dot" permanently watching one feed — Twitter mentions of his product — instead of
checking it himself. The point that matters isn't the specific tool; it's the shape: one
narrow job, running continuously, with memory of what it already flagged. Translate that
directly into your business: a dedicated watch on invoices over 14 days unpaid, a watch on a
competitor's pricing page, a watch on your inbox for a specific client's name. Not "an AI that
does my admin" — one job, watched forever.

The memory part matters as much as the watching part. Without it, the same watcher re-reports
the same invoice every single day and everyone starts ignoring it within a week. With it, the
watcher only speaks up about what's *new* since the last check.

**The example to use.** A ten-person agency sets up a standing watch on its invoice list: every
morning, check for invoices that just crossed 14 days unpaid, and only mention the ones that
weren't already mentioned yesterday. The owner used to remember to check this "when things felt
slow." Now it's checked every single morning, whether anyone remembers or not.

**The receipts.**

- Ramp built a swarm of automated monitors watching its spreadsheet product for bugs. In at
  least one documented case, a monitor flagged a real issue *before* a staff member's own bug
  report reached the team in Slack — the watch genuinely beat a human to it. The catch: once they
  scaled from about ten hand-written monitors to over a thousand, ordinary user activity started
  triggering a flood of false alarms, and they had to add a triage step just to separate real
  problems from noise. [Ramp: How we made Ramp Sheets self-maintaining](https://labs.ramp.com/research/ramp-sheets-self-maintaining/)
- In May 2026, someone gave an AI agent AWS credentials and one instruction: scan a hobbyist
  network called DN42, "immediately, without delay." With no spending cap and no pause-and-check
  step, the agent spun up five large AWS instances, load balancers, and Lambda functions trying
  to get the job done fast — and ran up a $6,531.30 bill in about 24 hours before its operator
  noticed the credit card charges and shut it off. [Decrypt: AI agent rekts dev with bogus scan, asks for crypto donations](https://decrypt.co/370988/ai-agent-rekts-dev-bogus-scan-crypto-donations)

**The common objection.** *"If it still has to check with a person, what did I actually
automate?"*

The honest answer: the noticing. Before, a person has to remember to go look — and they don't,
most days. After, the one or two things that actually matter get found every single day, without
anyone remembering to check. The automation's job was never to decide alone; it was to make sure
the right thing gets in front of a person at all.

**FAQ**

- *"Doesn't my accounting software already do this?"* Most tools will show you the data if you
  go look. A standing watch is the difference between a dashboard and someone tapping you on the
  shoulder — it decides *when* something is worth your attention, not just whether the data
  exists.
- *"What if it misses something important?"* It only watches what you point it at. It's not a
  substitute for your monthly real review — it's a daily net for the one or two signs you already
  know matter, so they don't slip past you on a busy week.
- *"What if it floods me with alerts?"* That's the single most common failure — see the Ramp
  story above. Build the "only mention what's new" memory check from day one; don't wait until
  people start muting it to add it.
- *"Who's responsible if it gets something wrong?"* The same person who owned the task before it
  existed. The watch flags; a person still decides. That division never goes away.
- *"Does this need AI at all, or is it just a scheduled report?"* Honestly — a lot of a standing
  watch is mostly scheduling plus a simple rule (a number crossing a threshold). AI earns its
  place when the "is this worth flagging" judgment is fuzzy, not when a plain if-this-then-that
  rule already does the job.

## 5. Live build — a standing watch on overdue invoices, 25–30 minutes

**What Rachael builds on screen**, scoped to fill the whole open-build block:

- **Tool:** Airtable (a table + a scheduled automation). Any tool that holds a list and can run
  on a schedule works the same way.
- **Trigger:** once a day, every morning.
- **Step 1:** find every invoice where `Status = Sent` and `Days Since Sent > 14`.
- **Step 2:** of those, check a `Flagged` field — skip any invoice already flagged on a previous
  day.
- **Step 3:** mark the newly-found ones `Flagged`, and send one digest message listing all of
  them together — never one message per invoice.
- **The cap (stop condition):** the automation sends at most one digest per day, and it only
  ever notifies a person internally — it never emails or contacts the client directly. If it
  can't tell whether something counts as "new," it skips it and waits for a person, rather than
  guessing.
- **Visible result:** a message appears — *"2 invoices just crossed 14 days unpaid: Acme Co
  ($1,200), Bolt LLC ($430)."*

**If the demo breaks:** have a pre-built version with a populated run history open in a second
tab. Switch to it, say "here's this morning's real digest," and keep going.

## 6. Open build and questions

- **What the room is doing:** building the same shape — one list, one threshold, one memory
  field, one daily digest — pointed at their own recurring thing: invoices, a lead queue, a
  renewal date, a competitor's page.
- **What to circulate and watch for:** people build a watcher with no memory field, so it would
  re-alert on the same thing every day. Stop and add the `Flagged` field before anything else.
- **Restart line if the room stalls:** "Say the sentence out loud: 'Every day, check ___, and
  only tell me about the ones I haven't heard about yet.' Whatever fills that blank is your
  build."
- **Two speeds:** a fast finisher adds a second condition (e.g., only flag invoices over $500).
  Someone still stuck with five minutes left should stop building and just write the one sentence
  from the restart line on their handout — that's a real, usable starting point for next week.

## 7. Close and the one-week assignment

**The close:** "You don't need an automation that does everything. You need one thing that's
still watching next Tuesday, whether you remember it or not — and that knows when to stop and
hand you the decision."

**The assignment:** "This week, build just the trigger and the memory field — the part that
notices and doesn't repeat itself. Not the digest message yet. If it can notice something new
and *not* nag you about it twice, the hard part is done."

## 8. Facilitator notes

**Prepare beforehand:**
- An Airtable base with an `Invoices` table, a `Flagged` field, and the working daily automation.
- A second tab with a populated run history for the demo-breaks fallback.
- Printed handouts.

**Timing risks:**
- The receipts section wants to turn into a longer AI-safety discussion — the DN42 story is
  genuinely fun to talk about. Cap it at the two stories as written; the stop-condition payoff
  lands in the best-practices section, not here.
- The open-build block is unscripted on purpose; don't let it collapse into Rachael building
  solo while the room watches. Call out "pause and build this part yourself" every few minutes.

**Questions beyond the FAQ that will come up:**
- *"Can I make this text me instead of Slack/email?"* Yes — same shape, different notification
  step. The watching and the memory field don't change.
- *"What if two different things both need watching?"* Build two separate standing watches, not
  one watcher doing two jobs. Keeps each one's stop condition clean and easy to reason about.

## 9. Best practices nobody tells you

**Give it a stop condition.** Name, in writing, the one thing it's never allowed to do without a
person — not "be careful," an actual cap. In this build: at most one digest a day, and it never
contacts a client directly. The DN42 agent had no cap and no pause step, was told to act
"immediately," and ran up a $6,531 bill in 24 hours before anyone noticed. A stop condition is
what would have made that agent stop at step one, before the second AWS instance ever launched.

**Triage before you alert.** A watcher with no sense of "is this actually new" turns into noise,
and noisy watchers get muted — which defeats the whole point. Ramp hit this at scale: once they
had over a thousand monitors, ordinary activity triggered a flood of false alarms, and they had
to add a triage step. In this build, that's the `Flagged` field — it's not an extra feature, it's
the difference between a watch people trust and one they tune out within a week.
