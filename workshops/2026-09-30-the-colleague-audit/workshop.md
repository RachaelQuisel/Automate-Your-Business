# The Colleague Audit: Stop Chatting With AI, Start Delegating To It

**Source:** Lenny's Podcast: Product | Career | Growth — How we built Grok Bot in a month | Roman Ugarte (SpaceXAI)
**Snips file:** ../../sources/snips/2026-09-22-grok-bot-in-a-month.md
**Built:** 2026-09-30
**Teach date:** TBD
**Length:** 60 minutes
**Audience:** Small business owners and operators

---

## 1. The promise

Most people use AI like a search box: type a question, get an answer, close the tab. By the end
of this hour you will have picked one real task in your business, written down what "done"
looks like for it, and given an AI tool enough access to actually do it — not chat about it.

You are not going to build a chief of staff today. You are going to hire your first AI colleague
for one task, and know exactly how to tell if it's working.

## 2. What they leave with

- One filled Colleague Audit worksheet for a real task they currently do themselves.
- A written definition of "done" for that task — not a vibe, a checkable fact.
- A routing rule: what the AI handles alone, and what it must hand to a person.
- The one piece of access they will grant it this week.

## 3. Agenda

| Minutes | Segment | Rachael is doing | The room is doing |
| --- | --- | --- | --- |
| 0–4 | The wrong question | Opening story, reframe | Listening |
| 4–13 | Idea 1: colleague, not chat window | Teaching | Listening, one show of hands |
| 13–21 | Idea 2: judge it by what finishes | Teaching | Taking notes on handout page 1 |
| 21–28 | Idea 3: build the filter first | Teaching at the whiteboard | Taking notes on handout page 1 |
| 28–38 | Live build | Building a filter rule on screen | Watching, asking |
| 38–52 | The Colleague Audit | Circulating, unsticking people | Filling the worksheet |
| 52–58 | Share-out and where this breaks | Asking three questions | Three people read theirs out |
| 58–60 | Close and the assignment | Landing it | Writing one line |

Room working: 14 minutes of worksheet + 6 minutes of share-out = 20 minutes.

## 4. The teaching

### Idea 1 — Treat the tool like a colleague with a computer, not a chat window

**The idea.** A chat window answers questions. A colleague with a computer does the work and
shows you the result. The difference is what you give it access to, not how smart it is.

