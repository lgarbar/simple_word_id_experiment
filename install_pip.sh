#!/bin/bash
# Installation script for Windows/Linux/Intel Macs
# This script sets up the PsychoPy experiment environment using pip

echo "Setting up PsychoPy experiment environment..."

# Check if Python 3.9 is available
python_version=$(python3 --version 2>&1 | grep -o '3\.[0-9]\+')
if [[ "$python_version" != "3.9" ]]; then
    echo "Warning: Python 3.9 is recommended for best compatibility."
    echo "Current Python version: $python_version"
    echo "Consider installing Python 3.9 if you encounter issues."
fi

# Create virtual environment
echo "Creating virtual environment..."
python3 -m venv psychopy-env

# Activate the environment
echo "Activating virtual environment..."
source psychopy-env/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Fix pyglet compatibility issue
echo "Fixing pyglet compatibility..."
pip install "pyglet<2.0"

echo ""
echo "Installation complete!"
echo ""
echo "To activate the environment in the future:"
echo "  source psychopy-env/bin/activate"
echo ""
echo "To run the experiment:"
echo "  python experiment.py"
echo ""
echo "To test the installation:"
echo "  python test_installation.py" 