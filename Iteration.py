from collections import Iterable
# python迭代是通过for...in来实现的。
# python的for不仅仅可以用在list和tuple,还可以用在其他任何可以迭代的对象上
# list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代
d = {'a': 123, 'b': 245, 'c': 'oop', 'd': 'ddc'}
# 打印出d的所有key,因为dict的存储顺序不想list一样顺序存储所以，迭代的顺序可能不一样。
for key in d:
    print(key)

# 默认情况下dict迭代的是key，想要dict的value可以这样(python2中的itervalues()已经在python3中被移出)
for value in d.values():
    print(value)

# 同时迭代(iteritems()在python3中也已经没有了）
for key, value in d.items():
    print(key, value)

# 字符串也是可以迭代对象因此可以用for
string = 'python大法好'
for char in string:
    print(char)

# 如何判断一个对象是不是可以迭代的，可以用python collections模块的Iterable类型判断
# from collections import Iterable
# True
print(isinstance(string, Iterable))
# False
my_int = 123
print(isinstance(my_int, Iterable))

# 如果要对list实现类型其他语言那样循环小标可以用python的enumerate函数
my_list = ['a', 'b', 'c', 'd']
for i, value in enumerate(my_list):
    print(i, value)
# for循环里同时引入两个变量
my_list2 = [(1, 1), (1, 2), (1, 3)]
for x, y in my_list2:
    print(x, y)

# 小结 任何可迭代对象都可以作用于for循环，包括我们知道有的数据类型，只要符合迭代条件，就可以使用for循环。




