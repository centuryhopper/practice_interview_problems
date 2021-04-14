class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if not nums1 or len(nums1) == 0:
            return nums2
        if not nums2 or len(nums2) == 0:
            return nums1

#         naive method:
#         j = 0
#         for i in range(m, len(nums1)):
#             nums1[i] = nums2[j]
#             j += 1

#         nums1.sort()

        # more optimized solution
        lst = [0 for i in range(m + n)]

        i, j, k = 0, 0, 0
        while i < m or j < n:

            # when one of them is out of bounds
            if (i >= m):
                lst[k] = nums2[j]
                j += 1
                k += 1
            elif (j >= n):
                lst[k] = nums1[i]
                i += 1
                k += 1
            else:
                if (nums1[i] <= nums2[j]):
                    lst[k] = nums1[i]
                    i += 1
                    k += 1
                else:
                    lst[k] = nums2[j]
                    j += 1
                    k += 1

        # print(lst)
        for i in range(len(lst)):
            nums1[i] = lst[i]
