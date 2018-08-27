from urllib.parse import urlparse


import requests

from mini_readability.parse import parse


def save_mini_readable(url: str) -> None:
    page_source = fetch(url)
    minified = minify(page_source)
    with open(result_filename(url), "w") as f:
        f.write(minified)


def fetch(url: str) -> str:
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text


def minify(page_source: str) -> str:
    page = parse(page_source)
    return str(page)


def result_filename(url: str) -> str:
    parts = urlparse(url)
    path = parts.path
    page_name = path.rsplit("/", 1)[-1]
    if not page_name:
        return "no_name.txt"
    file_name = page_name.rsplit(".", 1)[0]
    return f"{file_name}.txt"
