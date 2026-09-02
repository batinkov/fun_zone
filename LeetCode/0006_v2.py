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
        if numRows <= 1: # chars_per_section would be 0 or negative below
            return s

        chars_per_section = 2*numRows - 2

        # every full section fills exactly numRows-1 columns; a leftover of `rem`
        # characters needs one column while it is still descending, plus one more
        # for each step back up
        full, rem = divmod(len(s), chars_per_section)
        cols = full * (numRows - 1)
        if rem:
            cols += 1 if rem <= numRows else 1 + rem - numRows

        # None rather than a sentinel character: no input character can collide with it
        matrix = [[None]*cols for _ in range(numRows)]

        row, col = 0, 0
        going_down = True
        for ch in s:
            matrix[row][col] = ch

            # write first, then decide where the cursor goes: going down stays in
            # the same column, coming back up moves one column to the right
            if going_down:
                if row == numRows - 1:
                    going_down = False
                    row, col = row - 1, col + 1
                else:
                    row += 1
            else:
                if row == 0:
                    going_down = True
                    row += 1
                else:
                    row, col = row - 1, col + 1

        return ''.join(ch for matrix_row in matrix for ch in matrix_row if ch is not None)


if __name__ == '__main__':
    tests = (
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
        ("PAYPALISHIRING", 2, "PYAIHRNAPLSIIG"), # numRows == 2: the walk reverses on every character
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
