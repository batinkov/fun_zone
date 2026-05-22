#!/usr/bin/env python3

#   206. Reverse Linked List
#   
#   Given the head of a singly linked list, reverse the list, and return the reversed list.
#   
#   Example 1:
#   Input: head = [1,2,3,4,5]
#   Output: [5,4,3,2,1]
#   
#   Example 2:
#   Input: head = [1,2]
#   Output: [2,1]
#   
#   Example 3:
#   Input: head = []
#   Output: []
#   
#   Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

from dataclasses import dataclass


# Definition for singly-linked list.
@dataclass
class ListNode:
    val: int = 0
    next: ListNode | None = None

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        while head:
            aux = head
            head = head.next
            aux.next = None

            stack.append(aux)

        if stack:
            head = stack[-1]
            tail = head

        while stack:
            aux = stack.pop()
            tail.next = aux
            tail = aux
            tail.next = None

        return head


if __name__ == '__main__':
    tests = (
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), [5, 4, 3, 2, 1]),
        (ListNode(1, ListNode(2)), [2, 1]),
        (None, None),
        (ListNode(1), [1])
    )

    sol = Solution()
    for (head, _) in tests:
        res = sol.reverseList(head)
        print(res)

