"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。
输入: [1,2,3,4,5,6,7] 和 k = 3
输出: [5,6,7,1,2,3,4]
"""


class Solution:
    def rotate(self, nums, k):
        list1 = nums[(len(nums)-k):] + nums[:-k]
        print(list1)


nums = [1, 2, 3, 4, 5, 6, 7]
s = Solution()
s.rotate(nums, 3)