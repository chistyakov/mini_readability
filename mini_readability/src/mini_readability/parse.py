from typing import Iterable, Union

from lxml.etree import Element
from lxml.html import document_fromstring
from lxml.html.clean import clean_html

from mini_readability.config import get_config
from mini_readability.primitives import Page, PageItem, Header, Paragraph, Link, LineBreak


def parse(page_source: str, domain: str) -> Page:
    html = document_fromstring(page_source)
    return Page(title=get_title(html), items=list(get_items(html, domain)))


title_xpath = ".//title"


def get_title(html: Element) -> str:
    return html.findtext(title_xpath).strip()


def get_items(html: Element, domain: str) -> Iterable[PageItem]:
    html = clean_html(html)
    xpath = get_xpath(domain)
    for element in html.xpath(xpath):
        yield parse_item(element)


def get_xpath(domain: str):
    config = get_config()
    if domain not in config:
        assert "default" in config, f"No config for {domain}"
        return config["default"]["xpath"]
    return config[domain]["xpath"]


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
