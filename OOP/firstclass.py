# coding:utf-8
class Firstclass(object):
    hobby = 'computer'

    def __init__(self, name, age, sex):
        # 没有下划线表示公开的
        self.name = name
        # 一个下划线表示受保护的
        self._aget = age
        # 两个下划线表示私有的
        self.__sex = sex

    def get_sex(self):
        return self.__sex

if __name__ == '__main__':
    pro = Firstclass('张三', 12, '男')
    print dir(pro)
    print pro.__dict__
    print pro.get_sex()
