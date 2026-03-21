#!/bin/bash
set -e

VERSION="${1:-3.4.0}"
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