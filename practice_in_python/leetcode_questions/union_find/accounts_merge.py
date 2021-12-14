'''
[["Alex",Alex5@m.co,Alex4@m.co,Alex0@m.co],["Ethan",Ethan3@m.co,Ethan3@m.co,Ethan0@m.co],["Kevin",Kevin4@m.co,Kevin2@m.co,Kevin2@m.co],["Gabe",Gabe0@m.co,Gabe3@m.co,Gabe2@m.co],["Gabe",Gabe3@m.co,Gabe4@m.co,Gabe2@m.co]]

[["Hanzo",Hanzo2@m.co,Hanzo3@m.co],["Hanzo",Hanzo4@m.co,Hanzo5@m.co],["Hanzo",Hanzo0@m.co,Hanzo1@m.co],["Hanzo",Hanzo3@m.co,Hanzo4@m.co],["Hanzo",Hanzo7@m.co,Hanzo8@m.co],["Hanzo",Hanzo1@m.co,Hanzo2@m.co],["Hanzo",Hanzo6@m.co,Hanzo7@m.co],["Hanzo",Hanzo5@m.co,Hanzo6@m.co]]

[["David",David5@m.co,David8@m.co],["David",David1@m.co,David1@m.co,David8@m.co],["David",David0@m.co,David0@m.co,David5@m.co]]

'''


#region failed attempt
# class Solution:
#     def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
#         ds = DisjointSet(accounts)
#         return ds.getResult()

# class DisjointSet:
#     def __init__(self,accounts):
#         self.accounts = accounts
#         # print(self.accounts)
#         self.n = len(accounts)
#         self.parent = list(range(self.n))

#         for i in range(self.n):
#             for j in range(self.n):
#                 # avoid unioning elements with themselves
#                 if i != j:
#                     self.union(i,j)
#         # print(self.accounts)
#         # print(self.parent)
#         # collect all representatives after our union operation above
#         self.ans = [account for i,account in enumerate(self.accounts) if self.parent[i] == i]

#     def find(self,x:int)->int:
#         if self.parent[x] == x:
#             return x
#         self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]

#     def union(self,x:int,y:int)->None:
#         parent = self.parent
#         accounts = self.accounts
#         # terminate early if...
#         # 1. x and y are already in the same set
#         # 2. name of accounts at position x and y have different names
#         # 3. accounts have the same name but don't have any emails in common
#         rootX,rootY = self.find(x),self.find(y)
#         if rootX == rootY:
#             return
#         if accounts[rootX][0] != accounts[rootY][0]:
#             accounts[rootX] = sorted(set(accounts[rootX]))
#             return
#         stx = set(accounts[rootX][1:])
#         sty = set(accounts[rootY][1:])
#         anyInCommon = stx & sty
#         if not anyInCommon:
#             return

#         # if theres a match, merge the contents of the smaller account into the larger one
#         if len(stx) > len(sty):
#             for email in sty:
#                 if email not in stx:
#                     accounts[rootX].append(email)
#             accounts[rootX] = sorted(set(accounts[rootX]))
#             parent[rootY] = rootX
#         else:
#             for email in stx:
#                 if email not in sty:
#                     accounts[rootY].append(email)
#             accounts[rootY] = sorted(set(accounts[rootY]))
#             parent[rootX] = rootY

#     def getResult(self):
#         return self.ans
#endregion




'''
[["Alex",Alex5@m.co,Alex4@m.co,Alex0@m.co],["Ethan",Ethan3@m.co,Ethan3@m.co,Ethan0@m.co],["Kevin",Kevin4@m.co,Kevin2@m.co,Kevin2@m.co],["Gabe",Gabe0@m.co,Gabe3@m.co,Gabe2@m.co],["Gabe",Gabe3@m.co,Gabe4@m.co,Gabe2@m.co]]

[["Hanzo",Hanzo2@m.co,Hanzo3@m.co],["Hanzo",Hanzo4@m.co,Hanzo5@m.co],["Hanzo",Hanzo0@m.co,Hanzo1@m.co],["Hanzo",Hanzo3@m.co,Hanzo4@m.co],["Hanzo",Hanzo7@m.co,Hanzo8@m.co],["Hanzo",Hanzo1@m.co,Hanzo2@m.co],["Hanzo",Hanzo6@m.co,Hanzo7@m.co],["Hanzo",Hanzo5@m.co,Hanzo6@m.co]]

[["David",David5@m.co,David8@m.co],["David",David1@m.co,David1@m.co,David8@m.co],["David",David0@m.co,David0@m.co,David5@m.co]]

'''
#region failed attempt2

