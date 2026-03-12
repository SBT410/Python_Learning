# Create a list
empty = [] # empty list
print(empty)
print(type(empty))

letters = ['a', 'b', 'c']
print(letters)
print(type(letters))

numbers = [1,2,3]
print(numbers)

mixed = [1, 'a', True, None]
print(mixed)

empty = list()
print(empty)

letters = 'python'
print(letters)

letters = list('python')
print(letters)

numbers = list(range(5))
print(numbers)

# Nested List - Matrix

matrix = [['a','b','c'],
          ['d','e','f']]
print(matrix)
print(type(matrix))

mixed_matrix = [['a','b'],
                [1, 2, 3],
                [True],
                [None]]
print(mixed_matrix)
print(type(mixed_matrix))

# Read and Access List (Slicing & Indexing)
# Indexing
lst = ['a', 'b', 'c', 'd',]
print(lst)
print(lst[0])
print(lst[-1])

matrix = [['a','b','c'],  # Row 0
          ['d','e','f'],  # Row 1
          ['g','h','i']]  # Row 2

print(matrix)
print(matrix[1])
print(matrix [1] [1])
print(matrix [0] [0])
print(matrix [-1] [-1])

# Slicing
lst = ['a', 'b', 'c', 'd',]
print(lst)
print(lst[:3])
print(lst[1:])
print(lst[1:3])

matrix = [['a','b','c'],  # Row 0
          ['d','e','f'],  # Row 1
          ['g','h','i'],  # Row 2
          ['j','k','l']]  # Row 3

print(matrix)
print(matrix[:2])
print(matrix [1:])
print(matrix [1:2])
print(matrix [2] [:2])

# List Unpacking
person = ['Ram', 25, 'God', 'Ayodhya', 'India']
#name = person[0]
#age = person[1]
#role = person[2]
#place = person[3]
name, age, role, place, country = person
print(name)

# Rest Collector - Asterisk * : We are allow to use only one Asterisk one time

#person = [1,'Ram', 25, 'God', 'Ayodhya', 'India']
person = ['Ram', 25, 'God', 'Ayodhya', 'India']
#name, *details, country = person
name, *details = person
*details, country = person
#print(name)
print(details)
print(country)

# Skipping items Underscore "_" : we can use multiple underscore
person = ['Ram', 25, 'God', 'Ayodhya', 'Bharat']
#name, age, role, place, country = person
#name, _, role, _, country = person
#name, *_, country = person
#name, *_ = person
*_, country = person
print(country)

# Explore and Analyze - List :
# List Function

numbers = [1, 3, 5, 4, 2]
print("Max:", max(numbers))
print("Min:", min(numbers))
print("Sum:", sum(numbers)) # this will not work if we have any other datatype in list numbers e.g. [1, 3, 5, 4, '2']
print("Length:", len(numbers))

numbers = [1, 3, 5, 4, 2]
print('All:', all(numbers))
print('All:', all([1,0,5]))
print('All:', all(['a','b','c']))
print('All:', all(['a','','c']))

numbers = [1, 3, 5, 4, 2]
print('Any:', any(numbers))
print('Any:', any([1,0,5]))
print('Any:', any(['a','b','c']))
print('Any:', any(['a','','c']))
print('Any:', any([0,0,0]))

numbers = [1, 3, 5, 5, 4, 2]
print('Count:', numbers.count(5))
print('Index:', numbers.index(5))

numbers = [1, 3, 5, 5, 4, 2]
print(5 in numbers)
print(8 in numbers)
print(8 not in numbers)

list1= [1, 2, 3]
list2= [1, 2, 3]
list3= [1, 5, 3]
print(list1 == list2)
print(list1 == list3)
print(list1 < list3)

list1= [1, 2, 3]
list2= [1, 2, 3]
print(list1 is list2)

# Change List - Add items:

letters = ['a','b','c']
letters.append('x')
letters.append('z')
print(letters)

letters = ['a','b','c']
letters.insert(0,'x')
letters.insert(1,'z')
letters.insert(3,'y')
print(letters)

matrix = [
          ['a','b','c'],  # Row 0
          ['d','e','f'],  # Row 1
          ['g','h','i']   # Row 2
         ] 

#matrix.append(['x','y','z'])
#matrix.insert(0,['a','a','a'])
#matrix.append('x')
matrix[1].append('x')
matrix[0].insert(0,'z')
print(matrix)

# Change List - Delete items:

letters = ['a','b','c']
letters.clear()
print(letters)

letters = ['a','b','c','b']
#removed = letters.pop()
removed = letters.pop(0)
#letters.remove('b') # Delete By value - .remove() will delete only the first match
#letters.remove('b') # it will remove next value
#letters.pop()      # Delete By position - .pop() will remove and return the items
print(letters)
print('Removed item:',removed)

matrix = [
          ['a','b','c'],  # Row 0
          ['d','e','f'],  # Row 1
          ['g','h','i']   # Row 2
         ] 

#matrix.remove(['a','b','c'])
#matrix.pop()
#matrix[1].remove('e')
matrix[-1].pop(0)
matrix[0].pop() #for last value index is not required pop() will take auto
print(matrix)