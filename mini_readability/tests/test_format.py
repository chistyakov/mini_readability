import pytest

from mini_readability.primitives import Page, Paragraph, Header, Link, LineBreak


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
        (
            Page(
                title="БЫТИЕ",
                items=[
                    Paragraph(parts=["1 В начале сотворил Бог небо и землю."]),
                    Paragraph(
                        parts=[
                            "2 Земля же была безвидна и пуста, и тьма над бездною, и Дух Божий носился над водою."
                        ]
                    ),
                ],
            ),
            "БЫТИЕ\n\n"
            "1 В начале сотворил Бог небо и землю.\n\n"
            "2 Земля же была безвидна и пуста, и тьма над бездною, и Дух Божий носился над\n"
            "водою.\n\n",
        ),
        (
            Page(
                title="БЫТИЕ",
                items=[
                    Paragraph(parts=["1 В начале сотворил Бог небо и землю."]),
                    Paragraph(
                        parts=[
                            "2 ",
                            Link(
                                text="Земля",
                                href="https://mir24.tv/articles/16290778/zemlya-bez-kursa-ili-k-chemu-privedet-smena-magnitnyh-polyusov",
                            ),
                            " же была безвидна и пуста, и тьма над бездною, и Дух Божий носился над водою.",
                        ]
                    ),
                ],
            ),
            "БЫТИЕ\n\n"
            "1 В начале сотворил Бог небо и землю.\n\n"
            "2 Земля [https://mir24.tv/articles/16290778/zemlya-bez-kursa-ili-k-chemu-\n"
            "privedet-smena-magnitnyh-polyusov] же была безвидна и пуста, и тьма над бездною,\n"
            "и Дух Божий носился над водою.\n\n",
        ),
    ],
)
def test_format_page(page, expected_str):
    assert expected_str == str(page)
