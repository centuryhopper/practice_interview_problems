class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sort the box types with the number of units per box non-increasingly.
        boxTypes.sort(key=lambda box: -box[1])
        # print(boxTypes)
        cnt = 0
        for boxCnt, boxUnit in boxTypes:
            # [boxCnt....1]
            if truckSize == 0:
                break
            for i in range(boxCnt, 0, -1):
                diff = truckSize - i
                if diff >= 0:
                    truckSize -= i
                    cnt += (i * boxUnit)
                    break
        return cnt
