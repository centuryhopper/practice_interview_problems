# Dynamic Programming bsed Python
# implementation of Maximum Sum
# Increasing Subsequence (MSIS)
# problem

# maxSumIS() returns the maximum
# sum of increasing subsequence
# in arr[] of size n
def maxSumIS(arr, n) -> int:
	maxVal = 0
	msis = [0 for x in range(n)]
	for i in range(n):
		msis[i] = arr[i]
	for i in range(1, n):
		for j in range(i):
			if (arr[i] > arr[j] and
				msis[i] < msis[j] + arr[i]):
				msis[i] = msis[j] + arr[i]
	for i in range(n):
		if maxVal < msis[i]:
			maxVal = msis[i]
	print(msis)
	return maxVal

if __name__ == '__main__':
    	# Driver Code
	arr = [5,4,7,6,8,12]
	n = len(arr)
	print("Sum of maximum sum increasing " +\
						"subsequence is " +\
					str(maxSumIS(arr, n)))\


# This code is contributed
# by Bhavya Jain
