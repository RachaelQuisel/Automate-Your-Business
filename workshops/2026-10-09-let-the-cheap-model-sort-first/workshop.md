# Let the Cheap Model Sort First

**Title:** Let the Cheap Model Sort First
**Source:** Soft Fork snips, 2026-10-09: Snip 10 ("John Lindquist's 6 Jev Workflows for Apps, Data, and AI Agents", How I AI with Claire Vo, 2026-10-05, https://chatprd.ai/how-i-ai), Snip 6 (n8n free Jev decision-model window closes October 10, 23:59 UTC, 2026-10-05, https://dev.to/alifar/n8n-cloud-offers-free-jev-model-usage-through-gateway-credits-until-october-10-3epa)
**Snips file:** `sources/snips/2026-10-09-ai-tools-trending.md`: 12 snips, 2 used here, 10 held for later
**Built:** 2026-10-09
**Teach date:** TBD
**Length:** 60 minutes
**Audience:** Small business owners and operators: no technical background assumed

## 1. The promise

In the next hour, you will put a decider in front of one automation you already described: a cheap, fast model that answers in choices instead of paragraphs, so the expensive model only works on the items that matter. You will score a real batch of your own records, watch the big model stay silent on the easy ones, and leave with a written decision rule, a test you ran, and the habit of never paying the chef to check IDs at the door.

## 2. Agenda: 60 minutes

| Minutes | Segment |
|---------|---------|
| 0–8 | Opening frame: the six workflows + the three ideas |
| 8–18 | The decide-first pattern (decider, decision rule, doer) |
| 18–28 | Watch it work (demo: duplicate customer records, scored and cleaned) |
| 28–33 | Your questions |
| 33–58 | Write your decision rule (independent work) |
| 58–60 | Wrap-up, share-out seed, and homework |

*Facilitator note:* the 33–58 block is the build session. Pair share-out and Q&A live inside it: circulate, then at minute 53 pull the room together for a 3-minute share-out ("read your decision rule in thirty seconds") followed by questions to minute 58. Total: 25 minutes building, ~15 minutes Q&A, two minutes of close.

## 3. Facilitator script

### 0–8 · The six workflows + the three ideas

Say it in your own words (keep it under eight minutes):

- "Last week you learned to describe an automation in four lines: the trigger that wakes it up, the source where it reads, the transform that does the job, and the destination where the answer lands. The chat box builds the workflow from your words. That was yesterday's workshop."
- "This week Claire Vo, who runs a series called How I AI, aired an episode about a builder named John Lindquist. He walked through six real workflows built on a decision model called Jev. Voice-controlled apps, data deduplication, smart routing, chess, agent coordination, presentation coaching. Six different jobs. All six use the same shape: a small, cheap model makes the decision first, and the big expensive model only acts on what the decider passes through."
- "Jev is a decision model, which is a different kind of AI brain. Normal models write paragraphs. This one answers in choices: it is this, it is not this, or it does not know, plus how sure it is. The engineers call that a System One model, the way you know a face is a face without thinking about it. Fast gut read, typed answer, no essay."
- "And the timing matters. The decider he used is free inside n8n through tomorrow, October 10th, at 23:59 UTC. After that it costs the normal rate. But here is what I want you to hear: today we learn the pattern, not the product. After the window closes, any small cheap model can play the decider. The pattern is the skill. The free week is just the practice field."

Three big ideas in plain words. Say them, then point at them all hour:

1. **Decide first, act second.** The cheap decider sees everything. The expensive doer sees only what matters.
2. **A decision is a choice, not an essay.** The decider answers in picks and scores: duplicate or not, hot or cold, route A or route B. If it writes a paragraph, it is doing the wrong job.
3. **Watch what it does not do.** The savings are the calls you never paid for. Count the expensive model's silence as loudly as its work.

"Decide first, act second. A choice, not an essay. Watch what it does not do."

### 8–18 · The decide-first pattern

Draw the pattern on the board. Teach each part with the small-business version of Lindquist's data deduplication:

**Part 1: The pile.** "Every business has a pile. Duplicate customer records. Invoices that might be the same twice. Leads that show up in three places. The pile is what the expensive model would read one by one, billing you for every page."

**Part 2: The decision rule.** "You write the rule in one breath, the same way you wrote the four lines last week. 'Two customer records are the same person if the name matches and either the phone or the email matches.' The decider answers in scores: 0.95 means almost certainly a duplicate, 0.10 means almost certainly not. No paragraphs. Picks and numbers."

**Part 3: The decider.** "The cheap model reads the whole pile and scores every pair. It costs almost nothing per record. It answers in choices: duplicate, not duplicate, or unsure. The unsure ones go to a human. That is the job of the decider: check the IDs at the door, wave through the clear cases, flag the murky ones for the boss."

**Part 4: The doer.** "Only the likely duplicates go to the expensive model, which merges them carefully, writes the change log, and updates the list. The big model never sees the easy pairs. In Lindquist's workflow, that is where the money stays in your pocket: you did not pay the big model to read thousands of records just to say 'nope, not a duplicate' thousands of times."

Then the connection to yesterday's four lines:

**"The decider sits inside the transform."** "Take your four lines from yesterday. The trigger, source, and destination stay the same. The transform gets two steps now: first the decider scores, then the doer acts. Trigger: every Sunday night. Source: the customer list spreadsheet. Transform: the cheap decider scores duplicate pairs, the expensive model merges only the likely ones. Destination: the clean list, plus a review queue for the unsure cases. Same four lines. A bouncer at the door of the transform."

*Facilitator note:* name the deadline out loud. "The free Jev window inside n8n closes tomorrow, October 10th, at 23:59 UTC. Build your decision rule this week and you can test it for free. After that, the pattern still works: put a smaller, cheaper model, or even a plain simple model call, in the decider seat. The pattern is the lesson. The free week is the bonus."

Then the two traps, straight from the shape of Lindquist's six workflows:

**"The decider needs a real pile, and the unsure pile needs an owner."** "Trap one: scoring fake data. The decider looks perfect on a tidy sample and sloppy on your real records, because your real records are the mess. Test on the real pile, the one with the typos. Trap two: no owner for the unsure answers. The decider will say 'I do not know' on some records. If nobody is assigned to look at those, they pile up and rot. Name the person who reviews the unsure queue before you go live."

### 18–28 · Watch it work

Build one duplicate-record scoring demo live. No installation for attendees: follow-along demo, or narrate and map each part as you go. Keep it to ten minutes.

Work the example in plain words:

1. "Here is the pile." *(Show a messy customer list: "Maria Santos," "M. Santos," "Maria S." at the same phone number, plus clearly different people.)* "Every shop has this list. The question is which rows are the same person, and today a human squints at it on Sunday nights."
2. "Here is the decision rule." *(Write it on the board, reading aloud.)* "Same person if the name is close and the phone or email matches. Answer: duplicate or not, with a score, or unsure."
3. "Here is the decider." *(Run the cheap model over the pairs. Point at the scores: 0.98, 0.92, 0.55.)* "Fast. Cheap. No paragraphs. Just picks and numbers."
4. "Here is the doer, on only the likely ones." *(Only the high-score pairs go to the expensive model, which merges them and writes the change log.)* "Count what happened: the expensive model touched three pairs, not thirty. That silence is the savings."
5. "Here is the unsure pile." *(Point at the 0.55.)* "This one goes to the review queue, with a named owner. The decider does not guess. It flags."

*Facilitator note:* if the demo scores something oddly, celebrate it: "this is why we test on real data, and this is why the unsure queue exists." Ten minutes max, then open the floor.

### 28–33 · Your questions

Open floor. Answer in plain English. The three questions you will get, and the answers:

- "Do I have to use Jev or n8n for this?": "No. The pattern is the lesson, not the product. Any small, cheap model can sit in the decider seat, and yesterday's four-line formula works in any tool that builds from words. Jev is free inside n8n through tomorrow, which makes it a good practice field this week. After that, any simple cheap model call does the same job: read everything, answer in choices."
- "How much does this actually save?": "That depends on your pile, but the math is simple. Count what the expensive model used to read versus what it reads now. Every pair the decider answers with 'not a duplicate' is a call you did not buy. The roundup in today's research showed the same idea everywhere: Google routes work to the cheapest model per task, Microsoft splits work between the PC and the cloud, and everybody is metering now. The decider is your version of the same game."
- "What if the decider is wrong?": "Two kinds of wrong. Confident and wrong means your decision rule needs rewriting: test it on your real mess, not the tidy sample. Unsure means the system is working: that record goes to the named owner in the review queue. The worst case is not a wrong answer. The worst case is a decider nobody checks and an unsure queue nobody owns."

### 33–58 · Write your decision rule

Everyone works solo or in pairs on their decider plan (see `handout.md`). Circulate with only these prompts:

- "What is the pile? The list you pay to re-read, or the human squints at, over and over. Name it."
- "What is the decision, in one breath? Duplicate or not. Hot or cold. Route A or route B. If it takes two breaths, it is two deciders."
- "What does 'unsure' look like? Write the score range that goes to the human, and name the human."
- "What does the doer touch, and only the doer? Which expensive step sees only what the decider passes through?"
- "What is the free-week test? The deadline is tomorrow night. What real records will you score for free before it closes?"
- "And after the window: who is the decider then? Name the small cheap model or the simple model call that takes the seat."

At minute 53, pull the room together. Three-minute share-out: volunteers read their decision rule in thirty seconds. "My pile is ___. The decision is ___. The decider answers ___. The unsure ones go to ___. The expensive step only sees ___."

Then Q&A to minute 58, and seed the "what could go wrong" story for anyone who asks:

**What could go wrong.** "Two tales from the pattern. First, the overconfident decider. It scored a pile of leads hot-or-cold and routed half the warm ones to the delete pile, because the decision rule was written from a tidy sample and never tested on real leads. The fix is the real-pile test: score your actual mess, and look at the wrong ones yourself. Second, the orphaned unsure queue. The decider did its job and flagged forty records as unsure, and nobody was named to review them, so the pile sat for a month. The fix is the owner: name the person before you go live. The decider checks IDs. Somebody still works the rope."

### 58–60 · Wrap-up and homework

"Decide first, act second. A choice, not an essay. Watch what it does not do."

Homework: write one decision rule this week, before the October 10th free window closes. Score a real pile for free with the decider, count how many records the expensive step never had to read, and name the owner of the unsure queue. Bring back three things: your decision rule in one breath, what the real-pile test caught, and how many expensive calls you avoided. If the decider's scores were boring and the unsure queue was small, the rule was good.

*Facilitator note:* hold up a filled worksheet as you say this. "Bring this page back filled in, or better, bring the pile it scored."

## 4. Plain-English word list

Keep this on your facilitator copy. If you are tempted to say the left column, say the right column instead, and only use the product's own word after the plain version.

| Instead of... | Say... |
|---|---|
| Decision model / System One model | The cheap decider: the bouncer who checks IDs at the door |
| Jev (TypeSafe AI) | The decider in the demo, free to try through October 10th |
| Typed decision (choice, score, null) | A choice, not an essay: a pick, a score, or "unsure" |
| Calibrated probabilities | How sure it is, as a number |
| Downstream automation / LLM call | The expensive doer: the chef who only cooks |
| Smart routing / model routing | Sending each job to the cheapest brain that can do it |
| Data deduplication | Finding the same person twice in the pile |
| The unsure queue | The "I do not know" pile, with a named owner |
| Gateway credits / usage rates | What each run costs you |
| Trigger, source, transform, destination | Yesterday's four lines: what wakes it up, where it reads, the one job, where the answer lands |
| Unsure-queue owner | The person who works the rope |
