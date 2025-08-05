#!/usr/bin/env python3

WINDOW_CONFIG = {
    'size': [1920, 1080],
    'fullscr': True,
    'color': 'black',
    'units': 'pix'
}

TEXT_CONFIG = {
    'color': 'white',
    'height': 30,
    'wrapWidth': 800,
    'alignHoriz': 'center',
    'alignVert': 'center'
}

EXPERIMENT_CONTENT = {
    'Welcome_1': ['Welcome to the Experiment!'],
    'Instructions_1': ['Instructions:', 'You will see several pages of text', 'Repeat the words you see outloud.'],
    'List_1': ['Banana', 'Hairdresser', 'Closet', 'Mother'],
    'List_2': ['Cloud', 'Laugh', 'Penguin', 'Table'],
    'List_3': ['Chair', 'Dance', 'Bottle', 'Sunshine'],
    'ThankYou_1': ['Thank You!', 'You have completed the experiment.', 'Your data has been saved.', 'Press SPACEBAR to exit.']
}

DATA_CONFIG = {
    'csv_filename': 'data/experiment_data.csv',
    'include_timestamp': True,
    'record_mouse_clicks': False
}

KEYBOARD_CONFIG = {
    'progress_key': 'space',
    'exit_key': 'escape',
    'allowed_keys': ['space', 'escape']
}

DISPLAY_CONFIG = {
    'show_progress_indicator': False,
    'show_page_number': False,
    'auto_advance_timeout': None
}