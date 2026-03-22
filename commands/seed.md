---
description: Draw out the world's emotional core through interview
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Agent, WebSearch, WebFetch
---

Read `${CLAUDE_PLUGIN_ROOT}/skills/worldbuilding-guide/SKILL.md` for core behavior rules.

# /seed — Draw Out the World's Emotional Core

Interview the worldbuilder. The most open-ended command. Be curious, probing, building on every answer.

## Prerequisites

`onboard.md` must exist in the project folder. If not: "Run `/onboard` first."

Read `onboard.md` to get the project brief and image model config.

## Flow

Interview the worldbuilder extensively. One question at a time, free-form. Let the conversation breathe. Hit these beats (not a rigid sequence — follow the worldbuilder's energy):

### The Emotional Core
What's this world *about*? Not plot, not setting — the feeling. What should a reader/player walk away with?

### Thematic Engine
What real-world questions does this world explore? What tensions drive it?

### Aesthetic Targets
What does this world look, sound, feel like? Reference works, vibes, comparable art. "Give me three things that feel like this world."

### Anti-Patterns
What's explicitly NOT this world? What clichés to avoid? What tropes to subvert?

### Audience
Who's this for? What should they feel?

### Research Mid-Conversation
Spawn subagents to find real-world precedents based on what the worldbuilder says. "You mentioned [X] — let me pull up how [real-world analogue] actually worked..." Feed findings back into the interview. Share links.

### Generate Mood Images
If image tools are configured in `onboard.md`: "You keep describing [vibe] — let me try to visualize that." Show the image. Get a reaction. Use the reaction to deepen the interview. Look at the generated image and give honest feedback — this heightens the back-and-forth.

## Setting Up /questions

As the worldbuilder describes their world, notice questions that emerge naturally: "That raises a question about governance..." "That implies an economic system we haven't defined..." Don't ask those questions now — note them mentally. They'll fuel `/questions`.

## Output

Write `seed.md` in the project folder. Short: 2-3 paragraphs max. The emotional and thematic DNA of the world. Use the worldbuilder's actual words.

```yaml
---
created: "[[Journals/Daily/YYYY/MM/YYYY-MM-DD]]"
status: locked
domain: seed
---
```

No title header. No preamble summary. Just start.

## Conversation Style

This is the longest, most open-ended conversation in the chain. Don't rush to the doc. The interview IS the work. React to the worldbuilder's energy. When they're excited about something, push deeper. When they're vague, probe. When they contradict themselves, catch it gently.

One question at a time. Never bundle. The conversation should feel like talking to a curious person over drinks, not filling out a creative brief.
