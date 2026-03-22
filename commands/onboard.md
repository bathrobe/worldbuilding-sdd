---
description: Configure a new worldbuilding project workspace
allowed-tools: Read, Write, Edit, Bash, Glob, Grep, Agent, WebSearch, WebFetch
---

Read `${CLAUDE_PLUGIN_ROOT}/skills/worldbuilding-guide/SKILL.md` for core behavior rules.

# /onboard — Configure the Workspace

Runs once per project. Configuration, not creative work.

## Prerequisites

None. This is the entry point.

## Flow

### 1. VOICE.md Check

Check if a VOICE.md exists at vault root or project root. If not, ask (free-form, not a widget):

"Before we start — how do you write? Give me a paragraph of your published work or describe your style, and I'll draft a VOICE.md so I can match your voice when writing to the vault."

Draft it, get approval, write it.

### 2. Image Model Configuration

The plugin ships with a Nano Banana script at `${CLAUDE_PLUGIN_ROOT}/scripts/generate_image.py`. Check if `GEMINI_API_KEY` is set (in plugin `.env`, environment, or `~/.claude/.env`).

If the key exists, test it:
```bash
uv run ${CLAUDE_PLUGIN_ROOT}/scripts/generate_image.py "quick test: a single brushstroke on canvas" -s 1K -o /tmp/nb-test.jpg
```

If it works, show the image to the user — this doubles as a first visual spark. Store `image_model: nano-banana-pro` in `onboard.md`.

If no key, ask: "Do you have a Gemini API key? You can get one free at https://aistudio.google.com/apikey. The plugin works without images but they're a big part of the creative loop."

Also ask if they have other models (Flux via Replicate, etc.) and note those in `onboard.md`.

### 3. Project Folder Creation

Ask the user where in their vault this project should live. Then create:

```
[Project]/
  onboard.md
  seed.md
  questions.md
  atlas.md
  palette.md
  checklist.md
  World/
  Art/
    References/
    Maps/
    Factions/
    Locations/
    Characters/
    Props/
```

Don't pre-populate the .md files — just create empty ones so the folder structure is visible. `onboard.md` is the only one that gets content now.

### 4. Quick Brief

Ask: "One sentence: what's this world?"

Just enough to personalize the `/seed` interview. Not a brainstorm — that's /seed's job.

## Output

Write `onboard.md` in the project folder with:
- Image model choice and config details
- VOICE.md location (vault-relative path)
- Project brief (the one sentence)
- Folder paths

Add frontmatter:
```yaml
---
created: "[[Journals/Daily/YYYY/MM/YYYY-MM-DD]]"
status: locked
domain: config
---
```

## Conversation Style

Keep it brisk. This is setup, not the creative work. Four questions max, then write the config and move on. End by telling the user to run `/seed` when ready.
