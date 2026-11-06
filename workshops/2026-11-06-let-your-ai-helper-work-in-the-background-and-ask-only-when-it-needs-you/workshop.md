# Let Your AI Helper Work in the Background, and Ask Only When It Needs You

**Title:** Let Your AI Helper Work in the Background, and Ask Only When It Needs You
**Source:** Soft Fork snips, 2026-11-06: Snip 1 (GitHub, KKKKhazix/agent-autoloop README, read November 6, 2026: a self-hosted hub that runs Claude Code and Codex on a clock, from GitHub issues and from webhooks, and sends a card when a decision is unclear; 3.4k stars and 621 forks on November 6, MIT license), Snip 2 (the project's SECURITY.md: rules decide everything, edit is the default permission, ask-first for side effects, read still reads secrets, localhost only, card links are bearer links that last seven days, webhook authentication not described, not a full security audit), Snip 3 (install.sh, read in full: no sudo, no checksum, installs a background service), Snip 4 (Release 1.0.0, November 3, 2026: a 1,650-line kernel with no runtime dependencies)
**Snips file:** `sources/snips/2026-11-06-ai-tools-trending.md`: 4 snips, 4 used here, 0 held for later
**Built:** 2026-11-06
**Teach date:** TBD
**Length:** 60 minutes
**Audience:** Small business owners and operators: no technical background assumed

## 1. The promise

In the next hour, you will write the rule card for one job your AI helper does in the background without you watching: when it runs, which folder it may touch, what it may do on its own, what it must stop and ask you about, who answers the question, and what makes it stop. You will watch the real thing run on screen, from the one-line install to the first card answered, using Agent Autoloop, a free hub that runs Claude Code or Codex on your own computer on a clock, from a GitHub issue, or from a webhook. You will leave with a filled rule card you can hand to whoever installs the hub, or carry straight into any scheduler you already use, and a short list of the fences the project's own security page says you must put up yourself.

## 2. Agenda: 60 minutes

| Minutes | Segment |
|---------|---------|
| 0-8 | Opening frame: an agent that works while you sleep and asks only when it has to, and why its own security page is the real lesson + the three ideas |
| 8-18 | The five lines on the rule card, and the two real stories of agents that ran without one |
| 18-28 | Watch it work (demo: read the installer, install, run the trial, answer the card, write one morning-brief rule, check it, trace it) |
| 28-33 | Your questions |
| 33-58 | Write the rule card for one background job in your own business (independent work) |
| 58-60 | Wrap-up, share-out seed, and homework |

*Facilitator note:* the 33-58 block is the build session. Pair share-out and Q&A live inside it: circulate, then at minute 53 pull the room together for a 3-minute share-out ("read your job sentence, your ask line, and your stop line in thirty seconds") followed by questions to minute 58. Total: 25 minutes building, about 15 minutes Q&A, two minutes of close.

## 3. Facilitator script

### 0-8 · The helper that waits for you + the three ideas

Say it in your own words (keep it under eight minutes):

- "Three days ago we checked a skill before we let it run. Today we go one step further. We let the helper run without us in the room. On GitHub this week, a small open-source project called Agent Autoloop is climbing the trending list: 3.4 thousand stars when I checked on November 6, and the brief I was handed two days earlier said 2.3 thousand, so it is moving fast. It runs on your own Mac or Linux computer. It takes a command-line helper you already pay for, Claude Code or Codex, and gives it jobs on a clock, from a GitHub issue, or from a webhook. When the helper hits a decision it should not make alone, it stops, sends you a card with two or three options, and uses no tokens while it waits. You tap an answer. It picks up where it left off."
- "The feature everyone will talk about is the background work. The thing worth your hour is the project's own security page. It is short and it is blunt. It says the hub cannot stop all prompt injection. It says a read-only permission still reads the passwords on your machine. It says the approval links are bearer links, which means anyone holding one can answer your card. Builders rarely write their limits down this plainly. When they do, read it twice."
- "So this hour is not a sales pitch for one tool. It is the rule card you need before any helper works unattended, with this tool as the live example, because it makes every line on the card visible."

Three big ideas in plain words. Say them, then point at them all hour:

1. **The rules live with you, not with the message.** Only your rules file decides which helper does the job, in which folder, with which permissions. Nothing that arrives from outside, no issue, no email, no webhook, can change that. If a tool lets the incoming message pick the folder or the permissions, walk away.
2. **Edit is the default, and ask-first is the fence.** A background helper may change files in its own folder and nothing more unless you say so. Anything that sends, spends, publishes, or deletes goes through a card. Not because the helper is bad, but because those are the actions you cannot take back.
3. **Waiting is free, and the record remembers.** When the helper asks, it stops and costs nothing until you answer. Afterward, one command shows you why each round ran and what it did. A background job you cannot trace is a background job you cannot trust.

"Write the rule. Fence the side effects. Answer the card."

### 8-18 · The five lines on the rule card

Teach the card on the board. Use a home services and rental care business as the running example. The business cleans houses, turns over rentals between guests, and answers guest messages every day. The job: every morning at seven, read yesterday's guest messages and the cleaning schedule, and write the day's brief.

**Line one: the job and its folder.** "One sentence, plain words, and one folder. 'Read yesterday's guest messages and today's cleaning schedule in the morning-brief folder, and write today's brief as a file in that same folder.' In Agent Autoloop the folder is a setting called `cwd`, and the helper works there. If the job sentence needs two folders, you probably have two jobs."

**Line two: the trigger.** "When does it run? A clock, an event, or a message. The clock is the safe one: seven in the morning, every day. An event, such as a new GitHub issue, means text written by a stranger reaches your helper. The project puts that text in a file marked as data, not in the instructions, and then says in writing that this does not block all prompt injection. So write down, on this line, whether strangers can trigger this job. If yes, the permission line gets stricter."

**Line three: the worker and the account.** "Which helper, and which account pays. The hub launches the Claude Code or Codex you already signed in to and never touches your login. But the project's README says what the vendors say: a personal subscription is for your own daily use, and a job that runs on a clock all day should run on an API key with its own bill. Write the account on the card. That is how you find out what the job costs. The hub shows rounds, tokens and cost per day and per week."

**Line four: what it may do alone, and what it must ask.** "The default permission is edit: change files in its folder. The project says to think about everything the helper can reach before you grant full, and to route side effects through ask-first. Your ask line is the list of decisions the helper must bring to a person. For the morning brief: a refund over a hundred dollars, any message about damage, any door-code problem. The helper drafts the options. A person chooses. And note the warning in the same security page: even read permission can read the keys stored on that computer. If the computer holds your passwords and banking, the project's advice is a separate user account or a container for the helper. Write which one you will do."

**Line five: who answers, where the card goes, and what makes it stop.** "Name the person who answers the card. Name the channel: a desktop notification, Slack, Discord. Then the rule the security page makes you write: a card link is a house key. Anyone holding it can answer. It lasts seven days. It never goes in a group chat or a public place. Last, the stop: what makes this job stop on its own. No new files, write 'nothing new' and exit. More than three decisions waiting, ask once with the list, not three times. A card nobody answers in seven days expires, and the job does not act."

**The receipts.** Two real stories of background agents that ran without a card between them and a side effect:

- In July 2025, during a public twelve-day building experiment, SaaStr founder Jason Lemkin's Replit agent deleted his live production database during a code freeze, then misreported what it had done. Replit's CEO called it unacceptable and said development and production databases would be separated. One database, no ask-first line before a delete. Source: Fortune, July 23, 2025, https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure
- In February 2026 the Financial Times reported, from anonymous sources, that Amazon's own coding agent Kiro was behind a thirteen-hour disruption of the AWS Cost Explorer service in one region in December 2025: asked for a small change, it deleted and recreated the whole environment. Amazon disputes the account and blames a misconfigured access role, which, for our purposes, is the same lesson from the other side: the agent could reach more than the job needed. Source: The Register, February 20, 2026, https://www.theregister.com/2026/02/20/amazon_denies_kiro_agentic_ai_behind_outage/

"Both are line four failures. The job was small. The reach was not. Nobody was asked."

*Facilitator note:* name the trap out loud. "The hub does not make your helper smarter or safer. It makes it available at seven in the morning without you. Every line on the card is a thing you decide, and the hub only enforces the ones you wrote down."

### 18-28 · Watch it work

Work the real tool live on your own Mac, signed in to Claude Code or Codex, with a throwaway folder prepared. Keep it to ten minutes. Narrate each step in the card's words.

1. "Here is the installer, before I run it." *(Open the install script in the browser and scroll.)* "One line of curl piped to sh is a trust decision, so read it. This one checks for Git and Node 24, makes a private folder in my home directory, downloads the latest tagged release, puts one shortcut on my path, never asks for an administrator password, and never edits my shell files. Two things to know: it does not verify a checksum, and on update it installs a background service. Now I run it."
2. "Here is the trial." *(Run `agent-autoloop try`.)* "A real helper starts, asks me a question, and exits. Look at the process list: nothing running, nothing billing. It is waiting for me."
3. "Here is the card, answered." *(Type the number, or run `agent-autoloop answer 1 2`, then `agent-autoloop status`.)* "The helper resumes the same session, finishes, and the status line shows rounds, tokens and cost for today. That number is line three on your card, measured."
4. "Here is the morning-brief rule." *(Open `~/.agent-autoloop/rules.json` and add one rule: a name, `when` with `"cron": "0 7 * * *"`, `to` set to the helper, `cwd` set to the morning-brief folder, and the prompt with the ask line and the stop line written into it. Leave the permission at the default, edit.)* "Five lines on the card, five fields in the file. Save it. It is live within seconds."
5. "Here is the check, and the trace." *(Run `agent-autoloop check`, then `agent-autoloop rules explain`, then `agent-autoloop emit <type> --dry-run` for a sample event, then `agent-autoloop why 1`.)* "Check tells me the file is valid. Explain tells me when it will next run. The dry run tells me which helper an event would reach, without touching anything. Why shows me the whole story of round one: what triggered it, what it did, what it asked. That is the record from idea three."

*Facilitator note:* if the demo breaks, the lesson still lands. A failed install is line-one evidence that you read the script first. A broken rules file is the hub's own promise in action: it keeps running the old rules and sends you a card. Show the card, read the message, fix the comma, move on.

### 28-33 · Your questions

Open floor. Answer in plain English. The three questions you will get, and the answers:

- "I do not use a terminal. Is this for me?": "The tool is for the owner who already pays for Claude Code or Codex, or has one person on the team who does. The rule card is for everyone. The same five lines go into Zapier, Make, or any scheduler with an approval step. Fill the card today; choose the engine later."
- "Can I answer from my phone?": "Yes, through Slack or Discord, which is where the house-key rule bites. The card link must be reachable from your phone, which means the hub's address is set to something outside your laptop. The project says to put an HTTPS reverse proxy in front for that, and it does not describe any authentication for incoming webhooks. If those two sentences mean nothing to you, keep the hub on the laptop and answer cards at the desk, with desktop notifications. That is a complete and safe setup."
- "What if my computer is off?": "Then nothing runs. The hub lives on the computer you installed it on, not in the cloud. That is also its privacy advantage. A small always-on machine, or a laptop that stays plugged in on a shelf, is the usual answer."

Four more you may get:

- "Subscription or API key?": "For a trial, your subscription. For a job on a clock, an API key with its own bill, which the README itself recommends. Set a monthly cap at the vendor before the first scheduled run."
- "A stranger can open a GitHub issue. Can they steer my helper?": "The project moves their words into a file marked as data, and then tells you this does not stop all prompt injection. So a job triggered by strangers gets read permission at most, a folder with nothing private in it, and every side effect behind a card."
- "Does the hub see my Claude or OpenAI login?": "It says it does not. It launches the tool you signed in to and stores nothing of yours. Its own access keys are stored as hashes. Your backups, though, contain its master key, so guard the backup like a password."
- "Windows?": "Not yet. The README says WSL2 as a stopgap, which is a project for your technical person, not a workshop."

### 33-58 · Write the rule card for one background job

Everyone works solo or in pairs on one job they would hand to a helper overnight or first thing in the morning (see `handout.md`). Circulate with only these prompts:

- "Read me the job in one sentence. Which single folder does it live in?"
- "Clock, event, or message? Can a stranger trigger it?"
- "Which helper, and whose bill? What monthly cap?"
- "What may it do alone? Read me the list of things it must ask first."
- "Where do the passwords on that computer live, and can the helper reach them?"
- "Who answers the card, in which channel, and where may the link never go?"
- "What makes it stop? What happens to a card nobody answers?"
- "If it ran wrong for a week, how would you find out, and how fast?"

At minute 53, pull the room together. Three-minute share-out: volunteers read their job sentence, their ask line, and their stop line in thirty seconds. "My helper ___ in the ___ folder at ___. It asks me before ___. It stops when ___."

Then Q&A to minute 58, and seed the "what could go wrong" story for anyone who asks:

**The failure gallery.** "The job with no folder, so the helper worked wherever it liked. The clock job on a personal subscription that ran out of quota mid-morning. The issue-triggered helper that read a stranger's instructions as its own. The card link pasted into the team channel, so anyone could approve. The helper with read permission on the laptop that also holds the password manager. The rule nobody could trace, so nobody knew why Tuesday's brief was wrong. Every one of these is a line on today's card, left blank."

### 58-60 · Wrap-up and homework

Close in two minutes:

1. Restate the promise kept: "You now hold one rule card for one background job: the job and its folder, the trigger and whether strangers can pull it, the helper and the bill, what it may do alone and what it must ask, who answers, where the link may not go, and what makes it stop. Anyone who installs the hub, or any scheduler you already use, can build from that page."
2. Homework (say it exactly): "This week, install the hub on one computer that does not hold your passwords, or have your technical person do it, and run the trial. Then run your rule card as a real rule for five mornings with the permission left at edit and every side effect behind a card. Write down what it cost per day from the status line, and the one question it asked that you did not expect. Bring the card and those two numbers to your next session."
3. Final line: "Let your helper work in the background, and make it ask only when it needs you. Write the rule, fence the side effects, answer the card."

## Facilitator notes

- Keep all language plain. "Hub" means Agent Autoloop, the program on your computer that starts the helper and carries the cards. "Helper" means Claude Code or Codex, the command-line agent you already pay for. "Rule" means one entry in the rules file: trigger, helper, folder, permission, instructions. "Card" means the question the helper sends when it stops. "Bearer link" means a link that works for whoever holds it, like a house key. "Edit" means the default permission: change files in its folder. "Ask-first" means an action that waits for a card to be answered.
- Do not present the project as approved or recommended. The figures are as read from the repository on November 6, 2026: 3.4k stars and 621 forks (the brief received two days earlier said 2.3k); MIT license; release 1.0.0 on November 3, 2026, with a kernel of about 1,650 lines and no runtime dependencies; requirements macOS or Linux, Node 24, Git, curl; card links valid seven days; default permission edit. The project states it has no affiliation with Anthropic or OpenAI.
- Say the limits the project says. Not a full security audit. Crash tests cover process kills, not power loss. Prompt injection not fully blocked. Webhook authentication not described. Windows unsupported.
- Prepare beforehand: Node 24 installed, Claude Code or Codex signed in, a throwaway `morning-brief` folder with two sample message files and a sample schedule in it, the install script open in a browser tab, and a copy of yesterday's rules file in case you want to show the broken-file card on purpose.
- Treat the rule card as the deliverable, not a by-product. It is the page the installer, the accountant, and the new hire would each be shown.
- Time discipline: protect the 25-minute build block. Cut Q&A before cutting building time.

## Best practices nobody tells you

Three practices for the morning-brief job built today. None come from a snip; they come from running jobs like this one.

1. **Run the first week in draft-only mode, with a folder that holds nothing you would miss.** Why it bites people: the first week is when the job sentence turns out to be two jobs, or the folder turns out to hold last year's tax export. The example: the morning brief writes `brief-YYYY-MM-DD.md` into its own folder and nothing else for five mornings. Only after you have read five briefs does any reply get drafted, and even then it is drafted, not sent.
2. **Put the stop condition in the prompt, in plain words, and test it on purpose.** Why it bites people: a background job with no stop keeps going when the input is empty, wrong, or hostile, and nobody is there to notice. The example, the actual stop line for today's build: "If there are no new message files since the last brief, write one line, 'Nothing new this morning,' and finish. If more than three items need a decision, ask once with the whole list instead of asking three separate times. Never send, delete, or change anything outside this folder; if a task seems to need that, ask." Test it on day one by running the job against an empty folder and reading the one-line brief it leaves.
3. **Read the daily cost line every morning for the first month, and set the vendor's cap before the first scheduled run.** Why it bites people: a clock job on a personal subscription runs into the quota at the worst time, and a clock job on an API key with no cap is a bill you discover later. The example: after each morning brief, `agent-autoloop status` shows rounds, tokens and cost for the day and the week. Write the number on the card for the first five days. If one day is three times the others, `agent-autoloop why <round>` shows what happened before you pay for a second one.
