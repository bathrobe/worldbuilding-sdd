# Nano Banana Prompting

## Bundled Script

The plugin ships `scripts/generate_image.py` — a `uv run` script that calls the Gemini image API. Usage:

```bash
uv run ${CLAUDE_PLUGIN_ROOT}/scripts/generate_image.py "prompt" -o /path/to/output.jpg
```

Options: `--aspect-ratio` / `-a` (default `1:1`), `--size` / `-s` (`1K`/`2K`/`4K`, default `2K`), `--reference` / `-r` (repeatable, up to 14 images), `--use-search` (Google Search grounding). Always use `.jpg` extension.

After generating, open with Quick Look: `qlmanage -p "$IMAGE_PATH" &>/dev/null &`

Requires `GEMINI_API_KEY` in plugin `.env`, environment, or `~/.claude/.env`.

## Model Status

| Model | ID | Best For | Notes |
|-------|-----|----------|-------|
| **Nano Banana 2** (newest) | `gemini-3.1-flash-image-preview` | 4K output, most reliable | Actively supported |
| **Nano Banana Pro** | `gemini-3-pro-image-preview` | Highest quality, complex reasoning, up to 14 refs | $0.13-0.24/image, ~45% peak failure rates historically |
| **Nano Banana** | `gemini-2.5-flash-image` | Lower cost option | $0.039/image |
| **Imagen 4 Fast** | — | Cheapest | $0.02/image |

During `/onboard`, ask which model the user has access to and note any reliability preferences.

## Core Prompting Principles

**Natural language over tag soup.** NB Pro's autoregressive architecture understands intent, not keywords. Write like you're briefing a human artist.

- ❌ `"dog, park, 4k, realistic, trending on artstation, masterpiece"`
- ✅ `"A golden retriever catches a frisbee mid-leap in Central Park's Sheep Meadow. Late afternoon sunlight creates long shadows across the grass. Shot on 35mm film with shallow depth of field."`

**Edit, don't re-roll.** If an image is 80% right, iterate with specific edits rather than regenerating. For multiple simultaneous edits, use Markdown lists:

```
Make ALL of the following edits:
- Replace the background with a rainy Tokyo street
- Change her jacket from blue to red leather
- Add motion blur to passing traffic
- Keep her face and pose exactly the same
```

**Thinking mode** activates extended reasoning for complex compositions. Use for scenes requiring physics reasoning, precise counting, or real-world factual grounding via Google Search.

## ICS Framework

Structure prompts as **Image type + Content + Style**:

> "A photorealistic product photo [Image] of a premium leather watch band on a marble surface [Content] with soft directional lighting and minimal shadows, styled for a luxury e-commerce catalog [Style]."

## Character DNA Prompts

The foundation for consistent serialized characters:

```
[Identity Tag] + [Core Features] + [Viewpoint] + [Lighting] + [Style Lock]

Example: "Luna-Ki, round eyes with amber irises, teal asymmetric bob,
yellow hoodie with white star patch. 3/4 view, mid-shot, eye-level.
Soft diffused daylight, neutral white balance. Cel-shaded, clean lineart,
limited palette #FFD93D #2EC4B6 #1A1A2E."
```

**Preventing character drift:**
- Keep identity tag within the first 10 words of every prompt
- Fix your vantage point (same view/shot/level unless a scene demands otherwise)
- Define 2-3 brand hex codes for hair, clothing, key accessories — paste in every generation
- When drift occurs, return to your original anchor image rather than iterating from the drifted version

**Generate character sheets first** before any serialized project: *"Robot character sheet. Left: Front view. Right: Back view. Pure white background. Caption 'CHARACTER SHEET' with 'FRONT VIEW' and 'BACK VIEW' labels."* Save these as canonical anchors.

## Reference Image Cascading

NB Pro takes up to **14 reference images** per generation, with **6 high-fidelity object slots** and **5 human character slots**. Label inputs explicitly:

> "Image 1: Character sheet. Image 2: Previous scene. [New scene description]. Maintain the architecture, lighting color temperature, and atmospheric haze from the previous scene while moving the character to the marketplace plaza."

This is why `/palette` builds a reference library — it makes every `/build` image generation dramatically better.

## Style Bible Parameters

Lock these during `/palette` Phase 2:

| Element | Specification Example |
|---------|----------------------|
| **Projection** | 30° isometric, orthographic camera |
| **Lighting** | Top-left key light, 135° shadow angle, 20% opacity |
| **Palette** | #5263A5 #A7C7E7 #F1F1F1 #C9D6DF #679186 #EFCB68 |
| **Textures** | Clean matte materials, minimal noise, uniform edge treatment |
| **Typography** | Bebas Neue for headers, Inter for body, always white with 2px black outline |

## Faction Identity Systems

Prompt structure: *"Build a cohesive faction identity for [Faction] including: color palette ([colors]), typography ([style]), icons ([motifs]), pattern systems ([patterns]), and branded imagery ([visual elements]). Personality: [traits]."*

## Isometric Game Assets

Lock these parameters in every prompt: *"Orthographic look, 30° isometric projection, top-left key light, soft shadow, clean matte materials, palette [hex codes], minimal noise, game-ready tile 256×256, flat background, high consistency across set."*

Common fix: assets appearing in perspective instead of isometric — add "orthographic" explicitly. Noisy textures — add "clean matte materials, minimal texture noise, uniform edge treatment."

## Video Pipeline (Veo 3 + Google Flow)

NB Pro images serve as direct keyframes for Google's video generation:

- **Ingredients to Video**: Upload NB Pro outputs as character/object "ingredients" maintained across clips
- **Frames to Video**: Provide start/end keyframe images; Flow generates transitions
- **Extend**: Create 60+ second videos with continuous action
- **Scenebuilder**: Assemble clips into narrative sequences

For video input: use **16:9 at 2K**. PNG preserves quality better than JPEG for video initialization.
