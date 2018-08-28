#!/usr/bin/env python3


import argparse
import logging
from argparse import Namespace

from mini_readability.minify import save_mini_readable


def main() -> None:
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s:%(name)s:%(levelname)s %(message)s"
    )
    args = parse_arguments()
    save_mini_readable(args.url)


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser(description="Extract mini readable data by URL.")
    parser.add_argument("url", help="page URL")
    return parser.parse_args()


if __name__ == "__main__":
    main()
