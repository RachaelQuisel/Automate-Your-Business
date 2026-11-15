# The 60-20-20 Build: filled example

**This is an invented example.** The business, the people, the messages and the numbers below are
made up to show what a finished sort looks like. They are not a real client's data.

The example business is Greenline Outdoor, a nine-person landscaping company that takes quote
requests by email and web form. The owner is Priya. The job on this handout is answering
incoming quote requests.

## Part one: the job

- The one job you're sorting: Answering quote requests.
- What arrives to start this job: An email or web form submission — a name, an address, a job
  description in the sender's own words, sometimes a photo.

## Part two: the three piles

**Ready now — AI does this alone, no one checks it.**
- Pulling the name, address, job type, size (if mentioned), and whether a photo was attached out
  of the message and into the lead record.
- Flagging duplicate requests from the same address within 30 days.

**Almost ready — AI drafts it, a person checks before it counts as done.**
- Drafting a price estimate from Greenline's price sheet and similar past jobs.
- Drafting the reply email that goes with the estimate.

**Just a guess — a person does this fully, for now.**
- Deciding whether to take a job that smells like a liability problem (a tree limb near a power
  line, a drainage complaint, a client with a history of disputed invoices).
- Deciding whether to offer a discount for a referral or a long-time client.

## Part three: the ten-example check

- Pick ten real past examples of the piece you're least sure about. How many times out of ten
  would you have had to fix what AI produced? 6 / 10 (on draft pricing — it undercounted
  equipment-access difficulty on steep lots four times out of ten past jobs)
- Based on that number, which pile does it actually belong in? Almost ready, not ready now — the
  draft needs a person checking the access/slope line every time until that error rate drops.

## Part four: today's build — the ready-now piece

- What AI reads to do this piece: The incoming quote-request email or form submission.
- What it writes down, and where: A new row in the `Leads` table — Name, Address, Job type, Size
  (if mentioned), Photo attached (yes/no), Status.
- The one required fact that, if missing, makes it stop instead of guess: Address or job type.
- What happens when that required fact is missing (the stop condition): Status is set to
  `Needs manual read` and the row stops there — no address or job type gets invented.

## Part five: the handoff

- What status or flag marks a record as ready for the "almost ready" pile to pick up: Status =
  `Needs quote draft`.
- Who picks it up from there, today: Priya, every morning, for the pricing draft and the reply.

## One-sentence finish

"For the job of answering quote requests, AI alone handles logging every incoming lead's name,
address, job type, and photo. AI drafts the price estimate and the reply, and Priya checks it.
Deciding whether to take a liability-flagged job stays fully human for now. It stops instead of
guessing when the address or job type is missing from the message."

## Context example: what the automation reads

A real-looking quote request Greenline's intake automation would read. Invented.

```
From: taylor.reyes@example.com
Subject: Backyard cleanup quote?

Hi, we just moved into 4420 Birchwood Lane and the backyard is a disaster — tall
weeds, some kind of overgrown hedge along the back fence, and a dead tree branch
hanging over the shed. Can someone come take a look and give us a price? We don't
have a lot saved up right now so hoping it's not too bad. Attached a couple photos.

Thanks,
Taylor
```

## Definition of done: what the automation produces

The new row the intake automation writes into the `Leads` table within seconds of the email
above arriving. Invented.

```
Leads table — new row:

Name:          Taylor Reyes
Address:       4420 Birchwood Lane
Job type:      Yard cleanup (weeds, hedge trim), possible tree limb removal
Size:          Not mentioned
Photo attached: Yes (2 files)
Status:        Needs quote draft
```

Done means: the row exists, every field that was actually in the email is filled in correctly,
"Size" is left blank rather than guessed because the email never gave one, the tree-limb mention
is captured in the job type so it's visible to whoever drafts the quote (it may later trip the
liability pile, but that decision stays with Priya, not the intake step), and the status is
`Needs quote draft` — not `Needs manual read`, because both required fields, address and job
type, were present. If the email had arrived with no address, the status would read
`Needs manual read` instead, and the row would wait for Priya rather than showing a guessed-at
address.
