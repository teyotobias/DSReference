
# Different ways to create
my_dict = {}
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
my_dict = dict(name="Alice", age=25, city="New York")


# Accessing a value by key
name = my_dict["name"] # Alice
# Using get method to access a value
age = my_dict.get("age") # 25
# If the key does not exist, get returns None by default, or a specified value: here, 'Unknown'
country = my_dict.get("country", "Unknown") # Unknown


# Modifying a value by key
my_dict["age"] = 26 


# Adding new key-value pair
my_dict["country"] = "USA"

# Different ways to delete a key-value pair
age = my_dict.pop("age")
del my_dict["city"]
my_dict.clear()


# DICTIONARY OPERATIONS
is_name_present = "name" in my_dict # True

# Getting all keys
keys = my_dict.keys()
# Getting all values
values = my_dict.values()
# Getting all key-value pairs
items = my_dict.items()

# Iterating through keys
for key in my_dict:
    print(key)
# Iterating through values
for value in my_dict.values():
    print(value)
# Iterating through key-value pairs
for item in my_dict.items():
    print(f"Key: {key}, Value: {value}")


# BUILT-IN

length = len(my_dict)

# copying a dictionary
dict_copy = my_dict.copy()

# Merging dictionaries
other_dict = {"city": "Los Angelas", "zip": "90001"}
my_dict.update(other_dict)



'''
Common Problems/Patterns
Lookup Problems: Efficiently finding values based on keys.
Counting Problems: Using dictionaries to count occurrences of elements (e.g., frequency count, histogram).
Grouping Problems: Grouping elements based on certain properties (e.g., anagrams, categorization).
Memoization: Storing intermediate results in dynamic programming to avoid redundant calculations.
Cache Implementation: Implementing LRU (Least Recently Used) Cache.
Graph Representation: Using dictionaries to represent graphs (adjacency list).
'''

