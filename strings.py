
my_string = "Hello, World!"
multiline_string = """ This is a
multiline string!
"""

first_char = my_string[0]
last_char = my_string[-1]

concatenated_string = "Hello" + "World!"

repeated_string = "Hello" * 3 # HelloHelloHello

# Slicing
substring = my_string[:5] # "Hello"
substring = my_string[0:5] # "Hello"

# Modifying

new_string = my_string.replace("World", "Python")

# Converting to upper/lower case
upper_string = my_string.upper()
lower_string = my_string.lower()

# String Methods
words = my_string.split(", ") #['Hello', 'World!']
joined_string = " ".join(words) # "Hello World!"

# Stripping whitespace
stripped_string = "    Hello   ".strip() # "Hello"

# finding substrings
index = my_string.find("World") # 7

# using f-strings
name = "Alice"
formatted_string = f"Her name is {name}!"

formatted_string = "Her name is {}!".format(name)

# length
length = len(my_string)

# Checking if all characters are alphanumeric: letters or numbers, non-example: &,$,@,-,%,*, and empty space
is_alphanumeric = my_string.isalnum() # False because of '!'

# Checking if all characters are alphabetic:
is_alpha = my_string.isalpha() # False

# Iterating using a for loop:
for char in my_string:
    print(char)


"""
Common Problems/Patterns
Palindrome Problems: Checking if a string reads the same backward and forward.
Anagram Problems: Checking if two strings are anagrams.
Substring Search: Finding if a string contains a substring.
String Matching: Implementing algorithms like Knuth-Morris-Pratt (KMP), Rabin-Karp, etc.
Pattern Matching: Using regular expressions to find patterns in strings.
String Manipulation: Problems involving reversing strings, finding permutations, etc.
Dynamic Programming on Strings: Problems like longest common subsequence, edit distance, etc.
"""