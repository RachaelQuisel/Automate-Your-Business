# The Failure Math: Stop Trusting the Demo, Start Testing Your Own Work

**Source:** The a16z Show — Why Real-World AI Is Harder Than the Benchmark | EliseAI's Mario Martone
**Concept:** The Failure Math — testing a tool on your own real cases, and multiplying its miss rate
by your own volume, before you trust it — 1 of an estimated 4 from this episode
**Snips file:** ../../sources/snips/2026-10-23-real-world-ai-harder-benchmark.md — snips used: Why
Benchmark Accuracy Is Not Enough, Test New Models On Your Own Stack, Why Essential Industries Raise
AI Stakes, Automating High-Stakes Workflows At Scale
**Built:** 2026-11-01
**Teach date:** TBD
**Length:** 60 minutes (30 teach / 30 open build + questions)
**Audience:** Small business owners and operators

---

## 1. The promise

By 4:00 you will have tested one AI tool or automation against 20 of your own real, messy cases —
not the clean demo examples the vendor showed you — and you will have a number: what percentage of
your own work it actually gets right. You will also know what that number means once you multiply
it by how much of that work you do in a month.

## 2. What they leave with

- A filled Failure Math Log: 20 real cases from their own business, each marked pass or fail by a
  human, for one tool or automation they're considering (or already run).
- One number: their own measured pass rate, not the vendor's.
- One projection: how many failures that pass rate produces every month at their real volume.
- A written pass-rate floor — the number below which the tool does not go live unsupervised.

## 3. Agenda — 30 minutes teach, 30 minutes open

| Minutes | Segment |
| --- | --- |
| 0–3 | Hook — the 95% tool that got pulled anyway |
| 3–10 | The concept + where it comes from |
| 10–15 | What it means for a 10-person business + the example |
| 15–19 | The receipts — two real stories, with links |
| 19–25 | The honest objection + FAQ |
| 25–30 | Bridge to the build: what we're building for the next 30 minutes |
| 30–55 | Open build — Rachael builds live, the room builds alongside, questions anytime |
| 55–60 | Close and the one-week assignment |

## 4. The concept

**The idea.** A benchmark score, a vendor's accuracy claim, or a good demo tells you how a tool did
on someone else's cases. It does not tell you how it will do on yours. Test it on your own real
work, count the misses, then multiply that miss rate by your own volume — because that number, not
the vendor's slide, is what actually lands on someone's desk every month.

