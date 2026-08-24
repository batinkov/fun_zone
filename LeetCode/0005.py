#!/usr/bin/env python3

#   5. Longest Palindromic Substring
#   
#   Given a string s, return the longest in s.
#   
#   Example 1:
#   Input: s = "babad"
#   Output: "bab"
#   Explanation: "aba" is also a valid answer.
#   
#   Example 2:
#   Input: s = "cbbd"
#   Output: "bb"
#   
#   Constraints:
#       1 <= s.length <= 1000
#       s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        candidateLen = len(s)

        while True: # no need to check for condition, once the len becomes 1 this is already a palindrome
            begin = 0
            while (begin+candidateLen) <= len(s):
                candidate = s[begin:begin+candidateLen]
                if self.check_palindrome(candidate):
                    return candidate

                begin += 1

            candidateLen -= 1

        # return "" # this will never be reached so we don't need it

    @staticmethod
    def check_palindrome(s: str) -> bool:
        for i in range(0, (len(s)//2)):
            if s[i] != s[-i-1]:
                return False

        return True


if __name__ == '__main__':
    tests = (
        ('babad', 'bab'),
        ('cbbd', 'bb'),
    )
    sol = Solution()

    for test in tests:
        result = sol.longestPalindrome(test[0])
        assert result == test[1], f'Expected {test[1]}, got {result} instead'
    print('All tests PASSED')
