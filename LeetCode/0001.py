#!/usr/bin/env python3

#   1. Two Sum
#   
#   Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#   You may assume that each input would have exactly one solution, and you may not use the same element twice.
#   You can return the answer in any order.
#   
#   Example 1:
#   Input: nums = [2,7,11,15], target = 9
#   Output: [0,1]
#   Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#   
#   Example 2:
#   Input: nums = [3,2,4], target = 6
#   Output: [1,2]
#   
#   Example 3:
#   Input: nums = [3,3], target = 6
#   Output: [0,1]
#   
#   Constraints:
#       2 <= nums.length <= 104
#       -109 <= nums[i] <= 109
#       -109 <= target <= 109
#       Only one valid answer exists.


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}

        for i in range(len(nums)):
            current = nums[i]
            needed = target - current

            if needed in num_to_index.keys():
                needed_index = num_to_index[needed]
                return [i, needed_index]
            else:
                num_to_index[current] = i

        return []


if __name__ == '__main__':
    tests = (
        {'nums': [2,7,11,15], 'target': 9, 'expected': [0,1]},
        {'nums': [3,2,4], 'target': 6, 'expected': [1,2]},
        {'nums': [3,3], 'target': 6, 'expected': [0,1]},
    )

    sol = Solution()
    for test in tests:
        nums, target = test['nums'], test['target']
        res = sol.twoSum(nums, target)

        result = None
        if len(res) == 2:
            result = nums[res[0]] + nums[res[1]]

        assert result == target, f'Expected {test["expected"]} but got {res}'

    print('All tests passed')

