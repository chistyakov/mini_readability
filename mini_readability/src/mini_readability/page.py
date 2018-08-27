from dataclasses import dataclass
from typing import List, Union


@dataclass
class Link:
    href: str


@dataclass
class PageItem:
    parts: List[Union[str, Link]]


class Header(PageItem):
    pass


class Paragraph(PageItem):
    pass


@dataclass
class Page:
    title: str
    items: List[PageItem]
