"""每次上一或者两级，求上n级有多少种方法"""

# f(n) = f(n-1) + f(n-2)


def up_step(n):
    a = 1
    b = 2
    for i in range(n-1):
        a, b = b, a+b
    return a

print(up_step(4))

"""每次上n级"""


# f(n) = f(n-1) + f(n-2) + ... + f(n-n)
# f(n-1) = f(n-2) + ... + f(n-n)
# 两式相减得: f(n)= 2*f(n-1)
def up_step_n(n):
    if n == 0 or n == 1:
        return 1
    else:
        return 2*up_step_n(n-1)

print(up_step_n(4))