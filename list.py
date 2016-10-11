# __________________list的学习__________________

# 创建一个list
classmate = ['he', 'mean', 'tef']

# 计算list的长度
a = len(classmate)
print(a)

# 获取list某个索引的值
print(classmate[0])

# list追加元素到末尾
classmate.append('zh')
print(classmate)

# list把元素插入到指定位置
classmate.insert(1, 'Jack')
print(classmate)

# list删除末尾元素
classmate.pop()
print(classmate)

# list删除指定位置元素 用pop(i)方法 i是元素的索引位置
classmate.pop(0)
print(classmate)

# list把某个元素替换成别的元素，可以直接赋值给索引的位置
classmate[2] = 'tefs'
print(classmate)

# list里面的元素数据类型也可以不同
L = ['python', 123, True]
print(L)

# list里的元素也可以是另外一个list
O = ['python', ['最好的编程语言', 'php'], 'c#']
# 注意O只有3个元素 O[1] 是另外一个list 要拿到php值可以这样写 O[1][1]
# 因此可以看成一个二维数组，类似的还有三维，四维...,不过很少用到
print(len(O))
print(O)

# list中一个元素都没有那么它的长度为0是一个空的list
G = []
print(len(G))

# __________________tuple的学习__________________

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改

# 定义一个tuple
classmate2 = ('Ben', 'Jon', 'Kitty')
print(classmate2)

# 如果要定义一个空的tuple,可以写成(),但是定义一个元素的时候一定要(x, )这样定义为了消除歧义
kong = ()
print(kong)

# 定一个 “可变的” tuple 不是说tuple不可以变的嘛，没错tuple不可以变但是list可以变，把tuple里的元素定义成list就可以变啦但是记住变的是list不是tuple

bian = ('a', 'b', ['A', 'b'], 'c')
print(bian)
bian[2][0] = 'C'
bian[2][1] = 'D'
print(bian)

