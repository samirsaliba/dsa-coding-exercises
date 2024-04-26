# 2095. Delete the Middle Node of a Linked List
# You are given the head of a linked list. 
# Delete the middle node, and return the head of the modified linked list.

# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, 
# where ⌊x⌋ denotes the largest integer less than or equal to x.
# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return None

        hare_p = head
        tortoise_p = head

        while hare_p.next is not None:
            hare_p = hare_p.next.next
            previous = tortoise_p
            tortoise_p = tortoise_p.next
            if hare_p is None:
                break
        
        previous.next = tortoise_p.next
        return head
        

        