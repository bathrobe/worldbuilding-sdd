# Professional Art Pipeline

Film and game production pipeline adapted for a solo worldbuilder with an AI image model. This is the reference for `/palette` and concept art generation in `/build`.

## Production Pipeline (Pixar/ILM/Weta adapted)

1. **Mood boards** (earliest, broadest) — tone, atmosphere, color direction
2. **Color keys / color scripts** — emotional tone across scenes, sequential
3. **Environment sketches** — landscape, setting, establishing shots
4. **Character sketches** — diverse iterations, silhouette exploration
5. **Prop design** — specific objects, tech, artifacts
6. **Turnarounds / model sheets** — front/side/back views, production-ready
7. **Callout sheets** — concept art with labeled material/surface breakdowns
8. **Design packets** — comprehensive reference for all departments

## Named Deliverables

| Deliverable | What It Is | When |
|-------------|-----------|------|
| **Mood Board** | Curated visual collage — tone/atmosphere | /palette Phase 1 |
| **Style Bible** | Master reference: art style, colors, materials, rules | /palette Phase 2 |
| **Color Script** | Sequential emotional/visual progression | /palette Phase 2 |
| **Character DNA Prompt** | Identity tag + core features + viewpoint + lighting + style lock | /palette Phase 4 |
| **Character Turnaround** | 360° views: front, side, back, 3/4 | /palette Phase 4 |
| **Concept Sheet** | Iterations showing design evolution | /build |
| **Callout Sheet** | Marked-up concept showing material breakdowns | /build |

## Reference Flow Through the Plugin

1. `/palette` Phase 1 collects mood references → `Art/References/`
2. `/palette` Phase 2 locks the style bible → `palette.md`
3. `/palette` Phase 3-4 creates map and character anchors → `Art/Maps/`, `Art/Characters/`
4. Every `/build` art generation attaches relevant references from the library to the prompt
5. NB Pro takes up to 14 reference images — the palette phase builds the library that makes this powerful

## Style Lock Parameters

Lock these during /palette Phase 2:

| Element | Example |
|---------|---------|
| **Art style** | "first-person cell phone photos" or "scholastic utopian illustration" |
| **Color palette** | Hex codes — the "palette neighborhood" |
| **Lighting** | Quality, direction, mood |
| **Materials/textures** | What surfaces feel like |
| **Framing/perspective** | Camera position, focal length, intimacy level |
| **What it's NOT** | Visual anti-patterns |

## Maps

Image gen is NOT good at generating maps from text descriptions alone. The flow:

1. Worldbuilder sketches basic geography (Excalidraw, paper, any tool) — shapes, labels, spatial relationships
2. Attach sketch as reference image to the model. Model refines while preserving spatial logic.
3. Optionally: code up an interactive HTML page with modals/tooltips, or a detailed SVG.
4. Store in `Art/Maps/`

Don't skip the sketch. Don't try to generate a map from pure text.

## Asset Naming

`[subject]-[descriptor]-[number].png`

Examples: `mood-golden-street-01.png`, `character-clerk-turnaround-01.png`, `map-federated-polises-sketch-01.png`, `location-civic-center-exterior-01.png`, `prop-sunset-clause-token-01.png`
