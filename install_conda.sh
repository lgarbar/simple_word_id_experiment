#!/bin/bash
# Installation script for all platforms (recommended)
# This script sets up the PsychoPy experiment environment using conda

echo "Setting up PsychoPy experiment environment using conda..."

# Check if conda is installed
if ! command -v conda &> /dev/null; then
    echo "Error: conda is not installed. Please install Miniconda or Anaconda first."
    echo "Visit: https://docs.conda.io/en/latest/miniconda.html"
    echo ""
    echo "Alternative: You can use pip installation with install_other_platforms.sh"
    exit 1
fi

# Create conda environment with Python 3.9
echo "Creating conda environment with Python 3.9..."
conda create -n psychopy-experiment python=3.9 -y

# Activate the environment
echo "Activating conda environment..."
source $(conda info --base)/etc/profile.d/conda.sh
conda activate psychopy-experiment

# Install PsychoPy using conda-forge
echo "Installing PsychoPy via conda-forge..."
conda install -c conda-forge psychopy -y

# Install remaining dependencies
echo "Installing additional dependencies..."
pip install pandas matplotlib

# Fix pyglet compatibility issue
echo "Fixing pyglet compatibility..."
pip install "pyglet<2.0"

echo ""
echo "Installation complete!"
echo ""
echo "To activate the environment in the future:"
echo "  conda activate psychopy-experiment"
echo ""
echo "To run the experiment:"
echo "  python experiment.py"
echo ""
echo "To test the installation:"
echo "  python test_installation.py" 