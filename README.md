# PsychoPy Text Presentation Experiment with Real-Time Speech Detection

This project implements a real-time interactive text presentation experiment using **PsychoPy**. The experiment displays a sequence of text pages and advances either when the participant says the final word of the displayed content **or** presses the spacebar.

## Features

- **Text Presentation**: Displays text pages in fullscreen mode
- **Voice-Controlled Navigation**: Detects spoken words using Whisper and advances when the final word is spoken
- **Keyboard Support**: Also allows progressing by pressing the spacebar
- **Real-Time Transcription**: Leverages [`faster-whisper`](https://github.com/guillaumekln/faster-whisper) for accurate, real-time audio transcription
- **Data Recording**: Automatically logs timing information for each screen
- **CSV Export**: Saves collected data for later analysis

---

## Installation

### Prerequisites

- Python 3.9
- Conda (recommended for easiest installation)
- A microphone enabled on your system

### Option 1: Recommended Conda Installation

```bash
./install_conda.sh
```

Or manually follow:

```bash
conda create -n psychopy-experiment python=3.9
conda activate psychopy-experiment
conda install -c conda-forge psychopy
pip install pandas matplotlib pyglet<2.0 faster-whisper sounddevice
```

### Option 2: pip Installation (Not Recommended on macOS ARM)

```bash
./install_pip.sh
```

# Usage

## 1. Test installation

```bash
python test_installation.py
```

## 2. Run experiement

```bash
python experiment.py
```

You’ll see pages like:

- Welcome
- Instructions
- Word Lists (e.g., Banana\n\nRain\n\nArtichoke\n\nMother)
- Thank You

Speak the final word aloud to progress or press the spacebar.

# Experiment Flow

1. Welcome Page
2. Instructions Page
3. Practice or Task Page (displays a list of words)
4. The screen progresses when:
      - The last word on the screen is spoken aloud (automatically detected), OR
      - The spacebar is pressed manually

# Real-Time Transcription

The transcription is handled by transcribe.py, using a background thread with a RealtimeTranscriber class.

## Features of the Transcriber

- Uses sounddevice for audio input
- Runs Whisper in a background thread
- Provides a queue of detected words with timestamps
- Optional silence filtering (toggleable)

⸻

# Data Collection

Saved to: data/experiment_data.csv

Each row includes:

- Page_Name
- Start_Time
- End_Time
- Duration (in seconds)

# File Structure

audio_task/
├── experiment.py             # Main experiment script
├── transcribe.py             # Real-time transcription engine
├── config.py                 # Configuration (text content, layout)
├── analyze_data.py           # Analysis & plots
├── test_installation.py      # Installation test
├── requirements.txt          # pip dependencies
├── install_conda.sh          # Conda installer
├── install_pip.sh            # pip installer
├── fix_pyglet.py             # Compatibility helper for pyglet
├── data/
│   ├── experiment_data.csv         # Raw timing results
│   ├── experiment_summary.txt      # Generated summary
│   └── experiment_timing_analysis.png  # Graphical report
└── README.md               # This file

# Requirements

- Python 3.9
- psychopy
- faster-whisper
- sounddevice
- numpy, pandas, matplotlib
- pyglet<2.0

# License

MIT License