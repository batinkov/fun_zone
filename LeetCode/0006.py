#!/usr/bin/env python3

#   6. Zigzag Conversion
#
#   The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to
#   display this pattern in a fixed font for better legibility)
#
#   P   A   H   N
#   A P L S I I G
#   Y   I   R
#
#   And then read line by line: "PAHNAPLSIIGYIR"
#
#   Write the code that will take a string and make this conversion given a number of rows:
#    string convert(string s, int numRows);
#
#   Example 1:
#   Input: s = "PAYPALISHIRING", numRows = 3
#   Output: "PAHNAPLSIIGYIR"
#
#   Example 2:
#   Input: s = "PAYPALISHIRING", numRows = 4
#   Output: "PINALSIGYAHRPI"
#   Explanation:
#   P     I    N
#   A   L S  I G
#   Y A   H R
#   P     I
#
#   Example 3:
#   Input: s = "A", numRows = 1
#   Output: "A"
#
#   Constraints:
#       1 <= s.length <= 1000
#       s consists of English letters (lower-case and upper-case), ',' and '.'.
#       1 <= numRows <= 1000

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1: # cycle_len would be 0 below, and index % 0 raises
            return s

        rows = [[] for _ in range(numRows)]
        cycle_len = numRows*2 - 2

        for index, ch in enumerate(s):
            # where this character falls in one down-and-back-up cycle; the second
            # half of the cycle climbs back up, so it mirrors onto the first half
            offset = index % cycle_len
            row = offset if offset < numRows else cycle_len - offset

            rows[row].append(ch)

        return ''.join(''.join(row) for row in rows)


if __name__ == '__main__':
    tests = (
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
        ("PAYPALISHIRING", 2, "PYAIHRNAPLSIIG"), # numRows == 2: the mirroring branch never runs
        ("AB", 5, "AB"),                         # numRows > len(s): most rows stay empty
        ("A", 2, "A"),                           # single character, more than one row
        ("ab,.", 2, "a,b."),                     # ',' and '.' are allowed by the constraints
    )
    sol = Solution()

    for test in tests:
        result = sol.convert(test[0], test[1])
        expected = test[2]
        assert result == expected, f'Expected {expected}, got {result} instead for pair {test[0]} - {test[1]}'
    print('All tests PASSED')
