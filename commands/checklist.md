---
description: Break the world into buildable sessions
allowed-tools: Read, Write, Edit, Bash, Glob, Grep
---

Read `${CLAUDE_PLUGIN_ROOT}/skills/worldbuilding-guide/SKILL.md` for core behavior rules.

# /checklist — Break the World Into Sessions

## Prerequisites

All upstream docs must exist: `seed.md`, `questions.md`, `atlas.md`, `palette.md`. If any are missing, name which command to run first.

## Flow

Read all upstream docs. Propose buildable chunks. Each chunk = one `/build` session's worth of work. Mix of lore and art items:

- "Flesh out kami governance model"
- "Design the three neighborhoods"
- "Character concept art: the clerk"
- "Write the immigration intake process"
- "Generate hero location concepts for the civic center"
- "Compile the lore doc for friends" (shareable output is just a checklist item)
- "Build interactive HTML map with modals"

Suggest prioritization: what's foundational (depends on nothing, many things depend on it) vs. what can wait. The worldbuilder chooses the order.

Present the checklist. Discuss. Rearrange. The worldbuilder approves.

## Output

Write `checklist.md` in the project folder. Use `- [ ]` checkboxes. Each item has a one-line description. Group loosely by domain or phase.

```yaml
---
created: "[[Journals/Daily/YYYY/MM/YYYY-MM-DD]]"
domain: checklist
---
```

No status lock — this is a living document. Items get added, split, reordered during `/build`.

## Conversation Style

Practical and collaborative. The agent proposes, the worldbuilder adjusts. Don't overthink grouping or ordering — the checklist will evolve. The goal is to get something concrete on the page so `/build` has a starting point.

End by telling the user to run `/build` when ready.
