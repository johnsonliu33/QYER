from qyer_web.Comm.config import logger
import os

def case_log(data):
    num = data['用例编号']
    name = data["用例名称"]
    page = data["页面"]
    operate = data["操作"]
    expect = data["预期结果"]
    actul = data["实际结果"]
    logger.info("%s测试开始" % num)
    logger.info("%s开始" % name)
    logger.info("url:%s" % page)
    logger.info("入参:%s" % operate)
    logger.info("期望结果:%s" % expect)
    logger.info("实际结果:%s" % actul)


if __name__ == '__main__':
    from qyer_web.Comm.config import datapath
    from qyer_web.Comm.ReadExc import ReadExcle
    file = os.path.join(datapath,'F:\PythonTest\test\QYER\qyer_web\Data\QYER.xlsx')
    r = ReadExcle()
    data = r.readExcle()
    case_log(data)