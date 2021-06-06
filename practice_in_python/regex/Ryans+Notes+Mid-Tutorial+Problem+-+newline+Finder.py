'''
On Windows newlines are some times \n and other times \r\n
Create a regex that will grab each of the lines in this string,
print out the number of matches and each line.
'''
# regular expressions module
import re
# string to check for newlines and print line by line
long_str = '''Just some words
and some more\r
and more
'''
# matching normal character "\w" and space " "
# potentially there will be a newline, but using \n,
# prints an extra newline when running the loop below though
# instead I use carriage returns \r as the potential extra
# character which find the lines correctly because each
# line will always start after a carriage return
matchesrn = re.findall("[\w ]+[\r]?", long_str)
# See the matchesrn list
print(matchesrn)
# print the number of newline matches
print("newline Matches:", len(matchesrn))
# print the long_str line by line
for i in matchesrn:
    print(i)