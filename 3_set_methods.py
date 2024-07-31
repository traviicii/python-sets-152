from helper import d

# Set Methods

my_set = {'superman', 'batman', 'wonder woman', 'the flash'}
print('superman' in my_set)

if 'superman' in my_set:
    print("Hell yeah he is!")

d()

#-- set.add(item) : adds an item to a set
# if you try to add duplicate items to a set, it will simply be ignored
my_set.add('green lantern')
print(my_set)

my_set.add('superman') # nothing happens, already exists in the set
print(my_set)

d()

#-- set.update(iterable) : will add all items of that iterable (set, tuple, lists, dictionaries)
marvel = ['iron man', 'thor', 'loki', 'dr. strange']

my_set.update(marvel)
print(my_set)

movies = {'Avenger': 'Endgame', 'Far From Home': 'spider-man', 'Dark Knight': 'Batman'}
my_set.update(movies.items()) # .keys(), .values(), .items() <--- .items() add key:value pairs as tuples
print(my_set)

d()

#-- set.remove(item) : remove an item from the set, will throw a KeyError if the item doesn't exist in the set

my_set.remove('loki')
print(my_set)
print('loki' in my_set)

# my_set.remove('thanos') # throws a KeyError

d()

#-- set.discard(item) : remove an item from a set, without throwing a KeyError if the item doesn't exist in the set

my_set.discard('thanos') # nothing happens
my_set.discard('the flash')
print(my_set)
print('the flash' in my_set)

d()

#-- set.pop() : removes a random item from the set and returns it
# can't specify items, will throw a TypeError if you try to pass in an argument
rand_item = my_set.pop()
print(rand_item)
print(my_set)

d()

#-- set.clear() : removes all items from a set
my_set.clear()
print(my_set)