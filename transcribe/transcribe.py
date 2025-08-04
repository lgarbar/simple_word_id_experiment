import queue
import threading
import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel

OPENBLAS_NUM_THREADS = 1
OMP_NUM_THREADS = 1

model = WhisperModel("base", compute_type="int8")

class RealtimeTranscriber:
    def __init__(self, device=0, samplerate=16000, block_duration=2):
        self.device = device
        self.samplerate = samplerate
        self.block_duration = block_duration
        self.blocksize = int(samplerate * block_duration)
        self.audio_queue = queue.Queue()
        self.transcribed_words = queue.Queue()
        self.running = False
        self.thread = None
        self.filter_silence = True

    def toggle_silence_filter(self, enabled):
        self.filter_silence = enabled

    def _audio_callback(self, indata, frames, time, status):
        if status:
            print(status)
        self.audio_queue.put(indata.copy())

    def _run(self):
        with sd.InputStream(
            channels=1,
            samplerate=self.samplerate,
            blocksize=self.blocksize,
            callback=self._audio_callback,
            device=self.device,
        ):
            while self.running:
                audio = self.audio_queue.get()
                audio = audio.flatten().astype(np.float32)
                segments, _ = model.transcribe(audio, language="en", word_timestamps=True)
                for segment in segments:
                    for word in segment.words:
                        word_text = word.word.strip()
                        if word_text and (not self.filter_silence or word_text.lower() not in ['[silence]', '[noise]', '[laughter]']):
                            self.transcribed_words.put((word_text, word.start, word.end))

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self._run, daemon=True)
            self.thread.start()

    def stop(self):
        self.running = False
        if self.thread is not None:
            self.thread.join()

    def get_transcribed_words(self):
        words = []
        while not self.transcribed_words.empty():
            words.append(self.transcribed_words.get())
        return words
    
if __name__ == '__main__':
    import time

    transcriber = RealtimeTranscriber()
    transcriber.start()

    print("Listening...")

    try:
        while True:
            words = transcriber.get_transcribed_words()
            for word, start, end in words:
                print(f"{word} [{start:.2f}s - {end:.2f}s]")
            time.sleep(0.5)
    except KeyboardInterrupt:
        transcriber.stop()
        print("\nStopped.")