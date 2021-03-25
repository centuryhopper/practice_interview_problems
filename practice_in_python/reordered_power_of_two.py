

# brute force approach
# time: O(n*n!) because each permutation will take n! time
# space: O(n) because the height of the tree will depend on the size of our input
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        def permuteHelp(lst, l, r, powersOf2) -> bool:
            if l >= r:
                if ''.join(lst) in powersOf2:
                    return True
                return False
            retVal = False
            for i in range(l, r):
                lst[l], lst[i] = lst[i], lst[l]
                retVal |= permuteHelp(lst,l+1,r, powersOf2)
                # no need to keep traversing if we've already found a combo
                # that is a power of 2
                if retVal: return True
                lst[l], lst[i] = lst[i], lst[l]
            return retVal
        lst = list(str(N))
        powersOf2 = {str(2**i) for i in range(31)}
        retVal = permuteHelp(lst, 0, len(lst), powersOf2)
        return retVal









# online optimized solution
# class Solution:
#     def reorderedPowerOf2(self, N: int) -> bool:
#         a = 1
#         N = sorted(str(N))
#         while len(str(a)) < len(N): a *= 2
#         while len(str(a)) == len(N):
#             b = sorted(str(a))
#             if b == N: return True
#             a *= 2
#         return False