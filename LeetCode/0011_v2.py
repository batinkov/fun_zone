#!/usr/bin/env python3

#   11. Container With Most Water
#
#   You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of
#   the ith line are (i, 0) and (i, height[i]).
#
#   Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
#   Return the maximum amount of water a container can store.
#
#   Notice that you may not slant the container.
#
#   Example 1:
#   Input: height = [1,8,6,2,5,4,8,3,7]
#   Output: 49
#   Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of
#   water (blue section) the container can contain is 49.
#
#   Example 2:
#   Input: height = [1,1]
#   Output: 1
#
#   Constraints:
#       n == height.length
#       2 <= n <= 10^5
#       0 <= height[i] <= 10^4


class Solution:
    def maxArea(self, height: list[int]) -> int:
        # the area is capped by the shorter line, so moving the taller one inward only
        # loses width while staying under the same cap - it can never beat what is
        # already recorded. moving the shorter line is the only useful move. on a tie
        # either pointer may move: both inner candidates are capped by that same height
        # and are narrower, so neither can improve on the area just recorded.
        lo, hi = 0, len(height) - 1
        max_area = 0

        while lo < hi:
            max_area = max(max_area, (hi - lo) * min(height[lo], height[hi]))

            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1

        return max_area


if __name__ == '__main__':
    tests = (
        ([1,8,6,2,5,4,8,3,7], 49),
        ([1,1], 1),
        ([1,2,3,4,5], 6),       # strictly increasing: the best pair is not at the ends
        ([5,4,3,2,1], 6),       # strictly decreasing
        ([0,0], 0),             # zero heights are allowed by the constraints
        ([2,2,2,2], 6),         # all equal: the widest pair wins
        ([6,1,1,1,6], 24),      # tallest lines at both extremes
        ([1,0,0,0,1], 4),       # short lines far apart beat tall ones close together
        ([100,1], 1),           # the shorter line caps the area
        ([1]*10**5, 99999),     # the constraint's maximum n: width 99999 x height 1
        (list(range(1, 10**5 + 1)), 2500000000), # (99999-i)*(i+1), maximised at i=49999
    )
    sol = Solution()

    for test in tests:
        result = sol.maxArea(test[0])
        assert result == test[1], f'Expected {test[1]}, got {result} instead'
    print('All tests PASSED')
