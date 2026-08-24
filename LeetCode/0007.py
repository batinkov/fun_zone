#!/usr/bin/env python3

#   7. Reverse Integer
#
#   Given a signed 32 - bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range[-231, 231 - 1], then return 0.
#
#   Assume the environment does not allow you to store 64 - bit integers(signed or unsigned).
#
#   Example 1:
#   Input: x = 123
#   Output: 321
#
#   Example 2:
#   Input: x = -123
#   Output: -321
#
#   Example 3:
#   Input: x = 120
#   Output: 21
#
#   Constraints:
#   -231 <= x <= 231 - 1


class Solution:
    def reverse(self, x: int) -> int:
        x_negative = True if x < 0 else False
        if x_negative:
            x = -x

        # a negative result may reach a magnitude one larger than a positive one
        limit = 2**31 if x_negative else 2**31 - 1
        reverse = 0

        while x > 0:
            last_digit = x % 10
            x = x // 10

            # check before multiplying, so reverse never grows past 32 bits
            if reverse > (limit - last_digit) // 10:
                return 0

            reverse = 10*reverse + last_digit

        reverse = -reverse if x_negative else reverse

        return reverse


if __name__ == '__main__':
    tests = (
        (123, 321),
        (-123, -321),
        (120, 21),
        (1534236469, 0),
        (1563847412, 0),
    )
    sol = Solution()

    for test in tests:
        result = sol.reverse(test[0])
        assert result == test[1], f'Expected {test[1]}, got {result} instead'
    print('All tests PASSED')
