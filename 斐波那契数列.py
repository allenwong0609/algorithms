# 斐波那契数列特点：该数列从第三项开始，每个数的值为其前两个数之和
# 单独显示第几项


def x(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return x(n-1) + x(n-2)

# 列表方式显示多项
lis = []
a = int(input("显示的项数："))
for i in range(a):
    if i == 0 or i == 1:  # 第1,2项 都为1
        lis.append(1)
    else:
        lis.append(lis[i-2]+lis[i-1])  # 从第3项开始每项值为前两项值之和
print(lis)