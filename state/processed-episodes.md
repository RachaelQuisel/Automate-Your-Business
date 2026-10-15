# Processed episodes

One row per **workshop** built — not per episode. A single episode now yields several workshops
(one per concrete concept), so the same Gmail message ID appears more than once as its episode
gets mined for different concepts on different days. `Concept` names which one each row covers.

The routine reads this and the `Used in` field on every snip in `sources/snips/` before picking
a concept. A snip's `Used in` field is a list — a snip can be cited in more than one workshop.
An episode is exhausted (no longer a source for new workshops) only once at least 90% of its
snips have each been cited in two or more workshops. See `CLAUDE.md` Step 1 and Step 3.

Append-only. Newest at the bottom.

| Built | Show | Episode | Gmail message ID | Concept | Snips cited | Workshop |
| --- | --- | --- | --- | --- | --- | --- |
| 2026-09-30 | Lenny's Podcast: Product | Why companies are becoming a series of loops \| Anish Acharya (a16z) | `1a0ca56e2e758bc1` | (pre-dates per-concept tracking) | 7 of 14 | `workshops/2026-09-30-the-loop-audit` |
| 2026-09-30 | Lenny's Podcast: Product | How we built Grok Bot in a month \| Roman Ugarte (SpaceXAI) | `1a0ca2d95582bf0b` | (pre-dates per-concept tracking) | 10 of 17 | `workshops/2026-09-30-the-colleague-audit` |
| 2026-10-01 | Super Data Science: ML & AI | 1024: In Case You Missed It in August 2026 | `1a0a0b550e180e54` | (pre-dates per-concept tracking) | 10 of 11 | `workshops/2026-10-01-the-proof-audit` |
| 2026-10-13 | Lenny's Podcast: Product | OpenAI's Head of ChatGPT: We're entering a new era of AI (again) \| Tibo Sottiaux | `1a10ca55f2a41555` | Standing Watch | 3 of 10 | `workshops/2026-10-13-the-standing-watch` |
| 2026-10-15 | How I AI | Jev: 8 real use cases for the fastest, cheapest model I've ever used \| John Lindquist | `1a13a4c9edf357fa` | The Sorting Line | 5 of 11 | `workshops/2026-10-15-the-sorting-line` |

## Episodes archived, with mining status

Every episode whose snips are archived in `sources/snips/`, regardless of whether a workshop has
been built from it yet. This is what Step 3 scans each run — not just the newest Gmail search.

| Email date | Show | Episode | Gmail message ID | Snips file | Status |
| --- | --- | --- | --- | --- | --- |
| 2026-08-13 | The a16z Show | Sam Altman on Sora, Energy, and Building an AI Empire | `19ff8f685e56df2c` | `2026-08-13-sam-altman-sora-energy-ai-empire.md` | Not yet mined |
| 2026-09-04 | Lenny's Podcast: Product | How to close $100K+ enterprise deals, step by step \| Jen Abel | `1a06e9bf4b55c04c` | `2026-09-04-jen-abel-enterprise-deals.md` | Not yet mined |
| 2026-09-14 | Super Data Science: ML & AI | 1024: In Case You Missed It in August 2026 | `1a0a0b550e180e54` | `2026-09-14-super-data-science-august-recap.md` | 1 workshop built; 1 of 11 snips still at zero citations |
| 2026-09-22 | Lenny's Podcast: Product | Why companies are becoming a series of loops \| Anish Acharya (a16z) | `1a0ca56e2e758bc1` | `2026-09-22-series-of-loops.md` | 1 workshop built; 7 of 14 snips still at zero citations |
| 2026-09-22 | Lenny's Podcast: Product | How we built Grok Bot in a month \| Roman Ugarte (SpaceXAI) | `1a0ca2d95582bf0b` | `2026-09-22-grok-bot-in-a-month.md` | 1 workshop built; 7 of 17 snips still at zero citations |
| 2026-10-03 | The a16z Show | The Personal Agent Race Is Here \| Anish Acharya & David Pawlan | `1a0ff9bc1b066061` | `2026-10-03-personal-agent-race.md` | Not yet mined — 6+ strong themes identified |
| 2026-10-03 | The Vergecast | Dots get up in Muse's business | `1a100d80f5cf4aba` | `2026-10-03-dots-get-up-in-muses-business.md` | Not yet mined — mostly off-topic for this audience; a few usable themes |
| 2026-10-05 | Lenny's Podcast: Product | OpenAI's Head of ChatGPT: We're entering a new era of AI (again) \| Tibo Sottiaux | `1a10ca55f2a41555` | `2026-10-05-chatgpt-new-era-of-ai.md` | 1 workshop built (Standing Watch); 5+ more concepts identified, unbuilt |
| 2026-10-13 | How I AI | OpenAI Dev Day 2026: The releases that actually matter | `1a13781b209b24dc` | `2026-10-13-openai-dev-day-2026.md` | Not yet mined — mostly a product-release rundown, thin on owner-actionable concepts |
| 2026-10-13 | How I AI | How Grok Bot designers use AI agents to build personal sites and product prototypes \| John Bai & Peng Zheng | `1a13772dce7ef82f` | `2026-10-13-grok-bot-designers-build-prototypes.md` | Not yet mined — 4+ themes identified (start-small building, trash-can prototyping, one-bot-one-job, teaching bots to recover) |
| 2026-10-14 | How I AI | Jev: 8 real use cases for the fastest, cheapest model I've ever used \| John Lindquist | `1a13a4c9edf357fa` | `2026-10-14-jev-fastest-cheapest-model.md` | 1 workshop built (The Sorting Line); 6 of 11 snips still at zero citations |
| 2026-10-14 | David Senra | Creating Muse: The Fastest-Growing AI Product Since ChatGPT \| Alexandr Wang, Meta | `1a13a3d73a5d8b15` | `2026-10-14-creating-muse-ai-product.md` | Not yet mined — 4+ themes identified (trust builds in small bets, reliability over demo speed, show the benefit not the tech) |
| 2026-10-14 | The a16z Show | The Top 100 Consumer AI Apps: Who's Actually Paying? | `1a13a837527a0a32` | `2026-10-14-top-100-consumer-ai-apps.md` | Not yet mined — mostly market data; 2 themes with an owner angle (build durable value, go deep not broad) |
| 2026-10-14 | Hard Fork | A.I. Agents: Cute, Cuddly and Maybe Catastrophically Dangerous? | `1a13a67652d6c529` | `2026-10-14-cute-cuddly-catastrophically-dangerous-agents.md` | Not yet mined — one strong theme (what you hand an agent the keys to), rest is macro AI-safety/policy |
| 2026-10-14 | All-In with Chamath, Jason, Sacks & Friedberg | GPT-6 Hits AGI? Tech Euphoria 2.0, SF Mansion Shortage, NYC Bans AI in Schools & Venezuela Oil Deal | `1a13ab8e98d3325f` | `2026-10-14-gpt-6-agi-and-euphoria.md` | Not yet mined — mostly macro markets/policy/geopolitics; one usable theme (don't mistake a security bug for a rogue agent) |
| 2026-10-14 | Lenny's Podcast: Product | How we restructured Airtable's entire org for AI \| Howie Liu (co-founder and CEO) | `1a13b0c5244fd560` | `2026-10-14-airtable-reorg-for-ai.md` | Not yet mined — 7+ themes identified (protect time to experiment, prototype not spec, low-hanging fruit first) |

No episode above is exhausted by the 90%-used-twice rule — most haven't been touched at all.
Runway for daily workshops is currently measured in dozens, not days.
