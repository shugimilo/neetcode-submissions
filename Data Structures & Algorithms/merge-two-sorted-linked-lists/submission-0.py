# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val >= list2.val:
                current.next = list2
                print(f"Adding node from list2: {list2.val}")
                print(f"Skipping list1 node: {list1.val}")
                list2 = list2.next
            else:
                current.next = list1
                print(f"Adding node from list1: {list1.val}")
                print(f"Skipping list2 node: {list2.val}")
                list1 = list1.next
            
            current = current.next

        if list1:
            print
            current.next = list1
            print("Appending rest of list1")

        if list2:
            current.next = list2
            print("Appending rest of list2")


        return dummy.next