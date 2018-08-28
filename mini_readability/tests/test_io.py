from unittest import mock

import pytest

from mini_readability.io import result_filename, get_domain


@pytest.mark.parametrize(
    "url,expected_filename",
    [
        ("http://lenta.ru/news/2013/03/dtp/index.html", "/data/index.txt"),
        # TODO: unique name to prevent overriding of results
        ("https://lenta.ru/articles/2018/08/23/roditeli_cet/", "/data/no_name.txt"),
    ],
)
@mock.patch.dict("os.environ", {"OUTPUT_BASE_PATH": "/data"})
def test_result_filename(url, expected_filename):
    assert expected_filename == result_filename(url)


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
