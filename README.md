# DM Mono Nerd Font

Apply the [Nerd Fonts Patcher](https://github.com/ryanoasis/nerd-fonts) on the [DM Mono](https://github.com/googlefonts/dm-mono) font, extended with glyphs from [BlexMono](https://github.com/tonsky/FiraCode) (IBM Plex Mono derivative) for a [powerlevel10k](https://github.com/romkatv/powerlevel10k) compliant font.

![preview](./preview.png)

## Features

- **Nerd Font icons** — thousands of developer icons (powerline, devicons, fontawesome, etc.)
- **Cyrillic support** — full Russian alphabet (А-Я, а-я, Ё, ё) and Cyrillic Supplement (194 glyphs)
- **Arrows** — → ← ↑ ↓ ↔ and 18 more arrow glyphs (22 total)
- **Box Drawing** — all 128 box drawing characters for terminal UI elements
- **Block Elements** — all 32 block element characters for progress bars and shading
- **Monospace** — all glyphs (Latin, Cyrillic, symbols, and icons) at uniform 600-unit width

## Installation

### macOS

#### Homebrew (Recommended)
```bash
brew install --cask kilork/dm-mono-nerd-font/dm-mono-nerd-font
```

#### Manual
Download fonts from [Releases](https://github.com/kilork/dm-mono-nerd-font/releases) and double-click to install, or copy to `~/Library/Fonts/`.

### Linux

#### Install Script (Recommended)
```bash
curl -fsSL https://raw.githubusercontent.com/kilork/dm-mono-nerd-font/main/install.sh | bash
```

This auto-detects the latest version from GitHub releases.

#### Manual
Download fonts from [Releases](https://github.com/kilork/dm-mono-nerd-font/releases) and copy to `~/.local/share/fonts/` or `/usr/local/share/fonts/`.

```bash
mkdir -p ~/.local/share/fonts
cd ~/.local/share/fonts
curl -LO https://github.com/kilork/dm-mono-nerd-font/releases/download/v1.0.0/dm-mono-nerd-font-1.0.0.tar.gz
tar -xzf dm-mono-nerd-font-1.0.0.tar.gz
rm dm-mono-nerd-font-1.0.0.tar.gz
fc-cache -f -v
```

### Windows

Download fonts from [Releases](https://github.com/kilork/dm-mono-nerd-font/releases) and:
1. Double-click each `.ttf` file to install
2. Or right-click → Install for all users

## Available Fonts

All fonts belong to family **DMMono Nerd Font** with the following styles:
- Regular
- Light
- Medium
- Italic
- Light Italic
- Medium Italic

Use family name `DMMono Nerd Font` in your terminal emulator, then apply styles via font-weight and italic settings.

## Build from Source

### Prerequisites

- [FontForge](https://fontforge.org/) — for font patching (`brew install fontforge`)
- Git submodules — for nerd-fonts patcher and BlexMono source

### Build

```bash
git clone https://github.com/kilork/dm-mono-nerd-font
cd dm-mono-nerd-font
git submodule update --init --recursive

chmod +x patch.sh
./patch.sh
```

Output fonts will be in `dm-mono-nerd-font/` directory.

### Build Process

1. **`add-missing-glyphs.py`** — Extends DM Mono with missing glyphs from BlexMono Nerd Font:
   - Cyrillic characters (94 capitals, 94 lowercase)
   - Arrow symbols (22 glyphs)
   - Box drawing characters (128 glyphs)
   - Block elements (32 glyphs)
2. **`font-patcher`** — Applies Nerd Fonts icons (powerline, devicons, fontawesome, etc.)

## Versioning

This project uses its own [semantic versioning](https://semver.org/) independent of the Nerd Fonts upstream.
The current version is stored in the `VERSION` file.

To create a new release:
```bash
echo "1.1.0" > VERSION
git add VERSION && git commit -m "Bump version to 1.1.0"
git tag v1.1.0 && git push origin v1.1.0
```

The CI will automatically build, create a GitHub release, and update the Homebrew tap.

## Related Projects

- [DM Mono](https://github.com/googlefonts/dm-mono) — the base font
- [BlexMono](https://github.com/tonsky/FiraCode) — glyph source (based on IBM Plex Mono)
- [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts) — icon patcher
- [powerlevel10k](https://github.com/romkatv/powerlevel10k) — zsh theme
