from typing import Iterable

from lxml.etree import Element
from lxml.html import document_fromstring
from lxml.html.clean import clean_html

from mini_readability.page import Page, PageItem, Header, Paragraph, Link


def parse(page_source: str) -> Page:
    html = document_fromstring(page_source)
    return Page(title=get_title(html), items=list(get_items(html)))


def get_title(html: Element) -> str:
    return html.findtext(".//title")


def get_items(html: Element) -> Iterable[PageItem]:
    html = clean_html(html)
    for element in html.xpath(".//*[self::p or self::h1 or self::h2 or self::h3]"):
        parts = [element.text or ""]
        for sub_element in element.iterdescendants():
            text = sub_element.text or ""
            tail = sub_element.tail or ""
            if sub_element.tag == "br":
                text = "\n"
            if sub_element.tag == "a":
                parts.append(Link(href=sub_element.attrib["href"]))
            parts.append(text)
            parts.append(tail)
        if element.tag == "h1":
            yield Header(parts)
        else:
            yield Paragraph(parts)
