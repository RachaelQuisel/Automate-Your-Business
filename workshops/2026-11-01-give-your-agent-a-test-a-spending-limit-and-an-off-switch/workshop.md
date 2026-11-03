# Give Your Agent a Test, a Spending Limit, and an Off Switch

**Title:** Give Your Agent a Test, a Spending Limit, and an Off Switch
**Source:** Soft Fork snips, 2026-11-01: Snip 1 (Salesforce Agent Fabric: Agent Evals, hard spending caps, and an Agent Kill Switch, announced 2026-11-01), Snip 2 (Vercel Labs agent-desktop: a snapshot before and a snapshot after each action, 2026-10-31), Snip 5 (Gemini in Sheets: a source inside each AI-filled cell and a separate verification column, Google, 2026-10-28), Snip 11 (OpenAI Evals read-only on 2026-10-31 and shutting down 2026-11-30; Claude Opus 4.8 fast mode removed 2026-11-30)
**Snips file:** `sources/snips/2026-11-01-ai-tools-trending.md`: 13 snips, 4 used here, 9 held for later
**Built:** 2026-11-01
**Teach date:** TBD
**Length:** 60 minutes
**Audience:** Small business owners and operators: no technical background assumed

## 1. The promise

In the next hour, you will take one agent or automation you already trust and give it three things it probably does not have today: five written tests built from your real past jobs, with the right answer written down before the agent ever sees them; a spending limit written in dollars per week, with a hard stop and a named handoff when the stop fires; and a one-page failure rule that says who is told when a test fails, who alone can pull the agent offline, and what has to pass before it is allowed back. You will leave with the tests written, the limit set, the rule signed, and one rehearsed shutdown already done, on a quiet job, while nothing was on fire.

## 2. Agenda: 60 minutes

| Minutes | Segment |
|---------|---------|
| 0-8 | Opening frame: the agent that went wrong quietly after a cheaper model swap, the customer who became the test, and why the check has to run on live work + the three ideas |
| 8-18 | The six steps: write the inventory, write five tests and their right answers, score correctness and taste separately, set the dollar limit, write the failure rule, rehearse the shutdown |
| 18-28 | Watch it work (demo: one services business, one reply agent moved to a cheaper model, the weekly test that caught the wrong answer, the shutdown, the fix, the passing retest) |
| 28-33 | Your questions |
| 33-58 | Write your own five tests, limit, and failure rule for one trusted job, and rehearse its shutdown (independent work) |
| 58-60 | Wrap-up, share-out seed, and homework |

*Facilitator note:* the 33-58 block is the build session. Pair share-out and Q&A live inside it: circulate, then at minute 53 pull the room together for a 3-minute share-out ("name your job, the test that surprised you, and the name of the person who can stop it") followed by questions to minute 58. Total: 25 minutes building, about 15 minutes Q&A, two minutes of close.

## 3. Facilitator script

### 0-8 · The quiet failure, the customer as the test, and the fence + the three ideas

Say it in your own words (keep it under eight minutes):

- "On November 1, 2026, Salesforce announced a package for the control plane it sells for running agents. The headline pieces are not new powers. They are a test that keeps running after the agent goes live, a hard spending limit that blocks the agent when the budget is reached, and a kill switch that pulls an agent offline, with a person's sign-off where the company's policy requires one."
- "Their example is painfully ordinary, and that is why it matters. A retailer moved its order-support agent to a cheaper model to save money. The agent kept answering in the same friendly voice, and its answers about delayed orders quietly became wrong. Scheduled tests caught it. The system flagged it and asked for approval to quarantine the agent. The team fixed the instructions, re-ran the tests on the cheaper model, and only then put the agent back."
- "Salesforce's own figures say fewer than half of the organisations running agents check them on live work, even though 96 percent run agents on more than one platform. So the agent is everywhere and the checking is occasional. Every piece of what they shipped can be run on paper by a business of any size. That is what we do today."

Three big ideas in plain words. Say them, then point at them all hour:

1. **A test you wrote, with the right answer written first.** Five real past jobs. The right answer written down by the person who does the job, before the agent sees the test, and never edited after the score is known. The person or system that grades the test is never the agent being tested.
2. **A limit in dollars, with a handoff.** Not a token count nobody can picture and not a warning email nobody reads. A weekly amount in money, a hard stop when it is reached, and a written answer to what happens next: what pauses, what goes back to a person, and who is told.
3. **An off switch with a name on it.** One named person can stop the agent, the stop has been rehearsed once while nothing was wrong, and the way back is a rule, not a mood: the failure is fixed and all five tests pass again before the agent restarts.

"Test first. Limit in dollars. A named hand on the switch."

### 8-18 · The six steps

Teach the six steps on the board. Use a home services and rental care business as the running example. The business cleans houses, turns over a small number of rentals between guests, and answers guest messages every day. Its example job is the guest-message reply agent it already trusts.

