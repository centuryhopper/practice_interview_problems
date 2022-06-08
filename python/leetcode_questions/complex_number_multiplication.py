class Solution:
    # complex number form: a+bi
    # (a+bi) (c+di) = ac + adi + bci + bdi^2
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a,b = num1.split('+')
        c,d = num2.split('+')
        a = int(a)
        c = int(c)
        b = int(b[:-1])
        d = int(d[:-1])
        ans = b*d*-1
        ans += (a * c)
        return f'{ans}+{a*d+c*b}i'
    