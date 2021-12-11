import xml.etree.ElementTree as ET
import json
from urllib.request import urlopen
from itertools import groupby

""" Задание 1 """

# data = urlopen('https://lenta.ru/rss').read().decode('utf8')
# root = ET.fromstring(data)
#
# with open('news.json', 'w', encoding='utf-8') as file:
#     items = root.findall('.//item')
#     info = []
#     for item in items:
#         title = item.find('.//title').text
#         pubDate = item.find('.//pubDate').text
#         info.append({
#             'pubDate': pubDate,
#             'title': title,
#         })
#
#     json.dump(info, file, indent=4, ensure_ascii=False)

""" Задание 2"""

# data = urlopen('https://lenta.ru/rss').read().decode('utf8')
# root = ET.fromstring(data)
# result = []
# info = {}
# with open('newsText.json', 'w', encoding='utf-8') as file:
#     items = root.findall('.//item')
#     for item in items:
#         for child in item.iter():
#             try:
#                 info[child.tag] = item.find(f'.//{child.tag}').text
#             except AttributeError:
#                 pass
#         result.append(info)
#     json.dump(result, file, indent=4, ensure_ascii=False)


""" API, ДЗ """


def get_statistic(url):
    data = json.loads(urlopen(url).read().decode('utf8', 'ignore'))
    revisions = data['query']['pages']['192203']['revisions']
    values = groupby(revisions, lambda x: x['timestamp'].split('T')[0])
    for key, value in values:
        print(key, len(list(value)))


""" Градский """
URL = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE%2C_%D0%96' \
      '%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
get_statistic(URL)

""" Бельмондо """
URL = 'https://ru.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvlimit=500&titles=%D0%91%D0%B5%D0%BB%D1%8C%D0%BC%D0%BE%D0%BD%D0%B4%D0%BE%2C_%D0%96%D0%B0%D0%BD-%D0%9F%D0%BE%D0%BB%D1%8C'
get_statistic(URL)

""" Количество правок действительно увеличивается в день смерти человека """