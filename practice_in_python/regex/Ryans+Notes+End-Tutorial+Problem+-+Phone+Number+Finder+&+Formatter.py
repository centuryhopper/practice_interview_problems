'''
For your final Python / Regex problem I want you to match all of the following phone numbers and then print them.
rand_str = "14125551212 4125551212 (412)5551212 412 555 1212 412-555-1212 1-412-555-1212"
'''
import re
rand_str = "14125551211 4125551212 (412)5551213 412 555 1214 412-555-1215 1-412-555-1216"
# [1\(\-]? checks for a 1,(, or - at the beginning that may or may not be there
# (\d{3}) sub-matches first 3 digits - area code
# [ \-\)]? checks for a space, -, or ) that may or may not be there
# (\d{3}) sub-matches 3 digits
# [ \-]? checks for a space or - that may or may not be there
# (\d{4}) sub-matches last 4 digits
regex = re.compile(r"[1\(\-]?(\d{3})[ \-\)]?(\d{3})[ \-]?(\d{4})")
matches = re.findall(regex, rand_str)
for i in matches:
    # formats to output as ###-###-####
    print(f"{i[0][0:3]}-{i[1][0:3]}-{i[2][0:4]}")

