#!/usr/bin/env python3

#   3. Longest Substring Without Repeating Characters
#
#   Given a string s, find the length of the longest without duplicate characters.
#
#   Example 1:
#   Input: s = "abcabcbb"
#   Output: 3
#   Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
#

#   Example 2:
#   Input: s = "bbbbb"
#   Output: 1
#   Explanation: The answer is "b", with the length of 1.
#
#   Example 3:
#   Input: s = "pwwkew"
#   Output: 3
#   Explanation: The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence #   and not a substring.
#
#   Constraints:
#    0 <= s.length <= 10^5
#    s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        second_index = 0
        max_substring_len = 0

        for ch in s:
            if ch in chars:
                while s[second_index] != ch:
                    chars.remove(s[second_index])
                    second_index += 1
                second_index += 1
            else:
                chars.add(ch)

            max_substring_len = max(max_substring_len, len(chars))

        return max_substring_len


if __name__ == '__main__':
    tests = (
        ("", 0),
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("1R1T7", 4),
        ("abba", 2),         # the duplicate's earlier position is behind second_index
        ("dvdf", 3),         # same, with the answer starting after the shrink
        ("tmmzuxt", 5),      # answer spans a region the window shrank through earlier
        ("abcdefg", 7),      # all unique: the answer runs to the end of the string
        (" ", 1),            # constraints allow spaces
        ("a b c", 3),        # ...including spaces inside the answer
    )

    sol = Solution()
    for test in tests:
        input_str, expected = test
        result = sol.lengthOfLongestSubstring(input_str)
        assert result == expected, f'Expected {expected} but got {result} for {input_str}'
    print('All tests passed')
