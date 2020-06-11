# 导包
import unittest
import logging
from parameterized import parameterized
import app
from api.login_api import LoginApi
from utils import read_login_data, assert_common


# 创建unittest的类
class TestIHRMLogin(unittest.TestCase):
    # 进行初始化
    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 定义登录数据文件的路径
    filepath = app.BASE_DIR + "/data/login_data.json.json"

    @parameterized.expand(read_login_data(filepath))
    # 编写登录成功函数
    def test01_login(self, case_name, request_body, success, code, message, http_code):
        # 使用封装的接口调用登录接口，并接收返回的响应数据
        response = self.login_api.login(request_body,
                                        {"Content-Type": "application/json"})

        # 打印响应数据
        logging.info("登录成功的结果为：{}".format(response.json()))

        # 断言
        assert_common(self, http_code, success, code, message, response)
