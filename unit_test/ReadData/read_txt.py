#  不用导包
class ReadTxt(object):
    def readTxt(self):
        with open("../DataPool/triangle.txt", "r", encoding="utf-8") as f:
            """
            f.readlines(): 读取多行数据
            f.readline()   读取单行数据
            f.read()       读取数据,获取大量内容的问件事,一般需要限制文件大小
            
            """
            data = f.readlines()

            """
            strip():去除换行符号,空格,制表符
            split():使用传入的内容分隔数据,并返回列表型数据
            
            """
            data_list = []

            for i in data:
                data_list.append(i.strip().split(","))
            return data_list


if __name__ == '__main__':
    print(ReadTxt().readTxt())
