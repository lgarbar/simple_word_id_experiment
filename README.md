# PsychoPy Text Presentation Experiment

This project implements a simple text presentation experiment using PsychoPy. The experiment presents multiple pages of text that can be progressed by pressing the spacebar.

## Features

- **Text Presentation**: Displays multiple pages of text content
- **Spacebar Navigation**: Progress through pages by pressing the spacebar
- **Data Recording**: Automatically records timing data for each page
- **CSV Export**: Generates a CSV file with timing information for analysis

## Installation

### Prerequisites

- **Python 3.9** (recommended for best compatibility)
- **Conda** (recommended for all platforms)

### Platform-Specific Installation

#### All Platforms (Recommended)
**Option 1: Automated Installation**
```bash
./install_conda.sh
```

**Option 2: Manual Installation**
1. Clone or download this repository
2. Create a conda environment with Python 3.9:
   ```bash
   conda create -n psychopy-experiment python=3.9
   conda activate psychopy-experiment
   ```
3. Install PsychoPy using conda-forge:
   ```bash
   conda install -c conda-forge psychopy
   ```
4. Install remaining dependencies:
   ```bash
   pip install pandas matplotlib pyglet<2.0
   ```

#### Alternative: pip Installation
**Option 1: Automated Installation**
```bash
./install_pip.sh
```

**Option 2: Manual Installation**
1. Clone or download this repository
2. Create a virtual environment:
   ```bash
   python -m venv psychopy-env
   source psychopy-env/bin/activate  # On Windows: psychopy-env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```



## Usage

1. **Test Installation** (recommended first step):
   ```bash
   python test_installation.py
   ```

2. **Run the Experiment**:
   ```bash
   python experiment.py
   ```

3. **Analyze Results** (after running the experiment):
   ```bash
   python analyze_data.py
   ```

## Experiment Structure

The experiment consists of several text pages:
1. **Welcome Page**: Introduction to the experiment
2. **Instructions**: Detailed instructions for participants
3. **Practice Page**: A practice trial
4. **Main Task**: The main experimental task
5. **Thank You**: Completion message

## Data Collection

The experiment automatically records:
- **Page Name**: Identifier for each page (e.g., 'Instructions_1', 'Welcome_1')
- **Start Time**: When each page was initiated (using `time.time()`)
- **End Time**: When the participant progressed to the next page
- **Duration**: How long each page was displayed

Data is saved to `data/experiment_data.csv` in the data folder.

## Data Analysis

The `analyze_data.py` script provides comprehensive analysis of experiment results:

- **Timing Statistics**: Average, standard deviation, and per-page timing
- **Visualizations**: Bar charts and timeline plots of page durations
- **Summary Reports**: Text summaries exported to `experiment_summary.txt`
- **Data Export**: Easy-to-read CSV format for further analysis

Run the analysis after completing the experiment:
```bash
python analyze_data.py
```

## File Structure

```
audio_task/
├── experiment.py              # Main experiment script
├── config.py                  # Configuration settings
├── test_installation.py       # Installation test script
├── analyze_data.py           # Data analysis script
├── requirements.txt           # Python dependencies (for non-macOS ARM)
├── install_conda.sh          # Recommended conda installation script
├── install_pip.sh           # Alternative pip installation script
├── fix_pyglet.py            # Fix for pyglet compatibility issues
├── README.md                 # This file
├── data/                    # Data output folder
│   ├── experiment_data.csv   # Generated data file (after running)
│   ├── experiment_timing_analysis.png # Generated visualization
│   └── experiment_summary.txt # Generated summary report
```

## Customization

To modify the experiment content and settings, edit the `config.py` file:

- **Experiment Content**: Modify the `EXPERIMENT_CONTENT` dictionary
- **Window Settings**: Adjust `WINDOW_CONFIG` for display properties
- **Text Settings**: Modify `TEXT_CONFIG` for text appearance
- **Data Settings**: Change `DATA_CONFIG` for data collection options

Example of modifying experiment content:
```python
EXPERIMENT_CONTENT = {
    'Welcome_1': 'Your custom welcome message here',
    'Instructions_1': 'Your custom instructions here',
    # ... add more pages as needed
}
```

## Requirements

- **Python 3.9** (recommended for best compatibility)
- **Conda** (recommended for all platforms)
- **PsychoPy** (latest version via conda-forge)
- **pandas** (for data analysis)
- **matplotlib** (for visualizations)
- **pyglet<2.0** (for compatibility)
- **numpy** (automatically installed as dependency)

## Notes

- The experiment runs in fullscreen mode by default
- Press 'Escape' to exit the experiment early
- All timing data is automatically saved to CSV format
- The experiment is designed to be easily extensible for more complex studies

## Troubleshooting

### Installation Issues
If you encounter build errors on any platform:
1. Use conda instead of pip: `conda install -c conda-forge psychopy`
2. Ensure you're using Python 3.9: `conda create -n psychopy-experiment python=3.9`
3. The conda-forge channel handles system dependencies (SDL2, FFmpeg, etc.) automatically

### Common Issues
- **HDF5 errors**: Use conda installation
- **SDL2/FFmpeg errors**: Use conda installation
- **PyObjC build errors**: Use conda installation
- **Python version conflicts**: Use Python 3.9 for best compatibility
- **Pyglet compatibility errors**: Run `python fix_pyglet.py` or install `pyglet<2.0` 