import pytest
from app.helpers import parse_url_domain


@pytest.mark.parametrize(
    'test_input,expected',
    [
        ('https://restofworld.org/2021/saudi-arabia-tech-not-oil-the-hot-new-thing/', 'restofworld.org'),
        ('https://restofworld.org/2021/', 'restofworld.org'),
        ('http://restofworld.org/2021/', 'restofworld.org'),
        ('http://restofworld.org/', 'restofworld.org'),
        ('http://restofworld.org', 'restofworld.org'),
        ('restofworld.org', 'restofworld.org'),
        ('restofworld.org/2021/', 'restofworld.org'),
    ],
)
def test_parse_url_domain(test_input, expected):
    actual = parse_url_domain(test_input)
    assert actual == expected
