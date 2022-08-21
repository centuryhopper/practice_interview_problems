class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        toStr = str(num)
        # sum up all occurrences of k-beauty with the exception that the substring is 0
        return sum(1 for i in range(k-1,len(toStr)) if int(toStr[i-k+1:i+1]) != 0 and num % int(toStr[i-k+1:i+1]) == 0)
            
            
