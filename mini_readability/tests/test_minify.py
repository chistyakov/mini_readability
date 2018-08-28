from types import MappingProxyType
from unittest import mock

import pytest

from mini_readability.minify import minify
from .utils import sample


@pytest.mark.parametrize(
    "source_name,encoding,source_domain,expected_result_name",
    [
        # https://lenta.ru/articles/2018/08/23/roditeli_cet/
        (
            "lenta_ru_articles_2018_08_23.html",
            "utf-8",
            "lenta.ru",
            "lenta_ru_articles_2018_08_23.mini.txt",
        ),
        # https://www.gazeta.ru/politics/photo/uikend_v_gorah_kak_putin_otdohnul_v_tuve.shtml
        (
            "gazeta_ru_politics_photo_uikend_v_gorah_kak_putin_otdohnul_v_tuve.shtml",
            "windows-1251",
            "gazeta.ru",
            "gazeta_ru_politics_photo_uikend_v_gorah_kak_putin_otdohnul_v_tuve.txt",
        ),
    ],
)
@mock.patch(
    "mini_readability.parse.get_config",
    return_value=MappingProxyType(
        {
            "default": {"xpath": ".//*[self::p or self::h1 or self::h2 or self::h3]"},
            "lenta.ru": {"xpath": ".//*[self::p or self::h1]"},
            "gazeta.ru": {
                "xpath": ".//*[(self::p or self::h1 or self::h2) "
                'and not(ancestor::div[@class="bottom_info"]) '
                'and not(ancestor::div[@id="publications_by"]) '
                'and not(ancestor::div[@class="m_rub"])]'
            },
        }
    ),
)
def test_minify(
    mock_config, source_name, encoding, source_domain, expected_result_name
):
    page = sample(source_name, encoding=encoding)
    expected_minified = sample(expected_result_name)
    assert expected_minified == minify(page, source_domain)
