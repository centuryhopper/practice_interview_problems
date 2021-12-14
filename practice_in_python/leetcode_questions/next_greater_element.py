class Solution:
    '''
    [4,1,2]
    [1,3,4,2]
    {1:3,3:4}
    [4,2]

    [2,5,4]
    [5,3,2,4,6]
    {5:-1,3:4,2:4,4:6,6:-1}
    []
    [10,9,8,7,6,5,11]
    '''

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        improvement from an O(len(nums1) * len(nums2)) solution to a time of O(len(nums1) + len(nums2))
        '''
        d = {}
        lst = []
        n2 = len(nums2)
        for i in range(n2):
            cur = nums2[i]
            next = nums2[i+1] if i != n2-1 else -1
            while lst and cur > lst[-1]:
                d[lst.pop()] = cur
            if cur < next:
                d[cur] = next
            else:
                if i != n2-1:
                    lst.append(cur)
                d[cur] = -1
        ans = []
        for num in nums1:
            ans.append(d[num])

        return ans
