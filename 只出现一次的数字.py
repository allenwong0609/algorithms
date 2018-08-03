"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
"""


class Solution:
    def x(self, nums):
        dict1 = {}
        for i in nums:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        print(dict1)
        list1 = []
        for j in dict1:
            if dict1[j] == 1:
                list1.append(j)
        return list1


s = Solution()
print(s.x(nums=[2, 1, 2, 2, 3]))