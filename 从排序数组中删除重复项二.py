"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
"""


class Solution:
    def removeDuplicates(self, nums):
        if len(nums) < 3:
            return len(nums)
        index = 2
        k = 0
        for i in range(2, len(nums)):
            if nums[index-2] != nums[i]:
                if i != k:
                    nums[index] = nums[i]
                    k += 1
                    index += 1
        return index

nums = [1, 1, 1, 2, 3, 3, 3, 3]
s = Solution()
print(s.removeDuplicates(nums))