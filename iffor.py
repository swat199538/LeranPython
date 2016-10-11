# 条件判断
height = 1.75
width = 80.5
BIM = width/(height*height)
if BIM < 18.5:
    print("过轻")
elif BIM <= 25:
    print("正常")
elif BIM <= 28:
    print("过重")
elif BIM <= 32:
    print("肥胖")
elif BIM > 32:
    print("严重肥胖")

# for...in 循环
names = ['M', 'C', 'D', 'A', 'W', 'X']
for name in names:
    print(name)

# while 循环

# 循环100次
n = 99
while n > 0:
    print(n)
    n -= 1


L = ['Ben', 'Kitty', 'Aide', 'Alice']
for name in L:
    xx = 'hello,%s' % (name,)
    print(xx)

for x in range(2):
    print('ahh')
