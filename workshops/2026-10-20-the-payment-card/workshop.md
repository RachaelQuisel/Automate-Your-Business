# The Payment Card: Who Approves, the Cap, and the Stop Button

**Title:** The Payment Card: Who Approves, the Cap, and the Stop Button
**Source:** Soft Fork snips, 2026-10-20: Snip 1 ("AI Agents for Payments: Visa, BILL & Billtrust Partnership", Billtrust / Business Wire, 2026-10-20, https://www.billtrust.com/news/news-visa-bill-billtrust-launch-ai-agents-for-payments), Snip 4 ("Everything That Happened in AI Today Tuesday, October 20", The Neuron, 2026-10-20), Snip 5 ("Sumsub Expands Know Your Agent, Putting Businesses in Control of What AI Agents Can Access", PulseXPerTech, 2026-10-20)
**Snips file:** `sources/snips/2026-10-20-ai-tools-trending.md`: 13 snips, 3 used here, 10 held for later
**Built:** 2026-10-20
**Teach date:** TBD
**Length:** 60 minutes
**Audience:** Small business owners and operators: no technical background assumed

## 1. The promise

In the next hour, you will write an Approved Payment Card for one repeated payment in your business, the card that says who approves, what the cap is, which suppliers are on the list, and where the stop button is, so an agent can do the boring last step and never make the decision.

## 2. Agenda: 60 minutes

| Minutes | Segment |
|---------|---------|
| 0-8 | Opening frame: the agent that paid real invoices today + the three ideas |
| 8-18 | The five lines on the card, and why each one earns its place |
| 18-28 | Watch it work (demo: an approved invoice moves from inbox to paid, with the card checked at each step) |
| 28-33 | Your questions |
| 33-58 | Build your Approved Payment Card (independent work) |
| 58-60 | Wrap-up, share-out seed, and homework |

*Facilitator note:* the 33-58 block is the build session. Pair share-out and Q&A live inside it: circulate, then at minute 53 pull the room together for a 3-minute share-out ("read your cap line and your stop line in thirty seconds") followed by questions to minute 58. Total: 25 minutes building, ~15 minutes Q&A, two minutes of close.

## 3. Facilitator script

### 0-8 · The agent that paid real invoices today + the three ideas

Say it in your own words (keep it under eight minutes):

- "On October 20, Visa, BILL, and Billtrust launched a live pilot. Not a demo. Real transactions. An agent from BILL goes into a supplier's payment portal and pays an invoice, start to finish, the step a person used to do by logging in and typing numbers."
- "Here is the part that matters. The agent does not decide anything. The buyer approved the payment first. The agent only carries out approved payments, for the approved amount, tied to that one invoice."
- "And the agent does not borrow anyone's login. It is registered and recognized by name, and it carries a token, a stand-in number, instead of the real card details. The supplier can see who paid, when, and for which invoice."

Three big ideas in plain words. Say them, then point at them all hour:

1. **Approve first, automate second.** The human makes the decision while it is still a decision. The agent only does the carrying out.
2. **A named agent with a cap beats a shared login with hope.** If a tool acts for you, it should have its own name, its own limits, and no access to anything else.
3. **Every payment leaves a receipt a person can read.** Who approved it, what it paid, which invoice, and when. No receipt, no automation.

"Approve it. Cap it. Watch it."

### 8-18 · The five lines on the card

Teach the five lines on the board. Use one ordinary supplier payment as the running example.

**Line one: the approver.** "Name one person. Not a team, not 'finance.' One name who says yes before money moves. In the pilot, the buyer's approved instruction is the whole permission. Your card copies that: no approval, no payment, ever."

**Line two: the cap.** "A top amount, per payment and per week. Anything above the cap is not a payment the agent got wrong, it is a payment the agent must hand back to the approver. Write a number, not 'reasonable amounts.'"

**Line three: the supplier list.** "Only named suppliers the agent may pay. A new supplier is a human job: a person checks the bank details the first time, because a changed bank detail is the oldest trick in business fraud."

**Line four: the one-invoice rule.** "Each payment is tied to one invoice number and one amount that matches it. If the invoice and the amount do not match, the agent stops and asks. Matching is the check that catches both typos and scams."

**Line five: the stop and the receipt.** "How do you turn it off in one step, and where does the record land? In the news this week, Microsoft shipped controls that can limit an agent, require approval, or shut it down. Your card needs the small business version: one named place to switch it off, and one named place where every payment gets logged the same day."

Then the one test that makes it a card, not a wish:

**The stranger test.** "Hand the card to a stranger. Could they look at a payment and say yes or no, was this allowed, without asking you? If not, sharpen the line. 'Normal payments' fails. 'Under five hundred dollars, to a supplier on this list, against a matching invoice' passes."

*Facilitator note:* name the trap out loud. "The shared login feels harmless because it works. It also means the tool can do everything you can do, nobody can tell later which payments were yours and which were its, and changing the password breaks your own books. A named agent with a token fixes all three at once."

### 18-28 · Watch it work

Work one example live. No real money moves in this room: use a printed invoice and walk the card. Keep it to ten minutes.

1. "Here is the job." *(A supplier invoice for a regular monthly service.)* "Count the steps a person does today: open the portal, log in, find the invoice, type the amount, pay, save the receipt, mark it paid in the books. Seven steps, one of which is a decision."
2. "Here is the decision, kept human." *(The approver checks the invoice against the service actually received and approves it.)* "That check is the job. Everything after it is carrying."
3. "Here is the card checked, line by line." *(Approver named, amount under the cap, supplier on the list, invoice number matches the amount, stop and log in place.)* "Five yes answers, or the payment stops here and a person looks."
4. "Here is the carrying out." *(Walk the agent's path as the pilot describes it: registered agent, token instead of card details, payment tied to this invoice, supplier portal recognizes the agent.)* "Notice what the agent never holds: your login, and the choice of whether to pay."
5. "Here is the receipt." *(Read the log line aloud: approver, supplier, invoice, amount, time.)* "This line is what makes the system trustworthy on a bad day, not on a good one. When a payment is questioned in March, this line answers."

*Facilitator note:* if the room says their payments are too varied for a card, answer with the split: "Then card the three payments that are not varied, the ones that repeat every month, and keep the odd ones human. The pilot did not automate deciding. It automated the last manual step of payments that were already approved."

### 28-33 · Your questions

Open floor. Answer in plain English. The three questions you will get, and the answers:

- "Is this safe? It is money.": "That is exactly why the card exists. The version of this that is not safe is the one most people run today: a tool or a helper with the owner's login and no cap. A named agent, a cap, a supplier list, a matching invoice, and a log is stricter than that, not looser."
- "What if the agent pays the wrong supplier?": "That is what lines three and four are for. It can only pay listed suppliers, and only an amount that matches an invoice. If either check fails, it stops. And line five means you can switch it off in one step the moment anything looks wrong."
- "My business is too small for this.": "The card is one page and no software. It pays off the first time anyone, human or agent, pays a bill while you are away, because the rules are written instead of living in your head."

### 33-58 · Build your Approved Payment Card

Everyone works solo or in pairs on their card (see `handout.md`). Circulate with only these prompts:

- "Which payment repeats so often you could approve it half-asleep? Start there."
- "Who is the one named approver? A name, not a team."
- "What is your cap, in numbers, per payment and per week?"
- "Which suppliers are on the list today? Who adds a new one, and how are bank details checked the first time?"
- "Show me your one-invoice rule. What makes the agent stop and ask?"
- "Where is your stop switch, and where does the receipt land the same day?"

At minute 53, pull the room together. Three-minute share-out: volunteers read their cap line and their stop line in thirty seconds. "My payment is ___. My cap is ___. My stop is ___."

Then Q&A to minute 58, and seed the "what could go wrong" story for anyone who asks:

**What could go wrong.** "Two tales from this week. First, the open door. A security firm reported this week that 65 percent of organizations had at least one incident caused by an agent on their network in the past year, with private data exposed the top cause. Broad access granted once and never reviewed is how that happens. Second, the shared login. A tool holding your real login can pay anyone, any amount, and the log cannot tell its payments from yours. The fix for both is the same card: named agent, short access list, cap, matching invoice, one-step stop, same-day log."

### 58-60 · Wrap-up and homework

"Approve it. Cap it. Watch it."

Homework: within two weeks, pick your three most repeated payments and put each one on a card. Run the next three payments of each kind by hand against the card, checking the five lines out loud. Mark any line you had to guess at, and sharpen that line once. Bring back the card with the one line you changed highlighted. That changed line is the proof the card is real, not decorative.

*Facilitator note:* hold up a filled worksheet as you say this. "Bring this page back filled in, with your changed line highlighted, keep or fix."

## 4. Plain-English word list

Keep this on your facilitator copy. If you are tempted to say the left column, say the right column instead, and only use the product's own word after the plain version.

| Instead of... | Say... |
|---|---|
| Trusted Agent Protocol | A way for a portal to check that an agent is named, registered, and allowed in |
| Tokenized credentials | A stand-in number that works for one payment job, instead of your real card or login |
| Agentic commerce | Agents carrying out buying and paying steps a person approved |
| MCP | A standard plug that lets agents connect to tools and data |
| Access control / KYA | The written list of what each agent may see and do, and the human behind it |
| Deflection rate | The share of requests an agent settles without a person picking them up |
| Loop | A job that takes an approved item, carries out the steps, checks the result, and logs it |
