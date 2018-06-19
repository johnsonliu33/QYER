import xml.dom.minidom
file_name = "../Data/xml.xml"
#打开xml文档
domTree = xml.dom.minidom.parse(file_name)
# 返回文档的根节点
root = domTree.documentElement
# 返回带有指定标签名的对象的集合(在集合中获取所有电影)
musics = root.getElementsByTagName("music")
# 打印每部电影的详细信息
for music in musics:
    print("----music----")
    if music.hasAttribute("title"):
        print("歌名: %s" % music.getAttribute("title"))

        # 格式
    type = music.getElementsByTagName("format")[0]
    print("-格式: %s" % type.childNodes[0].data)
    year = music.getElementsByTagName("year")[0]
    print("-年份: %s" % year.childNodes[0].data)
    month = music.getElementsByTagName("month")[0]
    print("-月份: %s" % month.childNodes[0].data)
    start = music.getElementsByTagName("stars")[0]
    print("-星数: %s" % start.childNodes[0].data)
    desc = music.getElementsByTagName("description")[0]
    print("-描述:%s" % desc.childNodes[0].data)





# def read_xml(self,filepath,onenode,twonode):
#     # 打开文件的路径
#     root = xml.dom.minidom.parse(filepath)
#     # 获取路径数据所在位置节点
#     firstnode = root.getElementsByTagName(onenode)[0]
#     # 获取数据
#     secondnode = firstnode.getElementsByTagName(twonode)[0].firstChild.data
#     print(secondnode)



