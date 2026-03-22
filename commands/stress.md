---
description: Pressure-test the entire world for contradictions and gaps
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Agent, WebSearch, WebFetch
---

Read `${CLAUDE_PLUGIN_ROOT}/skills/worldbuilding-guide/SKILL.md` for core behavior rules.

# /stress — Pressure-Test

The devil's advocate pass. Read everything and find what's broken, missing, derivative, or ambiguous.

## Prerequisites

At least 3 `/build` sessions completed — some content must exist in `World/`. If `World/` is empty or has fewer than 3 notes: "Build more first. Run `/build` a few more times."

## Flow

Read every project doc: `seed.md`, `atlas.md`, `palette.md`, `questions.md`, `checklist.md`, and all `World/` notes. Then run these passes:

### 1. Contradictions

Atlas says X but a World note says Y. Timeline in one note conflicts with faction origin in another. Tone in seed doesn't match what's actually been built.

### 2. Underspecified Load-Bearing Walls

An atlas axiom that nothing in `World/` actually explains. A faction that exists in name only. A governance system referenced but never designed. A technology mentioned in multiple notes but never defined.

### 3. Derivative Detection

"This faction feels a lot like [existing IP]." Spawn subagents to search for similar worlds, factions, concepts. Flag anything too close. Help differentiate — don't just flag, suggest what would make it distinct.

### 4. Real-World Stress Testing

Apply real-world political, economic, and social logic to the world's systems. Examples:
- "You say X has sunset clauses. In real democratic systems, sunset clauses get extended 90% of the time. How does your world handle that?"
- "You have art competitions as the primary status mechanism. Historically, art patronage concentrates power. Does that happen here?"
- "Your immigration system screens for [X]. What are the civil liberties implications?"

Spawn subagents for research when real-world precedents are relevant.

### 5. Load-Bearing Unanswered Questions

Read `questions.md`. Identify questions that MUST be answered for the world to cohere. Not all of them — just the ones where the lack of an answer creates a structural hole.

### 6. Machine-Readability Check

Since the world bible will go to a code agent for a game: verify the docs are clear enough for another agent to parse without human context.

Flag:
- Ambiguous terms used differently across notes
- Undefined terms (used but never explained)
- Circular references
- Jargon without definition
- Notes that depend on vault-wide context to make sense
- Locked vs. open decisions that aren't clearly marked

## Output

Write a stress report — present it in conversation, don't just dump a file. For each issue:
- What's wrong
- Where it lives (file + section)
- Severity (structural, moderate, minor)
- Suggested fix or question to resolve it

The worldbuilder decides which to address. Each fix becomes a `/build` session or an inline edit.

## Conversation Style

Constructive adversary. The tone is "I'm trying to break this because I want it to be unbreakable." Not nitpicking — stress testing. Focus on structural issues first, surface-level stuff last. When flagging derivative content, be specific about what's similar and concrete about what would differentiate it.
