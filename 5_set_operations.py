from helper import d

# We can merge sets of data together very 'specifiaclly'

set1 = {-1, 0, 1, 2, 3, 4}
set2 = {1, 2, 3, 4, 5, 6, 7}

#-- set1.union(set2) : return a new set of all items from set1 and set2
# Does not affect the original sets
new_set = set1.union(set2)
print(new_set)

d()

#-- set1.intersection(set2) : return a new set of all items set1 and set2 have in common
intersect = set1.intersection(set2)
print(intersect)

d()

#-- set1.difference(set2) : return a new set of all the items from set1 that are different from set2
print(set1.difference(set2))
print(set2.difference(set1))

d()

#-- set1.symetric_difference(set2) : returns a set of all items from both sets that do not overlap (not in common)

sym_diff_set = set1.symmetric_difference(set2)
print(sym_diff_set)

d()

#-- set1.symetric_difference_update(set2) # does the same thing as .symetric_difference, however instead of returning a new set, this particular method actually updates/alters the original set the method is applied to

print(set1)
set1.symmetric_difference_update(set2)
print(set1)


d()
#-------------------------------------------

player1 = {'pikachu', 'charizard', 'mewtwo', 'squirtle'}
player2 = {'starme', 'baulbasaur', 'pikachu', 'ditto', 'evee', 'mewtwo'}

# print(player1.symmetric_difference(player2))
print(player1.difference(player2)) # cards from player1 collection that are different from player2
print(player2.difference(player1))