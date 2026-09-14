from pathlib import Path
import shutil
import sys

# paths.py determines exactly where the GitHub Actions workflow needs to place FFmpeg.
# My frozen application expects:

# application_dir()
# └── ffmpeg/
#     ├── ffmpeg.exe
#     └── ffprobe.exe

# because you have: return application_dir() / "ffmpeg" / "ffmpeg.exe"
# and: return application_dir() / "ffmpeg" / "ffprobe.exe"

# So use the following workflow in GitHub Actions.

def application_dir() -> Path:
    """Return the directory containing the application."""

    if getattr(sys, "frozen", False):
        # Running from a PyInstaller executable
        return Path(sys.executable).resolve().parent
        
    # Running from source
    return Path(__file__).resolve().parents[2]


def ffmpeg_path() -> Path:
    """Return the path to the FFmpeg executable."""

    if getattr(sys, "frozen", False):
        return application_dir() / "ffmpeg" / "ffmpeg.exe"

    ffmpeg = shutil.which("ffmpeg")
    
    if ffmpeg is None:
        raise FileNotFoundError(
            "FFmpeg was not found. Please install FFmpeg and make sure "
            "it is available on PATH."
        )

    return Path(ffmpeg)

    
def ffprobe_path() -> Path:
    """Return the path to the FFprobe executable."""

    if getattr(sys, "frozen", False):
        return application_dir() / "ffmpeg" / "ffprobe.exe"

    ffprobe = shutil.which("ffprobe")

    if ffprobe is None:
        raise FileNotFoundError(
            "FFprobe was not found. Please install FFmpeg and make sure "
            "FFprobe is available on PATH."
        )

    return Path(ffprobe)
