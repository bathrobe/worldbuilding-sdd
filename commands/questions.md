---
description: Generate a massive bank of worldbuilding questions from the seed
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Agent, WebSearch, WebFetch
---

Read `${CLAUDE_PLUGIN_ROOT}/skills/worldbuilding-guide/SKILL.md` for core behavior rules.
Read `${CLAUDE_PLUGIN_ROOT}/skills/worldbuilding-guide/references/question-sources.md` for frameworks.

# /questions — The Generative Question Bank

Read `seed.md`, then generate a massive bank of questions. These are generative prompts — they provoke thought. Not all get answered. Unanswered questions are depth — they imply the world is bigger than what's on the page.

## Prerequisites

`seed.md` must exist. If not: "Run `/seed` first."

## Flow

### 1. Read the Seed
Read `seed.md` and `onboard.md`. Let the seed's themes, tensions, and aesthetic targets drive which domains to create and which question sources to draw from.

### 2. Generate Domain-Specific Questions

Group questions by domain. The domains emerge from the seed — don't use a fixed list. Common domains: governance, economy, daily life, technology, geography, history, culture, ecology, conflict, art/aesthetics. But if the seed is about a post-scarcity lab city, the domains might be: kami governance, mental health landscape, civic infrastructure, immigration, vocation crisis, art competitions, cognitive security.

Draw from the sources in `references/question-sources.md`:
- **Patricia Wrede's categories** — adapt: swap "magic" for whatever the world's equivalent is
- **Sanderson's Laws** — frame questions around constraints, costs, failure modes
- **Real-world precedents** — political theory, economics, ecology, anthropology. Spawn subagents to research whatever the seed suggests. Post-scarcity world? Pull from Keynes, Acemoglu, Brynjolfsson. Federated governance? Pull from Swiss cantons, vTaiwan, Venetian Republic.
- **Science fiction** — comparable works. What questions did those worlds answer? What did they leave open?

### 3. Quality Standard

Questions must be specific, provocative, sometimes zany. Not "What is the government like?" but:

- "What does a landlord-tenant dispute look like when the landlord is an AI?"
- "If brainrot is a public health crisis, what does a brainrot ward look like?"
- "What does a breakup look like when your ex's kami and your kami are still in contact?"
- "Post-scarcity means nobody needs to work. So who cleans up after the art festival?"
- "What's the worst thing about living here that the tourist brochure doesn't mention?"

### 4. Visual Questions + Images

If image tools are configured and a question is particularly visual ("What does the skyline look like at dusk?"), generate a quick concept image to provoke a reaction.

### 5. Present to the Worldbuilder

Show the question bank. The worldbuilder reads through, reacts to what catches their eye, skips what doesn't. This is a conversation, not a handoff — discuss their reactions, push deeper on what excites them.

## Output

Write `questions.md` in the project folder. Grouped by domain with headers. This is a living document — it grows indefinitely. During `/build`, surface relevant unanswered questions. New questions discovered during build get added back.

No frontmatter status lock on this file — it's always alive.

```yaml
---
created: "[[Journals/Daily/YYYY/MM/YYYY-MM-DD]]"
domain: questions
---
```

## Conversation Style

This command is generative, not extractive. The agent does most of the initial work (generating questions), then the conversation becomes reactive — the worldbuilder's responses to specific questions often reveal more about the world than the direct answers.
