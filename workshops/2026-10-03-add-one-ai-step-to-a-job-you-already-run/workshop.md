# Add One AI Step to a Job You Already Run

**Title:** Add One AI Step to a Job You Already Run
**Source:** AI Tools Daily snips, 2026-10-03: Snip 1 (Zapier Next Gen Zaps, Sept 24, 2026, https://www.linkedin.com/posts/zapier_introducing-next-gen-zaps-every-zap-now-activity-7508595458706038784-Sueb), Snip 2 (Zapier "AI by Zapier" migration, Sept 30, 2026, https://help.zapier.com/hc/en-us/articles/47402591569805-Migrating-from-Agents-to-AI-by-Zapier), Snip 12 (Nvidia Open Agent Safety Platform, Sept 28, 2026)
**Snips file:** `sources/snips/2026-10-03-ai-tools-trending.md`: 12 snips, 3 used here, 9 held for later
**Built:** 2026-10-03
**Teach date:** TBD
**Length:** 60 minutes
**Audience:** Small business owners and operators: no technical background assumed

## 1. The promise

In the next hour, you'll learn the single safest way to put AI inside a workflow you already run: one AI step, in one automation, with a checkbox that makes it ask you before it does anything consequential. You'll leave with a filled-in AI Step Card naming the exact step, the tools it may touch freely, the tools that need your tap, and what you'll watch for two weeks.

## 2. Agenda: 60 minutes

| Minutes | Segment |
|---------|---------|
| 0–8 | The week the agent became a step (opening frame) + the three ideas |
| 8–18 | The anatomy of an AI step |
| 18–28 | Watch it work (live demo: add an AI step to a real Zap) |
| 28–33 | Your questions |
| 33–58 | Build your own (independent work) |
| 58–60 | Wrap-up, share-out seed, and homework |

*Facilitator note:* the 33–58 block is the build session. Pair share-out and Q&A live inside it: circulate, then at minute 53 pull the room together for a 3-minute share-out ("read your card in thirty seconds") followed by questions to minute 58. Total: 25 minutes building, ~15 minutes Q&A, two minutes of close.

## 3. Facilitator script

### 0–8 · The week the agent became a step + the three ideas

Say it in your own words (keep it under eight minutes):

- "This week Zapier, the tool a lot of you already use to connect your apps, made a quiet but huge change. It took its standalone AI agents, the free-floating kind that wander around doing tasks, and folded them into the regular workflow builder as one step called 'AI by Zapier.' The agent stopped being the product. It became one step inside the workflow."
- "At the same time, Zapier announced that every automation will get an AI manager that watches it and fixes it when it breaks. And Nvidia, the chip company, launched a platform with a hundred partners just for watching agents and enforcing rules on them. Everybody shipped the coworker this week, and everybody shipped the supervisor in the same box."
- "Here's why that matters to you. The old question was 'should I trust an AI agent with my business?' That's the wrong question. The new question is: 'which ONE step in a workflow I already understand should the AI do, and what does it have to ask me about first?' That question has an answer you can build this week."

Three big ideas in plain words. Say them, then point at them all hour:

1. **The agent is a step, not the system.** Don't hand a whole process to a free-floating agent. Give the AI exactly one job inside a workflow you already understand: read this, draft that, score these. The rest of the workflow stays boring and predictable.
2. **The leash is a checkbox.** For every tool the AI step can use, you decide: free to use, or ask me first. Reading the email is free. Sending the reply, issuing the refund, placing the order: ask me first. Trust is not a feeling. It's a checkbox.
3. **Boring beats clever.** The steps that are the same every time stay automatic and cheap. The AI handles only what's genuinely new each time. And you watch the whole thing for a month before you let it do anything unsupervised. The boring version is the correct version.

"Yesterday's rule still holds: AI interprets, automation enforces, people control consequential actions. Today we're putting that rule inside one step."

### 8–18 · The anatomy of an AI step

"Every AI step has the same five parts. Learn the parts and you can read any automation anyone shows you."

Draw this on the board or a slide, left to right:

**1. The start signal.** A time or an event that kicks the workflow off. (Example: a new trial signup. Example: every morning at nine.)

**2. The boring steps before.** The deterministic work: create the contact, add the row, start the clock. Same every time, cheap, no AI needed.

**3. The AI step.** The one interpretive job. It reads something new, decides something, or drafts something. (Example: read the signup form, figure out what kind of business they are, draft a personal follow-up email.)

**4. The human gate.** The checkbox. You list the tools the AI step may use freely (read the CRM, look up the order) and the tools that need your tap (send the email, issue the refund, publish the post). Anything that spends money, promises something, or can't be undone waits for a person.

**5. The ceiling and the boring steps after.** A cap on how many tasks the agent may run before it stops (Zapier's default is seventy-five), so a confused agent can't loop forever on your dime. Then the workflow finishes the way it always did: send on schedule, stop if the customer upgraded.

"Notice what the AI does NOT do here. It doesn't decide who gets emailed. It doesn't choose the timing. It does one job: interpret and draft. The machine around it is in charge."

*Facilitator note:* if anyone asks about the "AI manager that fixes broken Zaps" (Next Gen Zaps), say: "That's the supervisor. It's in beta. Today we're learning the step; the supervisor watches the step. Same leash, one level up." Keep it to one minute.

### 18–28 · Watch it work

Add an AI step to a real Zap live. Use a workflow the room already knows: the inquiry triage from the last workshop, or a simple new-lead Zap. Zapier or Make, whichever you use. No installation for attendees: follow-along demo.

Narrate only the moving parts, in plain words:

1. "Here's the workflow we already trust." *(Show the existing Zap: new form submission, create contact, add to sheet.)* "Boring, reliable, been running for months."
2. "Here's the one new step." *(Add the AI step after the trigger: read the submission, score how good a fit they are, draft a personal reply.)* "One job. Interpret and draft."
3. "Here's the leash." *(Open the tool permissions: 'read the CRM' is free; 'send email' is set to ask me first. Point at the seventy-five-task ceiling.)* "Reading is free. Sending asks. And if it ever loops, it hits the ceiling and stops."
4. "Here's the gate in action." *(Run it once. Show the draft it made. Read the draft aloud.)* "The draft is sitting here waiting. Nothing reached a customer. Would you press send on that, edit it, or throw it away?"

Then ask the room: "What would you change about the draft?" That question teaches the whole workshop: the human is the quality control, and the AI is the intern with infinite patience.

*Facilitator note:* If it glitches, narrate the fix: "this is what maintaining one looks like." Ten minutes max, then open the floor.

### 28–33 · Your questions

Open floor. Answer in plain English. The three questions you'll get, and the answers:

- "What if the AI step does something wrong?": It can only do what its tools allow, and the dangerous tools need your tap. The worst it can do unsupervised is write a bad draft that sits in a queue. That's the whole point of the gate.
- "What does the AI step cost?": Pennies per run for the reading and drafting. The ceiling keeps a runaway loop from surprising you. The expensive part is not building it; the expensive part is the week you spend wondering whether to trust it. The gate answers that.
- "Should I wait for the self-healing version?": No. The self-healing manager is in beta and it watches automations; it doesn't replace learning the step. Build the step now, and the manager will have something worth watching later.

### 33–58 · Build your own

Everyone works solo or in pairs on the AI Step Card (see `handout.md`). Circulate with only these prompts:

- "Which workflow do you already trust? Start there. Don't invent a new one."
- "What's the ONE interpretive job inside it? Reading, drafting, scoring, deciding?"
- "Which tools are free, and which ones need your tap? Be specific."
- "What does failure look like for yours? What would the draft get wrong?"

At minute 53, pull the room together. Three-minute share-out: volunteers read their card in thirty seconds. "My AI step does ___. Free tools: ___. Needs my tap: ___."

Then Q&A to minute 58, and seed the "what could go wrong" story for anyone who asks:

**What could go wrong.** "This week Nvidia launched a whole platform, with a hundred partners, just for watching AI agents and enforcing rules on them. Why? Because agents loop, agents drift, and one misdirected agent hit a government website two hundred thousand times in a single day last month. And the week before, the FTC opened its first investigation into agents acting without supervision. The industry is building the supervisor because the coworker needs one. Your version of the supervisor is much simpler: the checkbox, the ceiling, and your own eyes on the drafts for the first month. That's the whole safety platform, and it fits on one card."

### 58–60 · Wrap-up and homework

"The agent is a step, not the system. The leash is a checkbox. Boring beats clever."

Homework: add one AI step to one workflow you already run, or fill in the card for it if you're not ready to build. It can be ugly. Run it in draft-only mode for two weeks: let it read and draft, you press every button. Bring back two things: did the drafts get better, and did the gate catch anything?

*Facilitator note:* hold up a filled AI Step Card as you say this. "Bring this card back filled in, or better, bring the step it describes."

## 4. Plain-English word list

Keep this on your facilitator copy. If you're tempted to say the left column, say the right column instead, and only use the product's own word after the plain version.

| Instead of... | Say... |
|---|---|
| Trigger | The start signal: a time or an event |
| AI step / agentic step | The one job the AI does: read, draft, score, or decide |
| Tool calling | The tools the step may use |
| Require approval / approval gate | The human gate: ask me first (the checkbox) |
| Task guardrail / task cap | The ceiling: the max runs before it stops |
| Deterministic step | A step that's always the same, every time |
| Fluid determinism | New situations get AI; repeated steps stay automatic and cheap |
| Self-healing / AI manager | The supervisor: watches the automation and fixes what breaks |
| Sub-Zap / agent-to-agent | One workflow calling another workflow for help |
| Observability / audit log | The receipts: what it read, what it did, who approved it |
