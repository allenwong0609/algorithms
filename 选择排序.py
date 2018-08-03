def selectionSort(nums):
    for i in range(len(nums)-1):    # 遍历数组
        min = i      # 视为最小值坐标
        for j in range(i+1, len(nums)):  # 遍历i后面的数
            if nums[j] < nums[min]:      # 如果小于i，更新最小值坐标
                min = j
        nums[i], nums[min] = nums[min], nums[i]  # 交换位置，最小值在左边
    return nums

nums = [0, -3, -5, 15, 99, 8]
print(selectionSort(nums))
