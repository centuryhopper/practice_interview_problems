class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}

    def insert(self, key: str, val: int) -> None:
        self.d[key] = val

    def sum(self, prefix: str) -> int:
        ans = 0
        for k, v in self.d.items():
            if k[:len(prefix)] == prefix:
                ans += v
        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
