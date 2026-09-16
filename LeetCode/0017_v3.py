#!/usr/bin/env python3

#   17. Letter Combinations of a Phone Number
#
#   Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could
#   represent. Return the answer in any order.
#
#   A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#   1       2(abc) 3(def)
#   4(ghi)  5(jkl) 6(mno)
#   7(pqrs) 8(tuv) 9(wxyz)
#   *       0      #
#
#   Example 1:
#   Input: digits = "23"
#   Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
#
#   Example 2:
#   Input: digits = "2"
#   Output: ["a", "b", "c"]
#
#   Constraints:
#       1 <= digits.length <= 4
#       digits[i] is a digit in the range ['2', '9'].

MAPPING = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # each result index is read as a mixed-radix number: one "digit" per position,
        # with base len(letters) for that key. that makes any single combination
        # computable straight from its index, without building the others
        total = 1
        for digit in digits:
            total *= len(MAPPING[digit])
        results = ['' for _ in range(total)]

        weight = total # how many consecutive results share the same letter at this position
        for digit in digits:
            letters = MAPPING[digit]
            weight //= len(letters)

            for i in range(total):
                letter_index = (i // weight) % len(letters)
                results[i] += letters[letter_index]

        return results


if __name__ == '__main__':
    from itertools import product

    tests = (
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("2", ["a", "b", "c"]),
        ("7", ["p", "q", "r", "s"]),                          # four-letter key
        ("9", ["w", "x", "y", "z"]),                          # the other four-letter key
        ("22", ["aa", "ab", "ac", "ba", "bb", "bc", "ca", "cb", "cc"]),  # repeated digit
        ("79", ["pw", "px", "py", "pz", "qw", "qx", "qy", "qz",
                "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"]),
        ("7777", [''.join(p) for p in product('pqrs', repeat=4)]),  # largest output: 256 combinations
    )
    sol = Solution()

    for test in tests:
        result = sol.letterCombinations(test[0])
        # the list may come in any order, but the letters inside each combination may not
        assert sorted(result) == sorted(test[1]), f'Expected {test[1]}, got {result} instead'
    print('All tests PASSED')
