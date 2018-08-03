def insertSort(nums):
    for i in range(1, len(nums)):
        value = nums[i]
        index = i

        while index > 0 and value < nums[index-1]:
            nums[index] = nums[index-1]
            index -= 1
        nums[index] = value
    return nums
nums = [0, -3, -5, 15, 99, 8]
print(insertSort(nums))


