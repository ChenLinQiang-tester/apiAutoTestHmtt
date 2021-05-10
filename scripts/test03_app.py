import pytest

from api.api_app import ApiApp
from tool.get_log import GetLog
from tool.read_json import read_json
from tool.tool import Tool

log = GetLog.get_logger()


class TestApp:
    # 初始化
    def setup_class(self):
        # 获取APP api对象
        self.app = ApiApp()

    # 测试APP登录接口
    @pytest.mark.parametrize("mobile, code", read_json("data/app_login.json"))
    def test_app_login(self, mobile, code):
        # 调用APP登录接口响应对象
        r = self.app.api_app_login(mobile, code)
        # 断言
        Tool.common_token(r)
        Tool.common_assert(r)

    # 测试APP查看频道文章接口
    def test_app_channel_article(self):
        # 调用APP查看频道文章接口响应对象
        r = self.app.api_app_channel_article()
        # 断言
        Tool.common_assert(r, status_code=200)
