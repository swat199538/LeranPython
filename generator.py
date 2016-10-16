# 在Python中，这种一边循环一边计算的机制，称为生成器：generator

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
L = [a for a in range(1, 11)]
print(L)
L2 = (a for a in range(1, 11))
print(L2)

# 如何取到generator的值?当然是迭代
for key in L2:
    print(key)

