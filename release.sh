#!/bin/bash
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo "========================================"
echo "  DM Mono Nerd Font Release Script"
echo "========================================"
echo ""

# Read current version
if [ ! -f VERSION ]; then
    echo -e "${RED}Error: VERSION file not found${NC}"
    exit 1
fi

CURRENT_VERSION=$(cat VERSION | tr -d '[:space:]')
echo -e "${CYAN}Current version:${NC} ${CURRENT_VERSION}"
echo ""

# Check git status
if [ -n "$(git status --porcelain)" ]; then
    echo -e "${YELLOW}Warning: You have uncommitted changes:${NC}"
    git status --short
    echo ""
    read -p "Continue with uncommitted changes? [y/N] " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Aborted."
        exit 1
    fi
fi

# Get new version
echo -e "${CYAN}Enter new version:${NC} (e.g., 1.1.0)"
read -p "> " NEW_VERSION

# Validate version format (semver: X.Y.Z)
if ! echo "$NEW_VERSION" | grep -qE '^[0-9]+\.[0-9]+\.[0-9]+$'; then
    echo -e "${RED}Error: Version must be in format X.Y.Z (e.g., 1.1.0)${NC}"
    exit 1
fi

if [ "$NEW_VERSION" = "$CURRENT_VERSION" ]; then
    echo -e "${YELLOW}Warning: Version unchanged (${CURRENT_VERSION})${NC}"
    read -p "Create release anyway? [y/N] " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Aborted."
        exit 1
    fi
fi

TAG="v${NEW_VERSION}"

# Check if tag already exists
if git rev-parse "$TAG" >/dev/null 2>&1; then
    echo -e "${RED}Error: Tag '${TAG}' already exists${NC}"
    exit 1
fi

echo ""
echo "========================================"
echo -e "Release Summary:"
echo ""
echo -e "  ${CYAN}Current version:${NC}  ${CURRENT_VERSION}"
echo -e "  ${CYAN}New version:${NC}      ${NEW_VERSION}"
echo -e "  ${CYAN}Git tag:${NC}          ${TAG}"
echo "========================================"
echo ""

read -p "Proceed with release? [y/N] " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Aborted."
    exit 1
fi

# Update VERSION file
echo -e "${GREEN}1. Updating VERSION file...${NC}"
echo "$NEW_VERSION" > VERSION

# Commit
echo -e "${GREEN}2. Committing VERSION bump...${NC}"
git add VERSION
git commit -m "Bump version to ${NEW_VERSION}"

# Tag
echo -e "${GREEN}3. Creating tag ${TAG}...${NC}"
git tag "$TAG"

# Push
echo -e "${GREEN}4. Pushing commit and tag...${NC}"
git push origin main
git push origin "$TAG"

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}  Release ${TAG} created and pushed!      ${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo "The CI will now:"
echo "  1. Build the fonts (patch.sh)"
echo "  2. Create a GitHub Release with tarball and fonts"
echo "  3. Update the Homebrew tap automatically"
echo ""
echo "Monitor progress at:"
echo "  https://github.com/kilork/dm-mono-nerd-font/actions"
echo "  https://github.com/kilork/homebrew-dm-mono-nerd-font/actions"
