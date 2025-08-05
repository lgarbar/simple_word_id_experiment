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
    'Instructions_1': ['Instructions:', 'In this task, you will see several pages of text,', 'and you will read the words outloud.'],
    'Instructions_2': ['Instructions:', 'When a word is RED, slowly and clearly', 'read the word aloud.'],
    'Instructions_3': ['Instructions:', 'I will demonstrate first.'],
    'List_Demo_1': ['Condo', 'Makeup', 'Apple', 'Baker'],
    'Instructions_4': ['Instructions:', 'Now please read the text on the following pages.'],
    'List_1': ['Banana', 'Hairdresser', 'Closet', 'Mother'],
    'List_2': ['Cloud', 'Soccer', 'Penguin', 'Table'],
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