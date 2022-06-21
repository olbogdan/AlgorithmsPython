# Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.
#
# Return the shortest such subarray and output its length.
from collections import deque

def findUnsortedSubarray(nums: [int]) -> int:
    increasing = deque()
    decreasing = deque()

    increasing.append(nums[0])
    for i in range(1, len(nums)):
        if nums[i - 1] <= nums[i]:
            increasing.append(nums[i])
        else:
            break
    decreasing.append(nums[len(nums)-1])
    for i in range(len(nums) - 1, 0, -1):
        if nums[i - 1] <= nums[i]:
            decreasing.append(nums[i - 1])
        else:
            break

    if len(increasing) == len(nums) and len(decreasing) == len(nums):
        return 0

    while len(increasing) > 0 and len(decreasing) > 0 and increasing[-1] > decreasing[-1]:
        increasing.pop()

    beginUnsorted = len(increasing)
    endUnsorted = len(nums) - len(decreasing)
    unsortedSub = nums[beginUnsorted:endUnsorted]
    maxUnsortedValue = max(unsortedSub)
    minUnsortedValue = min(unsortedSub)
    while increasing and increasing[-1] > minUnsortedValue:
        increasing.pop()
    while decreasing and decreasing[-1] < maxUnsortedValue:
        decreasing.pop()
    res = len(nums) - len(increasing) - len(decreasing)
    return res

assert findUnsortedSubarray([2,3,4]) == 0
assert findUnsortedSubarray([5,2,3,4]) == 4
assert findUnsortedSubarray([2,6,4,8,10,9,15]) == 5
assert findUnsortedSubarray([1,1,1,1,1,1,1]) == 0
assert findUnsortedSubarray([1,3,1,1,1,1,1]) == 6
assert findUnsortedSubarray([3,2,3,2,4]) == 4
assert findUnsortedSubarray([2,6,4,8,10,9,15]) == 5