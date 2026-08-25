#!/usr/bin/env python3

#   8. String to Integer (atoi)
#
#   Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.
#
#   The algorithm for myAtoi(string s) is as follows:
#
#       Whitespace: Ignore any leading whitespace (" ").
#       Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
#       Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
#       Rounding: If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], then round the integer to remain in the range. Specifically, integers less than -2^31 should be rounded to -2^31, and integers greater than 2^31 - 1 should be rounded to 2^31 - 1.
#
#   Return the integer as the final result.
#
#   Constraints:
#       0 <= s.length <= 200
#       s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-' and '.'.


INT_MIN = -(2**31)
INT_MAX = 2**31 - 1


class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        is_negative = False

        # ignore spaces in the beginning; the spec counts only ' ' as whitespace,
        # so isspace() would be too broad (it also eats '\t', '\n', '\xa0', ...)
        while i < len(s) and s[i] == ' ':
            i += 1

        # check the sign '+' or '-' or none
        if i < len(s) and s[i] in ('+', '-'):
            is_negative = s[i] == '-'
            i += 1

        # leading zeroes need no special handling: 10*0 + 0 is still 0.
        # the range test must stay ASCII-only to match the ord() arithmetic below,
        # as isdigit() is also true for '٣', '²', '１' and friends
        result = 0
        while i < len(s) and '0' <= s[i] <= '9':
            result = result*10 + (ord(s[i]) - ord('0'))
            i += 1

        # apply the sign
        result = -result if is_negative else result

        # round the result into the 32-bit signed range
        return max(INT_MIN, min(INT_MAX, result))


if __name__ == '__main__':
    tests = (
        ('', 0),
        ('42', 42),
        ('   42', 42),                        # leading whitespace
        ('   -42', -42),                      # leading whitespace and a sign
        ('-042', -42),
        ('  0000000000012345678', 12345678),  # whitespace and leading zeroes together
        ('3.14', 3),
        ('1337c0d3', 1337),
        ('0-1', 0),
        ('-0', 0),
        ('words and 987', 0),
        ('+-12', 0),
        ('  +  413', 0),                      # space after the sign ends the number
        ('+', 0),
        ('-', 0),
        ('2147483647', 2147483647),           # exactly INT_MAX
        ('2147483648', 2147483647),           # one past INT_MAX
        ('-2147483648', -2147483648),         # exactly INT_MIN
        ('-2147483649', -2147483648),         # one past INT_MIN
        ('21474836460', 2147483647),
        ('-21474836460', -2147483648),
        ('000000000000000000', 0),
        (' ', 0),
    )
    sol = Solution()

    for test in tests:
        result = sol.myAtoi(test[0])
        assert result == test[1], f'Expected {test[1]}, got {result} instead'
    print('All tests PASSED')