**Step one: write the inventory, three lines per job.** "Every recurring agent job you run gets three lines in one shared list. The job's name in plain words. Its weekly spending limit in dollars. The name of the person who can stop it. Salesforce ships a scanner that finds agents a company did not know it had, including a pilot from March that became permanent and kept spending after its owner changed jobs. Your version is the list. If a job cannot fill in the third line, that job does not run next week, because a job nobody can stop is not an automation. It is a commitment you made while asleep."

**Step two: write five tests from real past jobs, and write the right answers first.** "Pick jobs you have done so often you could grade them in your sleep. A guest question answered fifty times. A summary produced twenty times. For each one, save the real starting material, then write what a good result contains, in your own words, before you run the agent on it. Short is fine. Three lines of what must be true is a standard. The order is the rule: the standard is written first, and it is never edited after the test runs, because moving the standard after seeing the score is how every report card in history got inflated."

**Step three: score correctness and taste separately.** "Run the five tests and give each result two scores. Correctness: are the facts right, the times, the prices, the promises the business actually keeps. Taste: does it sound like your business, in length, in warmth, in what it leaves out. An answer can pass one and fail the other, and the fix is different for each. Wrong facts mean the instructions or the sources the agent reads are wrong. Wrong sound means your examples of good work are missing or stale. Write which kind of failure each failed test is, because 'the agent did badly' is not a repair instruction."

**Step four: set the spending limit in dollars, and name the handoff.** "For this one job, write a weekly limit in dollars. Under it, write what the stop does. Does the job pause and say so. Does the unfinished work go back to a named person the same day. Who is told, and how. A stop with no handoff is a smaller failure scheduled in advance. Then look once at where the money actually went last month if your tool reports it, the way Anthropic's new cost breakdown does by model, workspace, and user: the highest-cost job is usually retrying a failing step nobody told it to give up on. The limit prevents the bill. The look explains it."

**Step five: write the failure rule on one page, in four lines.** "Line one: when a test fails twice in a row, the agent stops. Line two: this named person is told the same day, by a message they actually read. Line three: this named person, and only this person, can restart it. Line four: before it restarts, the failure is fixed and all five tests pass again. This is the paper version of what Salesforce described: the test flags the problem, approval is asked, the agent is quarantined, the instructions are fixed, the tests are re-run, and only then is it back. Write the four lines where the whole team can find them, not in the chat where the agent works."

**Step six: rehearse the shutdown once, while nothing is wrong.** "Pull the agent offline on purpose, on a quiet job, and time it. Who noticed. How long did the stop take. Did the handoff happen the way the rule says. Then bring it back through the whole rule, tests and all. A switch you have never used is a decoration. The rehearsal is the difference between a plan and a story you tell yourself about a plan. Add the record habit from today's other stories while you are here: like agent-desktop's snapshot before and after each action, and like the verification column in a spreadsheet of AI-filled cells, keep the test results, the score, and the restart decision in one place a second person can re-check."

### 18-28 · Watch it work

Work one example live. Use the same home services and rental care business. Keep it to ten minutes.

