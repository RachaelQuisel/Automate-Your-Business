# Write Down What Each Job Taught You

**Title:** Write Down What Each Job Taught You
**Source:** Soft Fork snips, 2026-10-26: Snip 1 (gotcha, "Your AI Coding Agent Forgets Your Codebase Every Session. So I Gave It a Memory That Lives in Git", Medium, Damien Vauchel, 2026-10-26), Snip 6 (25 slash commands that replaced rewritten prompts, Claude AI post on LinkedIn, 2026-10-25), Snip 12 (too many skills and conflicting instructions, Natasha the Robot, 2026-10-26)
**Snips file:** `sources/snips/2026-10-26-ai-tools-trending.md`: 13 snips, 3 used here, 10 held for later
**Built:** 2026-10-26
**Teach date:** TBD
**Length:** 60 minutes
**Audience:** Small business owners and operators: no technical background assumed

## 1. The promise

In the next hour, you will start a short memory for one repeated job in your business, so the next person, or the next helper, or you next month, does not have to learn the same lesson a second time. You will learn the three steps, you will write your first cards, and you will put a person in charge of reading each new card before it becomes the way your business does things.

## 2. Agenda: 60 minutes

| Minutes | Segment |
|---------|---------|
| 0-8 | Opening frame: the lesson you paid for twice + the three ideas |
| 8-18 | The three steps, the card, the durability test, and the review |
| 18-28 | Watch it work (demo: one week of a home services and rental business, with the memory and without it) |
| 28-33 | Your questions |
| 33-58 | Build your memory for one repeated job (independent work) |
| 58-60 | Wrap-up, share-out seed, and homework |

*Facilitator note:* the 33-58 block is the build session. Pair share-out and Q&A live inside it: circulate, then at minute 53 pull the room together for a 3-minute share-out ("read one card and its three durability answers in thirty seconds") followed by questions to minute 58. Total: 25 minutes building, about 15 minutes Q&A, two minutes of close.

## 3. Facilitator script

### 0-8 · The lesson you paid for twice + the three ideas

Say it in your own words (keep it under eight minutes):

- "A builder named Damien Vauchel wrote on October 26, 2026 about a problem anyone who works with a helper will recognise. His coding helper forgot his project every time a new session started. It spent about ten minutes at the start of each job rediscovering facts it had already learned in an earlier session. One example stayed with him. A payment company can return a code that looks like success on a card that was refused, while the real answer hides in another field. The helper had learned that once, the hard way. Then it forgot, and had to learn it again."
- "So he built a small open source plugin called gotcha. The memory lives in plain files inside the project itself, where the whole team can read it. Every job runs the same three steps. Read the memory first. Do the job. Write back what the job taught, before the work is finished."
- "Your business does not need to write code for this to matter. Think of the house your crew has visited six times, where the same gate latch, the same breaker, and the same water shutoff surprise a different person each visit. Think of the rental turnover where the same question about the washing machine comes back every few weeks. The lesson was paid for the first time, in time and in worry. If nobody wrote it down where the next person looks first, you will pay for it again."

Three big ideas in plain words. Say them, then point at them all hour:

1. **Memory has to live where the work starts.** A lesson kept in one person's head, or buried in an old chat, or saved in a folder nobody opens, is not memory for the business. It is memory for one person, on one good day.
2. **One lesson, one small card.** A card is short enough to read before a job and clear enough to check during a job. A long report written after a hard day will not be read before the next one.
3. **Nothing becomes the way we do things until a person reads it.** A helper can draft a card. A person decides whether the card is true, complete, and safe to follow next time. That review is not extra work on top of the loop. The review is what makes the loop worth trusting.

"Recall. Act. Write back."

### 8-18 · The three steps, the card, the durability test, and the review

Teach the three steps on the board. Use a home services and rental care business with nine staff as the running example. The business cleans houses, turns over a small number of rentals between guests, and sends people out for small repairs and checks.

**Step one: recall before acting.** "Before the job starts, read the short memory first. Not the whole history of the business. Only the cards for this job, this house, this customer, or this kind of work. This takes two or three minutes when the memory is kept short. The point is simple. Start from what the business already learned, instead of starting from zero and hoping the right person remembers. If a card covers the problem in front of you, follow its check first. It was written to save exactly this time."

**Step two: act.** "Do the job. Dig deeper only when the memory is silent or stale. Silent means no card covers what you are seeing. Stale means a card exists but it is old, the house or the system has changed since it was written, or its source is too weak to trust for this decision. In those two cases, do the slower work: look, test, call, and check the original source. When the memory does cover the job and it still fits, do not repeat the full investigation out of habit. That saved time is the whole reason the memory exists."

**Step three: write back after.** "Before the job counts as finished, ask one question. What did this job teach us that the memory did not already say? If there is an answer, write one small card for that one lesson. One lesson per card, so a card can be found, read, and corrected on its own."

Teach the card, field by field:

