# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        if head and head.next:
            nxt = head.next
            if nxt.next:
                fast = nxt.next
            else:
                return False
        else:
            return False

        while fast:
            if slow == fast:
                return True
            slow = slow.next
            if fast.next:
                nxt = fast.next
                if nxt.next:
                    fast = nxt.next
                else:
                    return False
            else:
                return False
