import re
from app.naive_bayes_classifier import clean


def parse_url_domain(url: str) -> str:
    match = re.match(r'http(s)?://', url)
    domain = url
    if match:
        domain = url[match.end():]
    domain = domain.split('/')[0]
    return domain


def get_news_string(news_item):
    try:
        domain = parse_url_domain(news_item.url)
    except:
        domain = None
    msg = f'{news_item.title} {news_item.author} {domain}'
    msg = clean(msg)
    return msg


def prepare_classifier_data(news):
    items = list(map(lambda it, it2: (get_news_string(it), it2.label), news, news))
    return zip(*items)
