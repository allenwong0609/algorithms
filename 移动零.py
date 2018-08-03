"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
说明:
必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""


class Solution:
    def x(self, nums):
        k = 0
        for i in range(len(nums)):
            if nums[i]:         # 元素不为0时是True，通过判断
                if i != k:      # 上一个数是0
                    nums[k], nums[i] = nums[i], nums[k]  # 与上一个0互换下标
                k += 1          # 第k个非0数
        return nums

nums1 = [0, 1, 0, 3, 12]
s = Solution()
print(s.x(nums1))
