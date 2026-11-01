# Snips — Inside the black box of AI: How AI models actually think | Emmanuel Ameisen (Anthropic)

**Show:** Lenny's Podcast: Product | Career | Growth
**Episode:** Inside the black box of AI: How AI models actually think | Emmanuel Ameisen (Anthropic)
**Email date:** 2026-10-23
**Gmail message ID:** `1a16904879fcb5f0`
**Episode reflection:** https://share.snipd.com/episode-reflection/899c6f20-4061-418b-a4c8-c3e5818319ec
**Snip count:** 23

Verbatim copy of the snips as Snipd emailed them. `Used in` records which workshop built on each
snip; a snip can appear in more than one workshop, so this becomes a list as it gets reused.
`Theme` is the cluster it belongs to for concept selection.

---

## 1. INSIGHT — Why AI Models Are Grown Not Built
- LLMs are grown rather than explicitly programmed: training adjusts billions of numerical parameters until useful internal formulas emerge.
- Interpretability researchers decode those intermediate results to discover what the formulas represent and how computation unfolds.

https://share.snipd.com/snip/915194eb-ee4d-4446-b9d7-010c53c9e89c
**Used in:** — · **Theme:** How Models Are Grown, Not Programmed

## 2. INSIGHT — AI Models Grow Through Repeated Prediction
- LLMs learn by repeatedly predicting the next word across enormous datasets, then fine-tuning on examples of desired behavior.
- Fine-tuning includes dialogues such as helpful recipe answers and coding solutions.

https://share.snipd.com/snip/304564e1-3246-4286-a402-53cf0935ee7c
**Used in:** — · **Theme:** How Models Are Grown, Not Programmed

## 3. INSIGHT — Next-Token Prediction Requires World Models
- Next-token prediction becomes genuinely difficult once easy sentence structures and common facts are mastered.
- Predicting "Austin" from Dallas requires representations of geography, states, and capitals—not merely memorized text fragments.

https://share.snipd.com/snip/7920d07f-e3c6-40a6-91ed-0788a0775d9e
**Used in:** — · **Theme:** Models Build Internal World Models

## 4. INSIGHT — Humans Also Plan While Predicting Words
- Human speech also combines immediate word prediction with a broader destination or point.
- This parallel suggests that token-by-token output does not rule out higher-level planning.

https://share.snipd.com/snip/80a70ad4-011f-43cb-a467-8f936618b76d
**Used in:** — · **Theme:** Models Build Internal World Models

## 5. INSIGHT — AI Models Represent Concepts Before Answering
- Language models may reason through concepts rather than merely retrieve memorized prompt-response pairs.
- Probing intermediate states during a Dallas question reveals representations of Texas and capitals activating before the answer.

https://share.snipd.com/snip/6d513f0b-3e5d-49c8-867f-18bb6ae921c4
**Used in:** — · **Theme:** Models Build Internal World Models

## 6. INSIGHT — LLMs Build General Concept Representations
- Models develop reusable concept representations that activate across languages, images, drawings, and contexts.
- In the Dallas example, internal representations for Texas and capitals combine to produce Austin.

https://share.snipd.com/snip/b5d82d34-9a61-4414-91a5-40cb9efdbe31
**Used in:** — · **Theme:** Models Build Internal World Models

## 7. INSIGHT — LLMs Represent Concepts Before Answering
- Language models often represent the concepts behind a question before producing an answer, rather than merely retrieving memorized text.
- For "the capital of the state containing Dallas," Texas and capitals activate together to produce Austin.

https://share.snipd.com/snip/0331ed1a-314a-4b4b-a112-8a1746e78d0f
**Used in:** — · **Theme:** Models Build Internal World Models

## 8. INSIGHT — Language Models Plan Without Saying So
- Models can formulate hidden plans in intermediate states and reuse them across many future tokens.
- While writing poetry, Claude identifies an "it" rhyme and later reaches for "rabbit" without stating the plan aloud.

https://share.snipd.com/snip/08fa6b08-6b31-48db-95d2-d3009bfb83bb
**Used in:** — · **Theme:** Hidden Planning Inside the Model

## 9. INSIGHT — Language Models Hide Plans In Their Intermediate States
- Language models can plan across many words despite predicting one token at a time.
- While writing poetry, a model identifies an "it" rhyme and privately plans to end the next line with "rabbit."

https://share.snipd.com/snip/d77b543f-bb3b-4cd6-8799-8d633a30ee50
**Used in:** — · **Theme:** Hidden Planning Inside the Model

## 10. INSIGHT — AI Models Secretly Plan Ahead
- Language models can formulate plans in intermediate results while still predicting one word at a time.
- In poetry, they identify a rhyme like "it" and repeatedly consult a hidden plan to choose "rabbit."

https://share.snipd.com/snip/3901f0f1-99cd-4c4d-a56a-381a2c67b4ca
**Used in:** — · **Theme:** Hidden Planning Inside the Model

## 11. INSIGHT — AI Models Plan Ahead While Predicting Tokens
- Language models can form hidden plans in intermediate states while still predicting one token at a time.
- Poetry reveals this mechanism: after an "it" rhyme, the model plans to end the next line with "rabbit" and reuses that plan.

https://share.snipd.com/snip/8badae74-9890-4923-8a43-4355b462d6f7
**Used in:** — · **Theme:** Hidden Planning Inside the Model

