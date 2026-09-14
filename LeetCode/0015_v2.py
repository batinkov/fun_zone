#!/usr/bin/env python3

#   15. 3Sum
#
#   Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and
#   j != k, and nums[i] + nums[j] + nums[k] == 0.
#
#   Notice that the solution set must not contain duplicate triplets.
#
#   Example 1:
#   Input: nums = [-1, 0, 1, 2, -1, -4]
#   Output: [[-1, -1, 2], [-1, 0, 1]]
#   Explanation:
#   nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
#   nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
#   nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
#   The distinct triplets are [-1, 0, 1] and [-1, -1, 2]. Notice that the order of the output and the order of the
#   triplets does not matter.
#
#   Example 2:
#   Input: nums = [0, 1, 1]
#   Output: []
#   Explanation: The only possible triplet does not sum up to 0.
#
#   Example 3:
#   Input: nums = [0, 0, 0]
#   Output: [[0, 0, 0]]
#   Explanation: The only possible triplet sums up to 0.
#
#   Constraints:
#       3 <= nums.length <= 3000
#       -10^5 <= nums[i] <= 10^5

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        result = []

        for i in range(len(nums) - 2):
            if nums[i] > 0: # sorted: nothing from here on can bring the sum back to 0
                break
            if i and nums[i] == nums[i-1]: # same anchor value as last time
                continue

            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]
                if total < 0:
                    lo += 1
                elif total > 0:
                    hi -= 1
                else:
                    result.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    while lo < hi and nums[lo] == nums[lo-1]: # skip repeats of the middle value
                        lo += 1

        return result


if __name__ == '__main__':
    tests = (
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([0, 0, 1], []),                            # two zeros are not enough for [0, 0, 0]
        ([5, -1, 0, 1], [[-1, 0, 1]]),              # the triplet does not involve index 0
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([0, 0, 0, 0], [[0, 0, 0]]),                # duplicates must collapse to one triplet
    )
    sol = Solution()

    def canon(triplets): # the order of the output and of each triplet does not matter
        return sorted(tuple(sorted(t)) for t in triplets)

    for test in tests:
        result = sol.threeSum(test[0])
        assert canon(result) == canon(test[1]), f'Expected {test[1]}, got {result} instead'
    print('All tests PASSED')
