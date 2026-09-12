import subprocess

from .path import ffmpeg_path

def transcode(input_file, output_file):
    ffmpeg = ffmpeg_path()
    
    command = [
        str(ffmpeg), "-i", str(input_file),
        "-c:v", "libx264", "-c:a", "aac",
        str(output_file),
    ]
    
    subprocess.run(command, check=True)
    # This is preferable to: `subprocess.run(["ffmpeg", ...])`
    # because the latter depends on FFmpeg being installed and available in PATH.
    
