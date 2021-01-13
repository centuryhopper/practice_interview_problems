# class Solution:
    # def __init__(self):
    #     self.cnt = 0

    # def helper_dfs(self, lst: list[int], cur: int, n: int) -> None:
    #     if cur > n:
    #         self.cnt += 1
    #         return
    #     for i in range(1, n + 1):
    #         if lst[i] == 0 and (cur % i == 0 or i % cur == 0):
    #             lst[i] = cur
    #             self.helper_dfs(lst, cur + 1, n)
    #             lst[i] = 0

    # def countArrangement(self, n: int) -> int:

    #     lst = [0] * (n + 1)
    #     self.helper_dfs(lst, 1, n)
    #     return self.cnt

class Solution:

    def countArrangement(self, n: int) -> int:
        lst = [i for i in range(n + 1)]
        accumulator = [0]
        self.helper_dfs(lst, 1, accumulator)
        return accumulator[0];

    def helper_dfs(self, lst: list[int], cur: int, accumulator: list[int]) -> None:
        if cur >= len(lst):
            accumulator[0] +=1
            return

        for i in range(cur, len(lst)):
            lst[i], lst[cur] = lst[cur], lst[i]
            if (lst[cur] % cur == 0 or cur % lst[cur] == 0):
                self.helper_dfs(lst, cur + 1, accumulator)
            lst[i], lst[cur] = lst[cur], lst[i]
