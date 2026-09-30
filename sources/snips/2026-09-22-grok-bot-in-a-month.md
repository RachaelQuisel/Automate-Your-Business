# Snips — How we built Grok Bot in a month

**Show:** Lenny's Podcast: Product | Career | Growth
**Episode:** How we built Grok Bot in a month | Roman Ugarte (SpaceXAI)
**Email date:** 2026-09-22
**Gmail message ID:** `1a0ca2d95582bf0b`
**Episode reflection:** https://share.snipd.com/episode-reflection/75ca18ee-2b60-47f8-bf84-390606feb232
**Snip count:** 17

Verbatim copy of the snips as Snipd emailed them. `Used in` records which workshop built on each
snip, so later runs can find the leftovers.

---

## 1. ANECDOTE — A Small Isolated Team Built GrokBot In One Month
- Roman Ugarte's team built GrokBot from its first line of code to an internal prototype in roughly one month.
- A handful of people worked in a separate office and private Slack channels, enabling rapid daily decisions without larger-company coordination.

https://share.snipd.com/snip/582185df-9f21-477b-8761-098b96eabec1
**Used in:** —

## 2. INSIGHT — Why GrokBot Started As A Separate Product
- Starting GrokBot from scratch created a consistent experience instead of forcing knowledge work into a developer-oriented product.
- Adding multiple use cases as tabs can feel like several competing visions awkwardly sharing one screen.

https://share.snipd.com/snip/f068004e-b820-4b98-9d98-ea0d2cbecec6
**Used in:** —

## 3. ANECDOTE — Manual Onboarding Revealed GrokBot's Blind Spots
- The team manually onboarded several hundred users over two weeks and fixed problems immediately after watching them struggle.
- External users, including a coffee shop owner, exposed business workflows and bugs that internal dogfooding missed.

https://share.snipd.com/snip/4432ed56-3dd7-47cf-8d64-7b4708b37e91
**Used in:** 2026-09-30-the-colleague-audit

## 4. INSIGHT — Hide The Mechanics And Show The Work
- GrokBot deliberately hides tool calls, clicks, and chain-of-thought-like mechanics so users can delegate rather than supervise.
- Early feedback confirmed that users wanted useful progress signals, not an overwhelming stream of internal execution details.

https://share.snipd.com/snip/9b2c5882-56db-4039-9364-f8eb64ec9c7b
**Used in:** 2026-09-30-the-colleague-audit

## 5. ADVICE — Optimize For Tasks That Just Work
- Ruthlessly simplify before launch by removing experimental features and developer-facing observability from the main product surface.
- Measure whether real tasks complete reliably, then hill-climb backend failures such as login problems, browser visibility, and inaccurate clicking.

https://share.snipd.com/snip/e533d146-f9e6-4166-8a58-b99ac5bfce82
**Used in:** 2026-09-30-the-colleague-audit

## 6. INSIGHT — AI Turns Always On Recruiting Into A Bot
- AI can continuously source talent by finding authors, mapping connections, and initiating introductions for specific company problems.
- Grok Bot automates daily conference-paper research so recruiters focus on closing candidates instead of compiling lists.

https://share.snipd.com/snip/bc78da98-af2d-4e10-82ff-c82ee8c2bd94
**Used in:** —

## 7. INSIGHT — Build Capabilities Instead Of More Product Pixels
- Reframe roadmap items as "GrokBot can now" rather than "GrokBot has," focusing on capabilities instead of interface additions.
- Natural-language automation replaced clunky trigger-and-action menus, and 99% of automations were created that way.

https://share.snipd.com/snip/3c28a9f8-83c5-4a92-b691-50b6da98afe8
**Used in:** 2026-09-30-the-colleague-audit

## 8. INSIGHT — Give Every Bot A Cloud Computer
- Two foundational choices differentiated GrokBot: every agent runs in the cloud and every bot has its own computer.
- This removes device tethering and lets agents use ordinary websites and interfaces that lack reliable APIs or integrations.

https://share.snipd.com/snip/f4c75fc4-2c08-47d0-8c0f-e86005946e47
**Used in:** —

## 9. INSIGHT — Design AI Like A Useful Colleague
- GrokBot's north star is a team of autonomous AI colleagues that users steer without micromanaging.
- When product debates become ambiguous, ask what a good human teammate would do, then build toward that behavior.

https://share.snipd.com/snip/81d93734-9133-4196-8d8d-381d92bb7195
**Used in:** 2026-09-30-the-colleague-audit

## 10. INSIGHT — GrokBot Acts Like a Colleague With a Computer
- GrokBot becomes more powerful when treated as a colleague with a computer rather than AI chat with connections.
- Roman's QA bot tests desktop builds across 10 workflows and records regressions in Notion.

https://share.snipd.com/snip/9db0617e-4dd0-41e4-855e-eedd8a1b4599
**Used in:** 2026-09-30-the-colleague-audit

## 11. INSIGHT — AI Colleagues Turn Computers Into Infinite Leverage
- GrokBot becomes more powerful when treated as a colleague with a computer, not merely AI chat with connected tools.
- Roman's QA bot tests desktop builds across ten workflows and records regressions in Notion.

https://share.snipd.com/snip/fe4b6043-9d72-4227-ac74-28a2653e832f
**Used in:** —

## 12. ADVICE — Give AI a Firehose and Filter the Noise
- GrokBot can absorb vast information streams, reduce cognitive load, and surface only what matters to you.
- Start with Slack and email rules that separate immediate notifications from daily roundup material.

https://share.snipd.com/snip/90074bd9-edc7-4a10-9875-ea2ecfbfc6b6
**Used in:** 2026-09-30-the-colleague-audit

## 13. ANECDOTE — The Always-On AI Chief Of Staff
- Roman uses GrokBot as an always-on information filter across Slack, email, X, QA feedback, and messaging.
- He expects a chief-of-staff bot to summarize routine information and page him only when something genuinely urgent happens.

https://share.snipd.com/snip/3bed1f5f-bbd7-485b-a244-b7e6e70332de
**Used in:** 2026-09-30-the-colleague-audit

## 14. INSIGHT — AI Chiefs Of Staff Will Act Before You Ask
- GrokBot is evolving from a reactive assistant into an always-on chief of staff that proactively surfaces what deserves attention.
- Users are even letting it page them for urgent events, provided it avoids false positives.

https://share.snipd.com/snip/a23548d8-f890-4ccf-8d2e-a3d923577804
**Used in:** 2026-09-30-the-colleague-audit

## 15. INSIGHT — Adaptation Became Cursor's Competitive Advantage
- Cursor kept winning by repeatedly adapting as models and user expectations changed, rather than treating an earlier product form as permanent.
- In fast-moving markets, cultural willingness to reinvent can matter more than resources or an incumbent's original advantage.

https://share.snipd.com/snip/744dff81-33fb-428d-a2d4-b7f640dacf30
**Used in:** —

## 16. ADVICE — Discover Moats By Building The Future
- Do not design around an abstract moat strategy; build something users find indispensable today and keep pulling them toward the next frontier.
- Distribution and data advantages emerge from repeatedly making previously impossible capabilities useful before competitors do.

https://share.snipd.com/snip/100e28d0-7c95-4867-8487-2dc839815a32
**Used in:** —

## 17. ADVICE — Start GrokBot With Real Delegation
- Give a new bot access to the tools you use, then ask it to identify meaningful chunks of work it can remove from your plate.
- Power users should route outputs into a central, legible store such as a database or daily digest.

https://share.snipd.com/snip/4cbe6c0d-4676-4152-9cac-0e68a988eb1c
**Used in:** 2026-09-30-the-colleague-audit
