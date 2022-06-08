
# doesnt work for n // k
# import struct

# def findMajority(lst, n, k) -> int:
#     int_size = struct.calcsize('i') * 8
#     # print(int_size)
#     num = 0

#     # loop through all the bits of number
#     for i in range(int_size):
#         cnt = 0
#         # loop to iterate through all elements in array
#         # to count the total set bit at position i
#         for j in range(n):
#             if lst[j] & (1 << i):
#                 cnt += 1
#         # if the total set bits exceeds n//k,
#         # this bit should be present in chosen element
#         print('cnt:', cnt)
#         if cnt > (n//k):
#             print(1 << i)
#             num += (1 << i)
#     count = 0
#     # print(num)

#     # iterate through array,
#     # get the count of candidate n//k elementt
#     for i in range(n):
#         if lst[i] == num:
#             count += 1
#     if count > (n//k):
#         print(num)
#     else:
#         print('n/k element not present')
# if __name__ == '__main__':

#     findMajority([1,1,3,6,6,6,6,6,9], 9, 3)
