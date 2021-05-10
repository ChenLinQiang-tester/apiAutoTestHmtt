import time
import requests
import api
from tool.get_log import GetLog

log = GetLog.get_logger()


class ApiApp:
    # 初始化
    def __init__(self):
        log.info("*"*200+"\n")
        # app登录url
        self.url_login = api.host + "/app/v1_0/authorizations"
        log.info("正在初始化app 登录url：{}".format(self.url_login))
        # app查看频道文章接口
        self.url_channel_article = api.host + "/app/v1_1/articles"
        log.info("正在初始化app查看频道文章 登录url：{}".format(self.url_login))

    # app登录测试接口
    def api_app_login(self, mobile, code):
        """
        :param mobile: 手机号
        :param code: 验证码
        :return:
        """
        log.info("-"*200)
        log.info("正在调用app登录接口")
        data = {"mobile": mobile, "code": code}
        interface = requests.post(url=self.url_login, json=data, headers=api.headers)
        log.info("调用方法：post 调用数据：{} 请求头：{}".format(data, api.headers))
        return interface

    # app查看频道文章接口
    def api_app_channel_article(self):
        """
        :param channel_id: 频道id，来源__init__.py
        :param timestamp: 时间戳 单位毫秒
        :param with_top: 置顶文章 1：包含 0：不包含
        :return: 响应对象
        """
        log.info("-" * 200)
        log.info("正在调用app查看频道文章接口")
        data = {"channel_id": api.channel_id, "timestamp": int(time.time()), "with_top": 1}  # 1:包含置顶文章；0：不包含
        interface = requests.get(url=self.url_channel_article, params=data, headers=api.headers)
        log.info("调用方法：get 调用数据：{} 请求头：{}".format(data, api.headers))
        return interface
