from dataclasses import dataclass
from typing import List, Union


@dataclass
class Link:
    text: str
    href: str

    def __str__(self) -> str:
        return f"{self.text} [{self.href}]"


@dataclass
class LineBreak:
    def __str__(self) -> str:
        return "\n"


@dataclass
class PageItem:
    parts: List[Union[str, Link, LineBreak]]

    def __str__(self) -> str:
        return "".join(str(p) for p in self.parts if p)


class Paragraph(PageItem):
    def __str__(self) -> str:
        return f"{super().__str__()}\n\n"


class Header(PageItem):
    def __str__(self) -> str:
        return f"{super().__str__()}\n\n"


@dataclass
class Page:
    title: str
    items: List[PageItem]

    def __str__(self) -> str:
        body = "".join(str(it) for it in self.items)
        return f"{self.title}\n\n{body}"
