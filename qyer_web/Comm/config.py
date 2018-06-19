import os
import logging


# 项目目录
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 数据库目录
datapath = os.path.join(basedir,"data")

# 日志配置
logdir = os.path.join(basedir,'log')
logpath = os.path.join(logdir,'2018log.log')

#获取logger
logger = logging.getLogger('apiteststudy')
#设置logger级别
logger.setLevel(logging.DEBUG)
#设置logger格式
datafmt = '%Y-%m-%d %H:%M:%S  '
fm = logging.Formatter(fmt='%(asctime)s%(name)-12s%(levelname)-8s%(message)s',datefmt=datafmt)
#输出到文件
fh = logging.FileHandler(logpath,encoding='utf-8')
fh.setFormatter(fm)
#添加到handler
logger.addHandler(fh)



# --------------------------------------------------------------------
#方法2
# logging.basicConfig(level=logging.DEBUG,filename='2018log.log',
#                     filemode='a',format='%(asctime)s - %(pathname)s[line:%(lineno)d]'
#                                         ' - %(levelname)s: %(message)s')


"""
logging.basicConfig()函数中可通过具体参数来更改logging模块默认行为，可用参数有
filename：用指定的文件名创建FiledHandler（后边会具体讲解handler的概念），这样日志会被存储在指定的文件中。
filemode：文件打开方式，在指定了filename时使用这个参数，默认值为“a”还可指定为“w”。
format：指定handler使用的日志显示格式。
datefmt：指定日期时间格式。
level：设置rootlogger的日志级别
stream：用指定的stream创建StreamHandler。
可以指定输出到sys.stderr,sys.stdout或者文件，
默认为sys.stderr。若同时列出了filename和stream两个参数，
则stream参数会被忽略。

"""


if __name__ == '__main__':
    logging.info('this is a test')
    # logger.info('this is a test')
    logging.debug('debug')
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")

    # 日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET