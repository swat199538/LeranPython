import os
# 列表生成式是Python内置的非常简单却强大的可以用来创建list的生成式
# 比如要生成list[1,2,3,4,5,6,7,8,9,10]可以这样(py2中range返回的是一个列表，py3中返回的是一个迭代值):
a = range(1, 11)
print(list(a))

# 生成[1x1, 2x2, 3x3, 4x4, ..., 10x10]怎么做？循环!
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

# 但是循环太繁琐，而列表生成式可以用在一行语句代替循环生成上面的list：
b = [x * x for x in range(1, 11)]
print(b)
# 写列表生成式时，把要生成的元素x*x放到前面，后面跟for循环，就可以把list创建出来,十分有用。

# for循环后面可以加上if判断，这样我们就可以筛选出仅偶数的平方:
c = [x * x for x in range(1, 11) if x % 2 == 0]
print(c)

# 还可以用两层循环，可以生成全排列
string1 = 'ABCD'
string2 = string1[::-1]
d = [m + n for m in string1 for n in string2]
print(d)

# 列出当前目录下所以文件和目录名
# import os
print([dirs for dirs in os.listdir('.')])

# for循环其实可以同时使用两个甚至多个变量，比如dict的items(),同时迭代key和value:
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for x, y in dict1.items():
    print(x, '=', y)

# 把list中所有的字符串变成小写
string3 = ['Python', 'PHP', 'C#']
print([char1.lower() for char1 in string3])

# 小结运用列表生成式，可以快速的生成list，可以通过一个list推导出另一个list，十分简洁
