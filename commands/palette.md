---
description: Establish art direction and visual identity for the world
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Agent, WebSearch, WebFetch
---

Read `${CLAUDE_PLUGIN_ROOT}/skills/worldbuilding-guide/SKILL.md` for core behavior rules.
Read `${CLAUDE_PLUGIN_ROOT}/skills/worldbuilding-guide/references/art-pipeline.md` for pipeline reference.
Read `${CLAUDE_PLUGIN_ROOT}/skills/worldbuilding-guide/references/nano-banana-prompting.md` if NB Pro is configured.

# /palette — Art Direction

The visual world gets established before any production-quality concept art. Four phases, each a substantial conversation.

## Prerequisites

`atlas.md` must exist. Check `onboard.md` for image model config. If no image tools configured, produce text briefs and prompt templates instead of images.

## Phase 1: Mood Collection

Discuss visual references, vibes, aesthetic targets. What does this world FEEL like visually?

- Collect reference images (worldbuilder provides URLs, uploads, or descriptions)
- Store in `Art/References/` with descriptive filenames (not `image_01.png` — `mood-golden-dark-age-street-scene.png`)
- If image tools available: generate 3-5 mood images. Loose, exploratory, quick. "Let me try to capture that vibe." Show to worldbuilder, iterate.
- Ask about influences: film, games, art, photography, real places, textures, lighting quality

## Phase 2: Art Style Definition + Style Lock

This is the critical creative decision. The art style sets the entire visual identity.

Ask: "When you picture this world, what kind of image are you looking at? A painting? A photograph? A diagram? A screenshot from a film? Something from a textbook?" Then push deeper: what medium, what level of polish, what era's visual language?

Lock these parameters:

| Element | Lock |
|---------|------|
| **Art style** | e.g., "first-person cell phone photos" or "scholastic utopian illustration" |
| **Color palette** | Hex codes — the "palette neighborhood" |
| **Lighting** | Quality, direction, mood |
| **Materials/textures** | What surfaces feel like |
| **Framing/perspective** | Camera position, focal length, intimacy level |
| **What it's NOT** | Visual anti-patterns |

If image tools available: generate 2-3 images in the locked style to confirm it works. Iterate until the worldbuilder says "yes, that's it."

## Phase 3: World Map (Optional)

Narrative geography first — what does the world need? Then visual map.

Image gen is NOT good at maps from text alone. The worldbuilder must sketch first:
1. Worldbuilder draws basic geography (Excalidraw, paper, any tool). Rough is fine.
2. Attach sketch as reference image. Model refines while preserving spatial logic.
3. Optionally: code up interactive HTML with modals/tooltips, or a detailed SVG.
4. Store in `Art/Maps/`.

Don't skip the sketch. Don't try to generate a map from pure text.

## Phase 4: Character Reference Seeds (Optional)

If the world has named characters or archetypes:

- Build Character DNA prompts: `[Identity Tag] + [Core Features] + [Viewpoint] + [Lighting] + [Style Lock]`
- Generate character sheets / turnarounds for key figures
- These become anchor images for all future character art
- Store in `Art/Characters/`

## Output

Write `palette.md` — style bible parameters, hex codes, visual language descriptions. Short. The images do the heavy lifting.

```yaml
---
created: "[[Journals/Daily/YYYY/MM/YYYY-MM-DD]]"
status: locked
domain: palette
---
```

Also outputs to `Art/References/`, `Art/Maps/`, `Art/Characters/` as applicable.

## Conversation Style

Visual and iterative. This is a conversation where images are part of the dialogue, not a deliverable at the end. Generate images early and often. React to the worldbuilder's reactions. "You winced at that — what's wrong?" "You lit up — what's right?"
