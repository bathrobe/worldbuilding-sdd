---
description: Build one checklist item — the repeatable workhorse
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Agent, WebSearch, WebFetch
---

Read `${CLAUDE_PLUGIN_ROOT}/skills/worldbuilding-guide/SKILL.md` for core behavior rules.
Read `${CLAUDE_PLUGIN_ROOT}/skills/worldbuilding-guide/references/art-pipeline.md` when generating concept art.
Read `${CLAUDE_PLUGIN_ROOT}/skills/worldbuilding-guide/references/nano-banana-prompting.md` if NB Pro is configured and art is involved.

# /build — The Workhorse

Repeatable. Run once per session. Pick up where the last session left off.

## Prerequisites

`checklist.md` must exist with at least one unchecked item. If not: "Run `/checklist` first" or "All items are checked — run `/stress` to pressure-test, or add new items to the checklist."

Read `onboard.md` for image model config. Read `atlas.md` and `palette.md` for locked decisions. Read any existing `World/` notes for context on what's already built.

## Session Flow

### 1. Pick a Focus

Show unchecked checklist items. Suggest the next logical one: "This builds on what we locked last time" or "This is foundational and unblocks three other items." The worldbuilder picks. If they say "let's do X" without looking at the checklist, that's fine too.

### 2. Interview + Research

Draw out the worldbuilder's ideas on the topic. One question at a time. Spawn subagents for real-world research when precedents would help.

Push back on contradictions with existing locked decisions. Catch drift: "This sounds like it contradicts what we locked in the atlas about [X]."

Surface relevant unanswered questions from `questions.md` when they're pertinent to the current topic.

### 3. Lock What Works

At natural stopping points, propose locks: "Can I lock this? [Precise statement of what's being locked]." Locked decisions are explicit — the worldbuilder says yes or not yet.

### 4. Write to Vault

Each topic gets a note in `World/`. Follow this format:

```yaml
---
created: "[[Journals/Daily/YYYY/MM/YYYY-MM-DD]]"
status: draft | locked
domain: governance | daily-life | economy | faction | character | location | ...
---
```

No title header. No preamble. Just start. 3-4 paragraphs max. If overflowing, split into a new linked note. Use the worldbuilder's words. Cross-reference via `[[wikilinks]]`. Link art assets with `![[Art/...]]`.

### 5. Concept Art

When visual decisions are being made and image tools are configured:
- Attach relevant references from `Art/References/` and `Art/Characters/` to the prompt
- Follow the locked style from `palette.md`
- Store outputs in the right `Art/` subfolder with descriptive filenames
- Show image to the worldbuilder for reaction
- Give honest feedback: "The composition works but the color palette drifted from what we locked"

### 6. Revise Upstream When Needed

When the worldbuilder has a stray thought that breaks an earlier decision:
1. Catch it. "Wait — if that's true, the atlas needs to say that."
2. Help update the upstream doc (atlas, questions, palette, or checklist).
3. Note what changed and why.
4. Flag any downstream content that's now potentially stale.
5. Return to the current build item.

### 7. Update Checklist

Mark the item done in `checklist.md`. Add new items discovered during the session — these often emerge from tangential riffs. Propose them: "That sounds like a new checklist item — 'Design the [X] system.' Want me to add it?"

## Conversation Style

The build session is a focused creative workshop. One topic per session. Deep, not broad. The agent is a collaborator who happens to be taking notes and writing to the vault. The conversation should feel productive and alive — not like dictation.
