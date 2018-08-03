def bubbleSort(nums):
    for i in range(len(nums)-1):     # 循环排序次数（第一个数不排，所以减一次）
        for j in range(len(nums)-1-i):   # 比较次数(循环排序次数i越大，比较次数越小)
            if nums[j] > nums[j+1]:      # 如果大于后一个数
                nums[j], nums[j+1] = nums[j+1], nums[j]  # 交换位置
    return nums

nums = [0, -3, -5, 15, 99, 8]
print(bubbleSort(nums))
