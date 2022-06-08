class Solution:

    def __init__(self):
        self.combos = []


    def getCombinations(self,i:int, digits:str, mapping: Dict[str,List[str]], strBuilder:List[str]) -> None:
        if i >= len(digits):
            self.combos.append(''.join(strBuilder))
            return
        for c in mapping[digits[i]]:
            # build string
            strBuilder.append(c)
            # recurse on that string s's combo
            self.getCombinations(i+1, digits, mapping, strBuilder)
            strBuilder.pop()





    def letterCombinations(self, digits: str) -> List[str]:

        if not digits: return []

        mapping = {
            '2' : list('abc'),
            '3' : list('def'),
            '4' : list('ghi'),
            '5' : list('jkl'),
            '6' : list('mno'),
            '7' : list('pqrs'),
            '8' : list('tuv'),
            '9' : list('wxyz'),
        }

        self.getCombinations(0, digits, mapping, [])
        # print(self.combos)

        return self.combos




    # online optimized solution
    # class Solution:
    #     def __init__(self):
    #         self.combinations = []

    #     def letterCombinations(self, digits: str) -> List[str]:
    #         digit_letters = {
    #             "2": ["a", "b", "c"],
    #             "3": ["d", "e", "f"],
    #             "4": ["g", "h", "i"],
    #             "5": ["j", "k", "l"],
    #             "6": ["m", "n", "o"],
    #             "7": ["p", "q", "r", "s"],
    #             "8": ["t", "u", "v"],
    #             "9": ["w", "x", "y", "z"],
    #         }

    #         if len(digits) == 0:
    #             return []

    #         if len(digits) == 1:
    #             return [digit_letters[char] for char in digits][0]

    #         self.combinations = digit_letters[digits[0]]

    #         for digit in digits[1:]:

    #             new_combinations = []
    #             print(new_combinations)

    #             for combination in self.combinations:

    #                 for char in digit_letters[digit]:
    #                     new_combinations.append(combination + char)
    #             self.combinations = new_combinations




    #         return self.combinations
