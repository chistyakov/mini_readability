from logging import getLogger

from mini_readability.io import fetch, get_domain, save
from mini_readability.parse import parse


def save_mini_readable(url: str) -> None:
    page_source = fetch(url)
    domain = get_domain(url)
    minified = minify(page_source, domain)
    save(minified, url)


def minify(page_source: str, domain: str = "default") -> str:
    page = parse(page_source, domain)
    formatted = str(page)
    getLogger(__name__).info("Successfully minified")
    return formatted
