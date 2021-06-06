'''
Find all of the following real email addresses in this sample data.
rand_str = "d+b@aol.com a_1@yahoo.co.uk A-100@m-b.INTERNATIONAL"
'''
import re
rand_str = "d+b@aol.com a_1@yahoo.co.uk A-100@m-b.INTERNATIONAL failtry@r. failtry2@e helloworld@ shouldnotshow"
regex = r"([\w\+\-]+)@([\w\+\-]+)\.([\w\-\+\.]+)"
rand_str_list = rand_str.split()
match_list = []
for i in rand_str_list:
    if re.search(regex, i):
        match_list.append(i)
for i in match_list:
    print(i)