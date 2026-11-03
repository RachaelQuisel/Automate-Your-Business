# Turn One Repetitive Task Into an Automation in Four Lines

**Title:** Turn One Repetitive Task Into an Automation in Four Lines
**Source:** AI Tools Daily snips, 2026-10-08: Snip 11 ("Day 10" n8n AI Assistant video, 2026-10-07, https://www.youtube.com/watch?v=Pux2mmIH1GA), Snip 8 (n8n Cloud free Jev decision-model usage through October 10, 2026-10-05), Snip 7 (Diagrid durable execution for n8n, 2026-10-06)
**Snips file:** `sources/snips/2026-10-08-ai-tools-trending.md`: 14 snips, 3 used here, 11 held for later
**Built:** 2026-10-08
**Teach date:** TBD
**Length:** 60 minutes
**Audience:** Small business owners and operators: no technical background assumed

## 1. The promise

In the next hour, you will turn one repetitive task into a running automation using four lines of plain English. You will write the trigger, the source, the transform, and the destination. You will watch an AI assistant build it from your words, test it on real data, and apply the three production rules before it goes live. You will leave with one automation described, one automation tested, and the discipline to keep it honest.

## 2. Agenda: 60 minutes

| Minutes | Segment |
|---------|---------|
| 0–8 | Opening frame: the week the wiring died + the three ideas |
| 8–18 | The four-line formula (trigger, source, transform, destination) |
| 18–28 | Watch it work (demo: one email automation, described, built, and tested) |
| 28–33 | Your questions |
| 33–58 | Describe your automation (independent work) |
| 58–60 | Wrap-up, share-out seed, and homework |

*Facilitator note:* the 33–58 block is the build session. Pair share-out and Q&A live inside it: circulate, then at minute 53 pull the room together for a 3-minute share-out ("read your four lines in thirty seconds") followed by questions to minute 58. Total: 25 minutes building, ~15 minutes Q&A, two minutes of close.

## 3. Facilitator script

### 0–8 · The week the wiring died + the three ideas

Say it in your own words (keep it under eight minutes):

- "For years the pattern was this. If you wanted an automation, you wired it. You dragged little boxes around a screen, connected them with lines, configured each one, and prayed the lines stayed connected. It was plumbing. Skilled people charged good money for the plumbing, and everybody else just did the repetitive task by hand."
- "This week the wiring died. A creator doing a series called 30 Days, 30 AI Agents posted day ten, and the whole video is him building real automations by typing plain English into a chat panel. No dragging boxes. He types four lines describing the job, and the AI assistant builds the automation. Three real builds, live on camera: an email summary, a chatbot with memory, and a multi-step agent workflow."
- "And the timing matters. Right now, through October 10th, the decision model he uses for the cheap routing step is free inside n8n. Two days left. So today you will learn the four-line formula, and this week you can try it for free."

Three big ideas in plain words. Say them, then point at them all hour:

1. **Describe it, don't wire it.** Four lines of plain English replace the plumbing: what wakes it up, where it reads, what it does, where the answer goes.
2. **Test on real data before you publish.** The demo is not the deployment. Run it on your real emails, your real receipts, your real mess, and watch what it does before any customer sees it.
3. **Boring is the promotion criterion.** The three production rules decide what goes live. If the first run was boring, the description was good.

"Describe it, don't wire it. Test on real data. Boring is the promotion."

### 8–18 · The four-line formula

Write the four lines on the board. Teach each one with the email example:

**Line 1: Trigger. "When does it wake up?"** "The trigger is the alarm clock. New email arrives. New row appears in the spreadsheet. Every morning at seven. Nothing happens until the trigger fires. If you cannot name the trigger in one breath, you do not have an automation yet, you have a wish."

**Line 2: Source. "Where does it read?"** "The source is where it looks. Your inbox. The receipts folder. The order spreadsheet. Name the exact place. 'My email' is not a source. 'The info@ inbox, unread, with attachments' is a source."

**Line 3: Transform. "What does it do?"** "The transform is the job. Summarize the email into three bullet points. Sort the receipts by vendor and month. Score the lead hot, warm, or cold. One job. If it takes two breaths to say, it is two automations."

**Line 4: Destination. "Where does the answer go?"** "The destination is where the result lands. A morning digest email. A Slack message. A new row in the tracker. Name the exact landing spot, and name who reads it."

Then the money line, the one that saves the token budget:

**"Put the cheap decider in front of the expensive doer."** "Here is the pattern the whole industry settled on this month. A small, cheap, fast model makes the decision: is this email urgent or not, is this lead hot or cold, which pile does this receipt go in. Then the big expensive model only works on the items that matter. The cheap model is the bouncer. The expensive model is the chef. You do not pay the chef to check IDs at the door."

*Facilitator note:* name the deadline out loud. "The Jev decision model is free inside n8n through October 10th at the end of the day. After that it costs the normal rate. That is your homework window."

Then the credentials warning, straight from the video:

**"The automation will ask for your passwords, and you decide what it gets."** "To read your inbox, it needs access to your inbox. Give it the narrowest access that works. A dedicated login beats your main password. Read-only beats read-and-send. The automation is an employee: it gets a key to the office, not a key to the safe."

### 18–28 · Watch it work

Build one email-summary automation live using the AI Assistant chat panel. No installation for attendees: follow-along demo, or narrate and map each part as you go. Keep it to ten minutes.

Work the example in plain words:

1. "Here is the repetitive task." *(Say it: "Every morning I dig through forty emails to find the five that need me.")* "That is the sigh. The automation goes where the sigh is."
2. "Here are the four lines." *(Type them into the chat panel, reading aloud.)* "Trigger: every weekday at 7 AM. Source: the info@ inbox, unread from the last 24 hours. Transform: summarize each email into one line, flag anything asking for money or a decision. Destination: one digest email to me with the flags on top."
3. "Here is the build." *(Let the assistant generate the workflow. Narrate: "I described it. It wired it. That is the whole trick of this week.")*
4. "Here is the test." *(Run it on real emails, or a realistic sample. Point at one summary it got wrong or one flag it missed.)* "This is the important minute. The demo worked. The test found the rough edge. The test is the job."
5. "Here are the three production rules." *(Read them off the handout.)* "One: it ran on real data, not a perfect sample. Two: I know exactly what it touches and what it cannot touch. Three: if it breaks halfway, it resumes where it stopped instead of starting over and emailing everyone twice."

*Facilitator note:* if the build glitches, narrate the fix: "this is what managing one looks like." Ten minutes max, then open the floor.

### 28–33 · Your questions

Open floor. Answer in plain English. The three questions you will get, and the answers:

- "Do I need to learn n8n for this?": "Not the wiring part. The chat panel builds the workflow from your four lines. What you need to learn is the describing part, which is what we are doing today. The four-line formula works no matter which tool you end up using. Describe it well, and any tool can build it."
- "What does it cost after the free window?": "The decision model goes back to the normal usage rate after October 10th. The pattern still holds: cheap decider in front, expensive doer behind. Budget it the way you budget any employee. The cheap model checks IDs at the door, the expensive model cooks. You would not pay chef wages for door work."
- "What if it breaks halfway through and does everything twice?": "That was the week's other story. The new durable execution layer checkpoints every step, so a crashed workflow resumes where it stopped instead of restarting. Ask your tool whether it resumes or restarts. Resumes is production. Restarts is a demo with a double-email feature."

### 33–58 · Describe your automation

Everyone works solo or in pairs on their four-line prompt (see `handout.md`). Circulate with only these prompts:

- "What is the repetitive task? The one you sigh at every week. Name it."
- "What is the trigger? When does it wake up? One breath."
- "What is the source? The exact place it reads. Not 'my email.' The exact inbox, folder, or sheet."
- "What is the transform? The one job. If it takes two breaths, it is two automations."
- "What is the destination? Where does the answer land, and who reads it?"
- "Now the test plan. What real data will you run it on first? What is the rough edge you expect?"
- "And the three production rules. Check each one. Would you bet a customer email on this yet?"

At minute 53, pull the room together. Three-minute share-out: volunteers read their four lines in thirty seconds. "My task is ___. Trigger: ___. Source: ___. Transform: ___. Destination: ___. I will test it on ___."

Then Q&A to minute 58, and seed the "what could go wrong" story for anyone who asks:

**What could go wrong.** "Two tales from this week. First, the double email. A workflow crashed on step eight of ten, restarted from zero, and emailed the customer twice. The fix is the resume question: does your tool resume where it stopped or restart from the beginning? Second, the confident wrong summary. The automation summarized forty emails beautifully and flagged the wrong one as urgent, because the cheap decider was never tested on real data. The fix is the test rule: real data before any customer sees it. The description is the easy part. The test is the job."

### 58–60 · Wrap-up and homework

"Describe it, don't wire it. Test on real data. Boring is the promotion."

Homework: build one automation this week, before the October 10th free window closes. Four lines, built in the chat panel, tested on your real data, three production rules checked. Bring back three things: your four-line prompt, what the real-data test caught, and what the first boring run felt like. If the first run was boring, the description was good.

*Facilitator note:* hold up a filled worksheet as you say this. "Bring this page back filled in, or better, bring the automation it describes."

## 4. Plain-English word list

Keep this on your facilitator copy. If you are tempted to say the left column, say the right column instead, and only use the product's own word after the plain version.

| Instead of... | Say... |
|---|---|
| AI Assistant / canvas chat panel | The chat box that builds the workflow from your words |
| Trigger | The alarm clock: what wakes it up |
| Source | Where it reads |
| Transform | The one job it does |
| Destination | Where the answer lands |
| Decision model / System One model | The cheap decider: the bouncer who checks IDs at the door |
| Downstream automation / LLM call | The expensive doer: the chef who only cooks |
| Gateway credits / usage rates | What each run costs you |
| Durable execution / checkpointing | It resumes where it stopped instead of starting over |
| Duplicate side effects | Doing the loud steps twice, like emailing the customer twice |
| Credentials / OAuth scope | What keys you hand it, and how narrow they are |
| Production rules | The three checks before anything goes live |
| RAG chatbot | A chatbot that reads your documents before answering |
| Embedding gotcha | The fiddly setup step that bites everyone once |
