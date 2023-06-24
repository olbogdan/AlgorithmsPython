package leetcode.medium
/*Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Note that:

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).


Example 1:

Input: nums = [3,6,9,12]
Output: 4
Explanation:  The whole array is an arithmetic sequence with steps of length = 3.
Example 2:

Input: nums = [9,4,7,2,10]
Output: 3
Explanation:  The longest arithmetic subsequence is [4,7,10].
Example 3:

Input: nums = [20,1,15,3,10,5,8]
Output: 4
Explanation:  The longest arithmetic subsequence is [20,15,10,5].


Constraints:

2 <= nums.length <= 1000
0 <= nums[i] <= 500
*/
class `1027 Longest Arithmetic Subsequence` {
    fun longestArithSeqLength(nums: IntArray): Int {
        val dp = mutableMapOf<Int, MutableMap<Int, Int>>()
        val n = nums.size
        var result = 1

        for (i in 0 until n) {
            val repsMap = mutableMapOf<Int, Int>()

            for (j in 0 until i) {
                val diff = nums[j] - nums[i]
                var reps = 1

                if (dp.containsKey(j) && dp[j]!!.containsKey(diff)) {
                    reps += dp[j]!![diff]!!
                }

                repsMap[diff] = reps
                result = maxOf(result, repsMap[diff]!!)
            }

            dp[i] = repsMap.toMutableMap()
        }

        return result + 1
    }
}