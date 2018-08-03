"""
给出两个数组，求交集
"""


class Solution:
    def x(self, num1, num2):
        list1 = []
        if len(num1) >= len(num2):
            n1 = num1
            n2 = num2
        else:
            n1 = num2
            n2 = num1
        for i in n2:
            if i in n1:
                list1.append(i)
        return list1

num1 = [1, 2, 2, 3]
num2 = [2, 3, 4, 2]
s = Solution()
print(s.x(num1, num2))
