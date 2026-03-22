#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["google-genai>=1.53.0"]
# ///
"""Generate images using Google Gemini (nano banana pro) API."""

import argparse
import os
import sys
import uuid
from pathlib import Path

from google import genai
from google.genai import types

# Key lookup order: env var → plugin .env → ~/.claude/.env
PLUGIN_ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
CLAUDE_ENV_PATH = Path.home() / ".claude" / ".env"
DEFAULT_OUTPUT_DIR = Path.home() / "Pictures" / "nano-banana"

VALID_ASPECT_RATIOS = ["1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9"]
VALID_SIZES = ["1K", "2K", "4K"]


def _read_key_from_file(path: Path) -> str | None:
    """Read GEMINI_API_KEY from a dotenv-style file."""
    if not path.exists():
        return None
    for line in path.read_text().splitlines():
        line = line.strip()
        if line.startswith("#") or not line:
            continue
        if line.startswith("GEMINI_API_KEY="):
            value = line.split("=", 1)[1].strip()
            # Strip surrounding quotes if present
            if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
                value = value[1:-1]
            return value
    return None


def load_api_key() -> str:
    """Load API key from env var, plugin .env, or ~/.claude/.env fallback."""
    api_key = os.getenv("GEMINI_API_KEY")
    if api_key:
        return api_key

    # Plugin-local .env
    api_key = _read_key_from_file(PLUGIN_ENV_PATH)
    if api_key:
        return api_key

    # Global fallback
    api_key = _read_key_from_file(CLAUDE_ENV_PATH)
    if api_key:
        return api_key

    raise ValueError(
        "GEMINI_API_KEY not found. Set it in environment, "
        f"{PLUGIN_ENV_PATH}, or {CLAUDE_ENV_PATH}"
    )


def generate_image(
    prompt: str,
    aspect_ratio: str = "1:1",
    size: str = "2K",
    output_path: str | None = None,
    reference_images: list[str] | None = None,
    use_search: bool = False,
) -> str:
    """Generate an image and return the saved file path."""
    api_key = load_api_key()

    if aspect_ratio not in VALID_ASPECT_RATIOS:
        raise ValueError(f"Invalid aspect_ratio. Must be one of: {VALID_ASPECT_RATIOS}")
    if size not in VALID_SIZES:
        raise ValueError(f"Invalid size. Must be one of: {VALID_SIZES}")

    client = genai.Client(api_key=api_key)

    # Build contents: prompt + any reference images
    contents = [prompt]
    if reference_images:
        for image_path in reference_images:
            image_bytes = Path(image_path).read_bytes()
            mime_type = "image/png" if image_path.lower().endswith(".png") else "image/jpeg"
            contents.append(types.Part.from_bytes(data=image_bytes, mime_type=mime_type))

    config = types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"],
        image_config=types.ImageConfig(
            aspect_ratio=aspect_ratio,
            image_size=size,
        ),
    )

    # Add Google Search grounding if requested
    if use_search:
        config.tools = [{"google_search": {}}]

    response = client.models.generate_content(
        model="gemini-3-pro-image-preview",
        contents=contents,
        config=config,
    )

    # Extract image from response
    image_data = None
    mime_type = None
    text_parts = []

    for part in response.parts:
        if part.text:
            text_parts.append(part.text)
        elif part.inline_data:
            image_data = part.inline_data.data
            mime_type = part.inline_data.mime_type

    if not image_data:
        error_msg = "No image generated"
        if text_parts:
            error_msg += f". Model said: {' '.join(text_parts)}"
        raise RuntimeError(error_msg)

    # Determine output path — always use .jpg (Gemini returns JPEG)
    extension = "png" if mime_type and "png" in mime_type else "jpg"
    if output_path:
        save_path = Path(output_path)
    else:
        DEFAULT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        save_path = DEFAULT_OUTPUT_DIR / f"{uuid.uuid4().hex}.{extension}"

    save_path.parent.mkdir(parents=True, exist_ok=True)
    save_path.write_bytes(image_data)

    # Print any text response from model
    if text_parts:
        print(f"Model response: {' '.join(text_parts)}", file=sys.stderr)

    return str(save_path.absolute())


def main():
    parser = argparse.ArgumentParser(description="Generate images with Gemini (nano banana pro)")
    parser.add_argument("prompt", help="Text description of image to generate")
    parser.add_argument("--aspect-ratio", "-a", default="1:1", choices=VALID_ASPECT_RATIOS,
                        help="Aspect ratio (default: 1:1)")
    parser.add_argument("--size", "-s", default="2K", choices=VALID_SIZES,
                        help="Image size (default: 2K)")
    parser.add_argument("--output", "-o", help="Output file path (default: UUID in ~/Pictures/nano-banana/)")
    parser.add_argument("--reference", "-r", action="append", dest="references",
                        help="Reference image path (can specify multiple)")
    parser.add_argument("--use-search", action="store_true",
                        help="Enable Google Search grounding for real-world data")

    args = parser.parse_args()

    try:
        output_path = generate_image(
            prompt=args.prompt,
            aspect_ratio=args.aspect_ratio,
            size=args.size,
            output_path=args.output,
            reference_images=args.references,
            use_search=args.use_search,
        )
        print(output_path)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
