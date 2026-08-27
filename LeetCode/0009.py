#!/usr/bin/env python3


#   9. Palindrome Number
#
#   Given an integer x, return true if x is a, and false otherwise.
#
#   Example 1:
#   Input: x = 121
#   Output: true
#   Explanation: 121 reads as 121 from left to right and from right to left.
#
#   Example 2:
#    Input: x = -121
#   Output: false
#   Explanation: From left to right, it reads - 121. From right to left, it becomes 121 -. Therefore it is not a palindrome.
#
#   Example 3:
#   Input: x = 10
#   Output: false
#   Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
#   Constraints:
#   -231 <= x <= 231 - 1
#
#   Follow up: Could you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        result = []
        while x > 0:
            remainder = x % 10
            result.append(remainder)
            x //= 10

        for i in range(len(result)//2):
            if result[i] != result[-(i+1)]:
                return False

        return True


if __name__ == '__main__':
    tests = (
        (121, True),
        (-121, False),
        (10, False),
        (0, True),
        (7, True),
    )
    sol = Solution()

    for test in tests:
        result = sol.isPalindrome(test[0])
        assert result == test[1], f'Expected {test[1]}, got {result} instead'
    print('All tests PASSED')

