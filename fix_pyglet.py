#!/usr/bin/env python3
"""
Quick fix for pyglet compatibility issue with PsychoPy.
Run this script if you encounter the error: 'module pyglet has no attribute canvas'
"""

import subprocess
import sys

def fix_pyglet():
    """Fix pyglet compatibility issue."""
    print("Fixing pyglet compatibility issue...")
    
    try:
        # Uninstall current pyglet version
        subprocess.run([sys.executable, "-m", "pip", "uninstall", "pyglet", "-y"], 
                      check=True, capture_output=True)
        print("✓ Uninstalled current pyglet version")
        
        # Install compatible pyglet version
        subprocess.run([sys.executable, "-m", "pip", "install", "pyglet<2.0"], 
                      check=True, capture_output=True)
        print("✓ Installed pyglet<2.0")
        
        print("\n✓ Pyglet compatibility issue fixed!")
        print("You can now run the experiment: python experiment.py")
        
    except subprocess.CalledProcessError as e:
        print(f"✗ Error fixing pyglet: {e}")
        print("Try running manually:")
        print("  pip uninstall pyglet -y")
        print("  pip install pyglet<2.0")

if __name__ == "__main__":
    fix_pyglet() 