import unittest
from Tools.HTMLTestRunner import HTMLTestRunner
import time

if __name__ == '__main__':
    # 1.组装测试用例
    case_dir = "../cases/"
    discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py")

    # 2.准备报告生成路径
    report_dir = "../Report/"

    # 3.获取当前时间
    now_time = time.strftime("%Y-%m-%d %H_%M_%S")

    # 4.设置报告名称
    report_name = report_dir +now_time +"Report.html"

    with open(report_name,"wb") as f:
        runner = HTMLTestRunner(stream=f,verbosity=2,
                                title="单元测试报告",description="运行环境:windows,执行人:QA")
        runner.run(discover)