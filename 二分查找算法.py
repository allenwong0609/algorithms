
def binarySearch(nums, target):
    first = 0
    last = len(nums) - 1
    while first <= last:
        mid = (first + last)//2
        print(mid)
        if nums[mid] > target:
            last = mid - 1
        elif nums[mid] < target:
            first = mid + 1
        else:
            return mid + 1
    return -1

nums = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(nums, 8))