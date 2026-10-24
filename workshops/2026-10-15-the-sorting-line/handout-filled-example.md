# The Sorting Line — filled example

**Automate Your Business** · This is a worked example, not a real client's data. Every name,
email, and number below is invented for illustration.

---

## Part 1 — Name the decision

**What comes in, over and over, that you currently decide by eye?** Every new message that lands
in the general `hello@` inbox for a 10-person landscaping company.

**Right now, who makes this call, and how?** The office manager opens every email each morning and
decides by reading it: is this a new customer, an existing one, or junk — then forwards it or
ignores it.

## Part 2 — Write the list

**Every possible right answer — the short list, written like a menu, not a paragraph:**

1. New client inquiry
2. Support question from an existing client
3. Spam or vendor pitch
4. "Not sure — needs a person" ← always include this one

## Part 3 — Build it

**Step 1 — What field does the automation set?** A single-select field named `Category` on the
`Inbox` table, limited to exactly the four options above — no free text allowed.

**Step 2 — What does it read to decide?** The email's subject line and body, plus whether the
sender's email address already matches a record in the `Clients` table.

**Step 3 — Where does each answer send it?** `New client inquiry` → the `Leads` view. `Support
question` → the `Support` view, sorted by client name. `Spam or vendor pitch` → archived, no view.
`Not sure` → stays pinned at the top of the main `Inbox` view.

## Part 4 — The stop condition

**What is it never allowed to do on its own — even for the categories it got right?** It never
replies to the sender itself, under any category. It only sorts and routes internally. If the
sender's identity or the message's intent isn't clear, it goes to `Not sure` instead of guessing
between `New client inquiry` and `Support question.`

---

## Context example — what the automation reads

A sample of what lands in the `Inbox` table one morning:

| From | Subject | Body (excerpt) | Known client? |
| --- | --- | --- | --- |
| maria.chen@example.com | "Quote for backyard redesign" | "Hi, I saw your work on Instagram and I'm looking for a quote on redoing my backyard..." | No |
| j.torres@example.com | "Sprinklers still not working" | "Hey, the sprinkler system you fixed last month stopped again on zone 3..." | Yes (Torres, since 2024) |
| info@turfsupplyco.com | "Bulk mulch pricing — partner with us" | "We'd love to offer your company wholesale rates on mulch and soil..." | No |
| r.patel@example.com | "question" | "hey do you guys still do the thing from before" | No |

## Definition of done — what success looks like

After the automation runs on the four rows above, the `Category` field reads:

| From | Category |
| --- | --- |
| maria.chen@example.com | New client inquiry |
| j.torres@example.com | Support question from an existing client |
| info@turfsupplyco.com | Spam or vendor pitch |
| r.patel@example.com | Not sure — needs a person |

Maria's and Torres's messages land in the right views automatically. The mulch pitch is archived
without anyone reading it. Patel's vague "the thing from before" message — with no client match
and no clear request — stays pinned at the top of the inbox instead of being guessed at. If a run
produces four confident, correct sorts with nothing guessed wrong and nothing silently dropped,
the build worked. If "the thing from before" ever gets auto-sorted into a real category instead of
flagged, the build isn't done yet, even if the other three were right.
