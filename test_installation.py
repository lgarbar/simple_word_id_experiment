#!/usr/bin/env python3
"""
Test script to verify PsychoPy installation and basic functionality.
"""

def test_imports():
    """Test that all required packages can be imported."""
    try:
        import psychopy
        print("✓ PsychoPy imported successfully")
        print(f"  Version: {psychopy.__version__}")
    except ImportError as e:
        print(f"✗ Failed to import PsychoPy: {e}")
        return False
    
    try:
        import pandas as pd
        print("✓ Pandas imported successfully")
        print(f"  Version: {pd.__version__}")
    except ImportError as e:
        print(f"✗ Failed to import Pandas: {e}")
        return False
    
    try:
        import numpy as np
        print("✓ NumPy imported successfully")
        print(f"  Version: {np.__version__}")
    except ImportError as e:
        print(f"✗ Failed to import NumPy: {e}")
        return False
    
    return True

def test_psychopy_basic():
    """Test basic PsychoPy functionality."""
    try:
        from psychopy import visual, core
        
        # Test window creation (without showing it)
        win = visual.Window(
            size=[800, 600], 
            fullscr=False, 
            color='black',
            units='pix',
            allowGUI=True
        )
        
        # Test text stimulus creation
        text = visual.TextStim(
            win=win,
            text="Test",
            color='white'
        )
        
        # Close window
        win.close()
        
        print("✓ Basic PsychoPy functionality test passed")
        return True
        
    except Exception as e:
        print(f"✗ PsychoPy basic functionality test failed: {e}")
        return False

def main():
    """Run all tests."""
    print("Testing PsychoPy Experiment Setup")
    print("=" * 40)
    
    # Test imports
    imports_ok = test_imports()
    
    if imports_ok:
        # Test basic functionality
        basic_ok = test_psychopy_basic()
        
        if basic_ok:
            print("\n✓ All tests passed! You're ready to run the experiment.")
            print("\nTo run the experiment, execute:")
            print("  python experiment.py")
        else:
            print("\n✗ Basic functionality test failed.")
            print("Please check your PsychoPy installation.")
    else:
        print("\n✗ Import tests failed.")
        print("Please install the required packages:")
        print("")
        print("Recommended (conda installation):")
        print("  conda create -n psychopy-experiment python=3.9")
        print("  conda activate psychopy-experiment")
        print("  conda install -c conda-forge psychopy")
        print("  pip install pandas matplotlib pyglet<2.0")
        print("")
        print("Alternative (pip installation):")
        print("  pip install -r requirements.txt")

if __name__ == "__main__":
    main() 