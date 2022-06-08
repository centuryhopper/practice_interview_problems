class Solution:
    '''
    Get the total sum and subtract the minimum and maximum value in the array. Finally divide the result by n - 2.
    '''
    def average(self, salary: List[int]) -> float:
        minn = float('inf')
        maxx = float('-inf')
        n = len(salary)
        summ = 0
        for sal in salary:
            minn = min(minn, sal)
            maxx = max(maxx, sal)
            summ += sal
        return (summ - minn - maxx) / (n-2)
