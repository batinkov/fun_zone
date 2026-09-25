#!/usr/bin/env python3

#   21. Merge Two Sorted Lists
#   
#   You are given the heads of two sorted linked lists list1 and list2.
#   
#   Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
#   
#   Return the head of the merged linked list.
#   
#   Example 1:
#   Input: list1 = [1,2,4], list2 = [1,3,4]
#   Output: [1,1,2,3,4,4]
#   
#   Example 2:
#   Input: list1 = [], list2 = []
#   Output: []
#   
#   Example 3:
#   Input: list1 = [], list2 = [0]
#   Output: [0]
#   
#   Constraints:
#       The number of nodes in both lists is in the range [0, 50].
#       -100 <= Node.val <= 100
#       Both list1 and list2 are sorted in non-decreasing order.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def from_list(values: list[int]) -> ListNode | None:
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head

def to_list(head: ListNode | None) -> list[int]:
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        result = ListNode()
        current = result

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next

        # whatever is left is already sorted and already linked, so attach it whole
        current.next = list1 or list2

        return result.next


if __name__ == '__main__':
    tests = (
        (ListNode(1,ListNode(2,ListNode(4))), ListNode(1,ListNode(3,ListNode(4))), ListNode(1,ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(4))))))),
        (None, None, None),
        (None, ListNode(0), ListNode(0)),
        (from_list([1, 2, 4]), None, from_list([1, 2, 4])),                     # the mirror of example 3
        (from_list([1, 2, 3]), from_list([4, 5, 6]),                            # disjoint: list1 drains first
         from_list([1, 2, 3, 4, 5, 6])),
        (from_list([1, 1, 1]), from_list([1, 1]), from_list([1, 1, 1, 1, 1])),  # every comparison is a tie
        (from_list([-100, -50]), from_list([-75, 0, 100]),                      # negative values
         from_list([-100, -75, -50, 0, 100])),
        (from_list(list(range(0, 100, 2))), from_list(list(range(1, 100, 2))),  # 50 nodes each: the size limit
         from_list(list(range(100)))),
    )
    sol = Solution()

    for test in tests:
        result = sol.mergeTwoLists(test[0], test[1])
        # the merge splices the input nodes into the result, so compare values, not objects
        assert to_list(result) == to_list(test[2]), f'Expected {to_list(test[2])}, got {to_list(result)} instead'
    print('All tests PASSED')
