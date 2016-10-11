# dict学习

# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

# 创建一个dict
d = {'M': 100, 'h': 50, 't': 60}
print(d['M'])

# 把数据放入dict的方法，除了初始化时指定外，还可以通过key放入
d['S'] = '我新放入的VALUE'
print(d)

# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
d['M'] = '200'
print(d)

# 如果key不存在，dict就会报错
# print(d['abc']) 因为没有abc这个key所以这里是会报错的

# 要避免key不存在的错误，有两种办法，一是通过in判断key是否存在
print('abc' in d)
# false

# 二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value
print(d.get('abc'))
print(d.get('abc', -1))

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('S')
print(d)

# 要注意的是，dict内部存放的顺序和key放入的顺序是没有关系的

# 和list比较，dict有以下几个特点：
# 1.查找和插入的速度极快，不会随着key的增加而变慢；
# 2.需要占用大量的内存，内存浪费多。
# 而list相反：
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。




