# Cartoon Video Transcoder CLI Tool

A command-line tool built in Python argparse for handling cartoon video transcoding tasks using bundled FFmpeg and FFprobe binaries.

---


## Installation & Setup

### Option A: Using the Compiled Binary (Recommended for Users)
1. Download the latest compiled binary (`cvtr`) from the internal [GitHub Releases / CI/CD Artifacts].
2. Move it to a directory included in your system's `PATH` (e.g., `/usr/local/bin/`).

### Option B: Installing from Source (For Development)
1. Clone the repository:
   ```
   git clone https://github.com/swagatobhaskar/cvtr-cli.git
   cd cvtr-cli
   ```

2. Set up a virtual environment and install dependencies:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    pip install .
    ```


## Run in Development
Running `ffprobe`: Navigate to the root `cvtr` directory and run `python3 -m src.cvtr.cli --input ~/Videos/my-movie.mp4 --probe`.

## Usage
Run the tool from your terminal by passing an input and output file path.
However, if `--output-path` or `-o` is not given, the default output path is chosen
which is `~/Videos/<filename>/` on Linux/Ubuntu and, `/my videos/<filename>/` on Windows.
    `cvtr --input input.mp4 --output ./output`

Available Options
- -i, --input (optional): Path to the source video file.
- -o, --output (optional): Path where the transcoded video should be saved.
- --probe, Run ffprobe on the selected video.

An example with `--help`: `python3 -m src.cvtr.cli --help`
    
```
usage: python3 -m src.cvtr.cli [-h] [-i INPUT] [-o OUTPUT] [--probe]

Transcode video using FFmpeg

options:
-h, --help           show this help message and exit
-i, --input INPUT    Input video file
-o, --output OUTPUT  Output video file
--probe              Probe input video with FFprobe
```

## Building the Executable (PyInstaller)
To compile the script and bundled binaries into a single standalone executable:
    `pyinstaller cvtr.spec`
    
The compiled binary will be generated inside the `dist/` folder.

## License
This project is licensed under the **MIT** License - see the LICENSE file for details.
