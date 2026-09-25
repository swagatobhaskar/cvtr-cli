import subprocess
from .utils import (
    probe_video, build_ffmpeg_command,
    generate_renditions, create_output_directories
)

def run_transcode(input_file, output_dir):    
    probe_result = probe_video(input_file)

    # store the probe result in a JSON file in the output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    probe_result_file = output_dir / "probe_result.json"
    with open(probe_result_file, "w") as f:
        import json
        json.dump(probe_result, f, indent=2)
        
    renditions = generate_renditions(probe_result["height"])

    if not renditions:
        raise ValueError(f"No valid renditions for source height- {probe_result['height']}")

    create_output_directories(output_dir)

    dash_dir = output_dir / "dash"

    cmd = build_ffmpeg_command(
        # input_file=str(input_file),
        input_file=str(input_file.resolve()),  # input path must be resolved to an absolute path too
        output_dir=dash_dir,
        renditions=renditions,
        fps=probe_result["fps"]
    )

    result = subprocess.run(
        cmd,

        # Capture the program's stdout and stderr instead of letting them go directly to the terminal.
        # capture_output=True,

        # Gives stdout/stderr as strings rather than bytes.
        text=True,

        # if you want FFmpeg's output to appear directly in your terminal
        check=False,

        # stdout and stderr arguments may not be used with capture_output.
        # capture_output=True is essentially shorthand for:
        # stdout=subprocess.PIPE,
        # stderr=subprocess.PIPE,

        # Relative on purpose: we set cwd=dash_dir when running this command,
        # so every output (manifest, init segments, media chunks, HLS master)
        # resolves the same way via the OS instead of FFmpeg's own path
        # parsing. FFmpeg's directory-inference from an absolute output path
        # is inconsistent between platforms (it works on Linux but the
        # relative init/media/hls_master names silently fall back to the
        # process's CWD on Windows), so don't rely on it.
        cwd=str(dash_dir),
    )
    # This is preferable to: `subprocess.run(["ffmpeg", ...])`
    # because the latter depends on FFmpeg being installed and available in PATH.

    if result.stdout:
        print(result.stdout)

    if result.stderr:
        print(result.stderr)

    if result.returncode != 0:
        raise RuntimeError(f"FFmpeg failed with exit code {result.returncode}: {result.stderr}")

    return {
        "status": "completed",
        "output_dir": str(output_dir),
        "manifest": str(output_dir / "dash" / "manifest.mpd"),
        "hls_master": str(output_dir / "dash" / "master.m3u8"),
        "metadata": probe_result,
    }
