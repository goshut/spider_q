### 1.网站分析

网站共28个分类
每个分类10000数据,要做全网监控的话,每天要爬28万条数据

### 2.爬取api 分析

https://www.indiegogo.com/private_api/discover:主数据来源
https://www.indiegogo.com/+"clickthrough_url":通过html.xpath('//meta[@name="sailthru.displayed_contributions"]/@content')[0] 获得众筹支持人数

### 3.数据库

原始数据成分复杂,冗余成分多,用mongodb做数据库
'funds_raised_amount_'+datetime.now().strftime('%Y-%m-%d')记录每日金额
"raised_"+datetime.now().strftime('%Y-%m-%d')记录每日增加金额
方便日后做榜单排名和数据分析

### 4.绘图

matplotlib.pyplot 绘制折线图方便数据展示

### 5.可有可无的前端展示

web框架选用flask

模板用jinja2格式

### 一些问题:

外国网站,网速是爬取速度的最大瓶颈.
会封id,大概为半小时.需要做简单的浏览器伪装.

建议挂外网代理.

### 日常操作:

爬数据>清洗数据>入库>做增量分析>做排行榜单>提前绘制数据图

代码已写好,可用脚本按顺序执行.

录制的MP4文件展示了一下数据在前端显示的大概样子.以及数据库的结构和文件数据

-----------------------------------------------------------------------------------
### 代码还没整理,很乱.

https://github.com/goshut/spider_q
