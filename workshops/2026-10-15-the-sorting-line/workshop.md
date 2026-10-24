# The Sorting Line: Teach One Decision to a Cheap Model, Not a Chatbot

**Source:** How I AI — Jev: 8 real use cases for the fastest, cheapest model I've ever used | John Lindquist
**Concept:** The Sorting Line — 1 of an estimated 5 from this episode
**Snips file:** ../../sources/snips/2026-10-14-jev-fastest-cheapest-model.md — snips used: Jev Turns Human Language Into Decisions, Constrained Interfaces Make Jev Powerful, Design Jev Around Classification Points, Jev Deduplicates Messy Records In Milliseconds, Add Classification Layers When Jev Falls Short
**Built:** 2026-10-15
**Teach date:** TBD
**Length:** 60 minutes (30 teach / 30 open build + questions)
**Audience:** Small business owners and operators

---

## 1. The promise

By 3:30 you'll know the difference between a decision and a conversation — and you'll be able to
spot the decisions hiding in your business that don't need a chatbot at all. By 4:00 you'll have
built (or started building) one of those: an automation that reads something messy and picks
exactly one answer from a short list you wrote down yourself, every single time.

## 2. What they leave with

- One working (or half-built) "sorting line" automation pointed at a real repetitive decision in
  their business.
- A written list of the exact allowed answers it's allowed to give — never a blank reply box.
- A filled handout showing the messy input it reads and which answer on the list it should pick.

## 3. Agenda — 30 minutes teach, 30 minutes open

| Minutes | Segment |
| --- | --- |
| 0–3 | Hook — the decision everyone keeps re-making by hand |
| 3–10 | The concept + where it comes from |
| 10–15 | What it means for a 10-person business + the example |
| 15–19 | The receipts — two real stories, with links |
| 19–25 | The honest objection + FAQ |
| 25–30 | Bridge to the build: what we're building for the next 30 minutes |
| 30–55 | Open build — Rachael builds live, the room builds alongside, questions anytime |
| 55–60 | Close and the one-week assignment |

## 4. The concept

**The idea.** Most of what feels like "I need an AI assistant" is actually "I need one decision
made, over and over, from a short list of options I already know." A sorting line doesn't hold a
conversation. It reads one messy thing and picks exactly one answer from a list you wrote down in
advance — nothing more, nothing improvised.

