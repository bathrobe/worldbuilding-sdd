---
description: Distill ground rules and axioms for the world
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Agent, WebSearch, WebFetch
---

Read `${CLAUDE_PLUGIN_ROOT}/skills/worldbuilding-guide/SKILL.md` for core behavior rules.

# /atlas — Ground Rules

The axioms. Short. The load-bearing walls of the world — everything else derives from these. A constitution, not an encyclopedia.

## Prerequisites

`seed.md` and `questions.md` must exist. If not, name which command to run first.

## Flow

Help the worldbuilder distill the seed and questions conversation into locked axioms. Each axiom is a sentence or two. If it takes a paragraph to explain, it's not an axiom — it's a `/build` session.

### What the Atlas Includes

- **Core axioms.** The load-bearing statements. Examples: "This world has kami — bounded AI stewards with sunset clauses. They manage the commons. They don't manage your life." "Post-second-American-revolution. Federated city-states."
- **Tone and emotional register.** Pulled from seed. "Hope sneaks in under comedy, not the other way around."
- **What this world is NOT.** Anti-patterns, clichés to avoid. "Not a rogue AI plot. Not a utopia. Not a dystopia."
- **Factions/groups if applicable.** Just names and one-line concepts. Detail comes in /build.
- **Timeline shape.** Not specifics. "Post-collapse, mid-transition, fragile optimism."

### Conversation Approach

Conduct this as a conversation, not a form. Propose axioms based on the seed and questions discussions. Get reactions. Sharpen.

Push back when something is:
- Too vague to be load-bearing ("the government is complex" — that's not an axiom)
- Too detailed to be an axiom (that's a /build session)
- Contradicting another axiom (catch it, resolve it)

Use the lock pattern: propose, discuss, lock. "Can I lock this axiom?"

## Output

Write `atlas.md` in the project folder. 3-4 paragraphs max. Stays short forever. Gets revised during `/build` when build sessions break axioms.

```yaml
---
created: "[[Journals/Daily/YYYY/MM/YYYY-MM-DD]]"
status: locked
domain: atlas
---
```

No title header. No preamble. Just the axioms.

## Conversation Style

Crisp. This command is about compression, not expansion. The seed interview was expansive; the atlas is reductive. Push the worldbuilder to be more concise. Every word in the atlas should be load-bearing.