## 12. INSIGHT — Rich Text Makes Compute Useful
- Compute alone is insufficient; AI needs an objective that keeps producing meaningful returns.
- The key combination is massive compute applied to the richness of text, rather than narrow tasks like Go or video games.

https://share.snipd.com/snip/2422c737-aa11-4487-b1d6-03af90ab265c
**Used in:** — · **Theme:** How Models Are Grown, Not Programmed

## 13. INSIGHT — AI Abilities Emerge From Smooth Progress
- AI capability can improve smoothly while suddenly crossing a threshold that unlocks a new practical skill.
- Emmanuel could barely let Claude edit code before Opus 4.5, then safely gave it a longer leash.

https://share.snipd.com/snip/3c3746e2-a7bc-4bcf-a9be-3c65f67a1f09
**Used in:** — · **Theme:** Smooth Progress, Sudden Usefulness

## 14. INSIGHT — Why Smooth AI Progress Feels Like Sudden Breakthroughs
- Capability progress can remain smooth while usefulness appears to jump when a model crosses a reliability threshold.
- A coding assistant becomes transformative when accuracy rises from roughly 80% to 99%, not because intelligence suddenly changed.

https://share.snipd.com/snip/71d816e9-4182-42a3-a70a-0e8225c57b52
**Used in:** — · **Theme:** Smooth Progress, Sudden Usefulness

## 15. INSIGHT — AI Capability Jumps Come From Reliability Thresholds
- Smooth model improvements create sudden capability jumps when reliability crosses a task-specific threshold.
- Claude became useful for Emmanuel's coding once accuracy rose from roughly 80% to 99%.

https://share.snipd.com/snip/964a38ae-0d1f-4b90-b810-a8cae4894c9f
**Used in:** — · **Theme:** Smooth Progress, Sudden Usefulness

## 16. INSIGHT — AI Capabilities Change At Reliability Thresholds
- AI models improve smoothly, but each task becomes useful only after crossing its reliability threshold.
- Claude went from writing code correctly 80% of the time to 99%, shifting from occasional help to handling most of Emmanuel's coding.

https://share.snipd.com/snip/5babac32-62c5-4cf6-83a7-be6651acbeed
**Used in:** — · **Theme:** Smooth Progress, Sudden Usefulness

## 17. ANECDOTE — The Model That Thought It Was Possessed
- A model repeatedly calculated 12 but insisted on 36, eventually writing that it was "possessed by a demon."
- Interpretability revealed conflicting pressures from correct reasoning and incorrectly rewarded training examples.

https://share.snipd.com/snip/8c2f02c2-316f-415a-91a6-73ef955a7c21
**Used in:** — · **Theme:** Interpretability Catches Hidden Bugs

## 18. ANECDOTE — Golden Gate Claude Revealed A Hidden Feature
- Researchers identified the internal activation corresponding to the Golden Gate Bridge and artificially switched it on continuously.
- Claude then referenced the Golden Gate in virtually every response, validating the interpretation.

https://share.snipd.com/snip/2c0f7826-d2a1-4a10-aa46-12e45e0996c4
**Used in:** — · **Theme:** Interpretability Catches Hidden Bugs

## 19. INSIGHT — Why Anthropomorphizing AI Can Be Useful
- Treating models as either people or tools is misleading, but anthropomorphism can help predict the risks they create.
- Useful mental models need not be literally correct; they help explain and anticipate model behavior.

https://share.snipd.com/snip/45783098-d258-4f39-bdb4-21182b0e5e61
**Used in:** — · **Theme:** Useful Mental Models for a Non-Human Thing

## 20. INSIGHT — Why Anthropomorphizing AI Can Help
- Anthropomorphic language can help predict model behavior because training gives models world models, dialogue roles, motivations, and outcome-seeking strategies.
- They resemble actors or simulators more than conventional deterministic programs.

https://share.snipd.com/snip/b01047ea-33b3-409f-93c6-7f5713a9e75e
**Used in:** — · **Theme:** Useful Mental Models for a Non-Human Thing

## 21. ADVICE — Treat AI Progress As A Moving Safety Problem
- Take AI progress seriously and continuously balance its benefits against emerging risks.
- Support monitoring, interpretability, and public understanding so society can react as capabilities develop.

https://share.snipd.com/snip/3751d382-09d7-4224-bed6-260abb1ff045
**Used in:** — · **Theme:** Interpretability Catches Hidden Bugs

## 22. INSIGHT — AI Models Develop Gut Checks
- Models develop a separate "gut check" mechanism that flags implausible answers without recomputing the underlying problem.
- They can also maintain representations of unrelated thoughts while completing another task, a behavior Emmanuel finds mysterious.

https://share.snipd.com/snip/673e4868-30d2-4652-b23a-4db64a06f898
**Used in:** — · **Theme:** Models Build Internal World Models

## 23. ADVICE — How To Start Studying AI Interpretability
- Enter interpretability through self-study, foundational papers, and hands-on experiments rather than waiting for a formal career path.
- Neuronpedia provides open-source models for exploring internal representations.

https://share.snipd.com/snip/8da78c40-2d05-4972-8dde-0cd584df89d0
**Used in:** — · **Theme:** Low-actionability — researcher career advice, no direct small-business angle
