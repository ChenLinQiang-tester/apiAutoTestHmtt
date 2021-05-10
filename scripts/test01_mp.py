import json
import pytest
import api

from tool.read_json import read_json
from tool.tool import Tool
from api.api_mp import ApiMp


class TestMp:
    # 1.初始化
    def setup_class(self):
        # 获取ApiMp对象
        self.mp = ApiMp()

    # 2.登录接口测试方法
    @pytest.mark.parametrize("mobile, code", read_json('data/mp_login.json'))
    def test01_mp_login(self, mobile, code):
        # 调用登录接口
        r = self.mp.api_mp_login(mobile, code)
        # 打印输出接口
        print("登录接口为：", json.dumps(r.json(), indent=2))
        # 提取token
        Tool.common_token(r)
        # 断言
        Tool.common_assert(r)

    # 3.发布文章接口测试方法
    def test_mp_article(self):
        # 1.调用发布文章接口
        r = self.mp.api_mp_article(title=api.title, content=api.content, channel_id=api.channel_id)
        # 2.提取文章id
        api.article_id = r.json().get("data").get("id")
        print("发布文章成功后的id:{}".format(api.article_id))
        # 3.断言
        Tool.common_assert(r)
