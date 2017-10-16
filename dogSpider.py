from huang.Spider import *
from huang.config import *

class run():
    def __init__(self):
        pass

    #获取所有列表
    def get_list(self):
        list = cfg.getType()
        for l in list.keys():
            print(l)
        return list

    #获取用户选择的分类
    def input_type(self):
        start = spider(url)
        list = self.get_list()
        #type = input('输入要选择下载的类型分类（复制一下就好）：\n')
        type = '亚洲无码'
        if type in cfg.getType() and type == '亚洲无码':
            print('有')
            newDir = start.newDir(type)
            listLink = list[type]
            oneList = start.openLink(listLink)



        elif type in cfg.getType() and type == '成人小说':
            pass


        else :
            print('没有或者暂时不支持此类型下载')




if __name__ == '__main__':
    cfg = config()
    url = cfg.url
    a = run()
    a.input_type()

