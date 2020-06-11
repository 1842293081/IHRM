# 导包
import time
import unittest
import HTMLTestRunner_PY3

import app
from script.test_emp_employee import TestIHRMEmployee
from script.test_ihrm_login import TestIHRMLogin

# 2.创建测试套件
suite = unittest.TestSuite()

# 3.将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestIHRMLogin))
suite.addTest(unittest.makeSuite(TestIHRMEmployee))
# 4.定义测试报告的目录和报告名称
# report_path = app.BASE_DIR + "/report/tpshop{}.html".format(time.strftime("%Y%m%d %H%M%S"))
report_path = app.BASE_DIR + "/report/tpshop{}.html"

# 5.使用HTMLTestRunner_PY3生成测试报告
with open(report_path, mode="wb") as f:
    # 实例化HTMLTestRunner_PY3
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=1, title="ihrm系统接口测试",
                                               description="我们的IHRM的接口测试报告")
    # 实例化runner原型测试套件，生成测试报告
    runner.run(suite)
