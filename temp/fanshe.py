# import commons
#  
# def run():
#   inp = input("请输入您想访问页面的url： ").strip()
#   if inp == "login":
#     commons.login()
#   elif inp == "logout":
#     commons.logout()
#   elif inp == "home":
#     commons.home()
#   else:
#     print("404")
#  
# if __name__ == '__main__':
#   run()







# 反射getatter
# getattr函数的使用方法：它接收2个参数，前面的是一个对象或者模块，后面的是一个字符串，注意了！是个字符串！

# 用户输入储存在inp中，这个inp就是个字符串，getattr函数让程序去commons这个模块里，寻找一个叫inp的成员（是叫，不是等于），这个过程就相当于我们把一个字符串变成一个函数名的过程。
# 然后，把获得的结果赋值给func这个变量，实际上func就指向了commons里的某个函数。最后通过调用func函数，实现对commons里函数的调用。这完全就是一个动态访问的过程，一切都不写死，全部根据用户输入来变化。
# 它的核心本质其实就是利用字符串的形式去对象（模块）中操作（查找/获取/删除/添加）成员，一种基于字符串的事件驱动！


# import commons
#  
# def run():
#   inp = input("请输入您想访问页面的url： ").strip()
#   func = getattr(commons,inp)
#   func()
#   
# if __name__ == '__main__':
#   run()




# 完善
# hasattr可以防止非法输入错误，并将其统一定位到错误页面。

# import commons
#   
# def run():
#   inp = input("请输入您想访问页面的url： ").strip()
#   if hasattr(commons,inp):
#     func = getattr(commons,inp)
#     func()
#   else:
#     print("404")
#   
# if __name__ == '__main__':
#   run()


# python的四个重要内置函数：getattr、hasattr、delattr和setattr较为全面的实现了基于字符串的反射机制。他们都是对内存内的模块进行操作，并不会对源文件进行修改。





# import__()方法会根据参数，动态的导入同名的模块。

# def run():
#   inp = input("请输入您想访问页面的url： ").strip()
#   modules, func = inp.split("/")
#   obj = __import__(modules)
#   if hasattr(obj, func):
#     func = getattr(obj, func)
#     func()
#   else:
#     print("404")
#   
# if __name__ == '__main__':
#   run()



# 优化

# def run():
#   inp = input("请输入您想访问页面的url： ").strip()
#   modules, func = inp.split("/")
#   obj = __import__("lib." + modules)   #注意字符串的拼接
#   if hasattr(obj, func):
#     func = getattr(obj, func)
#     func()
#   else:
#     print("404")
#   
# if __name__ == '__main__':
#   run()




# 继续优化

# def run():
#   inp = input("请输入您想访问页面的url： ").strip()
#   modules, func = inp.split("/")
#   obj = __import__("lib." + modules, fromlist=True) # 注意fromlist参数
#   if hasattr(obj, func):
#     func = getattr(obj, func)
#     func()
#   else:
#     print("404")
#   
# if __name__ == '__main__':
#   run()




# 其实，在上面的例子中，围绕的核心主题是如何利用字符串驱动不同的事件，比如导入模块、调用函数等等，这些都是python的反射机制，是一种编程方法、设计模式的体现，凝聚了高内聚、松耦合的编程思想，不能简单的用执行字符串来代替。当然，exec和eval也有它的舞台，在web框架里也经常被使用。



# 断言

# self.assertEqual("http://localhost:8080/ranzhi/www/s/index.php?m=index&f=index",
#                    self.driver.current_url,  "登录跳转失败")



# 数据存储CSV

# import csv
#  2 # 读取CSV文件到user_list字典类型变量中
#  3 user_list = csv.reader(open("list_to_user.csv", "r"))
#  4 # 遍历整个user_list
#  5 for user in user_list:
#  6     sleep(2)
#  7     self.logn_in('admin', 'admin')
#  8     sleep(2)
#  9     # 读取一行csv，并分别赋值到user_to_add 中
# 10     user_to_add = {'account': user[0],
# 11                     'realname': user[1],
# 12                     'gender': user[2],
# 13                     'dept': user[3],
# 14                     'role': user[4],
# 15                      'password': user[5],
# 16                      'email': user[0] + user[6]}
# 17      self.add_user(user_to_add)