- **What happened (the symptom):** what a person saw, heard, or was told, in plain words, without guessing the reason yet. Example opening line: "The kitchen lost power when the microwave and the kettle ran at the same time."
- **Why (the cause):** the reason, only as far as it was actually confirmed. If the reason was not confirmed, write that in this field instead of filling it with a guess.
- **How to check:** the short check the next person should do first, in order. One to three steps a person can do before calling for help.
- **The fix:** what solved it this time, or what to do when the check shows the same pattern again.
- **Source named:** who or what this came from, with a date where you have one. A named electrician and an invoice date. A call with a vendor and the name of the person who spoke. A guest message, a meter reading, a photo. A card with no source is an opinion, and it should say so.
- **Gaps marked "not confirmed":** write the exact words "not confirmed" for any part you did not check. Do not guess to make the card look finished. A card that honestly says the cause is not confirmed will send the next person to check. A card that guesses will send the next person down the wrong path with confidence.

**The durability test.** "Not every fact from a job belongs in the memory. Before a card is filed, ask three questions. The card must pass all three."

1. Is it not obvious at a glance? If anyone walking in would see it in ten seconds, it does not need a card.
2. Will it still be true next month? A one day delay, a temporary worker's preference, or a price that changes weekly will not pass. A breaker layout, a vendor portal that updates slowly, or a machine quirk that repeats will pass.
3. Would it have saved time today? If having this card at the start of today's job would not have changed anything, it is trivia, however interesting it is.

"If a card fails any one question, do not file it. Say so, and move on. A short memory that people trust beats a long memory that people skim and stop believing."

**The human review step.** "A person reads each new card before it becomes the way the business does things. The reviewer is a named person, not 'the team'. The reviewer checks four things: the symptom matches what actually happened, the source is named and can be found, every unconfirmed part is marked 'not confirmed', and the check and the fix are safe and clear enough for the next person to follow. The reviewer can approve the card as written, fix a small wording problem and approve it, or send it back with one clear reason. Until that review happens, the card is a draft. Label it as a draft where it lives, so nobody follows an unread card by mistake."

**The "nothing durable today" option.** "Some jobs teach nothing new, and that is a good result. On those days, write one line and stop: 'Nothing durable today.' Then give the date and the job name. That one line matters. It proves the write back step happened and the answer was honestly nothing, instead of leaving a gap that looks like somebody forgot. It also protects the memory from padding. Nobody should invent a lesson to avoid writing that line."

*Facilitator note:* name the two supporting lessons from the research out loud. "Two other stories from this week point the same way. One writer stopped rewriting the same prompts every Monday and turned each repeated explanation into a short saved instruction the helper reuses, because the file, not a person's memory, should carry the standard. That is Snip 6. Another writer found she had installed so many skills and plugins that their instructions conflicted and she could no longer see what her helpers were being told. That is Snip 12. Her fix was control: keep what sits in the helper's instructions visible, and only take updates from sources she had approved in advance. Keep your memory short, keep its sources named, and keep a person in charge of it, for the same reason."

### 18-28 · Watch it work

Work one example live. Use two printed weeks for the same home services and rental care business. Keep it to ten minutes.

