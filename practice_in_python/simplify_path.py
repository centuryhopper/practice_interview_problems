

class Solution:
    '''
    The canonical path should have the following format:

    The path starts with a single slash '/'.
    Any two directories are separated by a single slash '/'.
    The path does not end with a trailing '/'.
    The path only contains the directories on the path from the root directory to the target     file or directory (i.e., no period '.' or double period '..')
    '''

    # capture all directory names in a lst and join them with a /
    # at the very end
    def simplifyPath(self, path: str) -> str:
        lst = []
        directories = path.split('/')
        for directory in directories:
            if directory == '..':
                if lst:
                    lst.pop()
            elif directory == '' or directory == '.':
                continue
            else:
                lst.append(directory)
        string = '/'.join(lst)
        return '/' + string


# retLst = ['/']
#  directories = []
#   dots = []
#    for ch in path:
#         if ch.isalpha():
#             directories.append(ch)
#             dots.clear()
#         elif ch == '/':
#             if directories:
#                 retLst.append(''.join(directories))
#                 directories.clear()
#             if len(dots) == 2:
#                 if retLst:
#                     retLst.pop()
#             elif len(dots) >= 3:
#                 directories.extend(dots)
#                 retLst.append(''.join(directories))
#                 directories.clear()
#             dots.clear()
#         elif ch == '.':
#             dots.append(ch)

#     if len(dots) == 2 and not directories:
#         retLst.pop()
#     elif len(dots) >= 3:
#         retLst.append(''.join(dots))
#     if directories:

#     if not retLst:
#         return '/'
#     elif len(retLst) == 1:
#         if retLst[0] == '/':
#             return '/'
#         else:
#             return '/' + retLst[0]
#     print(retLst)

#     return '/'.join(retLst)[1:]
