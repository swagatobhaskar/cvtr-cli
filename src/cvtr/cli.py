import argparse
from pathlib import Path
import pprint
import json

from .ffmpeg import run_transcode
from .ffprobe import run_probe
from .utils import get_default_output_path

def init_parser():
    parser  = argparse.ArgumentParser(description="Transcode video using FFmpeg")

    # --input currently isn't required, despite the application apparently needing an input file.
    parser.add_argument("-i", "--input", type=Path, help="Input video file")
    parser.add_argument("-o", "--output", type=Path, help="Output video file")

    parser.add_argument("--probe", action="store_true", help="Probe input video with FFprobe")

    return parser

def get_output_path(file_name: str, output: Path | None = None) -> Path:
    # default output path (Linux): ~/Videos/cvtr/file_name/
    # default output path (Windows): ~/my_videos/cvtr/file_name/

    default_output_path = get_default_output_path(file_name)
    output_path = output if output else default_output_path

    return output_path

def main():
    parser = init_parser()
    args = parser.parse_args()

    input_file_path = args.input

    file_name = input_file_path.stem

    if not input_file_path or not input_file_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {input_file_path}")

    # FFprobe
    if args.probe:
        probe_result = run_probe(input_file_path)
        pprint.pprint(probe_result)
        return

    output_path = get_output_path(file_name, args.output)

    result = run_transcode(input_file_path, output_path)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
