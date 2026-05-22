#!/usr/bin/env python3

#   141. Linked List Cycle
#   
#   Given head, the head of a linked list, determine if the linked list has a cycle in it.
#   
#   There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
#   
#   Return true if there is a cycle in the linked list. Otherwise, return false.
#   
#   Example 1:
#   Input: head = [3,2,0,-4], pos = 1
#   Note: -4 points to 2
#   Output: true
#   Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
#   
#   Example 2:
#   Input: head = [1,2], pos = 0
#   Note: 2 points to 1
#   Output: true
#   Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
#   
#   Example 3:
#   Input: head = [1], pos = -1
#   Output: false
#   Explanation: There is no cycle in the linked list.
#   
#   Constraints:
#   
#   The number of the nodes in the list is in the range [0, 104].
#   -105 <= Node.val <= 105
#   pos is -1 or a valid index in the linked-list.
#    
#   Follow up: Can you solve it using O(1) (i.e. constant) memory?


from dataclasses import dataclass

# Definition for singly-linked list.
@dataclass
class ListNode:
    val: int
    next: ListNode | None = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                return True

        return False


if __name__ == '__main__':
    loop1 = ListNode(0)
    head1 = ListNode(1, ListNode(2, loop1))
    tail1 = ListNode(3, ListNode(4, ListNode(5, loop1)))
    loop1.next = tail1

    loop2 = ListNode(-4)
    head2 = ListNode(3, ListNode(2, ListNode(0, loop2)))
    loop2.next = head2.next

    head3 = ListNode(1, ListNode(2))
    head3.next.next = head3

    tests = (
        (head1, True),
        (ListNode(0, ListNode(1, ListNode(2, ListNode(3)))), False),
        (ListNode(0, ListNode(1, ListNode(1, ListNode(1, ListNode(1))))), False),
        (head2, True),
        (head3, True),
        (ListNode(1), False),
    )

    sol = Solution()
    for test in tests:
        assert sol.hasCycle(test[0]) == test[1], f'Loop detected in {test[0]}'
    print('All tests passed')

