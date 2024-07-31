
# Looping over sets is the same way we loop over lists or tuples, just don't have indexes or indecies

aset = {'apple', 'banana', 'orange'}

for fruit in aset: # we may see the items in a random order due to the unordered nature of sets
    print(fruit)


# We can't loop over sets with a while loop, because sets don't have indecies

# print(aset[1]) # we should get a TypeError, we can't index into sets!

alist = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

i = 0 # represents the index I want to access at each iteration of my while loop
while i < len(alist):
    print(alist[i])
    i += 1

# Can't do this with sets, because they are unordered and have no indexes to access