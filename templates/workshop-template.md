# Workshop template

Every workshop in `workshops/` follows this structure. 60 minutes, live, small business owners.
**One concrete concept per workshop** — not two or three. An episode's snips usually hold 5+
separate concepts; each gets its own workshop, its own day. The first 30 minutes teach the
concept end to end; the second 30 minutes are entirely open — building, and questions, with no
further script. Fill every section. Delete nothing.

---

## workshop.md

### Front matter block

```
# <Workshop title — a promise, not a topic>

**Source:** <Show> — <Episode title>
**Concept:** <this workshop's one concept> — <n> of an estimated <total> from this episode
**Snips file:** ../../sources/snips/<file>.md — snips used: <titles or numbers>
**Built:** <YYYY-MM-DD>
**Teach date:** TBD
**Length:** 60 minutes (30 teach / 30 open build + questions)
**Audience:** Small business owners and operators
```

### 1. The promise (1–2 sentences)

What the attendee can do at 4:00 that they could not do at 3:00. Concrete. One concept, so one
promise — no "and also." No "understand" or "learn about" — those are not things anyone can
check.

### 2. What they leave with

A bulleted list of tangible outputs: a built (or started) automation, a filled handout, a named
decision.

### 3. Agenda — 30 minutes teach, 30 minutes open

A table, minutes must add to 60:

| Minutes | Segment |
| --- | --- |
| 0–3 | Hook — why this, right now |
| 3–10 | The concept + where it comes from |
| 10–15 | What it means for a 10-person business + the example |
| 15–19 | The receipts — two real stories, with links |
| 19–25 | The honest objection + FAQ |
| 25–30 | Bridge to the build: what we're building for the next 30 minutes |
| 30–55 | Open build — Rachael builds live, the room builds alongside, questions anytime |
| 55–60 | Close and the one-week assignment |

The back 30 minutes is intentionally unscripted past the live-build spec in section 5 — it's
build time and Q&A, not a second round of teaching.

### 4. The concept

One concept. It gets:

- **The idea** in one sentence.
- **Where it comes from** — `[snip: <Title>](<link>)`. One to three snips; cite every one you
  lean on.
- **What it means for a 10-person business** — the translation out of podcast language.
- **The example** — a real, specific scenario from the snips or from Rachael's client work.
- **The receipts** — at least two real, sourced, external stories (not from a snip) where this
  concept played out — usually a specific company or agent getting it wrong in public, sometimes
  getting it right. Each needs a real link found by searching, not a `share.snipd.com` link and
  not an invented one. Say plainly what happened and why it matters for a small business, in a
  sentence or two per story. If fewer than two real ones turn up for this exact concept, include
  what you honestly found — never fabricate the rest to hit two.
- **The common objection** and the honest answer.
- **FAQ** — 3 to 5 other questions this topic reliably gets, each answered in 1–2 sentences. Real
  questions a skeptical small business owner would actually ask, not softballs.

### 5. Live build

One thing Rachael builds on screen, scoped to run the full 25–30 minutes of open build time
alongside the room — not a 10-minute demo. List the tool, the trigger, the steps, and the visible
result. Include what to do if the demo breaks.

### 6. Open build and questions

Guidance for running the unscripted back half:

- What the room is doing during this time (building the same thing alongside, on their own
  account/data).
- What to circulate and watch for — the one or two ways people usually get stuck.
- A restart line to use if the room stalls or goes quiet.
- How to handle the two-speed room: what a fast finisher can do next; what to tell someone who's
  still stuck with five minutes left.

### 7. Close and the one-week assignment

One sentence that lands the promise. Then a single assignment small enough to finish in a week.

### 8. Facilitator notes

Timing risks, questions that will come up beyond the FAQ, and anything to prepare beforehand.

### 9. Best practices nobody tells you

Two or three short, concrete practices for building the kind of automation this workshop teaches
— the kind of thing that only shows up after something has gone wrong once. These do not need a
snip behind them; they're operating knowledge, not podcast content. Each one gets:

- **The practice** in one sentence.
- **Why it bites people** — the failure it prevents, stated plainly.
- **The example** — tied to *this workshop's* live build specifically, not generic.

One of the 2–3 items is always a **stop condition**: a plain-English example of how the thing
being built in this workshop knows when to stop, pause, or hand off to a person, rather than
running forever or running past the point it's still right. Name the actual stop condition for
the actual example being built that day.

---

## handout.md

One page, printable, and designed to look good printed — real visual hierarchy (clear headings,
whitespace, maybe a simple rule or box), not a wall of text. No teaching content — this is a form
for the build-along, not a summary.

- Title and one-line purpose.
- The build-along worksheet: numbered prompts with blank space, shaped around the live build in
  section 5 (so filling it in tracks what's happening on screen).
- A back-of-page "if you only do one thing" line.

## handout-filled-example.md

The same handout, same structure, but filled in end to end with one realistic worked example —
so a reader can see what "done" looks like before they try it themselves. Invent the example;
label it clearly as an example, never as a real client's data. It must show, explicitly and
separately from the worksheet answers:

- **Context example** — a concrete sample of what the automation/agent should look at or use as
  input: an example email, order, ticket, record, whatever fits the day's build. Enough detail
  that someone could see exactly what "the agent reads this" means.
- **Definition of done** — a concrete example of the finished output. Specific enough that a
  reader could hold a real run's result next to this and tell whether it succeeded.
