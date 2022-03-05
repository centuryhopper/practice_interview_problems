class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def rec(low,high,i,path):
            nonlocal lst
            # avoid the path from going out of bounds
            if path and int(''.join(path)) > high:
                return
            if path:
                val = int(''.join(path))
                if low <= val <= high:
                    lst.append(val)
            for x in range(i,10):
                # only append if it follows the rules of the problem
                if not path or x-1 == int(path[-1]):
                    rec(low,high,i+1,path+[str(x)])
        lst = []
        rec(low,high,1,[])
        return sorted(lst)


