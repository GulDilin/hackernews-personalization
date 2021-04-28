import requests
import logging
import json
import re
from bs4 import BeautifulSoup

logger = logging.getLogger("news_parser")


def get_first_number(string):
    try:
        return int(re.findall(r'\d+', string)[0])
    except IndexError:
        raise ValueError('Cant parse any numbers')


def extract_item_info(item_tr):
    item_info = {}
    story_link = item_tr.find('a', 'storylink')
    item_info['title'] = story_link.string
    item_info['url'] = story_link.get('href')
    return item_info


def extract_first_number_or_zero(raw):
    try:
        return get_first_number(raw.string)
    except ValueError:
        logger.debug(f'Cant parse first number from {raw}. Return 0')
        return 0


def extract_sub_info(sub_tr):
    sub_info = {}
    sub_info_td = sub_tr.find_all('td')[-1]
    sub_info['points'] = extract_first_number_or_zero(sub_info_td.span)
    sub_info['author'] = sub_info_td.find('a', 'hnuser').string
    comments_raw = sub_info_td.find_all('a')[-1]
    sub_info['comments'] = extract_first_number_or_zero(comments_raw)
    return sub_info


def extract_news_item(content_table, item_id):
    news_item = {'id': item_id}
    item_tr = content_table.find(id=item_id)
    sub_tr = item_tr.next_sibling
    news_item.update(extract_item_info(item_tr))
    news_item.update(extract_sub_info(sub_tr))
    return news_item


def extract_news(content_table, items_ids):
    return [extract_news_item(content_table, items_id) for items_id in items_ids]


def extract_page(page):
    tables_list = page.table.find_all('table')
    logger.debug(f'tables_list: {len(tables_list)}')
    content_table = tables_list[1]
    items_ids = [tr.get('id') for tr in content_table.find_all('tr') if str(tr.get('id')).isnumeric()]
    logger.debug(f'Got items ids: {items_ids}')
    news = extract_news(content_table, items_ids)
    return news


def extract_url(base_url, next_id=None):
    url = base_url
    if next_id:
        url += f'?next={next_id}'
    logger.info(f'Collecting data from page: {url}')
    response = requests.get(url)
    page = BeautifulSoup(response.text, 'html.parser')
    news_list = extract_page(page)
    logger.debug(f'Excracted news: {json.dumps(news_list, indent=2)}')
    return news_list


def get_news(base_url, n_pages=1, next_id=None):
    if n_pages < 0:
        return ValueError('n_pages cannot be smaller than zero')
    page = 0
    news_list = []
    while page < n_pages:
        news = extract_url(base_url, next_id)
        news_list += news
        page += 1
    return news_list


if __name__ == '__main__':
    news = get_news('https://news.ycombinator.com/newest', 5)
    logger.info(f'News amount: {len(news)}')
    logger.info(f'Got news: {json.dumps(news, indent=2)}')
