import argparse
import random
import subprocess
import time
from pathlib import Path

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image_dir", type=Path)
    args = parser.parse_args()

    image_paths = list(args.image_dir.iterdir())
    random.shuffle(image_paths)
    for image_path in image_paths:
        subprocess.run(["open", image_path])
        time.sleep(0.3)
