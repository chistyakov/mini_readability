import pytest

from mini_readability.page import Page, Paragraph, Header, Link, LineBreak
from mini_readability.parse import parse


@pytest.mark.parametrize(
    "page_source,expected_page",
    [
        (
            "<html>"
            "<head>"
            "<title>Title</title>"
            "<script>foo</script>"
            "</head>"
            "<body>"
            "<p>text text text</p>"
            "</body>"
            "</html>",
            Page(title="Title", items=[Paragraph(parts=["text text text"])]),
        ),
        (
            "<html>"
            "<head>"
            "<title>Title</title>"
            "<script>foo</script>"
            "</head>"
            "<body>"
            "<div>Navigation</div>"
            "</body>"
            "</html>",
            Page(title="Title", items=[]),
        ),
        (
            "<html>"
            "<head>"
            "<title>Title</title>"
            "<script>foo</script>"
            "</head>"
            "<body>"
            "<div><p>text text text</p></div>"
            "</body>"
            "</html>",
            Page(title="Title", items=[Paragraph(parts=["text text text"])]),
        ),
        (
            "<html>"
            "<head>"
            "<title>Title</title>"
            "<script>foo</script>"
            "</head>"
            "<body>"
            "<div><h1>My header</h1></div>"
            "</body>"
            "</html>",
            Page(title="Title", items=[Header(parts=["My header"])]),
        ),
        (
            "<html>"
            "<head>"
            "<title>Title</title>"
            "<script>foo</script>"
            "</head>"
            "<body>"
            '<div><p>Start <a href="http://example.com">link</a> end.</p></div>'
            "</body>"
            "</html>",
            Page(
                title="Title",
                items=[
                    Paragraph(
                        parts=[
                            "Start ",
                            Link(text="link", href="http://example.com"),
                            " end.",
                        ]
                    )
                ],
            ),
        ),
        (
            "<html>"
            "<head>"
            "<title>Title</title>"
            "<script>foo</script>"
            "</head>"
            "<body>"
            "<div><h1>Header</h1></div>"
            '<div><p>Start <a href="http://example.com">link</a> end.</p></div>'
            "</body>"
            "</html>",
            Page(
                title="Title",
                items=[
                    Header(parts=["Header"]),
                    Paragraph(
                        parts=[
                            "Start ",
                            Link(text="link", href="http://example.com"),
                            " end.",
                        ]
                    ),
                ],
            ),
        ),
        (
            "<html>"
            "<head>"
            "<title>Title</title>"
            "<script>foo</script>"
            "</head>"
            "<body>"
            "<div><p>Foo<br>Bar</p></div>"
            "</body>"
            "</html>",
            Page(title="Title", items=[Paragraph(parts=["Foo", LineBreak(), "Bar"])]),
        ),
    ],
)
def test_extract_text(page_source, expected_page):
    parsed_page = parse(page_source)

    assert expected_page == parsed_page
