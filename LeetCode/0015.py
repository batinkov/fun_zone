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
        results = set()
        cache = set()
        cache.add(nums[0])

        for i in range(1, len(nums)):
            for j in range(i+1, len(nums)):
                target = -nums[i] - nums[j]

                if target in cache:
                    results.add(tuple(sorted([nums[i], nums[j], target])))

            cache.add(nums[i])

        return [list(t) for t in results]


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

    def canon(triplets): # the result comes from a set, so neither order is meaningful
        return sorted(tuple(sorted(t)) for t in triplets)

    for test in tests:
        result = sol.threeSum(test[0])
        assert canon(result) == canon(test[1]), f'Expected {test[1]}, got {result} instead'
    print('All tests PASSED')
