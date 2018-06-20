import temp.fanshe1

"""
python的反射
python的四个重要内置函数：getattr、hasattr、delattr和setattr
较为全面的实现了基于字符串的反射机制。
他们都是对内存内的模块进行操作，并不会对源文件进行修改。
delattr()  删除内存里面的方法
setattr()  #设置内存里面的方法
"""
# def run():
#     inp = input("pls send a url:").strip()
#     if hasattr(com,inp):
#         func = getattr(com,inp)
#         func(com)
#     else:
#         print("404")
# ----------------------------

"""
升级
通过__import__函数，我们实现了基于字符串的动态的模块导入。
modules,func = inp.split("/")处理了用户输入，
使我们获得的2个字符串，并分别保存在modules和func变量里。
"""

def run():
    inp = input("请输入您想访问页面的url： ").strip()
    modules, func = inp.split("/")

    obj = __import__(modules)    #如果不想导入import com，可以这种方式导入，
    print(obj)
    if hasattr(obj, func):   #判断在com模块中是否存在func这个字符串
        func = getattr(obj, func)    # 获取inp的引用
        func()   # 执行
    else:
        print("404")
# ------------------------------


# def run():
#     inp = input("请输入您想访问页面的url： ").strip()
#     modules, func = inp.split("/")
#     try:
#         obj = __import__('lib.' + modules, fromlist=True)  # 如果com有文件夹lib的话，导入该模块  com
#         print(obj)
#         if hasattr(obj, func):  # 判断有没有这个方法
#             fuc = getattr(obj, func)  # 获得这个方法
#             fuc()
#         else:
#             print('404')
#     except Exception as e:
#         print(e)


if __name__ == '__main__':
    run()



