import unittest
from Func.triangle import Triangle
from ReadData.read_json import ReadJson

triangle_class = Triangle()
readJson_class = ReadJson()


class TestTriangleJson(unittest.TestCase):
    def test_triangleJson(self):
        for i in range(len(readJson_class.readJson())):
            res = triangle_class.func_triangle(int(readJson_class.readJson()[i]["side1"]),
                                               int(readJson_class.readJson()[i]["side2"]),
                                               int(readJson_class.readJson()[i]["side3"]),

                                               )

            self.assertEqual(res, readJson_class.readJson()[i]["except"])

            print("三角形函数返回结果:", res)
            print(int(readJson_class.readJson()[i]["side1"]),
                  int(readJson_class.readJson()[i]["side2"]),
                  int(readJson_class.readJson()[i]["side3"]),
                  readJson_class.readJson()[i]["except"], ">>>>>验证成功"
                  )
