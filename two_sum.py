



# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# example nums = [2, 7, 11, 15], target = 9  => 2 + 7 = 9 =>  indices: [0,1]

def twoSum(lst , target):
    hashmap = {}

    for idx, num in enumerate(lst):
        complement = target - num

        # if found from the past
        if complement in hashmap:
            return [hashmap[complement], idx]
        # add to hashmap for record keeping
        else:
            hashmap[num] = idx
    # if not found, return empty list
    return []


















# def twoSum(lst : list, target: int) -> list:
#     lo , hi = 0, len (lst) - 1
#     print('lo: {}, hi: {}'.format(lo, hi))

#     # capture original list and tuple it so there's no reference
#     # between the original list and the tmp list
#     tmp = tuple(lst)

#     # sort the real list to get algorithm to work
#     lst.sort()
#     while lo < hi:
#         first, second = lst[lo], lst[hi]
#         sum = first + second
#         if sum > target:
#             hi -= 1
#         elif sum < target:
#             lo += 1
#         # if found
#         if sum == target:
#             a, b = tmp.index(lst[lo]), tmp.index(lst[hi])
#             if a == b:

#                 return [tmp.index(lst[lo]), tmp.index(lst[hi])]
#     return []



