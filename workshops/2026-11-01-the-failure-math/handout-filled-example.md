# The Failure Math — filled example

**Automate Your Business** · This is a worked example, not a real client's data. Every name,
email, and number below is invented for illustration.

---

## Part 1 — Pick the tool

**The AI tool or automation I'm testing today:** An AI inbox assistant that drafts replies to
customer questions sent to `support@` for a 10-person online pet-supply shop.

**What it's supposed to do:** Read each incoming customer email and draft a reply — answering
order-status, return-policy, and shipping questions automatically.

**The vendor's claimed accuracy (if they give you one):** 92%

---

## Part 2 — Your 20 real cases

Pulled from the actual `support@` inbox, the last two weeks, in order received — not cherry-picked.

| # | Real case (short description) | Tool's output | Pass / Fail |
| --- | --- | --- | --- |
| 1 | "Where's my order #4521?" | Correct status + tracking link | Pass |
| 2 | "Can I return opened dog food?" | Said yes — actual policy says no on opened food | Fail |
| 3 | "Do you ship to Alaska?" | Correct shipping zones answer | Pass |
| 4 | Angry customer, order 3 weeks late, typos, no order number | Drafted a generic apology, didn't ask for the order number | Fail |
| 5 | "What's in the Salmon Recipe treats?" | Correct ingredient list from product page | Pass |
| 6 | "I need to change my shipping address before it ships" | Correctly flagged as urgent, drafted hold-and-confirm reply | Pass |
| 7 | "Your competitor is cheaper, price match?" | Made up a price-match policy that doesn't exist | Fail |
| 8 | "Cat scratched the packaging, is the toy still safe?" | Correctly said to inspect and offered replacement | Pass |
| 9 | "Can I combine two discount codes?" | Correctly said no, codes don't stack | Pass |
| 10 | Spanish-language question about a delayed order | Replied in English, missed the request | Fail |
| 11 | "Is this gluten-free?" about a specific SKU | Correct answer, pulled from product data | Pass |
| 12 | "My dog is allergic, can you recommend a food?" | Gave a specific medical-sounding recommendation it wasn't authorized to give | Fail |
| 13 | "Order arrived damaged, need a replacement" | Correct replacement process, correct next steps | Pass |
| 14 | "How do I cancel my subscription box?" | Correct, step-by-step cancellation info | Pass |
| 15 | "You charged me twice" | Correctly identified as a billing issue, routed to a person | Pass |
| 16 | "When does the Black Friday sale start?" | Correct, matched current promo dates | Pass |
| 17 | Vague one-line message: "hey question" | Replied with a generic FAQ instead of asking what they needed | Fail |
| 18 | "Can I get this gift-wrapped?" | Correct — accurately said gift wrap isn't offered | Pass |
| 19 | "Return label never arrived" | Correct — re-sent label process, correct timeline | Pass |
| 20 | "Is this safe for puppies under 6 months?" | Correct — matched product's age guidance | Pass |

---

## Part 3 — The math

**Passes:** 14 out of 20 = **Your real pass rate:** 70%

**How much of this work do you do in a month?** About 240 support emails/month

**Projected wrong outputs per month at your real volume:**

(100% − 70%) × 240 = **72 wrong drafts going out a month** — more than two a day — unless a
person reads every draft first.

---

## Part 4 — Your floor

**The pass rate below which this tool does NOT run unsupervised:** 90%

**Who catches a miss before a customer sees it, until the tool clears that floor?** The shop
owner reads and approves every drafted reply before it sends, for at least the next round of
testing. The tool stays in "draft only, human sends" mode — it never gets to click send itself
until it clears 90% on a fresh 20-case test.

---

### If you only do one thing

Test on your own real cases before you trust the vendor's number. Twenty messy examples from your
own business tell you more than any demo.