**Where it comes from.**
[snip: Why Benchmark Accuracy Is Not Enough](https://share.snipd.com/snip/84efe4c4-d689-49b7-a1f5-59cd6fcd6fe6),
[snip: Test New Models On Your Own Stack](https://share.snipd.com/snip/9bce92fd-f928-4065-89f3-ef67c7ae0b53),
[snip: Why Essential Industries Raise AI Stakes](https://share.snipd.com/snip/ab91f0b0-4503-41de-a851-4d49fc2b3236),
and [snip: Automating High-Stakes Workflows At Scale](https://share.snipd.com/snip/4cdb38b7-4b63-4ebe-8268-3d62d8939f97).

**What it means for a 10-person business.** EliseAI's Mario Martone put a number on this: a 90%
accuracy rate looks great in a research paper. At EliseAI's real volume — roughly 60 million calls
a year — that "great" 90% means millions of wrong answers landing in front of a person. The team
doesn't trust the published number for a new model or provider; they run it against their own
stack and their own real conversations first, because that's the only test that tells them what
will actually happen at their scale.

You don't have 60 million calls a year. You might have 40 customer emails a week, or 200 invoices
a month. The math still works the same way. If a tool is "90% accurate" and you run 200 invoices
through it a month, that's 20 invoices a month that come out wrong — and somebody has to notice
that, or your books are wrong and nobody knows it yet. The percentage sounds small. The count
doesn't.

**The example.** Say you're considering an AI tool to draft replies to inbound customer questions.
The vendor says 92% accurate. Before you turn it loose: pull 20 real questions from your own inbox
from the last two weeks — the weird ones, the ones with typos, the ones where the customer is
annoyed — and run all 20 through the tool. Have a person read every single output and mark it pass
or fail. If it gets 15 of 20 right, that's 75% on your real work, not 92%. If you get 60 inbound
questions a week, 75% means 15 wrong replies a week going out under your business's name unless a
person catches them first.

**The receipts.**

- **McDonald's pulled its AI drive-thru after three years of live testing.** McDonald's and IBM
  ran an AI order-taking system at around 100 restaurants starting in 2021, aiming for a 95%+
  accuracy rate before wider rollout. Once it was running against real drive-thru noise and real
  customers — not a controlled demo — it started making viral, costly mistakes: adding $211 of
  chicken nuggets to a stranger's order, piling nugget after nugget onto one car's tab while the
  customers laughed and asked it to stop, and adding bacon to a soft-serve ice cream. McDonald's
  shut the test off in mid-2024. The lesson for a small business: a tool that looked ready enough
  to pilot at scale still needed real, messy, real-world cases to find its actual failure rate —
  and the failures that showed up were exactly the kind a quick real-world test would have caught
  early, before they went viral. ([Nation's Restaurant News](https://www.nrn.com/quick-service/mcdonald-s-is-ending-its-ai-drive-thru-test-with-ibm))
- **Air Canada had to pay for an answer its chatbot made up — and "it usually works" was not a
  defense.** In 2024, Canada's Civil Resolution Tribunal ruled Air Canada liable after its website
  chatbot wrongly told a grieving customer he could claim a bereavement discount *after* booking a
  full-price ticket, when the real policy required requesting it beforehand. Air Canada argued the
  chatbot was "a separate legal entity" responsible for its own words; the tribunal rejected that
  and ordered the airline to pay the refund plus damages. Nobody had tested the bot against that
  specific, real customer question before it went live. The lesson: once a tool answers in your
  business's name, "it's usually right" doesn't matter — the one untested edge case that's wrong
  is the one that costs you. ([CBS News](https://www.cbsnews.com/news/aircanada-chatbot-discount-customer))

**The common objection.** *"The vendor already tested it — isn't that enough?"*

The honest answer: they tested it on their data, with their examples, written by people who don't
know your customers, your product names, or the specific way your business gets asked for things.
Your test is cheap — an afternoon, 20 real cases, one person reading the outputs. A wrong number
published under your name, or a decision made on a bad automated output, costs a lot more than an
afternoon.

**FAQ**

- *"How many cases do I need to test before I trust the number?"* Twenty is a reasonable floor for
  a 60-minute workshop and a first pass. More matters less than realness — ten real, messy, recent
  cases beat a hundred invented clean ones.
- *"What if it fails on something rare — do I need 100% before I use it at all?"* No. You need to
  know exactly where it fails and build the escape hatch for that specific failure, not demand
  perfection nobody's tool has.
- *"What's a 'good' pass rate?"* It depends on what a miss costs. A wrong drive-thru order is a
  refund. A wrong answer about a legal deadline or a medical appointment is a different kind of
  expensive. Set your floor by the cost of being wrong, not by a round number that feels safe.
- *"Doesn't testing like this just slow down adoption?"* It costs an afternoon once. Compare that
  to the cost of a public failure or a customer who got the wrong answer and acted on it.
- *"The tool passed my test today — am I done?"* No. Re-test whenever the tool, the model behind
  it, or your own process changes. A pass rate from six months ago doesn't cover today's version.

## 5. Live build — the Failure Math Log, 25 minutes

**What Rachael builds on screen:** a reusable test log for any AI tool or automation under
consideration.

- **Tool:** Airtable (one table + two formula fields + one automation). A spreadsheet works the
  same way if that's what already holds the business's data.
- **Trigger:** a new row is added to the `Failure Math Log` table with a real case, the tool's
  output, and a human's Pass/Fail judgment.
- **Step 1:** a formula field computes the running pass rate: passes ÷ total tested so far.
- **Step 2:** a second formula field takes that pass rate, subtracts it from 100%, and multiplies
  by a `Monthly Volume` number the owner enters once — producing "projected wrong outputs per
  month at my real volume."
- **Step 3 (automation):** when at least 20 rows exist and the pass rate is below a `Pass Rate
  Floor` number also entered once, the automation posts a task or alert: "This tool is below your
  floor — do not turn it loose unsupervised yet."
- **Visible result:** add a few real pass/fail rows live, and watch the pass rate and the monthly
  failure projection update, then watch the floor alert fire if the number drops low enough.

**Say while building:** "This isn't a fancy tool. It's twenty rows and two formulas. The twenty
real cases are the only hard part, and that part is on you, not on Airtable."

**If the demo breaks:** have a second tab with the same base already populated with 20 test rows
and a visible pass-rate and projection. Switch to it, say "here's one already run," and keep going.

## 6. Open build and questions

**What the room is doing:** pulling 20 of their own real cases for one tool or automation they're
weighing (or already run unsupervised), building the same log, and scoring the cases by hand while
the base does the math.

**What to circulate and watch for:**
- People reaching for clean, easy examples instead of their actual messy backlog. Push them back to
  their real inbox, their real last month of invoices, their real customer list.
- People arguing with themselves over a borderline pass/fail. Tell them: if you'd have to quietly
  fix it before a customer saw it, it's a fail.

**Restart line if the room stalls:** "Open whatever this tool touches right now — your inbox, your
invoice folder, your call log — and copy the next five real items into the log. Don't pick, just
take the next five."

**Two-speed room:** a fast finisher who hits 20 rows can set their pass-rate floor and watch the
alert logic fire by typing in a few deliberately bad rows. Someone still stuck at five rows with
five minutes left should stop building the base and just finish scoring the rows they have by
hand — the number matters more than the automation around it today.

## 7. Close and the one-week assignment

**The close:**

> "The vendor's number tells you what their tool can do. Your twenty rows tell you what it will do
> in your business. Only one of those numbers should decide whether you trust it with real work."

**The assignment:**

> "Pick the one AI tool in your business you have never actually tested — the one you just started
> trusting because it seemed fine. This week, pull 20 real cases and score it. Write the pass rate
> on a sticky note on your monitor. That's the whole assignment."

## 8. Facilitator notes

**Prepare beforehand:**
- Airtable base with the `Failure Math Log` table, the two formula fields, and the floor-alert
  automation already built and tested.
- A second tab with 20 rows already scored, for the demo-breaks fallback.
- Printed handouts — scoring by hand on paper while the base runs is often faster than typing
  directly into Airtable mid-session.

**Timing risks:**
- Pulling "real" cases can turn into ten minutes of people hunting for their login instead of
  testing. Tell them up front: email, text export, call log, whatever's fastest to open.
- The floor-alert automation is the part most likely to eat time if someone's trigger logic
  doesn't fire. It's also the part most skippable — if time is short, cut it and just teach the
  two formula fields.

**Questions that will come up:**
- *"Can I test a tool I haven't bought yet?"* Yes — most vendors will let you run a trial batch.
  Ask for that explicitly before you sign anything; it's a reasonable ask and a serious vendor
  will expect it.
- *"What if I don't have 20 real examples yet because the business is new?"* Use the closest thing
  you have — even 8 or 10 — and say out loud that the number is less certain. Re-test at 20 once
  you have them.
- *"Who should be the person marking pass/fail?"* Whoever would normally catch the mistake today —
  usually the person already doing the work by hand. They know what "wrong" looks like fastest.

## 9. Best practices nobody tells you

- **The practice:** Pull your test sample from this month's real, unfiltered work — not the
  cleanest five examples you'd put in a sales deck. **Why it bites people:** a test built from easy
  cases always passes, and the first real failure then shows up in front of a customer instead of
  in your log. **The example:** in today's build, that means grabbing the next 20 items off the
  actual inbox or invoice pile in order, not the 20 that happen to look tidiest.
- **The practice:** Re-run the test every time the tool, the model behind it, or your own process
  changes — a six-month-old pass rate doesn't cover today's version. **Why it bites people:**
  vendors update models silently; a tool that passed in spring can fail in fall without anyone
  telling you. **The example:** set a recurring reminder to re-score 10 fresh rows in the Failure
  Math Log every time you notice the tool's output style change, not just once a year.
- **The practice — stop condition:** write your pass-rate floor down before you see the first
  result, and if the Failure Math Log's automation fires the "below your floor" alert, the tool
  stays routed to a person for every case, full stop, until it's re-tested and clears the floor.
  **Why it bites people:** without a number written down in advance, a disappointing result gets
  argued away in the moment ("it's probably fine"). **The example:** in today's build, that's the
  exact automation step — 20 rows, pass rate below the floor, alert fires, tool does not leave test
  mode.

**Snips not used in this workshop** (available for a later session — see the snips file): Why LLMs
Are Not Always The Answer and Choose Models By The Problem (a separate "pick the right tool for the
job" workshop), From Apartment Search To Automated Move-In (an end-to-end automation design
workshop), and Hire Researchers Who Want Real-World Impact (thin business-owner angle, likely
unused).
