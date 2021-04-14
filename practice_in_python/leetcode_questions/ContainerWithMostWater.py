class Solution:

    '''
    Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

    Notice that you may not slant the container.
    '''
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights)-1
        maxArea = abs(j - i) * min(heights[i], heights[j])
        # print('starting max area:', maxArea)
        while i < j - 1:
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            curArea = abs(j - i) * min(heights[i], heights[j])
            # print(curArea)
            maxArea = max(maxArea, curArea)
        return maxArea