1. "Here is the setup." *(The business's reply agent has answered guest messages well for two months. Five tests sit in a folder: a parking question, an arrival-time question, a question about a service the business never offers, a date question with a trap in it, and a complaint that needs warmth and no promises. The right answer for each is written in the owner's words. The weekly limit is written in dollars, and the owner is the named person who can stop the agent.)* "Nothing here took software. It took one quiet hour and the owner's own past messages."
2. "Here is the change nobody announced." *(To save money, the setup is moved to a cheaper, faster model on a Tuesday. The replies still sound lovely. On Friday the weekly tests run. Three pass. The arrival-time test fails: the reply offers an early arrival the business never promises, because cleaning takes the full time between guests. The parking test passes on facts and fails on taste: right answer, wrong tone, twice as long as the owner ever writes.)* "Read those two failures again. One is a fact failure, one is a sound failure. Yesterday this business learned about both from guests."
3. "Here is the rule doing its job." *(The failure rule says a failed correctness test on a promise the business never makes counts double, so the agent stops the same day. The owner is told by text message. Guest replies go back to the owner by hand for the weekend. Nobody apologises to a guest, because no guest received the wrong promise.)* "The failure happened inside a fence. The customer was never the test."
4. "Here is the fix, matched to the failure kind." *(The fact failure is an instruction failure: the standing facts file the agent reads does not state the arrival rule in the place the cheaper model looks. The owner moves that rule to the top of the file and states it as a never-offer. The taste failure is an examples failure: the folder holds no short reply. The owner adds two. The model itself is not changed back, because nothing yet says the cheaper model cannot do this job with better instructions.)* "Fix the instructions before you fire the model. It is cheaper, and half the time it is the truth."
5. "Here is the restart." *(All five tests run again. Five pass, both scores. The owner signs the restart line, with the date, under the test results. The agent goes back on Monday, at the cheaper model's cost, with the same weekly limit and the same five tests scheduled for Friday.)* "Same agent, same savings, one wrong promise caught by a test instead of a guest. That is the whole product Salesforce announced, running on paper, in a business with three cleaners and a shared inbox."

*Facilitator note:* if the room says their tool has no built-in tests, caps, or switch, answer with the paper version: "The test is a saved set of real jobs with written right answers. The cap is a weekly dollar figure checked on the same day each week, with a stop you perform yourself until the tool offers a hard one. The switch is the named person's ability to pause the job, which every scheduling and automation tool has somewhere. The products differ. The fence is the same, and the fence is the lesson."

### 28-33 · Your questions

Open floor. Answer in plain English. The three questions you will get, and the answers:

- "Is five tests enough to trust an agent?": "Five tests are not proof. They are a tripwire. They catch the common, expensive failures: the wrong fact, the invented promise, the tone drift after a quiet change. Add a test every time a real job teaches you a new way to fail, so the set grows from your own history, not from a template."
- "What if the agent passes and a customer still gets a wrong answer?": "Then that job becomes test six, with its material saved and its right answer written the same week. A test set that never grows is a photograph of the month you wrote it. And keep the human checks the other lessons built: approval before anything leaves the business, and a source you can open for any number a customer will rely on."
- "Where do my tests live, and who can change them?": "In a place you own, that the agent cannot edit. Today's news carried the warning twice: OpenAI's Evals platform became read-only on October 31, 2026 and shuts down on November 30, so test history kept only there needs exporting now; and a scorer the agent can reach is a scorebook it can rewrite. Keep the tests, the right answers, and the scores in your own files, and record the platform, the mode, and the model beside each run, because a mode can be retired on a date, like the Claude fast mode ending November 30, and an inventory that lists only a model name will miss it."

### 33-58 · Write your own tests, limit, and failure rule, and rehearse the shutdown

Everyone works solo or in pairs on one agent or automation they already trust (see `handout.md`). Circulate with only these prompts:

- "Read me your five tests. Which one has a promise in it that your business must never break?"
- "Show me a right answer. Did you write it before you ran the test, in your own words?"
- "Which failure is a fact failure and which is a sound failure? What repair does each one get?"
- "Read me your weekly limit. Is it in dollars? When it fires, whose desk does the work land on, the same day?"
- "Read your failure rule out loud. Who is told, who can stop it, who alone can restart it?"
- "What has to pass before the restart? Say the whole sentence."
- "Show me your inventory. Three lines per job: name, dollar limit, the person who can stop it. Which job could not fill in the third line?"
- "You just rehearsed the shutdown. How long did the stop take, and who noticed?"
- "Where do the tests live, and can the agent you are testing edit them? Move them if it can."

At minute 53, pull the room together. Three-minute share-out: volunteers name their job, the test that surprised them, and the name of the person who can stop it, in thirty seconds. "My job is ___. The test that surprised me was ___. The person who can stop it is ___."

Then Q&A to minute 58, and seed the "what could go wrong" story for anyone who asks:

**The failure gallery.** "The agent moved to a cheaper model by someone saving money, with no test running, discovered by a guest. The spending warning that went to a channel nobody reads, found in the monthly bill. The kill switch nobody had ever pressed, which needed a password nobody had. The test set the agent itself wrote and graded, all passing, forever. The right answers edited after a bad score, so the report card improved while the work did not. The tests left inside a platform that turned read-only, with the shutdown date already announced. Every one of these is prevented by a rule you used today: tests written first and kept in your own files, a limit in dollars with a handoff, a named owner, and a shutdown you have already rehearsed once."

### 58-60 · Wrap-up and homework

Close in two minutes:

1. Restate the promise kept: "You now hold an inventory with three lines per job, five tests with right answers written in your own words, two scores per test, a weekly spending limit in dollars with a named handoff, a four-line failure rule, and one shutdown already rehearsed while nothing was on fire."
2. Homework (say it exactly): "This week, run your five tests on every trusted agent job you have, on the same day, and write the scores where a second person can see them. Add one new test for every real failure you find. Bring your inventory, your scores, and the story of your rehearsal, how long the stop took and who noticed, to your next session."
3. Final line: "Give your agent a test, a spending limit, and an off switch. The test speaks first, the limit speaks in dollars, and a named hand is on the switch, every week."

## Facilitator notes

- Keep all language plain. "Test" here means a saved real job with a written right answer, run on a schedule and scored by someone or something other than the agent being tested. "Limit" means a weekly amount in dollars. "Off switch" means a named person's practised ability to stop the job.
- Do not present any product named in the news as approved or recommended. Salesforce's availability is stated exactly as announced: the kill switch, cost dashboard, wallet, and gateway policies generally available on 2026-11-01; Agent Evals and API Evals in beta in November 2026 and slated for general availability in January 2027, with some referenced features still in development, and the 75 percent token saving is Salesforce's test-scenario figure. The cost-analytics and nonprofit items, the agent-desktop token figures, and the platform deadlines are all stated with their sources and dates in the snips file.
- Treat the written right answers as the record of what good means for each job. They are never edited after a run; a changed standard is a new version, dated, with the old one kept.
- Time discipline: protect the 25-minute build block. Cut Q&A before cutting building time.
