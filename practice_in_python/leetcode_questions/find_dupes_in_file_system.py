from collections import defaultdict

class Solution:

    def findDuplicate(self, paths: List[str]) -> List[List[str]]:

        # key: str, val: list[string]
        d = defaultdict(list)

        for path in paths:
            lst = path.split()
            pathDir = lst[0]
            for i in range(1, len(lst)):
                currentFile = lst[i]
                size = len(currentFile)
                # openParenIdx
                o = currentFile.find('(')
                fileName = currentFile[:o]
                fileContents = currentFile[o+1:size-1]
                d[fileContents].append(pathDir+'/'+fileName)

        # print(d)

        return [dup for dup in d.values() if len(dup) > 1]



# slightly less verbose version
# from collections import defaultdict

# class Solution:

#     def findDuplicate(self, paths: List[str]) -> List[List[str]]:

#         # key: str, val: list[string]
#         d = defaultdict(list)

#         for path in paths:
#             lst = path.split()
#             pathDir = lst[0]
#             for i in range(1, len(lst)):
#                 nameAndContents = lst[i].split('(')
#                 fileName = nameAndContents[0]
#                 fileContents = nameAndContents[1][:-1]
#                 d[fileContents].append(pathDir+'/'+fileName)

#         # print(d)

#         return [dup for dup in d.values() if len(dup) > 1]






















