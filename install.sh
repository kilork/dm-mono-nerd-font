#!/bin/bash
set -e

# Auto-detect latest version from GitHub releases, or override via first argument
if [ -n "$1" ]; then
  VERSION="$1"
else
  VERSION=$(curl -fsSL "https://api.github.com/repos/kilork/dm-mono-nerd-font/releases/latest" \
    | grep '"tag_name"' \
    | sed 's/.*"tag_name": "v\(.*\)".*/\1/' 2>/dev/null || echo "1.0.0")
fi

INSTALL_DIR="${HOME}/.local/share/fonts"
TEMP_DIR=$(mktemp -d)

echo "Installing DM Mono Nerd Font v${VERSION}..."

mkdir -p "$INSTALL_DIR"

curl -fsSL "https://github.com/kilork/dm-mono-nerd-font/releases/download/v${VERSION}/dm-mono-nerd-font-${VERSION}.tar.gz" -o "${TEMP_DIR}/fonts.tar.gz"

tar -xzf "${TEMP_DIR}/fonts.tar.gz" -C "$INSTALL_DIR"

rm -rf "${TEMP_DIR}"

fc-cache -f -v 2>/dev/null || true

echo "Done! Installed fonts to ${INSTALL_DIR}/dm-mono-nerd-font/"
echo "Please restart your terminal to use the new fonts."