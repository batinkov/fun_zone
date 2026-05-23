#!/usr/bin/env python3

#   142. Linked List Cycle II
#   
#   Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
#   
#   There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.
#   
#   Do not modify the linked list.
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
#       The number of the nodes in the list is in the range [0, 104].
#       -105 <= Node.val <= 105
#       pos is -1 or a valid index in the linked-list.
#   
#   Follow up: Can you solve it using O(1) (i.e. constant) memory?



from dataclasses import dataclass

# Definition for singly-linked list.
@dataclass
class ListNode:
    val: int
    next: ListNode | None = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                break
        else:
            return None

        aux = head

        while aux is not slow:
            slow = slow.next
            aux = aux.next

        return aux


if __name__ == '__main__':
    loop1 = ListNode(0)
    head1 = ListNode(1, ListNode(2, loop1))
    tail1 = ListNode(3, ListNode(4, ListNode(5, loop1)))
    loop1.next = tail1

    tail2 = ListNode(-4)
    head2 = ListNode(3, ListNode(2, ListNode(0, tail2)))
    loop2 = head2.next
    tail2.next = loop2

    head3 = ListNode(1, ListNode(2))
    head3.next.next = head3

    tests = (
        (head1, loop1),
        (ListNode(0, ListNode(1, ListNode(2, ListNode(3)))), None),
        (ListNode(0, ListNode(1, ListNode(1, ListNode(1, ListNode(1))))), None),
        (head2, loop2),
        (head3, head3),
        (ListNode(1), None),
    )

    sol = Solution()
    for test in tests:
        assert sol.detectCycle(test[0]) == test[1], f'Loop detected in {test[0]}'
    print('All tests passed')

