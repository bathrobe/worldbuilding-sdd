# Worldbuilding SDD

Spec-driven worldbuilding. Eight commands take you from emotional seed to stress-tested world bible — interviewing, researching, locking decisions, generating concept art, and writing to your Obsidian vault.

## Commands

```
/onboard → /seed → /questions → /atlas → /palette → /checklist → /build → /stress
```

| Command | What It Does |
|---------|-------------|
| `/onboard` | Configure workspace: VOICE.md, image model, project folder, one-sentence brief |
| `/seed` | Interview to draw out the world's emotional and thematic core |
| `/questions` | Generate a massive bank of provocative worldbuilding questions |
| `/atlas` | Distill ground rules and axioms — the load-bearing walls |
| `/palette` | Establish art direction: mood boards, style lock, maps, character seeds |
| `/checklist` | Break the world into buildable sessions |
| `/build` | The workhorse — one checklist item per session, repeatable |
| `/stress` | Pressure-test everything for contradictions, gaps, and derivative content |

First five are sequential (prerequisites enforced). After `/checklist`, it's organic.

## How It Works

The agent is a curious interviewer. One question at a time, free-form. It researches aggressively (web search, real-world precedents), catches contradictions, and writes to the vault using your words. Decisions get explored, then locked. Locked decisions are permanent until explicitly revised during `/build`.

## Image Generation

BYOK (bring your own key). The plugin doesn't ship image gen tools. `/onboard` asks which model you have:

- **Nano Banana 2** or **Nano Banana Pro** (via Gemini API)
- **Flux** (via Replicate)
- Other, or none

Images are part of the creative conversation, not a deliverable at the end. The plugin generates concept art during brainstorming to tighten the feedback loop.

## Vault-Native

Reads and writes directly to your vault as plain Markdown. Wikilinks, frontmatter, the works. Each project creates a folder with structured lore notes in `World/` and art assets in `Art/`.

## Downstream Use

The world bible is designed to be machine-readable — drop it into a code repo and a coding agent can build from it. `/stress` checks for machine-readability as one of its passes.

## Setup

1. Install the plugin
2. Run `/onboard` to configure your first project
4. Optionally: set up a Nano Banana or Flux API key for image generation

## Dependencies

- A vault or folder of Markdown files (the plugin writes directly to it)
- Obsidian recommended (for wikilink navigation) but not required
