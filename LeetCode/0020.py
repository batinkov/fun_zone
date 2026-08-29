#!/usr/bin/env python3

#   20. Valid Parentheses
#
#   Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
#   An input string is valid if:
#       1. Open brackets must be closed by the same type of brackets.
#       2. Open brackets must be closed in the correct order.
#       3. Every close bracket has a corresponding open bracket of the same type.
#
#   Example 1:
#   Input: s = "()"
#   Output: true
#
#   Example 2:
#   Input: s = "()[]{}"
#   Output: true
#
#   Example 3:
#   Input: s = "(]"
#   Output: false
#
#   Example 4:
#   Input: s = "([])"
#   Output: true
#
#   Example 5:
#   Input: s = "([)]"
#   Output: false
#
#   Constraints:
#     1 <= s.length <= 10^4
#     s consists of parentheses only '()[]{}'.


CLOSERS = {')': '(', ']': '[', '}': '{'}


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for ch in s:
            if ch not in CLOSERS: # '(' or '[' or '{'
                stack.append(ch)
            elif not stack or stack.pop() != CLOSERS[ch]:
                return False

        return not stack


if __name__ == '__main__':
    tests = (
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("([)]", False),
        ("{[]}", True),     # nesting deeper than one level
        (")", False),       # closer with nothing on the stack
        ("(", False),       # opener never closed
        ("((", False),      # several leftover openers
    )
    sol = Solution()

    for test in tests:
        result = sol.isValid(test[0])
        assert result == test[1], f'For input {test[0]}. Expected {test[1]}, got {result} instead'
    print('All tests PASSED')
