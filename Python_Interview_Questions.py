# ------List----------

emp = ["Ram","Shyam","Sita","Radha","Ram"] # Allows Duplicate
print(emp)
emp.append("Shiv") # Add
print(emp)
emp[0] = "Krishn" # Change
print(emp)

# ------Tuple----------

db_records = ("Ram","30","Engineer")
print(db_records)
db_records.append("Shiv") # Add
print(db_records)
db_records = ("Ram","30","Engineer")
db_records[0] = "Krishn" # Change
print(db_records)

# ------Dict----------

employee = {"name": "Ram", "dept": "Engineering", "salary": 900000}
print(employee)
employee["salary"] = 950000  # update value
print(employee)

# ------Set----------
all_dept = {"Engineering", "HR", "Finance", "Delivery","TA","QA-QC"}
print(all_dept)
unique_dept = {"Engineering", "HR", "Finance", "Engineering","HR"}  # → 3 items
print(unique_dept)


# --------List Comprehension---------
#[expression   for item   in iterable   if condition]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Given List
evens = []                        # start with empty list
for num in numbers:               # loop through each number
    if num % 2 == 0:              # check if it's even
        evens.append(num)         # add it to the list

print(evens)


names = ["ramayana", "ram", "sita", "hanuman", "nal"]
# "Give me the name in UPPERCASE, for every name, but only if it's longer than 3 letters"
result = [name.upper() for name in names if len(name) > 3]
print(result)


# Get names of high earners, upper cased
employees = [
    {"name": "Ram", "salary": 95000},
    {"name": "Krishn",   "salary": 45000},
    {"name": "Hari", "salary": 120000},
]

high_earner = [e["name"].upper() for e in employees if e["salary"] > 80000]
print(high_earner)

# Real Project Scenario: In a data cleaning pipeline, you often filter out null/empty values from a raw column before processing:

raw_emails = ["sbtripathi@co.com", "", None, "VBtripathi@co.in", "   "]
valid_emails = [e.strip().lower() for e in raw_emails if e and e.strip()]
print(valid_emails)


# Opening, Reading, and Writing Files — CSV 

with open(r"C:\Users\Shashi B Tripathi\OneDrive\Documents\Desktop\UpSkill\Python\Python_Interview\employees.csv", "r") as file:
    print("Opened")


import csv
with open(r"C:\Users\Shashi B Tripathi\OneDrive\Documents\Desktop\UpSkill\Python\Python_Interview\employees.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


import csv
with open(r"C:\Users\Shashi B Tripathi\OneDrive\Documents\Desktop\UpSkill\Python\Python_Interview\employees.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["First Name"], row["Salary"])


# == vs is in Python
# == checks value equality — are the contents the same is checks identity exact same object in memory

a = [5,10,15]
b = [5,10,15]
c = a

print(a == b)   # True  — same contents
print(a is b)   # False — different objects in memory
print(a is c)   # True  — c points to the same object as a

# Handling Duplicates and Missing Values

data = [1, 2, 2, 3, None, 4, None, 3]

# Find duplicates
from collections import Counter
counts = Counter(data)
duplicates = [val for val, cnt in counts.items() if cnt > 1]
print (counts)

data = [1, 2, 2, 3, None, 4, None, 3]

# Find duplicates
from collections import Counter
counts = Counter(data)
duplicates = [val for val, cnt in counts.items() if cnt > 1]

# Remove duplicates (preserving order)


# Remove missing values


# Binary matrix is given and how to find the no. of unique rows
# Example
matrix = [
    [1, 0, 0],
    [1, 0, 0],
    [0, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
# Short Version
def count_unique_rows(matrix):
    return len(set(tuple(row) for row in matrix))

print(count_unique_rows(matrix))


# Long Version
def count_unique_rows(matrix):
    unique_rows = set()

    for row in matrix:
        unique_rows.add(tuple(row))   # convert list to tuple

    return len(unique_rows)

print(count_unique_rows(matrix))
