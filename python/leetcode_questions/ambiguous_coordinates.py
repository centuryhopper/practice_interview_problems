class Solution:

    def getValidStringSets(self, s) -> set[str]:
        n = len(s)
        st = set()

        # sandwiching case
        if s[0] == '0' and s[n-1] == '0':
            return set('0') if n == 1 else set()
        # trailing zero case
        if s[n-1] == '0':
            st.add(s)
            return st
        # leading zero case
        if s[0] == '0':
            st.add('0.' + s[1:])
            return st

        # cases without any zeros in the string
        for i in range(1, n):
            st.add(s[:i]+'.'+s[i:])
        # don't forget the original string as it is valid as well
        st.add(s)
        return st

    def ambiguousCoordinates(self, s: str) -> List[str]:
        # strip parentheses
        s = s[1:len(s)-1]
        print(s)
        lst = []

        # loop thru string and generate possible combos
        for i in range(1, len(s)):
            leftHalf = self.getValidStringSets(s[:i])
            rightHalf = self.getValidStringSets(s[i:])
            # print(leftHalf)
            # print(rightHalf)
            # print()

            # combine all of them
            for s1 in leftHalf:
                for s2 in rightHalf:
                    lst.append('(' + s1 + ', ' + s2 + ')')
        return lst
