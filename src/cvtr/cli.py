import argparse

from .ffmpeg import transcode

def main():
    parser  = argparse.ArgumentParser(description="Transcode video using FFmpeg")
    
    parser.add_argument("input", help="Input video file")
    parser.add_argument("output", help="Output video file")
    
    args = parser.parse_args()
    
    transcode(args.input, args.outpt)
    
if __name__ == "__main__":
    main()
    
    
# On the command line:
# cvtr input.mp4 output.mp4
# Or later: cvtr input.mp4 output.mp4 --codec h264 --quality 23

