import api
from tool.get_log import GetLog

log = GetLog.get_logger()


class Tool:
    # 1.提取token
    @classmethod
    def common_token(cls, response):
        try:
            # 提取token
            token = response.json().get("data").get("token")
            # 追加请求信息头
            api.headers["Authorization"] = "Bearer " + token
            log.info("正在提取token， 提取后的header：{}".format(api.headers))
        except Exception as e:
            log.error(e)
            raise

    # 2.断言
    @classmethod
    def common_assert(cls, response, status_code=201):
        log.info("正在调用公共断言方法")
        try:
            # 断言状态码
            print(response.status_code)
            assert status_code == response.status_code
            assert "OK" == response.json().get("message")
            log.info("断言成功")
        except AssertionError:
            log.error("断言失败 状态码：{}".format(response.status_code))
            raise
