import re

# exercises

# python tut 28 verify for the valid email address
# email_lst = 'db@aol.com m@.com @apple.com db@.com'
# lst =  re.findall('[a-zA-Z0-9._%+-]{1,20}@[a-zA-Z0-9.-]{2,20}.[a-zA-Z]{2,3}' , email_lst)
# print(lst)

# python tut 29
# s = "doctor doctor' doctors doctors''' doctor''''sss doctor's's's's's''''ss's'sssssss"
# reg = re.compile("[doctor]+['s]+")
# matches = re.findall(reg, s)
# print(matches)

# s = "cat cats catercats"
# reg = re.compile("[cat]+s?")
# matches = re.findall(reg, s)
# print(matches)

# python tut 30
s = '412-555-1212 412-555-1213 412-555-1214'
# s = '412-555-1212'
# reg = re.compile("[\d]{3,4}")
# reg = re.compile("412-(.{8})")
# reg = re.compile(r"412-([^\s]{8})") # 412-([^\s]*)-([^\s]*)
# matches = re.findall(reg, s)
# print(matches)



# python tut 32
# s = "12345 12345-1234 1234 12346-333"
# reg = re.compile("(\d{5}-\d{4}|\d{5}\s)")
# matches = re.findall(reg, s)
# print(matches, 'size = ', len(matches))

# s = "d+b@aol.com a_1@yahoo.co.uk A-100@m-b.INTERNATIONAL"
# reg = re.compile("[\w._%+-]+@[\w.-]+\.[a-zA-Z]+")
# matches = re.findall(reg, s)
# print(matches, 'size = ', len(matches))


# 14125551212 4125551212 (412)5551212 412 555 1212 412-555-1212 1-412-555-1212
# not so optimized regex for the string above:
# (1\d{10}|\d{10}|\(\d{3}\)\d{7}|\d{3}\s\d{3}\s\d{4}|(1-)?\d{3}-\d{3}-\d{4})
# slightly more optimized regex
# (1?\d{10}|\(\d{3}\)\d{7}|(1-)?\d{3}(\s|-)?\d{3}(\s|-)?\d{4})
s = "14125551212 4125551212 (412)5551212 412 555 1212 412-555-1212 1-412-555-1212"
reg = re.compile(r"(1?\d{10}|\(\d{3}\)\d{7}|(1-)?\d{3}(\s|-)?\d{3}(\s|-)?\d{4})")
matches = re.findall(reg, s)
print(matches, 'size = ', len(matches))




