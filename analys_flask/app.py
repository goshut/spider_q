from flask import Flask, render_template
from matplotlib import pyplot as plt

from analys import Analys
from datetime import datetime, timedelta


class Config:
    DEBUG = True


app = Flask(__name__)
app.config.from_object(Config)
a = Analys()
t_str = datetime.now().strftime('%Y-%m-%d')
raise_str = 'raise_' + t_str
res = a.stu.find({raise_str: {'$gt': 0}}).sort(raise_str, -1).limit(15)
raise_list = []
for i in res:
    raise_list.append(i['project_id'])


@app.route('/')
def index():
    t_str = datetime.now().strftime('%Y-%m-%d')
    raise_str = 'raise_' + t_str
    res = a.stu.find({raise_str: {'$gt': 0}}).sort(raise_str, -1).limit(15)
    art = a.stu.find({raise_str: {'$gt': 0}, "category": 'Art'}).sort(raise_str, -1).limit(15)
    Dance = a.stu.find({raise_str: {'$gt': 0}, "category": 'Dance & Theater'}).sort(raise_str,
                                                                                    -1).limit(15)
    Film = a.stu.find({raise_str: {'$gt': 0}, "category": 'Film'}).sort(raise_str, -1).limit(15)
    Music = a.stu.find({raise_str: {'$gt': 0}, "category": 'Music'}).sort(raise_str, -1).limit(15)
    Photography = a.stu.find({raise_str: {'$gt': 0}, "category": 'Photography'}).sort(raise_str,
                                                                                      -1).limit(15)
    Podcasts = a.stu.find({raise_str: {'$gt': 0}, "category": 'Podcasts, Blogs & Vlogs'}).sort(
        raise_str, -1).limit(15)
    Comics = a.stu.find({raise_str: {'$gt': 0}, "category": 'Comics'}).sort(raise_str, -1).limit(15)
    return render_template("list.html", all_data=res, art=art, Comics=Comics, Dance=Dance, Film=Film, Music=Music,
                           Photography=Photography, Podcasts=Podcasts)


@app.route('/show/<project_id>')
def show(project_id):
    res = a.stu.find_one({'project_id': int(project_id)})
    k_list = []
    v_list = []
    for k, v in res.items():
        if 'funds_raised_amount' in k:
            k_list.append(k)
            v_list.append(v)
    k_list.pop(0)
    v_list.pop(0)

    plt.figure(figsize=(12, 2), dpi=80)
    plt.plot(k_list, v_list)
    plt.savefig('./static/plt/' + str(res['project_id']) + '.png', format='png')
    plt.close('all')
    t_3 = datetime.now() - timedelta(days=3)
    str_3days = "funds_raised_amount_" + t_3.strftime('%Y-%m-%d')
    data_b3 = res.get(str_3days)
    t_str = datetime.now().strftime('%Y-%m-%d')
    funds_str = 'funds_raised_amount_' + t_str
    if data_b3:
        t_days = res[funds_str] - data_b3
    else:
        t_days = None
    raise_rank = raise_list.index(int(project_id)) + 1
    plt_url = '../static/plt/'+project_id + '.png'
    return render_template('show.html', res=res, t_days=t_days, raise_rank=raise_rank, plt_url=plt_url)


if __name__ == '__main__':
    app.run()
