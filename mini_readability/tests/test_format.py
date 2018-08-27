import pytest

from mini_readability.page import Page, Paragraph, Header, Link, LineBreak


@pytest.mark.parametrize(
    "page,expected_str",
    [
        (
            Page(title="Title", items=[Paragraph(parts=["text text text"])]),
            "Title\n\ntext text text\n\n",
        ),

        (Page(title="Title", items=[]), "Title\n\n"),

        (
            Page(title="Title", items=[Header(parts=["My header"])]),
            "Title\n\nMy header\n\n",
        ),

        (
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
            "Title\n\nStart link [http://example.com] end.\n\n",
        ),

        (
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
            "Title\n\nHeader\n\nStart link [http://example.com] end.\n\n",
        ),

        (
            Page(title="Title", items=[Paragraph(parts=["Foo", LineBreak(), "Bar"])]),
            "Title\n\nFoo\nBar\n\n",
        ),
    ],
)
def test_format_page(page, expected_str):
    assert expected_str == str(page)
