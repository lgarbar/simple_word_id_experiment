#!/usr/bin/env python3

import pandas as pd
import time
import threading
from psychopy import visual, core, event
from psychopy.visual import TextStim
from config import WINDOW_CONFIG, TEXT_CONFIG, EXPERIMENT_CONTENT, DATA_CONFIG, KEYBOARD_CONFIG
from transcribe import transcribe
import string

class TextExperiment:
    def __init__(self, transcriber):
        self.win = visual.Window(**WINDOW_CONFIG)
        self.experiment_data = EXPERIMENT_CONTENT
        self.timing_data = []
        self.current_word = None
        self.transcriber = transcriber

    def present_text_page(self, page_name, word_list):
        text_content = '\n\n'.join(word_list)
        text_stim = TextStim(win=self.win, text=text_content, **TEXT_CONFIG)

        final_word = word_list[-1].lower()

        start_time = time.time()
        text_stim.draw()
        self.win.flip()

        clock = core.Clock()
        continue_screen = False

        while not continue_screen:
            keys = event.getKeys(keyList=KEYBOARD_CONFIG['allowed_keys'])
            if KEYBOARD_CONFIG['exit_key'] in keys:
                return False

            if "space" in keys:
                continue_screen = True
                break

            new_words = self.transcriber.get_transcribed_words()
            for word, start, end in new_words:
                self.current_word = word.split()
                word = word.translate(str.maketrans('', '', string.punctuation))
                print(f"{word} [{start:.2f}s - {end:.2f}s]")
                if word.lower() == final_word:
                    print(f"Detected final word '{final_word}', advancing...")
                    continue_screen = True
                    break

            core.wait(0.1)

        end_time = time.time()
        self.timing_data.append({
            'Page_Name': page_name,
            'Start_Time': start_time,
            'End_Time': end_time,
            'Duration': end_time - start_time
        })
        return True

    def run_experiment(self):
        print("Starting experiment...")
        print("Speak or press SPACEBAR to progress.")
        print("Press ESCAPE to exit early.")

        for page_name, word_list in self.experiment_data.items():
            print(f"Presenting: {page_name}")
            proceed = self.present_text_page(page_name, word_list)
            if not proceed:
                print("Experiment terminated by user.")
                break

        self.win.close()
        self.save_data()
        print("Experiment completed!")

    def save_data(self):
        if self.timing_data:
            import os
            data_dir = os.path.dirname(DATA_CONFIG['csv_filename'])
            if data_dir and not os.path.exists(data_dir):
                os.makedirs(data_dir)

            df = pd.DataFrame(self.timing_data)
            df.to_csv(DATA_CONFIG['csv_filename'], index=False)
            print(f"Saved {len(self.timing_data)} data points to {DATA_CONFIG['csv_filename']}")
        else:
            print("No data to save.")

def main():
    transcriber = transcribe.RealtimeTranscriber()
    transcriber.toggle_silence_filter(True)
    transcriber.start()

    try:
        experiment = TextExperiment(transcriber)
        experiment.run_experiment()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        transcriber.stop()
        print("Transcriber stopped.")

if __name__ == "__main__":
    main()