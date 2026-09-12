from pathlib import Path
import sys

def application_dir() -> Path:
    if getattrs(sys, "frozen", False):
        # Running from PyInstaller
        return Path(sys.executable).resolve().parent
        
    # Running from source
    return Path(__file__).resolve().parents[2]

def ffmpeg_path() -> Path:
    return application_dir() / "ffmpeg" / "ffmpeg.exe"
    
def ffprobe_path() -> Path:
    return application_dir() / "ffmpeg" / "ffprobe.exe"

