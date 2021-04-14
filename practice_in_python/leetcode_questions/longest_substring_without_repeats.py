import numpy as np

#region dependency injection
# class Person:
#     def __init__(self, name='', age=0):
#         self.name = name
#         self.age = age

#     def myfunc(self):
#         print("Hello my name is " + self.name)

#     def __str__(self):
#         return 'person object'

#     def myself(self, person):
#         person = self
#         # print(self)
#         print(person)

# p1 = Person("John", 36)
# p2 = Person('',0)
# print(p1.myself(p2))
#endregion




def lengthOfLongestSubstring(s: str):
    """
    :type s: str
    :rtype: int
    """
    # edge cases
    n = len (s)
    if n <= 1 : return n

    curSubstr = ''
    substrLen = len(curSubstr)
    u_list = []
    listify = list(s)

    for ch in listify:

        # adds unique characters
        if not ch in u_list:
            u_list.append(ch)

        # we found a duplicate (ch already in u_list)
        else:
            # update the string if list length is greater
            if len(u_list) > len(curSubstr):
                curSubstr = ''.join(u_list)
                substrLen = len(curSubstr)

            # a list of size one or less is useless
            if len(u_list) < 2:
                u_list.clear()
                u_list.append(ch)
                continue

            tail = u_list[(u_list.index(ch) + 1):]
            u_list.clear()
            u_list += tail
            # print(u_list)

            # add the current char to the list after it's cleared from
            # the line above so we don't just skip it
            u_list.append(ch)
            # print(u_list)

    # check the list once again to see if it's
    # larger than our current substring
    if len(u_list) > len(curSubstr):
        curSubstr = ''.join(u_list)
        substrLen = len(curSubstr)

    return substrLen


print(lengthOfLongestSubstring("anviaj"))
print(lengthOfLongestSubstring("anvinj"))
print(lengthOfLongestSubstring('pwwkew'))
print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('bbbbb'))
print(lengthOfLongestSubstring('bbbbbac'))
print(lengthOfLongestSubstring('bacbbbb'))
print(lengthOfLongestSubstring('au'))
print(lengthOfLongestSubstring('dvdf'))
print()
print(lengthOfLongestSubstring('aabb'))
print(lengthOfLongestSubstring('abcaa'))
print(lengthOfLongestSubstring('aabac'))
print(lengthOfLongestSubstring('abcb'))











# for ch in listify:
#         # adds unique chars to the list
#         if not ch in u_list:
#             u_list.append(ch)

#         else:
#             if len(u_list) > len(curSubstr):
#                 curSubstr = ''.join(u_list)
#                 substrLen = len(curSubstr)
#             # if its greater, we clear in hopes there will
#             # be a greater on, if it's not greater, we still clear it
#             # bc our curSubtr already has the current largest unique substring
#             secondElem = u_list[-1]
#             u_list.clear()

#             # we don't want to append the last of element of the previous
#             # list state if the current character being checked is the same
#             if secondElem != ch:
#                 u_list.append(secondElem)

#             # add the current char to the list after it's cleared from
#             # the line above so we don't just skip it
#             u_list.append(ch)

#     if len(u_list) > len(curSubstr):
#         curSubstr = ''.join(u_list)
#         substrLen = len(curSubstr)
#     return substrLen