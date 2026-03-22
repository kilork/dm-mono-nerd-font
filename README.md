# DM Mono Nerd Font

Apply the [Nerd Fonts Patcher](https://github.com/ryanoasis/nerd-fonts) on the [DM Mono](https://github.com/googlefonts/dm-mono) font for a [powerlevel10k](https://github.com/romkatv/powerlevel10k) compliant font.

![preview](./preview.png)

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

#### Manual
Download fonts from [Releases](https://github.com/kilork/dm-mono-nerd-font/releases) and copy to `~/.local/share/fonts/` or `/usr/local/share/fonts/`.

```bash
mkdir -p ~/.local/share/fonts
cd ~/.local/share/fonts
curl -LO https://github.com/kilork/dm-mono-nerd-font/releases/download/v3.4.0/dm-mono-nerd-font-3.4.0.tar.gz
tar -xzf dm-mono-nerd-font-3.4.0.tar.gz
rm dm-mono-nerd-font-3.4.0.tar.gz
fc-cache -f -v
```

### Windows

Download fonts from [Releases](https://github.com/kilork/dm-mono-nerd-font/releases) and:
1. Double-click each `.ttf` file to install
2. Or right-click → Install for all users

## Available Fonts

- DMMono Nerd Font Italic
- DMMono Nerd Font Light
- DMMono Nerd Font Light Italic
- DMMono Nerd Font Medium
- DMMono Nerd Font Medium Italic
- DMMono Nerd Font Regular
- DM Mono Italic Nerd Font Complete
- DM Mono Light Italic Nerd Font Complete
- DM Mono Light Nerd Font Complete
- DM Mono Medium Italic Nerd Font Complete
- DM Mono Medium Nerd Font Complete
- DM Mono Regular Nerd Font Complete

## Build from Source

```bash
git clone https://github.com/kilork/dm-mono-nerd-font
cd dm-mono-nerd-font
git submodule update --init --recursive

chmod +x patch.sh
./patch.sh
```

Output fonts will be in `dm-mono-nerd-font/` directory.

## Related Projects

- [DM Mono](https://github.com/googlefonts/dm-mono)
- [Nerd Fonts](https://github.com/ryanoasis/nerd-fonts)
- [powerlevel10k](https://github.com/romkatv/powerlevel10k)