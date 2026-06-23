# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        # Print original list
        # print("Original linked list:")
        # iNode = head
        # res = ''
        # while iNode:
        #     arrow = '->' if iNode.next else ''
        #     print(f"[{iNode.val}]", end=arrow)
        #     iNode = iNode.next

        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        
        return prev