class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def strToInt(s:str)->int:
            mult = 1
            retVal = 0
            for i in range(len(s)-1,-1,-1):
                retVal += (ord(s[i]) - 48) * mult
                mult *= 10
            return retVal
                
        def intToStr(num:int)->str:
            lst = []
            while num > 0:
                lsb = num % 10
                lst.insert(0,chr(lsb+48))
                num//=10
            return ''.join(lst)
        
        if num1 == '0': return num2
        if num2 == '0': return num1
                
        # print(strToInt(num1))
        # print(intToStr(11), intToStr(123))
        return intToStr(strToInt(num1) + strToInt(num2))