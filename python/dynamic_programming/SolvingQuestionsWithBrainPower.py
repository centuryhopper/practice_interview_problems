'''
For each question, we can either solve it or skip it. How can we use Dynamic Programming to decide the most optimal option for each problem?
We store for each question the maximum points we can earn if we started the exam on that question.
If we skip a question, then the answer for it will be the same as the answer for the next question.
If we solve a question, then the answer for it will be the points of the current question plus the answer for the next solvable question.
The maximum of these two values will be the answer to the current question.
'''

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0]*n
        # we should always solve the last question if
        # it were the only question on the exam
        dp[-1] = questions[-1][0]
        for i in range(n-2,-1,-1):
            takeVal,questionsToSkip = questions[i]
            nextSolvable = dp[i+questionsToSkip+1] if i+questionsToSkip+1 < n else 0
            nextSolvable += takeVal
            dp[i] = max(nextSolvable,dp[i+1])
        # print(dp)
        return dp[0]
            
        
