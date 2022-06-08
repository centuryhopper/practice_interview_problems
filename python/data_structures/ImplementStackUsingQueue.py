from collections import deque

class MyStack:
    '''
    [1,]
    [1,]

    [1,2]
    [1,]



    '''

    def __init__(self):
        # problem states at most 100 calls will be made
        self.q1 = deque()
        self.q2 = deque()
        self.cur = 0
        self.cur2 = 0

    def push(self, x: int) -> None:
        q1 = self.q1
        q2 = self.q2
        q1.append(x)
        q2.append(x)

    def pop(self) -> int:
        q1 = self.q1
        q2 = self.q2
        ogQ1Size = len(q1)
        ogQ2Size = len(q2)
        # unload q2 contents into q1
        for _ in range(ogQ2Size-1):
            q1.append(q2.popleft())
        q2.popleft()

        # get last element of original q1
        for _ in range(ogQ1Size-1):
            q2.append(q1.popleft())
        ans = q1.popleft()
        # print(q1)
        # print(q2)
        return ans


    def top(self) -> int:
        q1 = self.q1
        q2 = self.q2
        ogQ1Size = len(q1)
        ogQ2Size = len(q2)
        # unload q2 contents into q1
        for _ in range(ogQ2Size):
            q1.append(q2.popleft())
        # get last element of original q1
        for _ in range(ogQ1Size-1):
            q2.append(q1.popleft())
        ans = q1.popleft()
        q2.append(ans)
        # print(q1)
        # print(q2)
        return ans


    def empty(self) -> bool:
        return not self.q1



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()