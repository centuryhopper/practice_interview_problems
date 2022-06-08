from collections import deque

class Graph():
    def __init__(self, filename:str):
        with open(filename, 'r') as f:
            self.n = int(f.readline())
            self.matrix = [[False]*self.n for _ in range(self.n)]
            i = 0
            for i,line in enumerate(f):
                strAr = line.split()
                for j,c in enumerate(strAr):
                    self.matrix[i][j] = int(c) == 1
    def toposort(self):
        incoming = [0] * self.n
        cnt = 0
        for i in range(self.n):
            for j in range(self.n):
                incoming[j] += 1 if self.matrix[i][j] else 0
        # print(incoming)
        q = deque()
        for i in range(self.n):
            # enqueue all nodes with no incoming edges first
            if incoming[i] == 0:
                q.append(i)
        while q:
            node = q[0]
            q.popleft()
            print(node)
            cnt+=1
            for i in range(self.n):
                if self.matrix[node][i]:
                    incoming[i]-=1
                    if incoming[i] == 0:
                        q.append(i)

        if cnt != self.n:
            print('Error: Graph contains a cycle!')

if __name__ == '__main__':
    g = Graph('./graph_txts/prereqs.txt')
    g.toposort()



