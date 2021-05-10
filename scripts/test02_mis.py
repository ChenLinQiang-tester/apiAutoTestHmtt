import pytest

import api
from api.api_mis import ApiMis
from tool.read_json import read_json
from tool.tool import Tool


class TestMis:
    # 1.初始化
    def setup_class(self):
        # 获取ApiMis对象
        self.mis = ApiMis()

    # 2.登录接口测试方法
    @pytest.mark.parametrize("account,password", read_json("data/mis_login.json"))
    def test_mis_login(self, account, password):
        # 获取登录响应对象
        r = self.mis.api_mis_login(account, password)
        print("后台管理系统登录成功后，请求headers：{}".format(api.headers))
        # 提取token值
        Tool.common_token(r)
        Tool.common_assert(r)

    # 3.查询文章接口测试方法
    def test_mis_search(self):
        # 获取文章查询接口响应对象
        r = self.mis.api_mis_search()
        Tool.common_assert(r, status_code=200)

    # 4.审核文章接口测试方法
    def test_mis_audit(self):
        # 获取审核文章接口响应对象
        r = self.mis.api_mis_audit()
        Tool.common_assert(r)
