'''
Get just the numbers minus the area codes from this string to solve this problem.
'''
import re
rand_str = "412-555-1212 412-555-1213 412-555-1214"
# outputs all of the characters after "412-" that are either a "0-9" or "-"
# using the + will output the criteria up until a break in 0-9 or -,
# then move onto the next iteration
regex = re.compile("412-([0-9-]+)")
matches = re.findall(regex, rand_str)
for i in matches:
    print(i)