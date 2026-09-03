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


# brute force over every pair of lines: correct, but quadratic. at the constraint's
# n = 10^5 that is roughly 11 minutes; see 0011_v2.py for the O(n) two-pointer scan.
class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0

        for begin in range(0, len(height)-1):
            for end in range(begin+1, len(height)): # begin+1: a container needs two distinct lines
                area = (end-begin) * min(height[begin], height[end])
                max_area = max(area, max_area)

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
    )
    sol = Solution()

    for test in tests:
        result = sol.maxArea(test[0])
        assert result == test[1], f'Expected {test[1]}, got {result} instead'
    print('All tests PASSED')
