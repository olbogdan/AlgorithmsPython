# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.
#
#
#
# Example 1:
#
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        debt = 0
        for i in range(len(nums)-2, -1, -1):
            debt += 1
            if debt - nums[i] <= 0:
                debt = 0

        return debt == 0


sol = Solution()
res = sol.canJump([5,9,3,2,1,0,2,3,3,1,0,0])
assert res is True
res = sol.canJump([3,2,1,0,4])
assert res is False
