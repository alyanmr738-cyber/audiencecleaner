#!/bin/bash
# Installation script for Audience Cleaner

echo "🎯 Audience Cleaner - Installation Script"
echo "=========================================="
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed."
    echo "Please install Python 3.6 or higher and try again."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ Error: pip3 is not installed."
    echo "Please install pip and try again."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo "✓ pip3 found: $(pip3 --version)"
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "Installing Audience Cleaner..."
echo ""

# Install the package
if pip3 install .; then
    echo ""
    echo "✅ Installation successful!"
    echo ""
    echo "You can now use the tool from anywhere with:"
    echo "  clean-audience input_file.csv"
    echo "  or"
    echo "  audience-cleaner input_file.csv"
    echo ""
    echo "Try it now:"
    echo "  clean-audience --help"
else
    echo ""
    echo "❌ Installation failed. Trying with --user flag..."
    if pip3 install --user .; then
        echo ""
        echo "✅ Installation successful (user-level)!"
        echo ""
        echo "Note: You may need to add ~/.local/bin to your PATH"
        echo "Add this to your ~/.bashrc or ~/.zshrc:"
        echo "  export PATH=\"\$HOME/.local/bin:\$PATH\""
    else
        echo ""
        echo "❌ Installation failed. Please check the error messages above."
        exit 1
    fi
fi

