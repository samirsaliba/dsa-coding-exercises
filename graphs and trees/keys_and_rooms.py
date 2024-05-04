# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. 
# Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

# When you visit a room, you may find a set of distinct keys in it. 
# Each key has a number on it, denoting which room it unlocks, 
# and you can take all of them with you to unlock the other rooms.

# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, 
# return true if you can visit all the rooms, or false otherwise.

from collections import deque
from typing import List

class Solution:

    def _dfs(self, rooms):
        visited = [False] * len(rooms)
        visited[0] = True
        open_rooms = deque([rooms[0]])

        while open_rooms:
            new_room = open_rooms.popleft()
            for key in new_room:
                if visited[key] == False:
                    visited[key] = True
                    open_rooms.appendleft(rooms[key])
        
        return all(visited)
            

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms: return rooms
        return self._dfs(rooms)
        
if __name__ == "__main__":
    s = Solution()

    examples = [
        {
            "args": {
                "rooms": [[1],[2],[3],[]],
            },
            "solution": True
        },
        {
            "args": {
                "rooms": [[1,3],[3,0,1],[2],[0]],
            },
            "solution": False
        },
    ]


    for i, example in enumerate(examples, start=1):
        print(f"Example {i}")
        print("Args:")
        print(example)
        print("Solution:")
        result = s.canVisitAllRooms(**example["args"])
        print(result)
        assert result == example["solution"], "Not the expected result"
        print()