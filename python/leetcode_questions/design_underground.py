from collections import defaultdict

# my current solution
class UndergroundSystem:
    def __init__(self):
        self.cIMap = defaultdict(tuple)
        self.cOMap = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.cIMap[id] = (stationName, t)

    # all customers that checkout must have checked in prior
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation = self.cIMap[id][0]
        startTime = self.cIMap[id][1]
        finalName = startStation + stationName
        if finalName not in self.cOMap:
            self.cOMap[finalName] = [t-startTime,1]
        else:
            self.cOMap[finalName][0]+=(t-startTime)
            self.cOMap[finalName][1]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total = self.cOMap[startStation+endStation][0]
        cnt = self.cOMap[startStation+endStation][1]
        return total / cnt


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)







# online more optimized solution
# class UndergroundSystem:

#     def __init__(self):
#         self.peopleInTube = {}
#         self.travelTimes = {}

#     def checkIn(self, id: int, stationName: str, t: int) -> None:
#         self.peopleInTube[id] = (stationName,t)

#     def checkOut(self, id: int, stationName: str, t: int) -> None:
#         prev = self.peopleInTube[id]

#         key = (prev[0], stationName)

#         if key in self.travelTimes:
#             self.travelTimes[key].append(t - prev[1])
#         else:
#             self.travelTimes[key] = [t - prev[1]]

#     def getAverageTime(self, startStation: str, endStation: str) -> float:
#         arr = self.travelTimes[(startStation,endStation)]

#         return sum(arr)/len(arr)




















# failed attempt
# class UndergroundSystem:
#     def __init__(self):
#         self.cIMap = defaultdict(lambda: defaultdict(int))
#         self.cOMap = defaultdict(lambda: defaultdict(int))

#     def checkIn(self, id: int, stationName: str, t: int) -> None:
#         self.cIMap[stationName][id] = t

#     # all customers that checkout must have checked in prior
#     def checkOut(self, id: int, stationName: str, t: int) -> None:
#         self.cOMap[stationName][id] = t

#     def getAverageTime(self, startStation: str, endStation: str) -> float:
#         cnt = 0
#         total = 0
#         for k,v in self.cOMap[endStation].items():
#             if k in self.cIMap[startStation]:
#                 cnt+=1
#                 total+=v

#         for k,v in self.cIMap[startStation].items():
#             if k in self.cOMap[endStation]:
#                 total-=v

#         return total / cnt