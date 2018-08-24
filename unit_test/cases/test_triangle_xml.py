import unittest

# 导入三角形类
from Func.triangle import Triangle

# daour xml 数据解析类

from ReadData.read_xml import ReadXml

triangle_class = Triangle()
readXml_class = ReadXml()


class TestTriangleXml(unittest.TestCase):
    def test_triangle_xml(self):
        for i in range(readXml_class.get_len("side")):
            res = triangle_class.func_triangle(int(readXml_class.readxml("side", i, "side1")),
                                               int(readXml_class.readxml("side", i, "side2")),
                                               int(readXml_class.readxml("side", i, "side3")))

            # 设置断言
            self.assertEqual(res, readXml_class.readxml("side", i, "except"))

            # 职位调试代码查看运行结果，核对代码执行过程，实际工作不需要书写这部分代码
            print("三角形函数返回的结果：", res)
            print(int(readXml_class.readxml("side", i, "side1")),
                  int(readXml_class.readxml("side", i, "side2")),
                  int(readXml_class.readxml("side", i, "side3")),
                  readXml_class.readxml("side", i, "except"), ">>>>>>>验证成功")
