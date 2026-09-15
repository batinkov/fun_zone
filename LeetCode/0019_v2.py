#!/usr/bin/env python3

#   19. Remove Nth Node From End of List
#
#   Given the head of a linked list, remove the nth node from the end of the list and return its head.
#
#   Example 1:
#   Input: head = [1, 2, 3, 4, 5], n = 2
#   Output: [1, 2, 3, 5]
#
#   Example 2:
#   Input: head = [1], n = 1
#   Output: []
#
#   Example 3:
#   Input: head = [1, 2], n = 1
#   Output: [1]
#
#   Constraints:
#       The number of nodes in the list is sz.
#       1 <= sz <= 30
#       0 <= Node.val <= 100
#       1 <= n <= sz
#
#   Follow up: Could you do this in one pass?
#

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def lists_equal(a: ListNode | None, b: ListNode | None) -> bool:
    # walk both lists in step; iterative, so long lists cannot hit the recursion limit
    while a is not None and b is not None:
        if a.val != b.val:
            return False
        a, b = a.next, b.next

    # equal only if both ran out together; a leftover node means the lengths differ
    return a is None and b is None


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        # a dummy node in front of head makes removing the head the same operation
        # as removing any other node, so no special case is needed
        dummy = ListNode(0, head)
        first = second = dummy

        for _ in range(n + 1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next


if __name__ == '__main__':
    def build_list(values: list[int]) -> ListNode | None:
        head = None
        for value in reversed(values):
            head = ListNode(value, head)
        return head

    tests = (
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),  2, ListNode(1, ListNode(2, ListNode(3, ListNode(5))))),
        (ListNode(1), 1, None),
        (ListNode(1, ListNode(2)), 1, ListNode(1)),
        (ListNode(1, ListNode(2)), 2, ListNode(2)),
        (build_list([1, 2, 3]), 3, build_list([2, 3])),                      # remove the head of a longer list
        (build_list([1, 2, 3]), 1, build_list([1, 2])),                      # remove the tail of a longer list
        (build_list(list(range(30))), 30, build_list(list(range(1, 30)))),   # maximum size: remove the head
        (build_list(list(range(30))), 1, build_list(list(range(29)))),       # maximum size: remove the tail
    )
    sol = Solution()

    for test in tests:
        result = sol.removeNthFromEnd(test[0], test[1])
        assert lists_equal(result, test[2]), f'Expected {test[2]}, got {result} instead'
    print('All tests PASSED')
