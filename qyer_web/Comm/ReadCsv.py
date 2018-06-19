import csv

class ReadCsv():
    def readcsv(self,filename):
        my_list = []
        # 打开csv文件
        csv_context = csv.reader(open(filename,"r"))
        # 内存地址
        # print(csv_context)
        for csv_con in csv_context:
            my_list.append(csv_con)
        # 把文件表头给切掉
        m_list = my_list[1:]
        return m_list

# 测试读取csv文件的方法正确不正确，只是在这个类里验证用
r = ReadCsv()
print(r.readcsv("../Data/csv.csv"))