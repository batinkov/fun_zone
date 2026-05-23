#!/usr/bin/env python3

#   876. Middle of the Linked List
#   
#   Given the head of a singly linked list, return the middle node of the linked list.
#   If there are two middle nodes, return the second middle node.
#   
#   Example 1:
#   Input: head = [1,2,3,4,5]
#   Output: [3,4,5]
#   Explanation: The middle node of the list is node 3.
#   
#   Example 2:
#   Input: head = [1,2,3,4,5,6]
#   Output: [4,5,6]
#   Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
#   
#   Constraints:
#   The number of nodes in the list is in the range [1, 100].
#   1 <= Node.val <= 100


from dataclasses import dataclass

@dataclass
class ListNode:
    val: int
    next: Node | None = None

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = head, head

        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next

        return p2


if __name__ == '__main__':
    tests = (
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 3),
        (ListNode(1, ListNode(2, ListNode(3, ListNode(4)))), 3),
        (ListNode(1), 1),
        (ListNode(1, ListNode(2)), 2),
        (None, None)
    )

    sol = Solution()
    for test in tests:
        res = sol.middleNode(test[0])
        val = res.val if res else res

        assert test[1] == val, f'expected {test[1]}, got {val} for {test[0]}'

    print('All tests passed')

