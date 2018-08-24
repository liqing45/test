import unittest
from Func.triangle import Triangle
from ReadData.read_csv import ReadCsv

triangle_class = Triangle()
readCsv_class = ReadCsv()


class TestTriangleCsv(unittest.TestCase):
    def test_triangle_csv(self):
        for i in range(len(ReadCsv().readCsv())):
            res = triangle_class.func_triangle(int(readCsv_class.readCsv()[i][0]),
                                               int(readCsv_class.readCsv()[i][1]),
                                               int(readCsv_class.readCsv()[i][2])
                                               )
    
            # 设置断言
            self.assertEqual(res, readCsv_class.readCsv()[i][3])
    
            print("三角形函数返回结果:", res)
            print(int(readCsv_class.readCsv()[i][0]),
                  int(readCsv_class.readCsv()[i][1]),
                  int(readCsv_class.readCsv()[i][2]),
                  readCsv_class.readCsv()[i][3], ">>>>>验证成功")
