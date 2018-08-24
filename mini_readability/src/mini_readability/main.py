import argparse
import logging
from argparse import Namespace

def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s:%(processName)s[%(process)d]:%(name)s:%(levelname)s %(message)s",
    )
    args = parse_arguments()
    print(args.url)


def parse_arguments() -> Namespace:
    parser = argparse.ArgumentParser(
        description="Extract mini readable data by URL."
    )
    parser.add_argument("url", help="page URL")
    return parser.parse_args()


if __name__ == "__main__":
    main()
