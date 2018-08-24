import unittest
from Tools.HTMLTestReportCN import HTMLTestRunner
import time

case_dir = "../cases/"
discover = unittest.defaultTestLoader.discover(case_dir, pattern="test*.py")
report_dir = "../Report/"
now_time = time.strftime("%Y-%m-%d %H_%M_%S")
report_name = report_dir + now_time + "Report.html"
with open(report_name, "wb") as f:
    runner = HTMLTestRunner(stream=f, verbosity=2, title="单元测试报告CN版", description="测试环境：win10，执行人：xie")
    runner.run(discover)

if __name__ == '__main__':
    unittest.main()
