from collections import deque
from data_structures.TreeNode import TreeNode


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root: return []
        lst = []
        d = deque()
        d.append(root)
        d.append(None)
        summ, cnt = 0, 0
        while d:
            poll = d[0]
            d.popleft()
            if poll is None:
                # we've dequeued null,
                # so reset the avg and cnts
                # for the next level

                # we only want to append a null in the queue
                # if there are more levels to traverse thru and calculate
                if d: d.append(None)
                lst.append(summ/cnt)
                summ = cnt = 0
            else:
                summ += poll.val
                cnt += 1
                # enqueue children, if any
                if poll.left: d.append(poll.left)
                if poll.right: d.append(poll.right)


        return lst

'''Interesting optimized solution found online''''
'''
def averageOfLevels(self, root: TreeNode) -> List[float]:

        queue = [root]
        answer = []

        while queue:
            temp = []
            answer.append(self.Average(queue))

            for el in queue:
                if el.left != None:
                    temp.append(el.left)
                if el.right != None:
                    temp.append(el.right)
            queue = temp

        return answer

    def Average(self, queue):
        total = 0
        n = 0

        for el in queue:
            total += el.val
            n += 1

        return float(total/n)
'''
