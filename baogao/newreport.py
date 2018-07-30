import unittest
import time
from tools.HTMLTestRunner import HTMLTestRunner
from tools.HTMLTestReportCN import HTMLTestRunner

if __name__ == '__main__':
    # 1. 组装测试用例
    dir_path = "./cases/"
    cases_loader = unittest.defaultTestLoader.discover(dir_path, pattern='iwebshop*.py')
    # 2. 报告存放路径
    report_dir = "./reports/"
    # 3. 获取当前时间
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")
    # 4. 准备报告名称
    report_name = report_dir + now_time + 'Report.html'

    # 开启报告写入文件流
    with open(report_name, 'wb') as f:
        # runner = HTMLTestRunner(stream=f, verbosity=1, title='iwebshop_login测试报告',
        #                         description='测试平台：Windows10 测试浏览器：Firefox 版本：v35.4 测试人员：QA01')

        runner = HTMLTestRunner(stream=f, verbosity=2, title='iwebshop_login测试报告',
                                description='测试平台：Windows10 测试浏览器：Firefox 版本：v35.4', tester='QA02')

        runner.run(cases_loader)
