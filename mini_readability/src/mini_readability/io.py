import os
from logging import getLogger
from urllib.parse import urlparse

import requests
import tldextract


def fetch(url: str) -> str:
    resp = requests.get(url)
    resp.raise_for_status()
    getLogger(__name__).info("Successfully fetched %s", url)
    getLogger(__name__).info("%s", resp.encoding)
    return resp.text


def get_domain(url: str) -> str:
    ext = tldextract.extract(url)
    return ext.registered_domain


def save(data: str, url: str):
    filepath = result_filename(url)
    with open(filepath, "w") as f:
        getLogger(__name__).info("write to %s", filepath)
        f.write(data)


def result_filename(url: str) -> str:
    base_path = os.environ["OUTPUT_BASE_PATH"]
    parts = urlparse(url)
    path = parts.path
    page_name = path.rsplit("/", 1)[-1]
    if not page_name:
        return os.path.join(base_path, "no_name.txt")
    file_name = page_name.rsplit(".", 1)[0]
    return os.path.join(base_path, f"{file_name}.txt")
