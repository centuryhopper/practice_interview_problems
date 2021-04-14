class Solution:

    # sliding algorithm
    # the set of strings must be
    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        if k > n: return False
        st = set()
        for i in range(k-1, n):
            # sliding window
            st.add(s[i-k+1:i+1])
        # print(st)
        return len(st) == 2 ** k



# optimized online solution
# class Solution:
#     def hasAllCodes(self, s: str, k: int) -> bool:
#         if len(s) < k - 1 + 2 ** k:
#             return False
#         remaining = 2 ** k
#         exist = set()
#         for i in range(len(s) - k, -1, -1):
#             if s[i:(i + k)] not in exist:
#                 remaining -= 1
#                 exist.add(s[i:(i + k)])
#             if i < remaining:
#                 return False
#             if remaining == 0:
#                 return True