**Where it comes from.** [snip: Design AI Like A Useful Colleague](https://share.snipd.com/snip/81d93734-9133-4196-8d8d-381d92bb7195)
and [snip: GrokBot Acts Like a Colleague With a Computer](https://share.snipd.com/snip/9db0617e-4dd0-41e4-855e-eedd8a1b4599).

**What it means for a 10-person business.** Most small business owners who "try AI" open a chat
tab, paste in a question, and copy the answer back into an email themselves. That's a smarter
search engine, not delegation. The team behind GrokBot built it around a different question:
what would a good human teammate do with this task, and what would they need access to in order
to do it? A good assistant doesn't wait for you to paste them the invoice — they have the
invoice already, because you gave them the login.

Translate that out of engineering: if you have a bookkeeper, you don't email them a screenshot
of every receipt and ask "what category is this?" You give them access to the books and they
categorize on their own, then you review. That's the standard to hold an AI tool to. If you're
still copy-pasting between five tabs to make it useful, you haven't delegated — you've just added
a smarter clipboard.

**The example to use.** Roman's own QA bot is the cleanest version of this: it doesn't chat about
testing, it opens the actual desktop build, runs ten real workflows, and writes the regressions
into Notion. Nobody asks it questions. It has a computer and a job.

**The common objection.** *"Isn't that just a fancier chatbot?"*

The honest answer: the model underneath might be the same one you'd chat with. The difference is
entirely what it's plugged into. A chatbot with no access to your calendar can only tell you how
to check your calendar. The same model with access to your calendar can move the meeting. You are
not upgrading the brain today. You are upgrading the access.

---

### Idea 2 — Judge it by whether the task finishes, not by how many things it can do

**The idea.** Before launch, the GrokBot team stripped out experimental features and judged the
product on one number: did the real task complete, reliably, every time.

**Where it comes from.** [snip: Optimize For Tasks That Just Work](https://share.snipd.com/snip/e533d146-f9e6-4166-8a58-b99ac5bfce82),
[snip: Hide The Mechanics And Show The Work](https://share.snipd.com/snip/9b2c5882-56db-4039-9364-f8eb64ec9c7b),
and [snip: Build Capabilities Instead Of More Product Pixels](https://share.snipd.com/snip/3c28a9f8-83c5-4a92-b691-50b6da98afe8).

**What it means for a 10-person business.** It is tempting to pick an AI tool because it has the
longest feature list, or because the sales page is impressive. That's the wrong test. The right
test is narrower and more boring: give it one real task, and watch whether it finishes the task
the same way, correctly, ten times in a row. A tool that does one thing reliably beats a tool
that does twenty things sometimes.

This also changes what you watch while it works. The team hid the tool calls and the
click-by-click mechanics on purpose — users didn't want to supervise every step, they wanted to
know it was making progress and see the result. If you find yourself babysitting every action an
AI tool takes, that's a sign the task isn't ready to be delegated yet, not a sign you need to
watch more closely forever.

**The example.** Picture the same manual-onboarding moment from this episode, translated: the
team watched real outside users — including a coffee shop owner, someone with zero patience for a
half-working tool — try to use GrokBot, and fixed what broke immediately.
[snip: Manual Onboarding Revealed GrokBot's Blind Spots](https://share.snipd.com/snip/4432ed56-3dd7-47cf-8d64-7b4708b37e91)
The lesson for you isn't "watch people use software." It's that the person who tells you whether
a task is truly delegated is the one actually doing it every day — not you testing it once and
declaring victory.

**The common objection.** *"Shouldn't I want the tool that can do more things?"*

The honest answer: eventually, maybe. But "GrokBot can now do X" beat "GrokBot has feature Y" as
the team's own measuring stick — capability, not surface area. One task, done reliably, saves you
real hours starting this week. Ten half-working features save you nothing and cost you the time
you spend checking their work.

---

### Idea 3 — Build the filter before you build the chief of staff

**The idea.** Before an AI tool can act on your behalf, it has to first prove it can tell the
difference between something urgent and something that can wait. Start there.

**Where it comes from.** [snip: Give AI a Firehose and Filter the Noise](https://share.snipd.com/snip/90074bd9-edc7-4a10-9875-ea2ecfbfc6b6),
[snip: The Always-On AI Chief Of Staff](https://share.snipd.com/snip/3bed1f5f-bbd7-485b-a244-b7e6e70332de),
and [snip: AI Chiefs Of Staff Will Act Before You Ask](https://share.snipd.com/snip/a23548d8-f890-4ccf-8d2e-a3d923577804).

**What it means for a 10-person business.** Roman didn't start by letting GrokBot act on his
behalf. He started by pointing it at his firehose — Slack, email, X, QA feedback — and having it
sort what needed him right now from what could wait for a daily roundup. Only after that filter
earned trust did it graduate to paging him directly for genuinely urgent events.

For you, the firehose is your inbox, your group texts, your voicemail, your DMs from clients. Most
of it is routine — a shipping update, a scheduling confirmation, a question you'll answer in the
next batch of emails you do anyway. A little of it is urgent — a client threatening to cancel, a
payment that bounced, a safety issue. The first job for an AI tool isn't to answer either kind.
It's to sort the pile into those two buckets correctly, so you can trust it with more later.

**The example.** The end state described in the episode is a bot that pages you only when
something is genuinely urgent, and earns that privilege by avoiding false alarms. You don't start
there. You start by having it build you a daily digest of the routine stuff and flag — not act
on — anything it thinks is urgent, so you can check its judgment for a week before you let it
act alone.

**The common objection.** *"What if it filters out something that actually was urgent?"*

The honest answer: at first, it will, sometimes. That's exactly why you watch it for a week before
you trust it to page you directly, and why the urgent bucket should default to "show me" rather
than "handle it" until it has a track record. A bad filter you're watching is a minor annoyance.
A bad filter you've stopped checking is a real risk. Keep the first version supervised.

## 5. Live build — a firehose filter, 10 minutes

**What Rachael builds on screen:** a rule that sorts incoming messages into "routine" and
"urgent," live.

- **Tool:** whatever inbox or messaging tool already holds the traffic (email rules plus an AI
  summarizer, or a no-code automation tool). Any tool that can read a message and route it works
  the same way.
- **Trigger:** a new email arrives in a specific inbox.
- **Step 1:** the AI reads the email and classifies it — routine, or urgent.
- **Step 2:** routine messages get added to a running daily digest. Urgent messages get sent
  straight to a Slack DM or a phone alert.
- **Visible result:** send two test emails live — one ordinary scheduling note, one flagged
  "client wants to cancel today" — and watch the digest pick up the first one quietly while the
  second one fires an alert on screen.

**Say while building:** "I am not building a chief of staff. I am building the one rule
underneath it — routine versus urgent — because that's the part that has to be right before
anything else is worth automating."

**Narrate as it runs.** Point at the screen when the digest updates silently. Point again when
the alert fires. Ask the room: what would you have wanted this to do with the second email if
you'd been at lunch? Make them say it out loud before you move on.

**If the demo breaks:** have a second tab open with a completed run already showing both the
digest entry and the fired alert from a rehearsal. Switch to it, say "here's one from this
morning," and keep going. Do not debug live — it teaches nothing and burns the minute you need for
the exercise.

## 6. The exercise — The Colleague Audit, 14 minutes

Handout page 1 is the three questions. Page 2 is the audit grid.

**The exact instruction to say out loud:**

> "Take three minutes and write down every task you personally do more than once a week where you
> are mostly reading something and deciding what to do about it — not thinking hard, just
> triaging. Do not judge them. Just list them. Then circle the one that eats the most of your
> week. That's the one you're auditing."

Then, at the 3-minute mark:

> "Now answer three questions about that one task. First: what does 'done' look like, in a
> sentence a stranger could check? Second: what access would a colleague need to do this without
> asking you first? Third: what's the one situation where it should stop and hand the whole thing
> to you?"

**Two examples for anyone who freezes:**

1. *Reading client emails.* Done: every email is either answered from a template, added to a
   task list, or flagged for you — nothing sits unread for more than a day. Access needed: the
   inbox, and your three standard reply templates. Hand-to-a-person trigger: the client mentions
   cancelling, a refund, or anything with a dollar figure over $1,000.
2. *Checking on overdue invoices.* Done: every invoice over 30 days has either a reminder sent or
   a note on why not. Access needed: the invoicing tool and a read-only view of the client list.
   Hand-to-a-person trigger: the client replies with a question, or the balance is over $5,000.

**While circulating, watch for the two failure patterns:**

- Someone has written "done" as a feeling — "when it's handled." Push them for the checkable
  fact: what would you see, specifically, that tells you it's handled.
- Someone has given the colleague access to everything "just in case." Push them to name the
  narrowest access that still lets the task finish. Broad access with no real need is how a small
  mistake becomes a big one.

## 7. Share-out and where this breaks — 6 minutes

**Three questions to ask the room:**

1. "Who wrote a 'done' that was actually a feeling, not a fact, on the first pass?" (Most hands.
   This is the most common finding and it normalizes it.)
2. "Read me your hand-to-a-person trigger." (Take three. Most will be too narrow on the first
   pass — improve one live by asking "what else would make you want to know immediately?")
3. "What's the one piece of access you're actually going to grant this week?" (Go around fast,
   one sentence each.)

**Where this breaks — say all four of these plainly:**

- **A task with no clear 'done' can't be delegated, only outsourced to worry.** If you can't
  write the finish line in one sentence, fix that first, before you touch any tool.
- **Watching every step defeats the purpose.** If you're checking each action instead of the
  result, you haven't delegated — you've just added a step. Check outcomes, spot-check process
  occasionally, not every time.
- **A filter you stop checking is worse than no filter.** The urgent-or-routine sort earns your
  trust over a week of you actually reviewing what it flagged. Skip that week and you won't know
  when it starts getting it wrong.
- **One task at a time, not a program.** The instinct is to hand over five things at once because
  you're excited. That's how you end up unable to tell which one is actually working. One task,
  two weeks, then the next one.

## 8. Close and the one-week assignment

**The close:**

> "You didn't come here to get better at asking questions. The task you just audited is the
> actual asset — you now know exactly what 'done' looks like for it, which is more than most
> people can say about their own to-do list, automated or not."

**The assignment — one week, one line to write now:**

> "On the bottom of your handout, write one sentence: 'This week I will give [tool] access to
> [the one thing] so it can handle [the task] on its own.' Not five tasks. One piece of access.
> When it finishes that one task correctly ten times, you'll know exactly what to hand it next."

## 9. Facilitator notes

**Prepare beforehand:**
- Two test emails ready to send live — one clearly routine, one clearly urgent — for the live
  build.
- A second browser tab with a completed rehearsal run (digest entry + fired alert) for the
  demo-breaks fallback.
- The three audit questions written on the whiteboard before anyone walks in.
- Printed handouts. People audit better on paper than on a laptop, and laptops open means email
  open.

**Timing risks:**
- Idea 3 (the filter) is the segment to cut if running long — it's the least hands-on, and the
  live build makes its point anyway. Cutting it buys 7 minutes.
- The live build wants to run long. Two test emails, two outcomes, nothing more. Set a visible
  timer.
- Do not let the share-out become a debate about which tool to use. Redirect to the task and the
  access; the tool question comes up in FAQ anyway.

**Questions that will come up:**

- *"Which AI tool should I actually use?"* — Whatever already touches the task: if the work lives
  in your inbox, start with something that can read and act on your inbox. Don't switch your
  whole stack to start one delegation; that's how three months go by with nothing automated.
- *"Is it safe to give it access to my email/invoicing/calendar?"* — Start read-only where you
  can, and start with the least access that lets the task finish, as covered in the exercise.
  Expand access only after you've watched it get the narrow version right for a couple of weeks.
- *"What if it does something wrong while I'm not watching?"* — That's exactly why the hand-to-a-
  person trigger exists, and why the filter stays supervised for its first week. You're not
  removing yourself from the loop. You're moving yourself to the exceptions.
- *"Isn't this a lot of setup for one task?"* — Yes, the first one is the slow one, the same way
  training a new hire is slower than doing the task yourself once. The second task you delegate
  will take a fraction of the time, because you'll already know what "done" and "access" and
  "escalate" mean for your business.

**Snips not used in this workshop** (available for a later session — see the snips file): the
small isolated team that shipped GrokBot in a month, why GrokBot started as a separate product
instead of a tab, always-on recruiting research, giving every bot its own cloud computer, the
near-duplicate "AI colleagues turn computers into infinite leverage" snip, Cursor's adaptation
advantage, and discovering moats by building the future. The team-and-moat-strategy snips are the
spine of a separate workshop on how to structure a small team around AI tools rather than how to
delegate a single task.