# class DisjointSet:
#     def __init__(self,accounts):
#         # this is the total number of unique groups so far
#         # and will later be the size of our output
#         self.numGroups = len(accounts)
#         self.accounts = accounts
#         self.parent = list(range(self.numGroups))
#         self.rank = [1]*self.numGroups
#         self.emailToIdx = {}
#         # group common accounts
#         for i,account in enumerate(self.accounts):
#             for email in account[1:]:
#                 if email in self.emailToIdx:
#                     self.union(i,self.emailToIdx[email][0])
#                 else:
#                     self.emailToIdx[email] = (i,account[0])
#         self.ans = [[] for _ in range(self.numGroups)]
#         curI = 0
#         # maps all root parents to the correct location in the output
#         mapper = {}
#         for email,(i,name) in self.emailToIdx.items():
#             if self.parent[i] not in mapper:
#                 mapper[self.parent[i]] = curI % self.numGroups
#                 curI+=1
#                 self.ans[mapper[self.parent[i]]].append(name)
#             self.ans[mapper[self.parent[i]]].append(email)
#     def find(x)->int:
#         if self.parent[x] == x:
#             return x
#         self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]
#     def union(self,x:int,y:int)->None:
#         parent = self.parent
#         rank = self.rank
#         accounts = self.accounts
#         # print(x,y)
#         # print(type(x),type(y))
#         try:
#             rootX = self.find(x)
#             rootY = self.find(y)
#         except Exception as e:
#             print(x,y,parent[x],parent[y])
#         if rootX == rootY:
#             return
#         if accounts[rootX][0] != accounts[rootY][0]:
#             return
#         if rank[rootX] > rank[rootY]:
#             parent[y] = rootX
#         elif rank[rootX] < rank[rootY]:
#             parent[x] = rootY
#         else:
#             parent[x] = rootY
#             rank[rootY]+=1
#         # two groups merged into one, so decrement this variable
#         self.numGroups-=1



# def accountsMerge(accounts):
#     ds = DisjointSet(accounts)
#     return ds.ans

# ans = accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])
# print(ans)

#endregion



# success!!!

class DisjointSet:
    def __init__(self,accounts):
        # this is the total number of unique groups so far
        # and will later be the size of our output
        self.numGroups = len(accounts)
        self.parent = list(range(self.numGroups))
        self.rank = [1]*self.numGroups

    def find(self,x) -> int:
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x:int,y:int)->None:
        parent = self.parent
        rank = self.rank
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX == rootY:
            return
        # two groups merged into one, so decrement this variable
        self.numGroups-=1
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX]+=1

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ds = DisjointSet(accounts)
        emailToIdx = {}
        # group common accounts
        for i,account in enumerate(accounts):
            for email in account[1:]:
                if email in emailToIdx:
                    ds.union(i,emailToIdx[email])
                else:
                    emailToIdx[email] = i

        ans = [[] for _ in range(ds.numGroups)]

        # next available index in self.ans
        next = 0
        groupId2Idx = {}
        for email,i in emailToIdx.items():
            # find which group contains this email's account
            groupId = ds.find(i)
            if groupId not in groupId2Idx:
                groupId2Idx[groupId] = next
                accName = accounts[groupId][0]
                ans[next].append(accName)
                ans[next].append(email)
                next+=1
            else:
                ans[groupId2Idx[groupId]].append(email)
        ans = list(map(lambda acc:[acc[0]]+sorted(acc[1:]),ans))
        return ans


