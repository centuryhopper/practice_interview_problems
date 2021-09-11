class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        bestKey = keysPressed[0]
        longestTime = releaseTimes[0]
        n = len(releaseTimes)
        for i in range(1,n):
            # print(bestKey)
            ithDuration = releaseTimes[i] - releaseTimes[i-1]
            if ithDuration > longestTime:
                bestKey = keysPressed[i]
                longestTime = ithDuration
            elif ithDuration == longestTime:
                bestKey = max(bestKey,keysPressed[i])
        return bestKey

