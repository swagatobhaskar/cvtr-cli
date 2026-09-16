import os
from pathlib import Path

# ----------------------------------------------------------
# Project paths and required environment variables
# ----------------------------------------------------------

# Directory containing this .spec file.
PROJECT_ROOT = Path(SPEC).resolve().parent

# Paths to the FFmpeg executables provided through the environment.
FFMPEG_PATH = os.environ.get("FFMPEG_PATH")
FFPROBE_PATH = os.environ.get("FFPROBE_PATH")

# Fail early if the required FFmpeg binaries are not configured.
if not FFMPEG_PATH:
    raise RuntimeError("FFMPEG_PATH environment variable is not set.")

if not FFPROBE_PATH:
    raise RuntimeError("FFPROBE_PATH environment variable is not set.")

# ----------------------------------------------------------
# FFmpeg binaries
# ----------------------------------------------------------

# Bundle FFmpeg and FFprobe with the application.
ffmpeg_binaries = [
    (FFMPEG_PATH, "ffmpeg"),
    (FFPROBE_PATH, "ffprobe"),
]

# ----------------------------------------------------------
# Analysis
# ----------------------------------------------------------

# Analyze the application and collect its Python dependencies.
a = Analysis(
    ["build_entry.py"],
    pathex=[
        str(PROJECT_ROOT / "src"),
    ],
    binaries=[],
    datas=ffmpeg_binaries,
    hiddenimports=[],
    hookspath=[],
    hooksconfig=[],
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

# ----------------------------------------------------------
# Python archive
# ----------------------------------------------------------

# Package pure Python modules into the PYZ archive.
pyz = PYZ(a.pure)

# ----------------------------------------------------------
# Executable
# ----------------------------------------------------------

# Build the final CLI executable.
exe = EXE(
    pyz,
    a.scripts,
    [],
    [],
    [],
    name="cvtr",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,   # Keep the console enabled for CLI usage.
    contents_directory=".",
)

# Collect the executable and bundled files into the distribution folder.
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    name="cvtr",
)
