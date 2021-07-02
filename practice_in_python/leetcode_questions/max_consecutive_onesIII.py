
#region My solution
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxVal = 0
        cntFlip = 0
        start = 0
        for end in range(len(nums)):
            # zero cases
            if nums[end] == 0 and cntFlip < k:
                # move ahead
                cntFlip+=1
            elif nums[end] == 0 and cntFlip >= k:
                # move start ahead until cntFlip == k
                while cntFlip >= k:
                    if nums[start] == 0:
                        cntFlip-=1
                    start+=1
                # cnt the 0 at end
                cntFlip+=1
            # one cases
            maxVal = max(maxVal, end-start+1)
        
        return maxVal
        
#endregion



#region TLE solution
# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         maxVal = 0
#         endWindow = 0
#         flipsLeft = k
#         i = 0
#         while i < len(nums):
#             endWindow = i
#             for j in range(i,len(nums)):
#                 endWindow = j
#                 if nums[j] == 0 and flipsLeft > 0:
#                     flipsLeft-=1
#                 # record most recent endWindow
#                 # and stop any further traversing
#                 # for this iteration
#                 elif nums[j] == 0:
#                     endWindow = j - 1
#                     break
#             flipsLeft = k

#             # print(endWindow)
#             maxVal = max(maxVal,endWindow - i + 1)
#             i+=1
#         return maxVal
#endregion
    
#region another TLE solution
# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         maxVal = 0
#         endWindow = 0
#         flipsLeft = k
#         i = 0
#         while i < len(nums):
#             endWindow = i
#             secondZeroIndex = None
#             for j in range(i,len(nums)):
#                 endWindow = j
#                 if nums[j] == 0 and flipsLeft > 0:
#                     if flipsLeft == k:
#                         firstZeroIndex = j
#                     flipsLeft-=1
#                 # record most recent endWindow
#                 # and stop any further traversing
#                 # for this iteration
#                 elif nums[j] == 0:
#                     endWindow = j - 1
#                     break
#             flipsLeft = k
#             # print(endWindow)
#             maxVal = max(maxVal,endWindow - i + 1)
#             if nums[endWindow] == 1 and secondZeroIndex != None:
#                 i = firstZeroIndex+1
#                 # print(i)
#             else:
#                 i+=1
#         return maxVal

#endregion
    
#region optimized solution found online
# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int: 
#         j = 0
#         # always move right to expand sliding window, move left when k < 0
#         for i in range(len(nums)):
#             if nums[i] == 0: k -= 1
#             if k < 0:
#                 if nums[j] == 0: k += 1
#                 j += 1
#         return i - j + 1

#endregion