**Where it comes from.** [snip: Jev Turns Human Language Into Decisions](https://share.snipd.com/snip/31d7ee81-5a81-494c-8ba2-aa4c364d98df),
[snip: Constrained Interfaces Make Jev Powerful](https://share.snipd.com/snip/585ae2b0-8ca8-4a78-968d-b0dd30b248c4),
[snip: Design Jev Around Classification Points](https://share.snipd.com/snip/820f228b-0dd8-4b25-898c-068b90d8f93a),
and [snip: Add Classification Layers When Jev Falls Short](https://share.snipd.com/snip/55b4349e-5bdf-483f-b519-91c6b31e2149).

**What it means for a 10-person business.** The podcast's example is a developer who stopped
asking a general-purpose chatbot to "figure out what I mean" and instead built a small, fast,
cheap model whose only job is to pick one answer from a fixed list — a switch statement, not a
conversation. Your business runs dozens of these moments every day without calling them that:

- Which inbox does this email belong in — new inquiry, support question, or spam?
- Is this invoice a duplicate of one already in the system, or a new one?
- Is this lead inside the area we serve, or outside it?
- Is this a complaint that needs a person today, or a routine question that can wait?

None of those need a conversation. Each one needs exactly one answer from a short list you could
write on an index card. That's the test: if you can list every possible right answer in advance,
it's a decision, not a chat.

**The example to use.** [snip: Jev Deduplicates Messy Records In Milliseconds](https://share.snipd.com/snip/a5d8a19d-3a43-462d-beaa-be71c77e2d32)
describes matching "Cedar Grove Office Products" and "Cedar Grove Office" as the same company in
milliseconds — not by generating a paragraph explaining the match, but by answering one question:
same company, yes or no? That's a decision with exactly two allowed answers. Walk the room through
how often their own customer or vendor list has the same kind of near-duplicate sitting in it right
now, found by nobody because nobody has time to read the whole list by eye.

**The common objection.** *"Isn't this just the same if/else logic I could write myself?"*

Sometimes, yes — and if it is, write the plain rule and skip AI entirely; an invoice over $5,000 is
just a number comparison. AI earns its place at the moment the deciding factor gets fuzzy: two
company names that are almost the same but not identical, an email that's clearly urgent but
doesn't use the word "urgent," a lead that's a judgment call. The skill this workshop teaches is
spotting which of your business's decisions are secretly fuzzy, then building exactly one narrow
tool for that one fuzzy moment — not a general assistant that tries to handle everything.

**The receipts.**

- In February 2024, a Canadian tribunal ruled against Air Canada after its website chatbot
  invented a bereavement-fare refund policy that didn't exist. A customer, Jake Moffatt, asked the
  bot about bereavement fares after a family death; the bot told him to book a regular ticket and
  apply for a retroactive partial refund within 90 days — advice that contradicted Air Canada's
  actual policy. The airline argued the chatbot was a "separate legal entity" it wasn't responsible
  for. The tribunal rejected that and ordered Air Canada to pay. The bot had been given an
  open-ended conversational job — "answer whatever the customer asks" — when the actual job needed
  was a narrow decision with a fixed, correct list of answers: refundable, not refundable, or ask a
  person. [Air Canada Held Responsible for Chatbot's Hallucinations](https://aibusiness.com/nlp/air-canada-held-responsible-for-chatbot-s-hallucinations-),
  [Air Canada tried to claim it wasn't responsible for its chatbot's false promises — but that didn't fly in court](https://www.tomsguide.com/ai/air-canada-tried-to-claim-it-wasnt-responsible-for-its-chatbots-false-promises-but-that-didnt-fly-in-court)
- In December 2023, an engineer got a Chevrolet dealership's ChatGPT-powered sales chatbot to agree
  to sell a 2024 Chevy Tahoe for $1, by instructing it to agree with everything the customer said
  and to end every reply with "that's a legally binding offer." The dealership never honored the
  "sale," but the stunt went viral and the bot had to be taken offline and fixed. A sales chatbot
  that can be talked into anything is the mirror image of a sorting line: it had no fixed list of
  allowed answers, so a determined customer could walk it anywhere. [We Tried To Buy A $1 Ford Bronco From AI Chatbots. It Didn't Work](https://www.motor1.com/news/701402/ford-bronco-chat-bot/),
  [Dealer's AI chatbot agrees to sell new car for just $1](https://gigazine.net/gsc_news/en/20231220-gm-dealer-chat-bot-tricked)

**FAQ**

- *"Isn't this just basic code, not really AI?"* Sometimes — and that's fine. If the rule is clean
  (an amount above or below a number), write the plain rule and don't bother with AI. Use a sorting
  line where the call is fuzzy: messy wording, inconsistent names, a judgment a person currently
  makes by eye.
- *"What if it picks the wrong bucket?"* That's exactly why "not sure — send to a person" is always
  one of the allowed answers, never an afterthought. A wrong guess among a few good buckets is rare
  and easy to catch; a chatbot inventing a whole paragraph of policy, like Air Canada's, is much
  harder to catch and much more expensive when it's wrong.
- *"Do I need an expensive AI plan for this?"* No. The entire point of a narrow decision is that it
  doesn't need your most powerful (or priciest) model. Save the expensive tool for genuinely
  open-ended work; sorting is cheap by design.
- *"Can this handle it if the customer writes back and asks a follow-up?"* Not this build. A
  sorting line answers one question and stops — it doesn't carry on a conversation. If you want
  back-and-forth replies, that's a different, much riskier tool to build, for exactly the reason
  the Chevy dealership found out.
- *"What if two categories both kind of fit?"* Decide the tie-break in advance, on paper, the way
  you'd settle a disagreement between two employees — "if it could be either A or B, it's always
  A." Writing that rule down before you build is faster than debugging a surprise later.

## 5. Live build — sorting new inbound leads and emails, 25–30 minutes

**What Rachael builds on screen**, scoped to fill the whole open-build block:

- **Tool:** Airtable (a table + an automation with an AI "pick one" step). Any tool that can run an
  AI classification step into a single-select field works the same way.
- **Trigger:** a new row appears in an `Inbox` table (fed by a form, a forwarded email, or a
  Zapier/Make connection to the real inbox).
- **Step 1:** write down the exact allowed answers before touching the automation — in this build:
  `New client inquiry`, `Support question from existing client`, `Spam or vendor pitch`, `Not sure
  — needs a person`.
- **Step 2:** the AI step reads the subject and body and sets one single-select field, `Category`,
  to exactly one of those four values — never free text.
- **Step 3:** route by category: new inquiries go to a `Leads` view, support questions go to a
  `Support` view, spam gets archived, and anything landing in `Not sure` stays visible at the top
  for a person to glance at.
- **The cap (stop condition):** if the model's confidence is low, or the message doesn't clearly
  match one of the first three categories, it must land in `Not sure — needs a person` rather than
  guess. It is never allowed to reply to the sender on its own.
- **Visible result:** a test email lands in the table and, seconds later, its `Category` field
  fills in on screen and it jumps into the right view.

**If the demo breaks:** have a pre-built version with a populated run history open in a second
tab. Switch to it, say "here's this morning's real sort," and keep going.

## 6. Open build and questions

- **What the room is doing:** building the same shape — one inbox or list, one short list of
  allowed answers, one single-select field — pointed at their own repetitive decision: inbound
  leads, support tickets, vendor invoices, duplicate customer records.
- **What to circulate and watch for:** people write an open text field instead of a fixed
  single-select, which quietly turns their sorting line back into a chatbot. Stop and convert it to
  single-select before anything else. Also watch for a missing "not sure" option — every list needs
  one.
- **Restart line if the room stalls:** "Say the sentence out loud: 'Every time ___ comes in, it's
  always one of these: ___, ___, ___, or I'm not sure.' Whatever fills those blanks is your build."
- **Two speeds:** a fast finisher adds a confidence threshold or a second classification layer
  (e.g., first decide if it's a real lead at all, then which category). Someone still stuck with
  five minutes left should stop building and just write out their short list of allowed answers by
  hand on the handout — that alone is real progress for next week.

## 7. Close and the one-week assignment

**The close:** "You didn't come here to build a chatbot. You came here to find the one decision
your business re-makes every single day and give it a short, honest list of answers — including
'I'm not sure.' That list is the actual asset. The tool that reads it is replaceable; the list
isn't."

**The assignment:** "This week, just write the list — the exact allowed answers for one real
decision in your business, including the 'needs a person' option. Don't build anything yet. If you
can write a list that a brand-new employee could follow on their first day without asking you a
single question, the hard part is already done."

## 8. Facilitator notes

**Prepare beforehand:**
- An Airtable base with an `Inbox` table, a `Category` single-select field with the four options
  above, and the working AI classification automation.
- A second tab with a populated run history for the demo-breaks fallback.
- Printed handouts.

**Timing risks:**
- The receipts section tempts a longer "can you believe that chatbot" tangent — both stories are
  genuinely fun. Cap it at the two as written; save the "give it a fixed list" payoff for the
  best-practices section.
- The open-build block is unscripted on purpose. Don't let it become Rachael building solo while
  the room watches — call out "pause and build this part yourself" every few minutes.

**Questions beyond the FAQ that will come up:**
- *"Can I use this to sort more than email — like photos or voice memos?"* Yes, same shape:
  whatever comes in, as long as you can write the finite list of right answers first.
- *"What if my list needs to change later?"* That's normal and fine — update the list the same way
  you'd update a written policy. The automation just reads whatever list you give it.

## 9. Best practices nobody tells you

**Give it a fixed list, never a blank box.** The moment an automation is allowed to answer in its
own words instead of picking from a list you wrote, you've quietly built a chatbot, with all the
same risk — and you won't notice until it says something you didn't expect. In this build, the
`Category` field is a single-select with four fixed options; the AI step can only choose among
them, nothing else is possible to write back.

**Make "not sure" one of the real options, not an afterthought — this is the stop condition.** In
this build, if the inbound message doesn't clearly match one of the first three categories, it
goes into `Not sure — needs a person` and nothing else happens to it automatically. That one
option is what would have stopped the Chevrolet dealership's bot cold: a sales chatbot with
"escalate to a human, I can't make this offer" as a required, always-available answer can't be
talked into a $1 car, because agreeing to a price was never one of its allowed moves.

**When one pass isn't accurate enough, add a second decision — don't widen the first one.**
[snip: Add Classification Layers When Jev Falls Short](https://share.snipd.com/snip/55b4349e-5bdf-483f-b519-91c6b31e2149)
describes chaining classification steps rather than loosening a single one until it tries to do
everything. In this build, if `Category` alone starts missing real leads, the fix is a second
step — "is this even a real inbound message, yes or no" — run before the four-way category choice,
not a fifth, vaguer category bolted onto the first list.
