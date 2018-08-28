from unittest import mock

import pytest

from mini_readability.io import build_path, get_domain


@pytest.mark.parametrize(
    "url,expected_path",
    [
        (
            "https://lenta.ru/articles/2018/08/23/roditeli_cet/",
            (
                "/data/lenta.ru/articles/2018/08/23/roditeli_cet",
                "/data/lenta.ru/articles/2018/08/23/roditeli_cet/no_name.txt",
            ),
        ),
        (
            "http://lenta.ru/news/2013/03/dtp/index.html",
            (
                "/data/lenta.ru/news/2013/03/dtp",
                "/data/lenta.ru/news/2013/03/dtp/index.txt",
            ),
        ),
    ],
)
@mock.patch.dict("os.environ", {"OUTPUT_BASE_PATH": "/data"})
def test_build_path(url, expected_path):
    assert expected_path == build_path(url)


@pytest.mark.parametrize(
    "url,expected_domain",
    [
        ("https://lenta.ru/articles/2018/08/23/roditeli_cet/", "lenta.ru"),
        ("http://user:pass@example.com:8080", "example.com"),
    ],
)
def test_get_domain(url, expected_domain):
    domain = get_domain(url)
    assert domain == expected_domain
