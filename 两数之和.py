"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
"""


class Solution:
    def x(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target:
                    return nums[i], nums[j]


s = Solution()
print(s.x([2, 7, 11, 15], 9))