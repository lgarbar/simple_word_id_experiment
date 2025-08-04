import queue
import sounddevice as sd
import numpy as np
from faster_whisper import WhisperModel

OPENBLAS_NUM_THREADS=1
OMP_NUM_THREADS=1

model = WhisperModel("base", compute_type="int8")

device = 0  # change to correct index if needed
samplerate = 16000
block_duration = 2  # seconds
blocksize = int(samplerate * block_duration)
audio_queue = queue.Queue()

def audio_callback(indata, frames, time, status):
    if status:
        print(status)
    audio_queue.put(indata.copy())

stream = sd.InputStream(
    channels=1,
    samplerate=samplerate,
    blocksize=blocksize,
    callback=audio_callback,
    device=device,
)
stream.start()
print("Listening for real-time transcription...")

try:
    while True:
        audio = audio_queue.get()
        audio = audio.flatten().astype(np.float32)
        segments, _ = model.transcribe(audio, language="en", word_timestamps=True)
        for segment in segments:
            for word in segment.words:
                print(f"{word.word.strip()} [{word.start:.2f}s - {word.end:.2f}s]")
except KeyboardInterrupt:
    print("\nStopping...")
    stream.stop()