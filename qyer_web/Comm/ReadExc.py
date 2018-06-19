import xlrd

class ReadExcle():
    def readExcle(self):
        # 打开excle
        book = xlrd.open_workbook("../Data/QYER.xlsx")
        # 定位sheet表
        table = book.sheet_by_name("Sheet1")
        # 统计行数
        row_Num = table.nrows
        # print("行数：",row_Num)
        # 统计列数
        col_Num = table.ncols
        # print("列数：",col_Num)


        # 获取整个excel的数据
        data = []
        # 方法1：以列表的形式
        for rowdata in range(1,row_Num):
            # 获取某一行数据
            row = table.row_values(rowdata)
            print("this is %d line:"%rowdata,row)
            if row:
                data.append(row)
        return data



        # 方法2：以字典的形式
        # 获取第一行数据
        # key = table.row_values(0)
        #
        # if row_Num <= 1:
        #     print("没有数据")
        # else:
        #     j = 1
        #     for i in range(row_Num-1):
        #         d = {}
        #         values = table.row_values(j)
        #         for x in range(col_Num):
        #             d[key[x]] = values[x]
        #         j += 1
        #         data.append(d)
        #     return data


if __name__ == '__main__':
    r = ReadExcle()
    s = r.readExcle()

