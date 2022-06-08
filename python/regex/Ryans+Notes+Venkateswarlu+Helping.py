#1) here i said not to take @ but it prints @ in output ,but  i don't need @ to be printed in output,how can i solve this ?
import re
rand_str = "@ Get this @ string"
# creating a list of items that split ever @ and space "@ "
rand_str = rand_str.split("@ ")
# empty list for matches
matches = ""
# compile words with a word boundary and end of string
# or word with a word boundary and a space at the end of the string
regex = re.compile(r"(\w.*\b$|\w.*\b\s$)")
# adds each match to the string as it loops through the string
for i in rand_str:
    if regex.match(i):
        matches += i
print(matches)

# using a simple word finder regex and .join()
import re
str_1 = "@ Get this @ string"
#regex = re.compile(r"[A-Za-z0-9]+") #could use this only for letter and numbers
regex = re.compile(r"\w+")
matches = re.findall(regex, str_1)
matches = ' '.join(matches)
print(matches)

#2) sir , i need to print all the words starting with 'a' (from str_1 , mentioned above), how can i do this?
import re
str_1 = "I am Arun and, I am working as a full stack developer"
# looking for words that start with a or A
regex = re.compile(r"\b[aA]\w*")
matches = re.findall(regex, str_1)
print("Matches :", len(matches))
print(matches)

#Dereks solution to 1)
import re
rand_str = "@ Get this @ string"
regex = re.compile(r"[^A-Za-z]+\s?")
rand_str = regex.sub(" ", rand_str)
print(rand_str)