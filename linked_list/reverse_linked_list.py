# 206. Reverse Linked List
# Given the head of a singly linked list, reverse the list, 
# and return the reversed list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        q = []
        node = head
        while node is not None:
            q.append(node)
            node = node.next

        new_head = q.pop()
        last_node = new_head
        while q:
            node = q.pop()
            last_node.next = node
            last_node = node
        last_node.next = None

        return new_head