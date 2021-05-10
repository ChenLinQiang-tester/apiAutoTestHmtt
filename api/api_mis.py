import requests

import api
from tool.get_log import GetLog

log = GetLog.get_logger()


class ApiMis:
    # 1.初始化
    def __init__(self):
        log.info("*"*200+"\n")
        # 1. 登录url  post
        self.url_login = api.host + "/mis/v1_0/authorizations"
        log.info("正在初始化后台管理系统 登录url：{}".format(self.url_login))
        # 2. 查询文章url  get
        self.url_search = api.host + "/mis/v1_0/articles"
        log.info("正在初始化后台管理系统 查询文章url：{}".format(self.url_search))
        # 3. 审核文章url  put
        self.url_audit = api.host + "/mis/v1_0/articles"
        log.info("正在初始化后台管理系统 审核文章url：{}".format(self.url_audit))

    # 2. 登录
    def api_mis_login(self, account, password):
        """
        :param account:账号
        :param password: 密码
        :return: 响应对象
        """
        log.info("-"*200)
        log.info("正在调用后台管理系统登录接口")
        # 1.参数数据
        data = {"account": account, "password": password}
        # 2. 调用post方法
        interface = requests.post(url=self.url_login, json=data, headers=api.headers)
        log.info("请求方法：post 请求数据：{} 请求信息头：{}".format(data, api.headers))
        return interface

    # 3. 查询文章
    def api_mis_search(self):
        """
        :param title: 文章标题，数据来源__init__.py中获取
        :param channel: 文章所属频道，数据来源__init__.py中获取
        :return: 响应对象
        """
        log.info("-" * 200)
        log.info("正在调用后台管理系统查询文章接口")
        # 1.参数数据
        data = {"title": api.title, "channel": api.channel}
        # 2.调用get方法
        interface = requests.get(url=self.url_search, params=data, headers=api.headers)
        log.info("请求方法：get 请求数据：{} 请求信息头：{}".format(data, api.headers))
        return interface

    # 4. 审核文章
    def api_mis_audit(self):
        """
        :param article_ids: 文章id，数据来源发布文章后服务器生成
        :param status: 2 为审核通过
        :return:响应对象
        """
        log.info("-" * 200)
        log.info("正在调用后台管理系统审核文章接口")
        # 1.参数数据
        data = {"article_ids": [api.article_id], "statue": 2}
        # 2.调用put方法
        interface = requests.put(url=self.url_audit, json=data, headers=api.headers)
        log.info("请求方法：get 请求数据：{} 请求信息头：{}".format(data, api.headers))
        return interface
