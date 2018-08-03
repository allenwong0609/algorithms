"""
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。
"""


class Solution:
    def removeDuplicates(self, nums):
        if len(nums) < 2:       # 长度至少为1
            return len(nums)
        index = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[index - 1]:   # 这个数大于前面一个数
                nums[index] = nums[i]       # 作为当前长度的最后一个数
                index += 1
        return index


# 非原地删除方法:
#
#
# class Solution:
#     def removeDuplicates(self, nums):
#         list1 = []
#         for i in nums:
#             if i not in list1:
#                 list1.append(i)
#         nums = list1
#         print(nums)
#         return len(nums)

nums = [0, 0, 1, 1, 2]
s = Solution()
print(s.removeDuplicates(nums))
