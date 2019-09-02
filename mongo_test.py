from pymongo import MongoClient


class DbTest:
    def __init__(self):
        self.client = MongoClient("localhost", 27017)
        self.db = self.client.indiegogo_test
        self.stu = self.db.new_stu
        # s1 = {"category": 'Art', "clickthrough_url": "/projects/scribit-turn-your-wall-into-a-wonderwall",
        #       "funds_raised_amount_2019_8_31": '2431343', "project_id": "2392244"}
        # stu.insert(s1)
        # stu.update({"project_id": '2392244'}, {'$set': {"funds_raised_amount_2019_9_1": '2431366'}}, multi=True, upsert=True)

    def write_data(self, project_id, data):
        self.stu.update({"project_id": project_id}, {'$set': data}, multi=True, upsert=True)
