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

# Change List - Update items:

letters = ['a','b','c','b']
letters[0] = 'x'
print(letters)


matrix = [
          ['a','b','c'],  # Row 0
          ['d','e','f'],  # Row 1
          ['g','h','i']   # Row 2
         ] 

matrix[1] = ['x', 'y','z']
matrix[0][1] = 's'
print(matrix)

# Sorting List

#letters = ['c','a','d','b']
numbers = [7,2,5,3,1,9]
#letters.sort()
#letters.sort(reverse=True)
#print(letters)
numbers.sort()
numbers.sort(reverse=True)
print(numbers)

matrix = [
          ['d','e','f'],  # Row 0
          ['g','h','i'],  # Row 1
          ['a','b','c']   # Row 2
         ] 

matrix = [
          ['d','e','f'],  # Row 0
          ['a','z','i'],  # Row 1
          ['a','a','c']   # Row 2
         ] 

#matrix.sort()
#matrix.sort(reverse=True)
matrix[1].sort()
print(matrix)

# If we dont want to change the original list we can create new list using sorted() 

letters = ['c','a','d','b']
#new_list = sorted(letters)
new_list = sorted(letters, reverse=True)
print('Original List:', letters)
print('Sorted List:', new_list)

# Reverse the data

numbers = [7,2,5,3,1,9]
#numbers.reverse()
#new_num = reversed(numbers)
new_num = list(reversed(numbers))
print('Original List:', numbers)
print('Reverse List:', new_num)

# Copying List - Assignment

letters = ['a','b','c']
letters_copy = letters
#letters.pop()
#letters_copy.append('z')
print('Original:', letters)
print('Copy:', letters_copy)

# Copying List - Shallow Copy

letters = ['a','b','c']
letters_copy = letters.copy()
letters.pop()
#letters_copy.append('z')
print('Original:', letters)
print('Copy:', letters_copy)


matrix = [
          ['a','b',],  # Row 0
          ['c','d',]   # Row 1
         ] 

matrix_copy = matrix.copy()
matrix.pop()
matrix_copy[0].append('z')
print('Original:', matrix)
print('Copy:', matrix_copy)

# Copying List - Deep Copy

import copy
matrix = [
          ['a','b',],  # Row 0
          ['c','d',]   # Row 1
         ] 

matrix_copy = copy.deepcopy(matrix) # it will create true, independent copy of all levels no matter how nested is our list
matrix.pop()
matrix_copy[0].append('z')
print('Original:', matrix)
print('Copy:', matrix_copy)

# Testing - IS operator 

import copy
original = [
          ['a','b',],  # Row 0
          ['c','d',]   # Row 1
         ] 

# Assignment

copy1 = original
print('Same Object?' , original is copy1,'\n')

# Shallow Copy

copy2 = original.copy()
print('Same Object?' , original is copy2)
print('Shared List?',original[0] is copy2[0], '\n')

# Deep Copy

copy3 = copy.deepcopy(original)
print('Same Object?' , original is copy3)
print('Shared List?',original[0] is copy3[0], '\n')

# Combining List

# Using Operators

letters = ['a','b','c']
numbers = [1, 2, 3]
#comb = letters + numbers
comb = [letters , numbers]
print(comb)
#print(letters * 2)

# Using extend()

letters = ['a','b','c']
numbers = [1, 2, 3]
letters.extend(numbers)
print(numbers)
print(letters)

# Using zip()

letters = ['a','b','c']
#numbers = [1, 2, 3]
numbers = [1, 2, 3, 4] # Python stops at the shortest list so 4 will not be included in output list
#comb = list(zip(letters , numbers))
comb = list(zip(letters , numbers, 'hi')) # we can pair the list with string value
print(comb)

# Example of zip()

ids = [101, 102, 103]
names = ['jai','shri','ram']
print(list(zip(ids, names)))


# List Iterator
# Iterators and Iterable

letters = ['a','b','c']
#nums = 12345
for l in letters:
#for n in nums:
    print(l.upper())

# to store new result in a list

letters = ['a','b','c']
new_list = []
for l in letters:
    new_list.append(l.upper())
    print(new_list)

# Iterators - enumerate, reversed, zip
letters = ['a','b','c']
#print(list(enumerate(letters,start)))
#print(list(enumerate(letters,start=1)))
for index, value in enumerate(letters):
    print(index, value)

# TO use analyse the data if it bad
letters = ['a','','c']
for index, value in enumerate(letters):
    print(index, value)

letters = ['a','b','c']
#print(list(reversed(letters)))
for l in reversed(letters):
    print(l)

letters = ['a','b','c']
num = [1, 2, 3]
#print(list(zip(letters,num)))
for l,n in zip(letters,num):
    print(l,n)

letters = ['a','b','c']
print(list(map(str.upper, letters)))

num = ['1', '2', '3']
print(list(map(int, num)))

names = [' Jai ','Shri ',' Ram']
#print(list(map(str.strip,names)))
for n in map(str.strip,names):
    print(n)


letters = ['a','b','', None,'c', False]
print(list(filter(None, letters)))
print(list(filter(bool, letters)))

items = ['sql','543','python', '55']
#print(list(filter(str.isalpha, items)))
for i in (filter(str.isalpha, items)):
    print(i)


multiple =lambda x: x*2
print (multiple(2))


addition = lambda x,y: x + y
print(addition(3,5))


check = lambda i : i in 'python'
print(check('x'))


prices = ['$55.56','$9.5','$100.00']
print(list(map(lambda p : float(p.replace('$','')),prices)))

p = '$55.56'
print (float(p.replace('$','')))


prices = [120,555,300,55,99]
print(list(filter(lambda p : p >= 100,prices)))

# To filter students who got marks more than 70
students = [['Jai', 60],
            ['Shri', 95],
            ['Ram', 100]
           ]
print(list(filter(lambda row: row[1] > 70,students)))
# Logic - print(students[2][1] > 70)


students = [['Jai', 60],
            ['Shri', 95],
            ['Ram', 100]
           ]
#Logic - print(students[2][0].startswith('R'))

print(list(filter(lambda row: row[0].startswith('R') ,students)))


#******* MOST IMP *********
# List Comprehension

domains = ['www.google.com',
           'openai.com',
           'localhost',
           'WWW.SBT.COM']

'''cleaned = [
            d.lower().replace('www.','') # Data Transformation
            for d in domains             # For Loop
            if '.' in d                  # Data Filtering
]'''
# we can do it in one line 
cleaned = [ d.lower().replace('www.','') for d in domains if '.' in d ]
print(cleaned)


my_list = [10, 20, 30 , 10]
print(my_list) # Ordered # Allow Duplicates
print(my_list[1]) # Indexed
my_list[3] = 55
print(my_list) # Mutable
