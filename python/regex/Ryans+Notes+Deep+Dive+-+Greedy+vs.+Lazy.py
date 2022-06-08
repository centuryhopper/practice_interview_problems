import re

rand_str = """some something sometimes somewhere someplace somewhat
somebody sometime someone somehow someday someway"""

# ============================================================
# Greedy: *
regex = re.compile(r"some*")
matches = re.findall(regex, rand_str)
print(matches)
# Only outputs some for all words
# ['some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some']

# Greedy: ?
regex = re.compile(r"some?")
matches = re.findall(regex, rand_str)
print(matches)
# Only outputs some for all words
# ['some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some']

# Greedy: +
regex = re.compile(r"some+")
matches = re.findall(regex, rand_str)
print(matches)
# Only outputs some for all words
# ['some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some']
# ============================================================
# Greedy: .*
regex = re.compile(r"some.*")
matches = re.findall(regex, rand_str)
print(matches)
# Outputs the entire string up until a newline
# ['some something sometimes somewhere someplace somewhat', 'somebody sometime someone somehow someday someway']

# Greedy: .+
regex = re.compile(r"some.+")
matches = re.findall(regex, rand_str)
print(matches)
# Outputs the entire string up until a newline
# ['some something sometimes somewhere someplace somewhat', 'somebody sometime someone somehow someday someway']

# Greedy: .?
regex = re.compile(r"some.?")
matches = re.findall(regex, rand_str)
print(matches)
# Only outputs some or someX
# ['some ', 'somet', 'somet', 'somew', 'somep', 'somew', 'someb', 'somet', 'someo', 'someh', 'somed', 'somew']
# ============================================================
# Lazy: *?
regex = re.compile(r"some*?")
matches = re.findall(regex, rand_str)
print(matches)
# Only outputs som for all words
# ['som', 'som', 'som', 'som', 'som', 'som', 'som', 'som', 'som', 'som', 'som', 'som']

# Lazy: +?
regex = re.compile(r"some+?")
matches = re.findall(regex, rand_str)
print(matches)
# Only outputs some for all words
# ['some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some']

# Lazy: ??
regex = re.compile(r"some??")
matches = re.findall(regex, rand_str)
print(matches)
# Only outputs som for all words
# ['som', 'som', 'som', 'som', 'som', 'som', 'som', 'som', 'som', 'som', 'som', 'som']
# ============================================================
# Lazy: .*?
regex = re.compile(r"some.*?")
matches = re.findall(regex, rand_str)
print(matches)
# Only outputs some for all words
# ['some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some']

# Lazy: .+?
regex = re.compile(r"some.+?")
matches = re.findall(regex, rand_str)
print(matches)
# Only outputs some or someX
# ['some ', 'somet', 'somet', 'somew', 'somep', 'somew', 'someb', 'somet', 'someo', 'someh', 'somed', 'somew']

# Lazy: .??
regex = re.compile(r"some.??")
matches = re.findall(regex, rand_str)
print(matches)
# Only outputs some for all words
# ['some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some', 'some']
# ============================================================
# +t?
regex = re.compile(r"some+t?")
matches = re.findall(regex, rand_str)
print(matches)
# Only outputs some or somet
# ['some', 'somet', 'somet', 'some', 'some', 'some', 'some', 'somet', 'some', 'some', 'some', 'some']

# +t*
regex = re.compile(r"some+t*")
matches = re.findall(regex, rand_str)
print(matches)
# Only outputs some or somet
# ['some', 'somet', 'somet', 'some', 'some', 'some', 'some', 'somet', 'some', 'some', 'some', 'some']

# +t?
regex = re.compile(r"some+t?")
matches = re.findall(regex, rand_str)
print(matches)
# Only outputs some or somet
# ['some', 'somet', 'somet', 'some', 'some', 'some', 'some', 'somet', 'some', 'some', 'some', 'some']

# +t{0,4}
regex = re.compile(r"some+t{0,4}")
matches = re.findall(regex, rand_str)
print(matches)
# Only outputs some or somet
# ['some', 'somet', 'somet', 'some', 'some', 'some', 'some', 'somet', 'some', 'some', 'some', 'some']
# ============================================================
# \w
regex = re.compile(r"some\w")
matches = re.findall(regex, rand_str)
print(matches)
# Only outputs the words with some and a letter after some as someX (not some only)
# ['somet', 'somet', 'somew', 'somep', 'somew', 'someb', 'somet', 'someo', 'someh', 'somed', 'somew']

# \w+
regex = re.compile(r"some\w+")
matches = re.findall(regex, rand_str)
print(matches)
# Only outputs the words with some and a letter after some, as the entire word (not some only)
# ['something', 'sometimes', 'somewhere', 'someplace', 'somewhat', 'somebody', 'sometime', 'someone', 'somehow', 'someday', 'someway']

# \w{0,10}
regex = re.compile(r"some\w{0,10}")
matches = re.findall(regex, rand_str)
print(matches)
# Outputs all words (since there is less than 10 letters after some)
# ['some', 'something', 'sometimes', 'somewhere', 'someplace', 'somewhat', 'somebody', 'sometime', 'someone', 'somehow', 'someday', 'someway']

# \w?
regex = re.compile(r"some\w?")
matches = re.findall(regex, rand_str)
print(matches)
# Only outputs some or someX
# ['somet', 'somet', 'somew', 'somep', 'somew', 'someb', 'somet', 'someo', 'someh', 'somed', 'somew']

# \w*
regex = re.compile(r"some\w*")
matches = re.findall(regex, rand_str)
print(matches)
# Outputs all words
# ['some', 'something', 'sometimes', 'somewhere', 'someplace', 'somewhat', 'somebody', 'sometime', 'someone', 'somehow', 'someday', 'someway']