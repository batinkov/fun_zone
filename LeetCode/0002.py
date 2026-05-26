#!/usr/bin/env python

#   2. Add Two Numbers
#   
#   You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#   
#   You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#   
#   Example 1:
#   Input: l1 = [2,4,3], l2 = [5,6,4]
#   Output: [7,0,8]
#   Explanation: 342 + 465 = 807.
#   
#   Example 2:
#   Input: l1 = [0], l2 = [0]
#   Output: [0]
#   
#   Example 3:
#   Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
#   Output: [8,9,9,9,0,0,0,1]
#   
#   Constraints:
#   The number of nodes in each linked list is in the range [1, 100].
#   0 <= Node.val <= 9
#   It is guaranteed that the list represents a number that does not have leading zeros.


from dataclasses import dataclass

@dataclass
class ListNode:
    val: int
    next: ListNode | None = None

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = l1, l2
        curr, carry = 0, 0
        result = ListNode(0)  # sentinel; real head is result.next
        tail = result

        # `or carry` keeps the loop alive for the trailing overflow digit
        # (e.g. 999 + 1 → 1000, where the result is longer than either input)
        while n1 or n2 or carry:
            if n1:
                curr += n1.val
                n1 = n1.next
            if n2:
                curr += n2.val
                n2 = n2.next
            if carry:
                curr += carry

            tail.next = ListNode(curr % 10)
            tail = tail.next

            carry = curr // 10
            curr = 0

        return result.next


    def toNumber(self, head: Optional[ListNode]) -> int:
        counter = 1
        res = 0

        while head:
            res += counter * head.val
            counter *= 10

            head = head.next

        return res


if __name__ == '__main__':
    tests = (
        (ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4))), 807),
        (ListNode(0), ListNode(0), 0),
        (
            ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
            ListNode(9, ListNode(9, ListNode(9, ListNode(9)))),
            10009998
        )
    )

    sol = Solution()
    for test in tests:
        l1, l2, expected = test
        res = sol.addTwoNumbers(l1, l2)
        number = sol.toNumber(res)
        assert number == expected, f'Expected {expected} but got {number} for {l1} + {l2}'
    print('All tests passed')

