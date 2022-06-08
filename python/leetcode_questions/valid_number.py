

class Solution:
    def isNumber(self, s: str) -> bool:
        n = len(s)

        # make sure that signs appear only at index 0 and right after index of e + 1

        # at least one number check
        cnt = 0
        numberLoc = -1
        es = 0
        eLoc = -1
        decimals = 0
        decimalLoc = -1
        plusLoc = -1
        minusLoc = -1
        numbers = set('0123456789')
        # make sure there are no invalid letters
        invalidLetters = set('abcdfghijklmnopqrstuvwxyzABCDFGHIJKLMNOPQRSTUVWXYZ')
        for i,c in enumerate(s):
            if c in invalidLetters:
                return False
            if c in numbers:
                if numberLoc == -1:
                    numberLoc = i
                cnt+=1
            if c == 'e' or c == 'E':
                es+=1
                if es > 1: return False
                eLoc = i
            if c == '.':
                decimals+=1
                decimalLoc = i
                if decimals > 1:
                    return False
            if c == '+':
                plusLoc = i
                if (plusLoc != 0 and plusLoc != eLoc+1):
                    return False
                if plusLoc == n-1:
                    return False
            if c == '-':
                minusLoc = i
                if (minusLoc != 0 and minusLoc != eLoc+1):
                    return False
                if minusLoc == n-1:
                    return False
        # need at least one number
        if cnt == 0:
            return False
        if decimalLoc > eLoc and eLoc != -1:
            return False
        if eLoc == 0 or eLoc == n-1:
            return False
        # return False if the first found number comes after e
        if numberLoc > eLoc and eLoc != -1:
            return False
        return True



'''
Online state machine solution
class Solution:
    def isNumber(self, s: str) -> bool:
        number = re.compile("^[+-]?[0-9]+(\.[0-9]*)?([eE][+-]?[0-9]+)?$|^[+-]?\.[0-9]+([eE][+-]?[0-9]+)?$")
        return number.match(s)

class Solution(object):
    def isNumber(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        #define a DFA
        currentState = 0
        state = [
            {'blank': 0, 'sign': 1, 'digit': 2, '.': 3},
            {'digit': 2, '.': 3},
            {'digit': 2, '.': 4, 'e': 5, 'blank': 8},
            {'digit': 4},
            {'digit': 4, 'e': 5, 'blank': 8},
            {'sign': 6, 'digit': 7},
            {'digit': 7},
            {'digit': 7, 'blank': 8},
            {'blank': 8}
        ]

        for c in s:
            if c == 'E':
                c = 'e'
            elif c >= '0' and c <= '9':
                c = 'digit'
            elif c == ' ':
                c = 'blank'
            elif c in ['+', '-']:
                c = 'sign'
            if c not in state[currentState].keys():
                return False
            currentState = state[currentState][c]
        if currentState not in [2,4,7,8]:
            return False
        return True

'''