#!/bin/bash
# Helium (.ium) Setup Script for Linux and macOS

# Get the absolute path of the current directory
PROJECT_DIR=$(pwd)
LAUNCHER_PATH="$PROJECT_DIR/ium"

# Check if shell is zsh or bash
if [ -n "$ZSH_VERSION" ]; then
    RC_FILE="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    RC_FILE="$HOME/.bashrc"
else
    RC_FILE="$HOME/.profile"
fi

# Add alias to rc file if it doesn't exist
if ! grep -q "alias ium=" "$RC_FILE"; then
    echo "alias ium='\"$LAUNCHER_PATH\"'" >> "$RC_FILE"
    echo "Added 'ium' alias to $RC_FILE."
    echo "To use it, restart your terminal or run: source $RC_FILE"
else
    echo "'ium' alias already exists in $RC_FILE."
fi
