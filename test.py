from datetime import datetime, timedelta

import requests
import json
from mongo_test import DbTest
from Config import HEADERS

from pymongo import MongoClient
from lxml import etree


def get_request(class_name=None, n=1):
    url = 'https://www.indiegogo.com/private_api/discover'

    json_data = {"sort":"trending","category_main":None,"category_top_level":None,"project_timing":"all","project_type":"campaign","page_num":n,"per_page":100,"q":"","tags":[]}

    response = requests.post(url, json=json_data, headers=HEADERS)

    text_data = response.text
    a_dict = json.loads(text_data)
    res = a_dict['response']['discoverables']
    return res


def get_contributions():
    url = "https://www.indiegogo.com/projects/your-pocket-sized-aerial-photographer-air-pix"
    response = requests.get(url, headers=HEADERS)
    text_data = response.text
    print(text_data)
    html = etree.HTML(text_data)
    contributions = html.xpath('//meta[@name="sailthru.displayed_contributions"]/@content')[0]
    print(contributions)


def data_deal(s):
    t_now = datetime.now().strftime('%Y-%m-%d')

    # t_now = datetime.now() - timedelta(days=1)
    # t_now = t_now.strftime('%Y-%m-%d')

    s['funds_raised_amount' + '_' + t_now] = s['funds_raised_amount']
    # project_id = s['project_id']
    # return s


if __name__ == '__main__':
    db = DbTest()
    # print(get_request())
    # data = get_request()
    # for i in data:
    #     data_deal(i)
    #     db.write_data(i["project_id"], i)
    # get_contributions()
    for i in range(100):
        print(i)
        res = get_request(n=i+1)
        for j in res:
            data_deal(j)
            db.write_data(j["project_id"], j)


