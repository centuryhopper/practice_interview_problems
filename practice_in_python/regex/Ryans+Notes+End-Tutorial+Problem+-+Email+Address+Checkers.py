'''
1. 1 to 20 lowercase and uppercase letters, numbers, plus ._%+-
2. An @ symbol
3. 2 to 20 lowercase and uppercase letters, numbers, plus .-
4. A period
5. 2 to 3 lowercase and uppercase letters
'''

import re
email_list = "db@aol.com m@.com @apple.com db@.com"

# This way checks for each instance of a valid email address and displays them
print("Display valid email addresses method:")
# Have to use \. and \- to search for the period and subtraction sign in re.findall()
for i in re.findall("[\w\._%+\-]{1,20}@[\w\.\-]{1,20}\.\D{1,3}", email_list):
    print(i, "is a valid email address")

print()

# This method turns each email into a list index and then checks
# each email individually to determine if it is valid or not
# then prints the email and if it is valid or not
print("Display all email addresses and if they are valid method using .split():")
email_list = email_list.split()
for i in email_list:
    # Have to use \. and \- to search for the period and subtraction sign in re.search()
    if re.search("[\w\._%+\-]{1,20}@[\w\.\-]{1,20}\.\D{1,3}", i):
        print(i, "is a valid email address")
    else:
        print(i, "is an invalid email address")

print()

print("Display all email addresses and if they are valid method without .split():")
email_list = "db@aol.com m@.com @apple.com db@.com"
# starts from the 0th index in email_list when iterating
# the through the string to find the space's indexes in the string
current_index = 0
# Empty list for indexes of the spaces in the string
space_index_list = []
# Checks for spaces creates index_list for the indexes of the spaces
# adds 1 index per loop
for i in email_list:
    if i.isspace():
        space_index_list.append(current_index)
    current_index += 1

# Checking from the beginning of the email_list
# this gets increased to be the index of the space as
# it checks through the string for emails
first_letter_index = 0
# This will be to check if all of the spaces have been
# found and the words before them checked if email is valid
# it is increased by 1 each loop, so at the end it will correspond
# to having 1 word left to check
space_index_length_check = 1
# This checks the total length of the list of space indexes for the last
# word check with space_index_length_check
space_index_length = len(space_index_list)
# Loops through each index value of the email_list that is a space and checks
# if the emails are valid
for i in space_index_list:
    # Set the end index to the spaces index "i" for each loop iteration
    # this will be the last index of the word
    current_index = i
    # Handles the first word, checks from the beginning of the string to the first space
    # The first_letter_index is increased to be i (the space) after each loop iteration
    if first_letter_index == 0:
        if re.search("[\w\._%+\-]{1,20}@[\w\.\-]{1,20}\.\D{1,3}", email_list[first_letter_index:current_index]):
            print(email_list[first_letter_index:current_index], "is a valid email address")
        else:
            print(email_list[first_letter_index:current_index], "is an invalid email address")
    # Handles cases after the first word, except for the last word.
    # checks from the previous space (first_letter_index in this case)
    # to the next space (current_index in the case).
    elif first_letter_index != 0:
        if re.search("[\w\._%+\-]{1,20}@[\w\.\-]{1,20}\.\D{1,3}", email_list[first_letter_index:current_index]):
            print(email_list[first_letter_index:current_index], "is a valid email address")
        else:
            print(email_list[first_letter_index:current_index], "is an invalid email address")
    # Handles the last word by seeing if the space_index_length_check (which increases by 1 each loop iteration
    # match the space_index_length which is a static value (the number of spaces in the string).
    # This then runs from the last space (i+1) to the end of the email_list (which is the len)
    if (space_index_length_check == space_index_length):
        if re.search("[\w\._%+\-]{1,20}@[\w\.\-]{1,20}\.\D{1,3}", email_list[i+1:len(email_list)]):
            print(email_list[i+1:len(email_list)], "is a valid email address")
        else:
            print(email_list[i+1:len(email_list)], "is an invalid email address")
    # Each loop iteration this increases by 1 so that the list length and the index check matches
    # to let the program know it is on the last word
    space_index_length_check += 1
    # This sets the first letter of the next email at the end of the loop to the index of the space + 1
    first_letter_index = i+1