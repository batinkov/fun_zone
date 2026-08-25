#!/usr/bin/env python3

#   14. Longest Common Prefix
#
#   Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
#
#   Example 1:
#   Input: strs = ["flower", "flow", "flight"]
#   Output: "fl"
#
#   Example 2:
#   Input: strs = ["dog", "racecar", "car"]
#   Output: ""
#   Explanation: There is no common prefix among the input strings.
#
#   Constraints:
#   1 <= strs.length <= 200
#   0 <= strs[i].length <= 200
#   strs[i] consists of only lowercase English letters if it is non-empty.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:  # min() below would raise ValueError on an empty list
            return ''

        max_prefix_len = min(len(s) for s in strs)

        for i in range(max_prefix_len):
            for n in range(len(strs)):
                if strs[0][i] != strs[n][i]:
                    return strs[0][:i]

        return strs[0][:max_prefix_len]


if __name__ == '__main__':
    tests = (
        ([], ""),                              # outside the constraints; guards the ValueError
        (["abc"], "abc"),
        (["abc", "abc"], "abc"),               # full match: the only case that runs the loop to the end
        (["abc", "ab"], "ab"),                 # shortest string is the answer, and it is not strs[0]
        (["", "abc"], ""),                     # empty string in the list
        (["a", "b"], ""),                      # mismatch at the very first character
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
    )
    sol = Solution()

    for test in tests:
        result = sol.longestCommonPrefix(test[0])
        assert result == test[1], f'Expected {test[1]}, got {result} instead'
    print('All tests PASSED')
