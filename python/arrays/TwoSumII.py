class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        i = 0
        j = len(numbers) - 1
        while i < j:
            summ = numbers[i] + numbers[j]
            if summ < target:
                i+=1
            elif summ > target:
                j-=1
            else:
                ans.extend([i+1,j+1])
                break
        return ans
        
        
        