1. "Here is the week without the memory." *(On Monday, a worker visits a rental house and finds the kitchen has no power. He calls an electrician, who finds that the microwave and the kettle share one circuit and the breaker has tripped. The visit takes an extra hour. On Thursday, a different worker at the same house hits the same problem, does not know about Monday, and starts the same calls again. On Friday, the office nearly pays a pool service invoice a second time because the vendor portal still shows it as open, even though the card payment went through on Wednesday. Nothing here is a skill problem. Every person worked hard. The business simply had no memory where the work starts.)* "The business paid for the breaker lesson twice in four days, and nearly paid a bill twice in the same week."
2. "Here is the same week with recall first." *(Before Monday's visit, the worker reads the cards for this house. There is no breaker card yet, so the memory is silent. He does the slower work, the electrician confirms the cause, and the job is not finished until a draft card is written.)* The draft card reads, in full: "What happened: the kitchen lost power when the microwave and the kettle ran at the same time. Why: both appliances share one circuit, confirmed by the electrician on site. How to check: check breaker six in the hall panel before calling an electrician. The fix: move the kettle to the dining room outlet and leave a note by the microwave. Source: electrician visit, invoice and date named on the card. Gaps: not confirmed whether the toaster on the same counter causes the same trip." *(A named reviewer reads the card that evening, checks the invoice, and approves it. On Thursday, the second worker reads that card first, checks breaker six, moves the kettle, and is back on the job in five minutes.)*
3. "Here is write back for a money lesson, not a house lesson." *(The office card reads: "What happened: the pool service portal showed an invoice as open two days after it was paid by card. Why: the portal updates slowly after card payments, confirmed on a call with the vendor office. How to check: look for the payment confirmation message before paying any invoice from this vendor a second time. The fix: wait two business days, check the confirmation, then check the portal again. Source: call with the vendor office, person named, date on the card. Gaps: not confirmed whether the same delay applies to bank payments.")* "That card passes all three durability questions. It is not obvious at a glance, because the portal looks like it is telling the truth. It will still be true next month. And it would have saved real money worry this week."
4. "Here is the durability test refusing a card." *(A worker proposes a card that says the traffic on the main road was bad on Tuesday. It fails question one in spirit and question two directly: it will not reliably be true next month, and it would not have saved time as a written rule. It is not filed. The worker writes 'Nothing durable today' for that part of the job instead.)* "Refusing trivia is not wasted effort. Every weak card you keep makes the strong cards harder to find and easier to doubt."
5. "Here is the review step catching a guess." *(A draft card says a washing machine at a rental 'probably needs a new pump' because it stopped mid cycle. The reviewer sends it back. The symptom is real. The cause was never checked. The card is rewritten: the cause field now says 'not confirmed', the check field says how to run the short test the repair person described, and the source names the person who ran the machine that day. The card can now help the next person without pretending to know more than the business knows.)* "The card got shorter and more honest, and that is why the next person can trust it."

*Facilitator note:* if the room says their helper cannot do some of this yet, answer with the shape point: "Start with paper or one shared document. The loop is the product. Recall, act, and write back work with a notebook, a shared file, or any helper you already pay for. Add a tool later, when the habit is real and the cards are piling up in a good way."

### 28-33 · Your questions

Open floor. Answer in plain English. The three questions you will get, and the answers:

- "Will this become a giant pile that nobody reads?": "Only if you skip the two guards you built today. The durability test keeps trivia out at the door, and one lesson per card keeps each card short enough to read before a job. Recall also means reading only the cards for this job or this house, not the whole file. If the memory for one job grows past about twenty cards, sit down for twenty minutes, merge the cards that say the same thing, and remove the ones that are no longer true. That clean up is part of owning a memory, in the same way the cleanup story in the research was part of owning a set of skills."
- "What if a card is wrong?": "That is what the source, the 'not confirmed' label, and the human review are for. A card names where it came from, so a wrong card can be traced and corrected instead of argued about. When a card turns out to be wrong in the field, do not quietly delete it and move on. Correct it the same day, note what changed and why, and let the reviewer read the correction. A memory that shows its corrections earns more trust than one that pretends it was always right."
- "How much time does this add to each job?": "About two or three minutes to recall at the start, and about five minutes to write back at the end, on a job that taught something. On a job that taught nothing, the write back is one line: 'Nothing durable today.' Compare that with the cost in the demo: an hour lost to a lesson the business had already paid for, repeated four days later. The loop is cheap on ordinary days and very cheap on the day it saves a repeat."

### 33-58 · Build your memory for one repeated job

Everyone works solo or in pairs on their memory for one repeated job (see `handout.md`). Circulate with only these prompts:

- "Read me the job you chose. How often does it repeat, and who does it besides you?"
- "What is the last lesson this job taught you twice? Start there."
- "Read your first card out loud. Where does the symptom stop and the cause start?"
- "Name your source out loud. Could another person find it from what you wrote?"
- "Show me one place you wrote 'not confirmed'. What would it take to confirm it?"
- "Run the durability test on that card, question by question. Say the answers out loud."
- "Who is your reviewer? Say the name. When will they read this week's cards?"
- "Where will this memory live, so the next person reads it before the job, not after?"

At minute 53, pull the room together. Three-minute share-out: volunteers read one card and its three durability answers in thirty seconds. "Today this job taught me ___. Next time, we will check ___ first."

Then Q&A to minute 58, and seed the "what could go wrong" story for anyone who asks:

**The failure gallery.** "The notebook that lived in one worker's truck, full of good lessons, that no other worker ever saw. The shared folder with two hundred long reports and no short cards, which everyone agreed was useful and nobody opened before a job. The helper that wrote confident cards with no sources, so the first wrong card made the team distrust all of them, including the true ones. The owner who filed every small fact from every job, until the memory was mostly trivia and the important cards drowned in it. The draft card that was followed before anyone reviewed it, because nobody had labelled it as a draft. Every one of these is prevented by a rule you used today: memory where the work starts, one lesson per card, a named source, 'not confirmed' instead of a guess, the durability test, and a person who reviews. None of them is prevented by buying a more powerful helper."

### 58-60 · Wrap-up and homework

Close in two minutes:

1. Restate the promise kept: "You now hold the start of a memory for one repeated job: the three steps written down, your first cards in the card format, the durability test, and a named reviewer who reads each new card before it becomes the way your business does things."
2. Homework (say it exactly): "This week, run recall, act, and write back on one repeated job for five workdays. Read the cards before each job. Write one card for each durable lesson, or write 'Nothing durable today.' Have your reviewer read every new card before the next workday starts. Bring your cards, and the one card your reviewer sent back, to your next session."
3. Final line: "You already pay for every lesson once, in time, money, or worry. Write it down, and you stop paying for it twice."

## Facilitator notes

- Keep all language plain. "Durability test" may be used only with its three questions stated in full, as they are stated in this plan and on the handout.
- Do not present any product named in the news as approved or recommended. The loop and the card are the deliverable; the products are the examples. Gotcha is an open source plugin described by its builder, and it should be described that way.
- Treat every vendor number and time saving in the source story as a claim the builder or the vendor made about itself, and say so when you use one. The ten minute rediscovery figure is the builder's reported experience from his own work, and should be described that way.
- Time discipline: protect the 25-minute build block. Cut Q&A before cutting building time.
