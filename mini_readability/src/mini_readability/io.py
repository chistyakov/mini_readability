import os
from logging import getLogger
from typing import Tuple
from urllib.parse import urlparse

import requests
import tldextract


def fetch(url: str) -> str:
    resp = requests.get(url)
    resp.raise_for_status()
    getLogger(__name__).info("Successfully fetched %s", url)
    return resp.text


def get_domain(url: str) -> str:
    ext = tldextract.extract(url)
    return ext.registered_domain


def save(data: str, url: str):
    dir_path, file_path = build_path(url)
    os.makedirs(dir_path, exist_ok=True)
    with open(file_path, "w") as f:
        getLogger(__name__).info("write to %s", file_path)
        f.write(data)


def build_path(url: str) -> Tuple[str, str]:
    base_path = os.environ["OUTPUT_BASE_PATH"]
    parts = urlparse(url)
    rel_path, filename = split_path(parts.path)
    dir_path = join_parts(base_path, parts.netloc, rel_path)
    file_path = join_parts(dir_path, filename)
    return dir_path, file_path


def split_path(path: str) -> Tuple[str, str]:
    left_path, _, right_path = path.rpartition("/")
    if not right_path:
        return left_path, "no_name.txt"
    no_ext = right_path.rsplit(".", 1)[0]
    return left_path, f"{no_ext}.txt"


def join_parts(*parts) -> str:
    return "/" + "/".join(p.strip("/") for p in parts)
