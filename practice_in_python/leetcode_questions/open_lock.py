from collections import deque

class Solution:

    # lock must be a four digit string
    def getAllNeighbors(self,lock:str) -> set[str]:
        if len(lock) != 4: return None
        ret = set()
        # go thru each digit and toggle by one in
        # both directions
        lst = list(lock)
        for i in range(4):
            # clockwise (add)
            tmp = lst[i]
            lst[i] = '0' if lst[i] == '9' else chr(ord(lst[i]) + 1)
            ret.add(''.join(lst))
            lst[i] = tmp

            # counterclockwise (subtract)
            lst[i] = '9' if lst[i] == '0' else chr(ord(lst[i]) - 1)
            ret.add(''.join(lst))
            lst[i] = tmp

        return ret


    def openLock(self, deadends: List[str], target: str) -> int:
        # queue of strings
        q = deque(['0000'])
        visited = set(deadends)
        cnt = 0
        # bfs (append all neighbors of every dequed integer)
        while q:
            # most recent size of queue since the current state
            size = len(q)
            # this loop will process all of the current state's neighbors
            while size > 0:
                size-=1
                # dequeue a lock
                lock = q.popleft()
                # if it's been visited already, then skip it and reset count
                if lock in visited:
                    continue
                visited.add(lock)
                # if it's the target, then update the cnt and don't get neighbors
                if lock == target:
                    return cnt
                # get all of its neighbors
                # enqueue them into q
                st = self.getAllNeighbors(lock)
                for combination in st:
                    if combination in visited:
                        continue
                    q.append(combination)
            # a move is counted once all of the current state's neighbors are processed
            cnt += 1



        # if we ran out of options
        return -1




