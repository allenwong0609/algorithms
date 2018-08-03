"""
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
"""


class Solution:
    def x(self, nums):
        list1 = []
        k = 0
        for i in nums:
            if i in list1:
                k += 1
            list1.append(i)
        if k == 0:
            return False
        else:
            return True

s = Solution()
print(s.x(nums=[1, 2, 3, 1]))

