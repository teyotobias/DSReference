
my_set = set()

# Creating a set with elements
my_set = {1,2,3,4,5}

# Creating a set from a list
my_set = set([1,2,3,4,5])

# Adding elements
my_set.add(6)
my_set.update([7,8,9]) # 1,2,3,4,5,6,7,8,9

# Removing a specific element (raises KeyError if not found)
my_set.remove(6)

# Removing a specific element (does not raise error if not found)
my_set.discard(10)

# Removing and returning arbitrary element
popped_element = my_set.pop()

# Removing all elements:
my_set.clear()


# SET OPERATIONS

set1 = {1,2,3}
set2 = {3,4,5}

union_set = set1 | set2 # 1,2,3,4,5
union_set = set1.union(set2) # 1,2,3,4,5

intersection_set = set1 & set2 # 3
intersection_set = set1.intersection(set2) # 3

difference_set = set1 - set2 # 1,2
difference_set = set1.difference(set2) # 1,2

# A symmetric difference set includes those that are in one, but not the other. For both.
sym_diff_set = set1 ^ set2 # 1,2,4,5
sym_diff_set = set1.symmetric_difference(set2)

# Checking membership
is_present = 2 in set1 # true

# Checking if not in the set
is_not_present = 6 not in set1 # True


# SET COMPARISONS
set1 = {1,2,3}
set2 = {1,2,3,4,5}

# Checking if set1 is a subset of set2
is_subset = set1 <= set2 # True
is_subset = set1.issubset(set2) # True

# Checking if set2 is a superset of set1
is_superset = set2 >= set1 # True
is_superset = set2.issuperset(set1)

# Iterating using a set
for element in set1:
    print(element)

# length of a set
length = len(set1)

# Copying a set
set_copy = set1.copy()

'''
Common Problems/Patterns
Duplicate Detection: Finding duplicates in arrays or strings.
Union-Find Problems: Tracking and merging sets of elements (e.g., connected components in a graph).
Hashing: Using sets to achieve average O(1) time complexity for insert and lookup operations.
Subset Problems: Finding if a set is a subset of another, or finding all subsets.
Set Operations: Problems involving union, intersection, and difference operations.
Unique Elements: Ensuring all elements are unique in a collection.
'''

