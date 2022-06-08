
from collections import deque, OrderedDict


class Solution:
    def intToRoman(self, num: int) -> str:

        # d = OrderedDict({
        #     1 : 'I',
        #     5 : 'V',
        #     10 : 'X',
        #     50 : 'L',
        #     100 : 'C',
        #     500 : 'D',
        #     1000 : 'M',
        # })

        d = OrderedDict({
            1000: 'M',
            500: 'D',
            100: 'C',
            50: 'L',
            10: 'X',
            5: 'V',
            1: 'I',
        })

        d2 = {
            4: 'IV',
            9: 'IX',
            40: 'XL',
            90: 'XC',
            400: 'CD',
            900: 'CM',
        }

        lst = deque()
        tmpLst = deque()
        multiplier = 10
        while num > 0:
            val = num % multiplier
            if val in d2:
                lst.appendleft(d2[val])
            elif val in d:
                lst.appendleft(d[val])
            else:
                # loop thru dictionary to find the greatest
                # key less than it
                tmp = val
                for k, v in d.items():
                    # exhaust tmp for largest key less than
                    # it, then reset tmp to current k
                    # and exhaust for second largest, etc, etc (greedy method)
                    while k <= tmp:
                        tmpLst.append(v)
                        tmp -= k
                lst.extendleft(reversed(tmpLst))
                # print(tmpLst)
                tmpLst.clear()
            num -= val
            multiplier *= 10

        return ''.join(lst)


'''
fancy solution found online:

def intToRoman(self, num: int) -> str:
        thousands = ["", "M", "MM", "MMM"]
        hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        units = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return thousands[num//1000] + hundreds[num%1000//100] + tens[num%100//10] + units[num%10]

'''
