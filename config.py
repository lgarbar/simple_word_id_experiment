#!/usr/bin/env python3
"""
Configuration file for the PsychoPy text presentation experiment.
Modify these settings to customize the experiment.
"""

# Window settings
WINDOW_CONFIG = {
    'size': [1920, 1080],  # Window size in pixels
    'fullscr': True,        # Fullscreen mode
    'color': 'black',       # Background color
    'units': 'pix'          # Units for coordinates
}

# Text stimulus settings
TEXT_CONFIG = {
    'color': 'white',       # Text color
    'height': 30,           # Text height in pixels
    'wrapWidth': 800,       # Text wrapping width
    'alignHoriz': 'center', # Horizontal alignment
    'alignVert': 'center'   # Vertical alignment
}

# Experiment content - modify this dictionary to change the text pages
EXPERIMENT_CONTENT = {
    'Welcome_1': ['Welcome to the Experiment!'],
    
    'Instructions_1': ['Instructions:', 'You will see several pages of text', 'Repeat the words you see outloud.'],
    
    'List_1': ['Banana', 'Rain', 'Artichoke', 'Mother'],

    'List_2': ['Cloud', 'Laugh', 'Penguin', 'Table'],

    'List_3': ['Chair', 'Dance', 'Bottle', 'Sunshine'],
    
    'ThankYou_1': ['Thank You!', 'You have completed the experiment.', 'Your data has been saved.', 'Press SPACEBAR to exit.']
}

# Data collection settings
DATA_CONFIG = {
    'csv_filename': 'data/experiment_data.csv',  # Output CSV filename
    'include_timestamp': True,                    # Include timestamp in data
    'record_mouse_clicks': False                 # Record mouse clicks (future feature)
}

# Keyboard settings
KEYBOARD_CONFIG = {
    'progress_key': 'space',    # Key to progress to next page
    'exit_key': 'escape',       # Key to exit experiment early
    'allowed_keys': ['space', 'escape']  # All allowed keys
}

# Display settings
DISPLAY_CONFIG = {
    'show_progress_indicator': False,  # Show progress bar/dots
    'show_page_number': False,         # Show current page number
    'auto_advance_timeout': None       # Auto-advance after X seconds (None = disabled)
} 