def re_data_list():
    data_list = []
    with open("F:/PythonTest/test/QYER/qyer_web/Data/data.txt","r",encoding='utf-8') as f:
        for i in f.readlines():
            # 截取等号右侧的数据
            data_list.append(eval(i.split("=")[-1]))
        print("data is:",data_list)
    return data_list

re_data_list()