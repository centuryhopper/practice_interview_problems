# from functools import reduce

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        def listToDecimal(arr) -> int:
            arr = list(map(lambda i:str(i),arr))
            binaryString = ''.join(arr)
            return int(binaryString,2)
            
        ones = [i for i,num in enumerate(arr) if num == 1]
        print(f'{ones = }')
        numOnes = len(ones)
        
        # number of ones in the input must be divisible by 3
        if numOnes % 3 != 0: return [-1,-1]
        if numOnes == 0:
            return [0,len(arr)-1]
        
        # make sure all sections have the same number of ones       
        
        # then we can check if all sections are the same number
        numOnesPerSection = numOnes // 3
        print(f'{numOnesPerSection = }')
        
        # left and right bound represent the bounds for the middle subarray
        # and record results
        leftBound = ones[numOnesPerSection-1]+1
        rightBound = ones[2*numOnesPerSection-1]+1
        
        print(f'{leftBound = }, {rightBound = }')
        leftSection,middleSection,rightSection = arr[:leftBound],arr[leftBound:rightBound],arr[rightBound:]
        left,middle,right = listToDecimal(leftSection), listToDecimal(middleSection), listToDecimal(rightSection)
        print(f'left section: {leftSection}, middle section: {middleSection}, right section:  {rightSection}')
        print(f'left section ones count = {leftSection.count(1)} middle section ones count = {middleSection.count(1)} right section ones count = {rightSection.count(1)}')
        print(f'{left = } {middle = } {right = }')
        if left == middle == right:
            return [leftBound-1, rightBound]
        
        return [-1,-1]