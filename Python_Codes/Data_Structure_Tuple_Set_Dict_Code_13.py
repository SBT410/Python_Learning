# Data Structure - TUPLE

my_tuple = (10, 30, 20, 10)
print(my_tuple) # Ordered # Allow Duplicates
print(my_tuple[3]) # Indexed
#my_tuple[3] = 55
#print(my_tuple) # Immutable(Not allowed, Not Editable)
#my_tuple.remove() #(Not allowed)
#my_tuple.pop()    #(Not allowed)
#my_tuple.add()    #(Not allowed)
print(sorted(my_tuple)) # Output of this function will be list not tuple


# Data Structure - SETS

my_sets = {10, 30, 20, 10}
print(my_sets) # Unordered # Duplicates Not allowed
#print(my_sets[0]) # Indexing not allowed
my_sets.remove(20)
print(my_sets) # Mutable

# Set Methods

new_sets = {10, 20, 30, 40}
new_sets.add(50)         # to add single value
new_sets.add(10)         # It will ignore coz duplicate in not allowed
new_sets.update('Hi')    # for string
#new_sets.update([1, 2])  # for lists
new_sets.update({5, 55}) # for sets
print(new_sets)

new_sets = {10, 20, 30, 40}
#new_sets |= {1, 2} # Short cut for update function
#new_sets.remove(10)
#new_sets.remove(100) # Code will failed if we use value which is not present in sets
new_sets.discard(100) # we will not get any error with this function
print(new_sets)

# Math Operator in Sets
# Mathematical Operations

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
print(set1.union(set2))  # Unique value from both set, it will remove duplicate if any
print(set1 | set2)       # Short cut for union
print(set1)              # we are not changing the original value of any of the sets
print(set2.intersection(set1)) # common value from both of the sets (sharing same in both sets)
print(set1 & set2)       # Short cut for intersection
print(set1.difference(set2)) # return the value that are in set1 but not in set2
print(set1 - set2)       # Short cut for difference
print(set2 - set1)       # Return value will change if we change the variables side
print(set1.symmetric_difference(set2)) # return non shared value from both the sets
print(set1 ^ set2)       # Short cut for symmetric_difference


# Relationship Methods in Sets

set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
set3 = {30, 40, 50, 60}
set4 = {5, 6}
print(set1.issubset(set2))
print(set2.issubset(set3))
print(set1.issuperset(set2))
print(set2.issuperset(set3))
print(set1.isdisjoint(set2))
print(set3.isdisjoint(set4))


my_dict = {}