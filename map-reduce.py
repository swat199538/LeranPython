# python内建函数map学习
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
L = [a for a in range(1, 11)]


def function(x):
    return x*x

r = map(function, L)
print(list(r))

print(list(map(str, [a for a in range(1, 11)])))

