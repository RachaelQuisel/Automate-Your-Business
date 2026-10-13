# Workshop template

Every workshop in `workshops/` follows this structure. 60 minutes, live, small business owners.
Fill every section. Delete nothing.

---

## workshop.md

### Front matter block

```
# <Workshop title — a promise, not a topic>

**Source:** <Show> — <Episode title>
**Snips file:** ../../sources/snips/<file>.md
**Built:** <YYYY-MM-DD>
**Teach date:** TBD
**Length:** 60 minutes
**Audience:** Small business owners and operators
```

### 1. The promise (2–3 sentences)

What the attendee can do at 4:00 that they could not do at 3:00. Concrete. No "understand" or
"learn about" — those are not things anyone can check.

### 2. What they leave with

A bulleted list of tangible outputs: a filled worksheet, a named decision, a written list.

### 3. Agenda

A table: minute range, segment name, what Rachael is doing, what the room is doing. The minutes
must add to 60. At least 15 of those minutes are the room working, not Rachael talking.

### 4. The teaching

Two or three ideas, no more. Each one gets:

- **The idea** in one sentence.
- **Where it comes from** — `[snip: <Title>](<link>)`.
- **What it means for a 10-person business** — the translation out of podcast language.
- **The example** — a real, specific scenario from the snips or from Rachael's client work.
- **The common objection** and the honest answer.

### 5. Live build

One thing Rachael builds on screen in 10 minutes or less. List the tool, the trigger, the steps,
and the visible result. Include what to do if the demo breaks.

### 6. The exercise

What the room does, on the handout, with timings. Include the exact instruction Rachael says out
loud, and two examples to unstick anyone who freezes.

### 7. Share-out and where this breaks

Three questions to ask the room. Then the honest limits: what this approach does not fix, and the
failure modes to warn about.

### 8. Close and the one-week assignment

One sentence that lands the promise. Then a single assignment small enough to finish in a week.

### 9. Facilitator notes

Timing risks, the segment to cut if running long, questions that will come up and the answers,
and anything to prepare beforehand.

### 10. Best practices nobody tells you

Two or three short, concrete practices for building the kind of automation this workshop teaches
— the kind of thing that only shows up after something has gone wrong once. These do not need a
snip behind them; they're operating knowledge, not podcast content. Each one gets:

- **The practice** in one sentence.
- **Why it bites people** — the failure it prevents, stated plainly.
- **The example** — tied to *this workshop's* live build or exercise specifically, not generic.

One of the 2–3 items is always a **stop condition**: a plain-English example of how the thing
being built in this workshop knows when to stop, pause, or hand off to a person, rather than
running forever or running past the point it's still right. Name the actual stop condition for
the actual example being built that day.

---

## handout.md

One page, printable, and designed to look good printed — real visual hierarchy (clear headings,
whitespace, maybe a simple rule or box), not a wall of text. No teaching content — this is a form,
not a summary.

- Title and one-line purpose.
- The worksheet itself: numbered prompts with blank space.
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
