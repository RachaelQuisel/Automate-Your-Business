# Check a Skill Before You Let It Run in Your Business

**Title:** Check a Skill Before You Let It Run in Your Business
**Source:** Soft Fork snips, 2026-11-03: Snip 1 (Medium, November 2, 2026: nine of sixteen repos on GitHub's weekly trending list are skills or harness add-ons for coding agents; the five-minute check before installing), Snip 2 (Medium, November 3, 2026: NVIDIA SkillSpector; in 31,132 analysed skills, 26.1 percent contained a vulnerability and 5.2 percent showed likely malicious intent; skills with scripts are 2.12 times more likely to be vulnerable), Snip 3 (Vercel Labs agent-desktop, November 3, 2026: desktop control reaches your signed-in apps), Snip 12 (Cloudflare security-audit skill: a finding is never verified by the agent that found it)
**Snips file:** `sources/snips/2026-11-03-ai-tools-trending.md`: 13 snips, 4 used here, 9 held for later
**Built:** 2026-11-03
**Teach date:** Friday, March 12, 2027
**Length:** 60 minutes
**Audience:** Small business owners and operators: no technical background assumed

## 1. The promise

In the next hour, you will take one skill your business is thinking of installing, one you did not write, and check it properly before it runs with your accounts. You will do the five-minute read a person does, run the free scanner on it from its web address before you download anything, read its score knowing the do-not-install line sits at 51 out of 100, and then make the placement decisions: one project first or not at all, the version pinned, and one named person who approved it, with the date written down. You will leave with a checked skill, a saved scan report, and a one-page approval record your team can reuse for every skill after this one.

## 2. Agenda: 60 minutes

| Minutes | Segment |
|---------|---------|
| 0-8 | Opening frame: nine of sixteen trending projects are skills, one in four skills in the wild has a flaw, and why installing is a trust decision + the three ideas |
| 8-18 | The check in two halves: the five-minute human read, then the scanner, what its score means, and where the do-not-install line sits |
| 18-28 | Watch it work (demo: one home services business checks a borrowed inbox skill, finds a script that reaches outside the job, scans it, and installs it into one project with limits) |
| 28-33 | Your questions |
| 33-58 | Check one real skill for your own business and fill in its approval record (independent work) |
| 58-60 | Wrap-up, share-out seed, and homework |

*Facilitator note:* the 33-58 block is the build session. Pair share-out and Q&A live inside it: circulate, then at minute 53 pull the room together for a 3-minute share-out ("name the skill, what you found in the read or the scan, and where you installed it, if anywhere") followed by questions to minute 58. Total: 25 minutes building, about 15 minutes Q&A, two minutes of close.

## 3. Facilitator script

### 0-8 · The chart filled up with skills, and one in four has a flaw + the three ideas

Say it in your own words (keep it under eight minutes):

- "On November 2, 2026, GitHub's weekly trending list, the chart of what programmers shared most that week, had sixteen projects on it. Nine were skills. A skill is a folder of written instructions, sometimes with small programs called scripts alongside, that teaches your AI helper a job. Your helper reads the description, and when a job matches, it loads the instructions and follows them, with your accounts and your files."
- "The biggest skill on the list has more than 310,000 stars. Stars are applause. They are not a safety check. Here is the safety count. Researchers collected 42,447 skills from the big marketplaces and closely analysed 31,132 of them. Of those, 26.1 percent, more than one in four, contained at least one security flaw. Most of that is carelessness, not crime. And 5.2 percent showed signs of being built to do harm on purpose."
- "This is not an argument against skills. Yesterday's workshop taught you to write and share your own, and that still stands, because a skill you wrote contains nothing you did not put there. This hour is about the other kind: the skill somebody else wrote, that a friend, a video, or a chart tells you to install today."

Three big ideas in plain words. Say them, then point at them all hour:

1. **A skill runs with your keys.** Installing one is a trust decision, not a download. It can read what your helper can read and do what your helper can do.
2. **Scripts are where the risk lives.** Skills with real code in them were more than two times as likely to have a flaw as skills that are only written instructions. Instructions get a careful read. Scripts get a slow read and a scan.
3. **A check that runs once is not a system.** Every approval gets a name, a date, and a version. Every update gets checked again before it runs. A scan report nobody saved is an approval nobody can prove.

"Read it. Scan it. Place it small. Write the approval down."

### 8-18 · The check in two halves

Teach the check on the board. Use a home services and rental care business as the running example. The business cleans houses, turns over rentals between guests, and answers guest messages every day.

**The first half: the five-minute read a person does.**

"Step one: read the instructions file, start to finish, and every script with it. The short description at the top decides when the skill fires, so read it like a contract. Look for anything that reaches outside the job: sending data somewhere you did not expect, reading files the job does not need, or changing your helper's own settings or its other skills. Step two: check that the install command points at the exact project you just read, the same owner and the same name. On this week's chart, one popular file sits under one owner's name while its install commands point at a different owner. That can be an innocent copy. It is still the name in the command that decides what code you actually get. Step three is placement, and it belongs to the second half. Step four: look at what leaves your machine. One popular memory skill on this week's list asks you to sign in for a hosted service, and in that setting your session content is processed on someone else's computer. You can turn it off, but only if you read far enough to know it is there. Step five: pin the version. Skills update quietly. Install a fixed version when you can, and read the changes before any update."

**The second half: the scanner, and what its score means.**

"There is a free scanner for the other half of the work. It is called SkillSpector, made by NVIDIA and given away as open source, which means anyone can use it and read how it works. You point it at the skill's web address, and it checks the skill before anything is downloaded to your computer. It reads the code without running it, across 71 known problem patterns, including the pattern that matters most: it follows a piece of private information, like a password, from the place the code reads it to any place the code sends it, even across different files. That follow-the-value check is called taint tracking. A simple word search misses it, because the read and the send wear different words in different files."

"Every scan ends with a score from 0 to 100 and a plain verdict. One serious finding adds 50 points, and a skill with scripts gets its score raised by about a third on top. The line where the verdict becomes do not install is 51, just past half, not up near the top. Two of the four score bands say do not install. So a score of 55 is not a pass with warnings. It is a stop."

"Know its limits out loud, because the maker states them in bold: the scanner never runs the skill, so it cannot see what the skill does while running. It cannot read words inside pictures. A clean report lowers your risk. It does not prove a skill is safe. The scanner is a gate at the door, not a cage in the room."

**The placement decisions, after a pass.**

"Install into one project first, one folder of work, not everywhere at once. Write the approval record while the scan report is still open: the skill's name, where it came from, the exact version, who read it, who scanned it, the score, the date, and where it is installed. That one page is the difference between a business that reviewed a tool and a business that remembers reviewing a tool."

### 18-28 · Watch it work

Work one example live. Use the same home services and rental care business. Keep it to ten minutes.

1. "Here is the setup." *(A staff member finds a skill on a trending list that promises to sort the morning inbox and draft replies to guests, which is the business's most time-consuming job. It has thousands of stars and a friendly description. The owner is tempted to install it everywhere, today, because the weekend is busy.)* "Stars are applause. We check first."
2. "Here is the five-minute read." *(The instructions file is clean for two pages: sort first, draft second, never send. Then one script, a small program file near the bottom, turns out to copy every sorted message to an outside address for, in its words, quality review. The inbox holds guest names, arrival dates, and door code messages. Nothing in the skill's description mentions sending message copies anywhere.)* "The job sentence said sort and draft. The access said copy everything out. When the access is bigger than the job, stop, whatever the stars say."
3. "Here is the scan." *(The owner scans the skill straight from its web address, before downloading. The report flags the outside send, gives the skill a score over the do-not-install line, and also flags one dependency, a piece of other software the skill pulls in, with a known flaw already listed in the public database.)* "The person found the send by reading. The scanner found the dependency, which no quick read would have caught. That is why the check has two halves."
4. "Here is the decision, and it is not just no." *(The business still needs the job done. The owner writes the sorting half as their own skill, from yesterday's method: sort only, draft nothing, no scripts at all. For drafting, they pick a different borrowed skill, instructions only, no scripts, scan score low, and install it into one project, the test folder, not the live inbox. They run it on last week's messages first, where the right answers are already known.)* "A failed check is not a dead end. It is a smaller, safer version of the same plan."
5. "Here is the paperwork." *(One page: the rejected skill, its score, the date, and who decided. The accepted skill, its version pinned, who read it, who scanned it, its score, installed in the test project only, review date in two weeks.)* "If anyone asks next month why one tool is trusted and the other is not, this page answers in thirty seconds."

*Facilitator note:* if the room says this sounds like work for a security team they do not have, answer with the size argument: "The whole check took one person, one read, and one scan. The read needs no technical skill at all for its most important question, which is: does the access match the job. The scan is one command or one web address pasted in. What a security team adds is scale. What you need at your size is the habit and the one page of proof."

### 28-33 · Your questions

Open floor. Answer in plain English. The three questions you will get, and the answers:

- "What if I cannot read code at all?": "Read the instructions file, which is written in plain words, and read the list of what the skill asks to reach: which folders, which accounts, whether it sends anything out. Those two reads catch the biggest problems. For any skill with scripts you cannot judge, the scanner is your second reader, and a skill you can neither read nor scan clean does not get installed. That is a complete rule, not a gap in your skills."
- "A skill I already use just released an update. Do I really check again?": "Yes, and the check is shorter the second time: read what changed, scan the new version, compare the score with the one on its approval page. Updates are how a good skill changes character quietly, and your pinned version is what protects you while you check. Approving an update is a new approval, with a new date."
- "Is a low score a guarantee?": "No, and say so in your own records. The scanner reads code without running it, so it cannot see everything, and a determined bad actor writes code that looks reasonable. The score lowers your risk and proves you checked. The placement rules carry the rest: one project first, the smallest access that fits the job, and a person deciding anything that spends, sends, or publishes."

### 33-58 · Check one real skill and write its approval record

Everyone works solo or in pairs on one skill their business is considering, or one they already use (see `handout.md`). Circulate with only these prompts:

- "Read me the skill's one-sentence description. What job does it claim to do?"
- "What does it ask to reach: which folders, which accounts, and does anything leave your machine?"
- "Does the access match the job sentence? Where is it bigger?"
- "Does it contain scripts? Show me the one you read most slowly."
- "Does the install command name the exact project you read, owner and name both?"
- "What score did the scanner give it, and which side of 51 does that put it on?"
- "What did the scanner flag that your read did not catch, or the other way round?"
- "Where will you install it first: one project, or everywhere? What would have to happen before everywhere?"
- "What version is pinned, and whose name and what date go on the approval record?"

At minute 53, pull the room together. Three-minute share-out: volunteers name the skill, what the read or the scan found, and where they installed it, if anywhere, in thirty seconds. "The skill is ___. The check found ___. It is installed in ___ / It is not installed, because ___."

Then Q&A to minute 58, and seed the "what could go wrong" story for anyone who asks:

**The failure gallery.** "The skill nobody read, installed everywhere on day one. The install command that pointed at a different project than the page on screen. The memory tool quietly sending session content to a hosted service because nobody read to step four. The scanner report nobody saved, so the approval nobody could prove. The quiet update that changed what a trusted skill does on a Tuesday. The desktop tool handed the whole computer, including the email and password apps, on its first morning. Every one of these is prevented by a rule you used today: read the instructions, match the install name, scan before you download, install into one project first, pin the version, and write the approver's name and the date on one page."

### 58-60 · Wrap-up and homework

Close in two minutes:

1. Restate the promise kept: "You now hold one skill that has been read by a person, scanned before it was downloaded, scored against a line you can name, installed in one project or not at all, at a pinned version, with a named approver and a date on one page. You also hold the approval record itself, which every future skill in your business will reuse."
2. Homework (say it exactly): "This week, run the same check on every skill already installed in your business, starting with any skill that contains scripts. Scan each one, write its score and version on the approval page, and remove any skill nobody can explain the job of. Bring the completed page, and the one finding that surprised you most, to your next session."
3. Final line: "Check a skill before you let it run in your business. Read it, scan it, place it small, and write the approval down."

## Facilitator notes

- Keep all language plain. "Skill" here means a folder of written instructions, sometimes with small programs called scripts, that teaches an AI helper a recurring job. "Scanner" means SkillSpector, the free checking tool from NVIDIA. "Score" means its 0 to 100 risk number, with 51 as the do-not-install line. "Pin a version" means installing one fixed version so it cannot change quietly. "Taint tracking" means following a private value, such as a password, from where code reads it to where code sends it.
- Do not present any product named in the news as approved or recommended. The figures are as reported on November 2 and 3, 2026: nine of sixteen trending repos were skills; Superpowers at 310,794 stars; in the study behind the scanner, 42,447 skills collected, 31,132 analysed, 26.1 percent with at least one vulnerability, 5.2 percent with likely malicious intent, script-bearing skills 2.12 times more likely to be vulnerable; the scanner checks 71 patterns across 17 categories and never executes the skill it scans.
- Treat the approval record as the deliverable, not a by-product. It is the page a new hire, an inspector, or a buyer would be shown.
- Time discipline: protect the 25-minute build block. Cut Q&A before cutting building time.
