# The following question has two parts:
# Your friend, John, is holding an integer array A[1,n], and he tells you that the array is sorted, and contains all the integers from 0 to n except one. John challenges you to find the missing integer.  He allows you to ask him questions in the form: What is the j-th bit of A[i]?" and he is going to answer you honestly. So, you can vary the values of i and j in each question you ask him. Design an algorithm to find out the missing integer using O(log2 n) questions.
# Now, John has changed the input, and the array A becomes unsorted. Design an algorithm using O(n) questions to find out the missing integer.
from functools import reduce

# constraint: array must contain value from 0 to n
def find_missing_value(lst:list[int], n:int) -> int:
    # gaussian sum formula
    expected_sum = n * (n+1) / 2
    res = reduce(lambda x, y: x + y, lst, 0)
    return int(expected_sum - res)

print(find_missing_value([1,2,3,4,5,7], 7))




