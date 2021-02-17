from collections import deque
import numpy as np


class Solution:

    # neighbors can't have the same color as the current node in order to be bipartite
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph or len(graph) <= 1:
            return True
        d = deque()
        color = [None] * len(graph)
        visited = [False] * len(graph)
        for idx, node in enumerate(graph):
            if visited[idx]:
                continue
            d.append(idx)
            while d:
                val = d[0]
                neighbors = graph[val]
                d.popleft()
                for neighbor in neighbors:
                    if not color[neighbor]:
                        # color opposite to current dequeued node
                        color[neighbor] = not color[val]
                        visited[neighbor] = True
                        d.append(neighbor)
                    elif color[neighbor] == color[val]:
                        print(color)
                        return False

        return True


# more space optimized solution because of not using an extra visited array
# from collections import deque
# import numpy as np

# class Solution:

#     # neighbors can't have the same color as the current node in order to be bipartite
#     def isBipartite(self, graph: List[List[int]]) -> bool:
#         if not graph or len(graph) <= 1: return True
#         d = deque()
#         color = [None] * len(graph)
#         for idx, node in enumerate(graph):
#             if color[idx] is not None: continue
#             d.append(idx)
#             while d:
#                 val = d[0]
#                 neighbors = graph[val]
#                 d.popleft()
#                 for neighbor in neighbors:
#                     if not color[neighbor]:
#                         # color opposite to current dequeued node
#                         color[neighbor] = not color[val]
#                         d.append(neighbor)
#                     elif color[neighbor] == color[val]:
#                         return False



#         return True

