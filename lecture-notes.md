# Lecture Notes: Sets

# #1 What are sets?
- Sets are a collection datatype in python, that can be immutable/mutable, unordered, unindexable, and all
- items within a set must be unique and 


## Characteristics:
- Unordered : Items in sets have no order and there for cannot be indexed into
- Mutable : You can change how many items a set has, and remove said items
- All elements in a set need to be unique, converting a list into a set will remove all duplicate items from the set
- All elements inside the set must be immutable

## Why bother:
- ensures elements are unique
- instantaneous membership checks
- straight forward comparison operations

## Creating Sets

```python
empty_set = set()   #define empty sets with the set() constructor since {} is a dict
print(type(empty_set))

new_set = {'one', 'two', 'three'}

pop_set = {'one', ('this','that','other'), 'three'} #sets use curly braces, items separated by commas
print(pop_set)
print(type(pop_set))



alist = ['item', 'item', 'stuff', 'thing', 'oddity']
set_list = set(alist)
alist = list(set_list) #the items will 'float' around since they don't have a specified order
print(alist)

atuple = ('item', 'item', 'stuff', 'thing', 'oddity')
set_tup = set(atuple)
atuple = tuple(set_tup)
print(atuple)

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value1'}
new_set = set(my_dict.values())
print(new_set)
```

# #2 Looping

```python
#Loop over sets the same way we loop over lists and tuples

aset = {'apple', 'orange', 'banana'}

for fruit in aset: #may see the items in random order due to the unordered nature of sets
    print(fruit)

#cant use a while loop to loop over sets, because sets dont have indices
```

# #3 Set Methods

- Membership checks on sets : check to see if item in set, return True or False
    - One of the primary reasons we use sets, because this happens instantaneously

```python

my_set = {'superman', 'batman', 'wonder woman', 'the flash'}

print('superman' in my_set) #True
```

- `set.add(item)` : add items to a set
```python
#If you try to add a duplicate item, it simply gets ignored
my_set.add('green lantern')
print(my_set)

my_set.add('superman') #nothing happens, already exists in the set
print(my_set)
```

- `set.update(iterable)` : will add all the items of that iterable (set, tuple, string, list, dict) to my set
```python
marvel = ['iron man', 'thor', 'loki', 'dr. strange']
my_set.update(marvel)
print(my_set)

movies = {'Avenger': 'Endgame', 'Far From Home': 'Spider-Man', 'Dark Knight': 'Batman'}
my_set.update(movies.keys()) # .keys(), .values() , .items() adds kvps as a tuple
print(my_set)
```

- `set.remove(item)` : removes an item from the set, will throw an KeyError if the item does not exist in the set
```python
my_set.remove('loki')
print(my_set)

#my_set.remove('Thanos') #throws KeyError
```

- `set.discard(item)` : removes an item from the set, without throwing an error if the item doesn't exist
```python
my_set.discard('green lantern')
print(my_set)

my_set.discard('Thanos') #nothing happens
```


- `set.pop()` : removes a random item from the set and returns it
    - cant specify items, will throw a TypeError if you pass in an arg
```python
rand = my_set.pop()
print(rand)
print(my_set)
```

- `set.clear()` : removes all items
```python
my_set.clear()
print(my_set)
```

# #4 Advanced Sets

## Advnaced set methods

Methods used to compare 2 sets

- `set1.issubset(set2)` : returns True if all items from set1 can be found in set 2 else False
```python
set1 ={1,2,3,4}
set2 = {1,2,3,4,5,6,7}

print(set1.issubset(set2)) #True
```

- `set1.issuperset(set2)` : returns True if set1 contains all items from set2 else False
```python
set1 ={1,2,3,4}
set2 = {1,2,3,4,5,6,7}

print(set1.issuperset(set2)) #False
```

- `set1.isdisjoint(set2)` : Returns True if there no common items between the sets
```python
set1 = {1,2,3,4}
set2 = {1,2,3,4,5,6,7}

print(set1.isdisjoint(set2))


fruit_set = {'apple', 'banana', 'pear'}
veg_set = {'carrots', 'potatos', 'broccoli'}

print(fruit_set.isdisjoint(veg_set))


#tuples : ()
#lists : []
#sets : {item}
#dictionaries : {key:value}
```

# #5 Set Operations

We can merge sets very 'specifically'

```python
# We'll work with these two example sets
set1 ={-1,0,1,2,3,4}
set2 = {1,2,3,4,5,6,7}
```

- `set1.union(set2)` : returns set of all items from set1 and set2
     - does not effect original sets
```python
new_set = set1.union(set2)
print(new_set)
```

- `set1.intersection(set2)` : return set of all the items set1 and set2 have in common
```python
intersect = set1.intersection(set2)
print(intersect)
```

- `set1.difference(set2)` : return all the items from set1 that are different from the items in set2
```python
diff_set = set1.difference(set2)
print(diff_set)
```

- `set1.symetric_difference(set2)` : returns a set of all the items from both sets that don't overlap (not in common)
```python
sym_diff_set = set1.symmetric_difference(set2)
print(sym_diff_set)

sym_diff_set.add(10)
print(sym_diff_set)

set1.symmetric_difference_update(set2) # Does the same things as .symetric_difference, however instead of returning a new set, this particular method actually alters/updates the original set the method is applied to
print(set1)
```