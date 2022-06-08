import re

# Search for an exact string match
# searched = re.search("ape", "The ape was at the apex")
# if searched:
#     print("There is an ape", searched)

# findall() returns a list of matches and . is used to match any 1 character or space
# # Finditer can be used to return an iterator of matches
# all_apes = re.findall("ape.", "The ape was at the apex")
# print(all_apes)
# for i in all_apes:
#     print(i)

# finditer returns an iterator of matching objects
# You can use span to get the location
# string = "The ape was at the apex"
# it = re.finditer("ape.", string)
# # print(it)
# for i in it:
#     # Span returns a tuple
#     coordinates = i.span()
#     print(f'start and end indices for this match found: {coordinates}')
#     # Slice the match out using the tuple values
#     print(string[coordinates[0]:coordinates[1]])


# Square brackets will match any one of the characters between the brackets not including upper and lowercase varieties unless they are listed
# We can also define characters in a range and define that we want to match anything except a defined number of characters
animalStr = "Cat rat mat fat pat at"
all_animals = re.findall(r"\w+at", animalStr) # [crmfp]at
for i in all_animals:
    print(i)
print()


# We can also allow for characters in a range
# Remember to include upper and lowercase letters
# some_animals = re.findall("[C-Mc-m]at", animalStr)
# for i in some_animals:
#     print(i)
# print()


# # Use ^ to denote any character but whatever characters are
# # between the brackets
# some_animals = re.findall("[^Crmp]at", animalStr)
# for i in some_animals:
#     print(i)
# print()


# # You can replace items and define pattern objects
# owl_food = "rat cat mat pat"

# # You can compile a regex into pattern objects which
# # provide additional methods
# regex = re.compile("[^mp]at")

# # sub() replaces items that match the regex in the string
# # with the 1st attribute string passed to sub
# owl_food = regex.sub("owl", owl_food)

# print(owl_food)

# # Regex use the backslash to designate special characters and Python does the same inside strings which causes issues
# # Let's try to get "\\stuff" out of a string
# rand_str = "Here is \\stuff"

# # This won't find it
# print("Find \\stuff : ", re.search("\\stuff", rand_str))

# # This does, but we have to put in 4 slashes which is
# # messy
# print("Find \\stuff : ", re.search("\\\\stuff", rand_str))

# # You can get around this by using raw strings which
# # don't treat backslashes as special
# print("Find \\stuff : ", re.search(r"\\stuff", rand_str))

