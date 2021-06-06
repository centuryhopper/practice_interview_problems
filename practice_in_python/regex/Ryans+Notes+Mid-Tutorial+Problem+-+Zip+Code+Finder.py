'''
# Create a regex that will match for 5 digit zip codes or zip codes with 5 digits a dash and
# then 4 digits. Here is sample data :
# rand_str = "12345 12345-1234 1234 12346-333"
'''
import re
#Derek's method from the video.tutorial
# has an issue, it will not find the zip if
# the last number in the string is a 5digit only zip code.
# here is a test to show it below.

# the last zip in this case is added for the ending with 5-4
rand_str = "12345 12345-1234 1234 12346-333 12346-3334"
# here is a test with a 5 digit zip code at the end
# the solution given does not give the 12346 zip
rand_str2 = "12345 12345-1234 1234 12346-333 12346-3334 12346"
# here is a test with an incorrect zip-code at the end
rand_str3 = "12345 12345-1234 1234 12346-333 12346-3334 12346-12"
regex = re.compile(r"(\d{5}-\d{4}|\d{5}\s)")
matches = re.findall(regex, rand_str)
matches2 = re.findall(regex, rand_str2)
matches3 = re.findall(regex, rand_str3)
print("5digit-4digit at end:", matches)
print("5digit at end:", matches2)
print("5digit-2digits at end:", matches3)

import re
# Here is my method where I use 3 cases as OR's | to
# find the zip codes
# case 1: the 5-4 with a word boundary
# case 2: the 5 without a slash using a negative look ahead
# case 3: the 5 with a end of string at the end for the
# case of the last zip being a 5digit only

# the last zip in this case is added for the ending with 5-4
rand_str = "12345 12345-1234 1234 12346-333 12346-3334"
# here is a test with a 5 digit zip code at the end
# the solution given (can be seen below) does not give the 12346 zip
rand_str2 = "12345 12345-1234 1234 12346-333 12346-3334 12346"
# here is a test with an incorrect zip-code at the end
rand_str3 = "12345 12345-1234 1234 12346-333 12346-3334 12346-12"
# Here is the given solution:
# regex = re.compile(r"(\d{5}-\d{4}|\d{5}\s)")
# in my solution I do either 5digits-4digits or 5digits without a -
# and use word boundaries to section off each zip code entry
# \d{5}-\d{4}\b searches for the 5digits-4digits,
# will find them at end too, see matches output
# \d{5}\b(?!-) searches for 5digits, without -,
# excluding what it does find (a space) using a look ahead.
# \d{5}\b$ searches for any 5digits at the end of the string
regex = re.compile(r"(\d{5}-\d{4}\b|\d{5}\b(?!-)|\d{5}\b$)")
matches = re.findall(regex, rand_str)
matches2 = re.findall(regex, rand_str2)
matches3 = re.findall(regex, rand_str3)
print("5digit-4digit at end:", matches)
print("5digit at end:", matches2)
print("5digit-2digits at end:", matches3)

# Derek's method from Q&A:
zc_str = "12345 12345-55555 12347-555 12346 12345-5555 12348"
# turns the zips into a list to eliminate spaces and make easier to parse
zc_list = zc_str.split()
match_list = []
# Checks if the beginning is at the there is 5 digits ^\d{5}
# then checks if there is a -4digits that may or may not
# be at the end in the submatch (-\d{4})?
# if it is isn't at the end then the 5 digits is the end $
regex = re.compile(r"^\d{5}(-\d{4})?$")
for i in zc_list:
    if regex.match(i):
        match_list.append(i)
print(match_list)

# Derek's method from Q&A but using re.findall() instead of re.match()
zc_str = "12345 12345-55555 12347-555 12346 12345-5555 12348"
zc_list = zc_str.split()
regex = re.compile(r"^\d{5}(-\d{4})?$")
match_list = []
for i in zc_list:
    if re.findall(regex, i):
        match_list.append(i)
print(match_list)