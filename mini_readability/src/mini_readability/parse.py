from typing import Iterable, Union

from lxml.etree import Element
from lxml.html import document_fromstring
from lxml.html.clean import clean_html

from mini_readability.page import Page, PageItem, Header, Paragraph, Link, LineBreak


def parse(page_source: str) -> Page:
    html = document_fromstring(page_source)
    return Page(title=get_title(html), items=list(get_items(html)))


title_xpath = ".//title"


def get_title(html: Element) -> str:
    return html.findtext(title_xpath)


valuable_data_xpath = ".//*[self::p or self::h1 or self::h2 or self::h3]"


def get_items(html: Element) -> Iterable[PageItem]:
    html = clean_html(html)
    for element in html.xpath(valuable_data_xpath):
        yield parse_item(element)


def parse_item(element: Element) -> PageItem:
    parts = [element.text or ""]
    for sub_element in element.iterdescendants():
        parts.extend(get_parts(sub_element))
    if element.tag == "h1":
        return Header(parts)
    else:
        return Paragraph(parts)


def get_parts(sub_element: Element) -> Iterable[Union[str, Link, LineBreak]]:
    text = sub_element.text or ""
    tail = sub_element.tail or ""
    if sub_element.tag == "br":
        return LineBreak(), tail
    if sub_element.tag == "a":
        return Link(text=text, href=sub_element.attrib["href"]), tail
    return text, tail
