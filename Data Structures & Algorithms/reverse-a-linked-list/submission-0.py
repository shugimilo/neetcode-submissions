# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            print(f"Appending {head}, {head.val} to stack")
            stack.append(head)
            head = head.next

        print(f"Stack at the end of the first loop: {stack}")

        dummy = ListNode()
        current = dummy

        while stack:
            print(f"current.next = {stack[-1]}")
            current.next = stack[-1]
            stack.pop()
            current = current.next

        current.next = None

        return dummy.next