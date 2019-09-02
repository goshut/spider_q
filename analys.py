from pymongo import MongoClient
from datetime import datetime, timedelta


class Analys:
    def __init__(self):
        self.client = MongoClient("localhost", 27017)
        self.db = self.client.indiegogo_test
        self.stu = self.db.new_stu

    def count_1day(self):
        pass


if __name__ == '__main__':
    a = Analys()
    t_str = 'funds_raised_amount_' + datetime.now().strftime('%Y-%m-%d')
    tb_now = datetime.now() - timedelta(days=1)
    tb_str = 'funds_raised_amount_' + tb_now.strftime('%Y-%m-%d')
    res = a.stu.find({t_str: {"$gt": 0}, tb_str: {"$gt": 0}})
    raise_t = 'raise_' + datetime.now().strftime('%Y-%m-%d')

    print(res)
    n = 0
    for i in res:
        n += 1
        print(n)
        raise_point = i[t_str] - i[tb_str]
        raise_1 = {raise_t: raise_point, 'raise': raise_point}
        a.stu.update({'project_id': i['project_id']}, {'$set': raise_1}, multi=True, upsert=True)

    # res = a.stu.find({"project_id": 2523101, })
    # res.update({"funds_raised_amount_2019-09-01": 88888})

    # res = a.stu.find({'raise_2019-09-01': {'$gt': 0}, "category": 'Art'}).sort('raise_2019-09-01', -1).limit(10)
    # for i in res:
    #     print(i['raise_2019-09-01'], 'https://www.indiegogo.com' + i['clickthrough_url'], i['image_url'])
