"""公共变量"""
# 1.请求域名
from config import base_path
from tool.read_json import read_json


host = "http://ttapi.research.itcast.cn"
# 2.请求信息头
headers = {"Content-Type": "application/json"}
# 文章id
article_id = None
# 发布文章数据
data_article = read_json(base_path+"/data/mp_article.json")
# 文章标题
title = data_article[0][0]
# 文章内容
content = data_article[0][1]
# 文章所属频道id
channel_id = data_article[0][2]
# 文章所属频道
channel = data_article[0][3]