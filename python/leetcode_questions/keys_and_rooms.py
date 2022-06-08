from collections import deque

class Solution:

    # iterative DFS
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        myPocket = deque()
        visited = [False] * len(rooms)
        # enter room 0
        myPocket.append(0)

        while myPocket:
            # use your key
            curKey = myPocket[-1]
            myPocket.pop()
            # only enter if you haven't entered before
            if not visited[curKey]:
                visited[curKey] = True
                # keep all other keys found in this room in your pocket
                for key in rooms[curKey]:
                    myPocket.append(key)
        # all(iterable) returns true only when everything in the
        # input iterable is true
        return all(visited)



