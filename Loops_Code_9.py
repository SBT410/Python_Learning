# FOR LOOP
print("Round: 1")
print("Round: 2")
print("Round: 3")
print("Round: 4")
print("Round: 5")

for i in (1,2,3,4,5):
    print(f"Round: {i}")

# Tuple Example
items = (1,2,3,4,5)
for item in items:
    print(f"Round: {item}")
# List Example
items = [1,2,3,4,"Hi"]
for item in items:
    print(f"Round: {item}")

# There i sno rule in FOR loop that the item must be either be numbers or string value we can we do mix
# String Example
#items = "python"
items = " python" # if we have space in the string
for item in items:
    print(f"Round: {item}")

# Range Example (Range is a Build-in function)

#for item in range(5): # by default it will start from 0 index
# range(stop)
for item in range(55): # we can decide the range to run the code
    print(f"Round: {item}")

# Using above example our range will start from 0 but if we use below we can decide the starting range
# range(start, stop)
for item in range(1, 6): # we can decide the starting range to run the code
    print(f"Round: {item}")

# Using above example our range will start from 1 but if we use below we can decide the steps between range
# range(start, stop, step)
for item in range(2, 10, 2):
#for item in range(0, 10, 2): # we can use this for even numbers and also we can decide the steps between range to run the code
    print(f"Round: {item}")

for item in range(1, 10, 4):
#for item in range(1, 10, 2): # we can use this for odd numbers and also we can decide the steps between range to run the code
    print(f"Round: {item}")


# We use for loop to go through the values and aggregate the data like - sum, count, avg

scores = [55,40,25,35,65]
total = 0
for score in scores:
   # total = total + scores
     total += score  #shortcut
     print("Current Total: ", total)
print("Final Total: ", total)

# we can use for loops to transform data like cleaning data before processing

files = ['  Report.csv' , 'DATA.csv ' , ' final.TXT']
# above we have inconsistent casing and unnecessary spaces
for file in files:
    #file = file.strip()
    #file = file.strip().lower()
     file = file.strip().lower().replace('.txt' , '.csv')
     print(f"Processing {file}")
 # Tips - always clean first then transform the data.

# Challenges 1 - Print the 7 times table from 1 to 10 using a for loop
for item in range(7, 77, 7):
    print(item)

# Challenges 2 - Print left-aligned pyramid of star with 6 rows using a for loop
rows = 6
for item in range(1, rows + 1):
    print("*" * item)

# Loop Control statements

# Break Statement
names = ['Ram','Krishn','','Hari']
for name in names:
    if name == '':
        print("Empty value detected!")
        break
    print(f"Name =", name)

# Continue Statement

names = ['Ram','Krishn','','Hari']
for name in names:
    if name == '':
        print("Empty value detected!")
        continue
    print(f"Name =", name)

# Pass Statement - It is just placeholder to be changed later

names = ['Ram','Krishn','','Hari']
for name in names:
    if name == '':
        pass       #todo: Handle Empty Value
    print(f"Name =", name)

# After discussion with my team we change the empty string with unknown
names = ['Ram','Krishn','','Hari']
for name in names:
    if name == '':
        #pass       #todo: Handle Empty Value
        name = name.replace('', 'unknown')
    print(f"Name =", name)

# TASK
# Loop through a list of days and print only the working days skipping the weekends
# Skip weekend in calendar loop
days = ['Mon','Tue','Sun','Wed','Fri','Sat'] 
for day in days:
    print(f'Workday: {day}')

# to skip the weekend
days = ['Mon','Tue','Sun','Wed','Fri','Sat']
weekends = ['Sat', 'Sun']
for day in days:
    if day in weekends:
        continue
    print(f'Workday: {day}')


# Scan email to block unsafe data from entering the system

emails = [
    'sbt@gmail.com',
    'vt@gmail.com',
    'DROP TABLE USER;', #it is a kind of SQL Injection which can destroy DB or Read all the user info or it can hack our system
    'st@outlook.com',
    'vb@google.com'
]

for email in emails:
    if ';' in email:
        print('SQL Injection; Hacker Attack ') # to prevent this kind of SQL Injection stop the processing data before that
        break
    print(f'Processing Email {email}')


# Else in Loop

numbers = [1,4,3,5,7]
for i in numbers:
    print(i)
#else: # No use of else without else also we will get the same result 
print('Loop is completed')

# Else + Break in Loop
# Check the even numbers

numbers = [1,4,3,5,7]
#numbers = [1,3,5,7,9]
for i in numbers:
    if i % 2 == 0:
        print(f'Even No. found: {i}')
        break
else: # If code do not fulfill the loop condition else will run
    print('All no. are odd')

# for-else use cases
# Check for missing name in a list

names = ['Ram', 'Sita', 'Krishn', 'Lav-Kush']
#names = ['Ram', 'Sita', None, 'Lav-Kush']
for name in names:
    if name is None:
        print('Found the missing name')
        break
else:
    print('All names are available')

# Check if all files are csv file

files = [
    'data.csv',
    'report.pdf',
    'report1.txt',
    'data1.csv'
]

for file in files:
    if not file.endswith('.csv'):
        print(f'{file} file is not csv')
        break
else:
    print('All files are csv')

# In above example we can find only first file name which is not a csv 
# but if we want all the file which are not csv then we need to use continue statement without else
files = [
    'data.csv',
    'report.pdf',
    'report1.txt',
    'data1.csv'
]

for file in files:
    if not file.endswith('.csv'):
        print(f'{file} file is not csv')
        continue


# Challenge - Check whether any file name appears more than once 
# print "Duplicate found" if duplicate exist otherwise print "All files are unique"


file_list = [
    'report.csv',
    'data.xlsx',
    'summary.docx',
    'report.csv',
    'data.csv'
]
for file in file_list:
    if file_list.count(file) > 1:
        print(f"Duplicate found: {file}")
        break
else:
    print("All files are unique")