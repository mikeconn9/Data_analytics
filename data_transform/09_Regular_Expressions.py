# Metacharacters
# '.': Any character; '^': Start of a string; '$': End of a string. 
# Example: r"^gr.y$": Start with a 'g', end with a 'y'

import re

#word = input()

pattern = r"^m..e$" # 4 characters, starting with a 'm', end with a 'e'

if re.match(pattern, "mine"):
    print("Match")
else:
    print("No match")

# Character Classes
# Provide a way to match only one of a specific set of characters.
# Also range, such as [A-Za-z], [0-9].
# [1-5][0-9]: Match any two-digit number from 10 to 59
# ^ at the start of a character class to invert it. Example: r"[^A-Z]", excludes uppercase strings.
# Please differentiate with starting with a uppercase character: r"^[A-Z]".

pattern1 = r"[aeiou]"

if re.search(pattern1, "gray"):
    print("Match 1")

# More Metacharacters: +, ?, { and }.
# Means "zero or more repetitions of the previous thing", it tries to match as many repetitions as possible.
# The "previous thing" can be a single character, a class, or a group of characters in parentheses.
# pattern = r"egg(spam)*": Strings start with "egg" and follow with zero or more "spam"s.
# +: ONE or more repetitions. *: ZERO or more repetitions.
# (?:42)+: matches strings that contain one or more 42s.
# Lookahead Assertions (?=): Ensure conditions without consuming characters in the string.
# Lookahead assertions are an advanced feature in regular expressions that allow you to check for the presence (or absence) 
# of specific patterns ahead in the input string without consuming any characters. This makes them useful for 
# validating conditions or combining multiple requirements in a single pattern.
# For example, Positive Lookahead ((?=...)):
# 1. Ensures that the specified pattern ... exists AHEAD in the string.
# 2. Does not consume or "match" the characters in the lookahead, meaning the regex continues checking 
# the rest of the pattern from where it left off.

# ----How Lookahead Works----
# A lookahead is like a checkpoint: it looks forward in the string to verify a condition 
# but doesn't actually move the regex pointer forward.
# After the lookahead, the regex engine continues matching from where it was before the lookahead started.
    
                      
pattern1 = r"(?:42)+"

if re.search(pattern1, "ab42d"):
    print("Match 2")

# ?: Means zero or one repetitions.
# {x,y} means "between x and y repetitions of something". {1,0} is the same as '+'.
# If x is missing, it is taken to be zero. If y is missing, it is taken to be infinity.

#=============================================
#How to write a pattern:
# Example: Write a pattern for a string with at least one uppercase letter, one digit.
# Step 1: Write the start/end: r"^$"
# Step 2: Write a lookahead for one uppercase letter. So the scan only look for the pattern 
# but not "move the pointer". (?=.*[A-Z]): Any number of characters but at least one uppercase letter.
# Step 3: Write a lookahead for a digit: (?=.*[0-9]).
# Step 4: Any number of characters after them. .+
# Step 5: Concatenate them together.

password = input()
pattern = r"^(?=.*[A-Z])(?=.*\d).+$"

if re.match(pattern, password):
    print("Password created")
else:
    print("Wrong format")



#===========Groups=====================
import re

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")

if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())

#1. Named groups: (?P<name>...), same as normal group except that they can be accessed by group(name)

#2. Capturing groups: (....): 
#Captures the part of the string that matches pattern.
#Captured groups are numbered in the order of their opening parentheses, starting from 1.

import re

text = "Name: John, Age: 25"
pattern = r"Name: (\w+), Age: (\d+)"  # Two capturing groups
match = re.search(pattern, text)

if match:
    print(match.group(1))  # Output: John (first group)
    print(match.group(2))  # Output: 25 (second group)

#Non-capturing groups: (?...): These group a part of the pattern without saving the matched content for later use. 
# Useful when grouping is needed but capturing is unnecessary.

#Example1:
import re

text = "hello123"
pattern = r"(?:hello)\d+"  # Non-capturing group for 'hello'
match = re.match(pattern, text)

if match:
    print(match.group())  # Output: hello123 (no separate group captured)

#Example2:
import re

text = "hello hello world"
pattern = r"(\b\w+\b) \1"  # Matches a repeated word
match = re.search(pattern, text)

if match:
    print(match.group(1))  # Output: hello

#Example3:
pattern = r"(?P<first>abc)(?:def)(ghi)"

match = re.match(pattern, "abcdefghi")

if match:
    print(match.group("first"))
    print(match.groups()) #Output: ('abc', 'ghi')

#Example4:
import re
pattern = r"(a)(b(?:c)(d)(?:e))"

match = re.match(pattern, "abcde")

if match:
    len(match.groups())

#===========Special Sequences=====================
#1. \n: This matches the expression of the group of that number.

#Example1:
import re

pattern = r"(.+)\1"

match = re.match(pattern, "word word") #Output: Match

match = re.match(pattern, "?! ?!") #Output: Match

#2. \d: digits; \s: Whitespace; \w: Word characters
# \D: The opposite to the lower-casea versions. This matches anything that isn't a digit.

#3. \A, \Z: Match the beginning and end of a string, respectively.
#\b: matches the empty string between \w and \W characters. Informally, it represents the boundary between words.
# "\b(cat)\b": Basically matches the word "cat" surrounded by word boundaries. It matches " cat ", ">cat<", but not "scattered".
#\B: matches the empty string anywhere else.

#=================Quantifiers=================
#1. {}: The curly braces {} in regular expressions are quantifiers. They specify how many times the preceding element 
# (character, group, or character class) must appear.

#Summary Table
#Pattern	Description
#a{3}	Exactly 3 as
#a{2,4}	Between 2 and 4 as
#a{3,}	At least 3 as
#a{,3}	At most 3 as