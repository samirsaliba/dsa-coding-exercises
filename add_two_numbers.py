# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# This ListNode class was also given
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def construct_int_linked_list(l):
    first_node = ListNode(val=int(l[0]))
    curr_node = first_node
    for i in l[1:]:
        next_node = ListNode(val=int(i))
        curr_node.next = next_node
        curr_node = next_node
    return first_node

def linked_list_to_arr(l):
    arr = [l.val]
    while l.next is not None:
        l = l.next
        arr.append(l.val)
    return arr
    
class Solution:
    def _reverse_list(self, node_start):
        curr_node = node_start
        stack = [str(curr_node.val)]
        while curr_node.next is not None:
            curr_node = curr_node.next
            stack.append(str(curr_node.val))
        return stack[::-1]

    def _list_to_num(self, l):
        return int("".join(l))

    def _num_to_reverse_list(self, num):
        num = str(num)
        return construct_int_linked_list(num[::-1])
    
    def addTwoNumbers(self, l1, l2):
        num1 = self._list_to_num(self._reverse_list(l1))
        num2 = self._list_to_num(self._reverse_list(l2))
        result = num1 + num2
        return self._num_to_reverse_list(result)

if __name__ == "__main__":
    s = Solution()
    examples = [
        {
            "args": {
                "l1": [2,4,3],
                "l2": [5,6,4],
            },
            "solution": [7, 0, 8]
        },
        {
            "args": {
                "l1": [0],
                "l2": [0],
            },
            "solution": [0]
        },
        {
            "args": {
                "l1": [9,9,9,9,9,9,9],
                "l2": [9,9,9,9],
            },
            "solution": [8,9,9,9,0,0,0,1]
        }
    ]
    for i, example in enumerate(examples, start=1):
        print(f"Example {i}")
        print("Args:")
        print(example)
        print("Solution:")
        l1 = construct_int_linked_list(example["args"]["l1"])
        l2 = construct_int_linked_list(example["args"]["l2"])  
        result = linked_list_to_arr(s.addTwoNumbers(l1, l2))
        print(result)
        assert result == example["solution"], "Not the expected result"
        print()