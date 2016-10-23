# 打印等腰三角形
d = 10
l = [' '*(2*d-1)]*d
for i in range(d):
    l[i] = list(l[i])
    x = i
    y = 0
    x = d - x - 1
    l[i][x] = "*"
    while y < i:
        x += 2
        l[i][x] = '*'
        y += 1
    l[i] = ''.join(l[i])
    print(l[i])

