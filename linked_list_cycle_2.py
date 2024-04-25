# 142. Linked List Cycle II
# Given the head of a linked list, return the node where the cycle begins. 
# If there is no cycle, return null.

# There is a cycle in a linked list if there is some node in the list 
# that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). 
# It is -1 if there is no cycle.
# Note that pos is not passed as a parameter. Do not modify the linked list.

class Solution:
    def _naive_solution(self, head):
        curr_node = head
        _visited = {curr_node: 0}
        i = 1
        while curr_node.next is not None:
            curr_node = curr_node.next
            if curr_node in _visited:
                return curr_node
            _visited[curr_node] = i
            i+=1
        return None

    def _find_cycle_start_tortoise_hare(self, head, hare):
        # cycle has been found - so to find the start we reset 
        # the tortoise pointer and walk them both at same pace
        # where they meet is where the cycle begins
        tortoise = head
        while tortoise != hare:
            tortoise = tortoise.next
            hare = hare.next
        return tortoise


    def _hare_tortoise_algorithm(self, head):
        # basically two pointers walk the list
        # one moves slow per iteration (1 move) and one moves fast (2 moves)
        # if they meet, then the list must have a cycle
        tortoise_p = head
        hare_p = head
        
        while hare_p and hare_p.next:
            tortoise_p = tortoise_p.next
            hare_p = hare_p.next.next                
            if tortoise_p == hare_p:
                return self._find_cycle_start_tortoise_hare(head, hare_p)
        
        # if the fast pointer has run through the whole list 
        # w/o bumping into the slow one, then there is no cycle 
        return None

    def detectCycle(self, head):
        if not head or head.next is None:
            return None

        return self._hare_tortoise_algorithm(head)


# The class List Node and the functions below are just for checking the correctedness
# of this script, they are not part of the solution
class ListNode:
    def __init__(self, val, pos=None):
        self.val = val
        self.next = None
        self._pos = pos

def construct_linked_list(l, cycle=None):    
    if cycle is None:
        cycle = (-1, -1)
    
    first_node = ListNode(val=l[0], pos=0)
    curr_node = first_node
    pos=1
    nodes = [curr_node]
    for i, val in enumerate(l[1:], start=1):
        if i==cycle[1]:
            curr_node.next = nodes[cycle[0]]
        else:
            curr_node.next = ListNode(val=val, pos=pos)
            curr_node = curr_node.next
            pos+=1
        nodes.append(curr_node)
    return first_node

def check_result(expected, actual):
    print(actual._pos) if hasattr(actual, '_pos') else print(actual)

    if actual is None:
        assert expected==-1, "Not the expected result"
    else:
        assert actual._pos == expected, "Not the expected result"

if __name__ == "__main__":
    s = Solution()

    examples = [
        {
            "args": {
                "l": [3,2,0,-4],
                "cycle": (1,3)
            },
            "solution": 1
        },
        {
            "args": {
                "l": [1,2],
                "cycle": (0, 1)
            },
            "solution": 0
        },
        {
            "args": {
                "l": [1]
            },
            "solution": -1
        },
    ]


    for i, example in enumerate(examples, start=1):
        print(f"Example {i}")
        print("Args:")
        print(example)
        print("Solution:")
        head = construct_linked_list(**example["args"])
        result = s.detectCycle(head)
        check_result(example["solution"], result)
        print()