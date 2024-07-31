from helper import d
# Python Sets

# What are sets?

# Sets are a collection data type, mutable, unordered, unindexible
# All items in a set must be unique

#-- Characteristics
# Unordered : Items in sets have no order and therefore cannot be indexed into
# Mutable : you can change how many items a set has, we can add/remove items
# All elements in a set must be unique, converting a list into a set will remove all duplicate items from the set
# All items in a set must be immutable (strings, tuples, numbers?)

#-- Why bother?
# We can ensure the elements are unique
# Instantaneous membership checks
# Straight forward comparison operations

empty_set = set() # We use the set() constructor since {} already represent an empty dictionary
print(type(empty_set))

# dictionary data structure- key : value
# Sets are structured differently. Sets are just a collection of data, each separated by a comma
new_set = {'one', 'two', 'three'}
print(type(new_set))

d()

# Converting a list into a set to remove duplicate data, then back into a list
alist = ['item', 'item', 'stuff', 'thingy', 'oddity'] 
print(alist)
set_list = set(alist) # type casting my list into a set to remove duplicate data
print(set_list)

alist = list(set_list)
print(alist)

d()

# Converting a tuple into a set to eliminate duplicate data, then back into a tuple
atuple = ('item', 'item', 'stuff', 'thingy', 'oddity')
print(atuple)
set_tup = set(atuple) # duplicate data is now removed
print(set_tup)

atuple = tuple(set_tup)
print(atuple)

d()

# Converting a dictionary into a set, can't convert it back into a dictionary

my_dict = {
    'key1': 'value1',
    'key2': 'value2',
    'key3': 'value1'
}

# .values() : provides only the values stored in a dictionary
new_set_values = set(my_dict.values())
print(f"new_set_values: {new_set_values}")

# .keys() : provides only the keys from a dictionary
new_set_keys = set(my_dict.keys())
print(f"new_set_keys: {new_set_keys}")

# .items() : provides tuples of both key and value for each key : value pair in the dictionary
new_set_items = set(my_dict.items())
print(f"new_set_items: {new_set_items}")

# reminder
# my_dict['keys2'] # represents the data stored at that key --> 'value2'