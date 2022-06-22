"""Based on https://qiita.com/wataoka/items/261fc12c956a517049d8"""

import argparse
import sys
from pathlib import Path

import emoji
import numpy as np
from PIL import Image

# 1が明、-1が暗
MOON_MATRICS = [
    # 🌑 :new_moon:
    np.matrix(
        [
            [-1, -1, -1, -1],
            [-1, -1, -1, -1],
            [-1, -1, -1, -1],
            [-1, -1, -1, -1],
        ]
    ),
    # 🌒 :waxing_crescent_moon:
    np.matrix(
        [
            [-1, -1, -1, 1],
            [-1, -1, -1, 1],
            [-1, -1, -1, 1],
            [-1, -1, -1, 1],
        ]
    ),
    # 🌓 :first_quarter_moon:
    np.matrix(
        [
            [-1, -1, 1, 1],
            [-1, -1, 1, 1],
            [-1, -1, 1, 1],
            [-1, -1, 1, 1],
        ]
    ),
    # 🌔 :waxing_gibbous_moon:
    np.matrix(
        [
            [-1, 1, 1, 1],
            [-1, 1, 1, 1],
            [-1, 1, 1, 1],
            [-1, 1, 1, 1],
        ]
    ),
    # 🌘 :waning_crescent_moon:
    np.matrix(
        [
            [1, -1, -1, -1],
            [1, -1, -1, -1],
            [1, -1, -1, -1],
            [1, -1, -1, -1],
        ]
    ),
    # 🌗 :last_quarter_moon:
    np.matrix(
        [
            [1, 1, -1, -1],
            [1, 1, -1, -1],
            [1, 1, -1, -1],
            [1, 1, -1, -1],
        ]
    ),
    # 🌖 :waning_gibbous_moon:
    np.matrix(
        [
            [1, 1, 1, -1],
            [1, 1, 1, -1],
            [1, 1, 1, -1],
            [1, 1, 1, -1],
        ]
    ),
    # 🌕 :full_moon:
    np.matrix(
        [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
    ),
]

MOON_EMOJI_NAMES = [
    ":new_moon:",
    ":waxing_crescent_moon:",
    ":first_quarter_moon:",
    ":waxing_gibbous_moon:",
    ":waning_crescent_moon:",
    ":last_quarter_moon:",
    ":waning_gibbous_moon:",
    ":full_moon:",
]

MOON_PIXELS = 4


def preprocess(path: Path, col: int):
    image = Image.open(path)
    gray_image = image.convert("L")

    width = col * MOON_PIXELS
    # gray_image.width : gray_image.height = width : height
    height = int(width * (gray_image.height / gray_image.width))
    fixed_height = height - height % MOON_PIXELS  # heightをMOON_PIXELSの倍数に直す

    rough_image = gray_image.resize((width, fixed_height))
    # np.matrix(image_matrix.tolist()) だと転置しない
    image_matrix = np.matrix(rough_image)
    # 画素の値を-1から1に変換する
    normalized_image_matrix = (image_matrix / 128.0) - 1.0

    return normalized_image_matrix


def similar_moon_index(part) -> int:
    max = -10000

    for i, moon in enumerate(MOON_MATRICS):
        hadamard = np.multiply(part, moon)

        if max < hadamard.sum():  # 類似しているほどsumが大きくなる！
            max_index = i
            max = hadamard.sum()

    return max_index


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=Path)
    parser.add_argument("--col", type=int, default=50)
    args = parser.parse_args()

    image_matrix = preprocess(args.path, args.col)

    moon_strings = []
    for row_start in range(0, image_matrix.shape[0], MOON_PIXELS):
        for col_start in range(0, image_matrix.shape[1], MOON_PIXELS):
            part = image_matrix[
                row_start : row_start + MOON_PIXELS,
                col_start : col_start + MOON_PIXELS,
            ]
            max_index = similar_moon_index(part)
            moon_strings.append(emoji.emojize(MOON_EMOJI_NAMES[max_index]))
        moon_strings.append("\n")

    for s in moon_strings:
        sys.stdout.write(s)
