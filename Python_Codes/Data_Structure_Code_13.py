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


my_dict = {
        'a':10,
        'b':20,
        'c':20,
        'a':40
               }

print(my_dict)         # Ordered # Keys are unique and Values allow Duplicates
#print(my_dict[2])     # not indexed
print(my_dict['b'])    # it is keyed means we can access individual value with the help of key
my_dict['c'] = 80
print(my_dict)         # Mutable


# Methods in Dict
user = {'id':1, 'age':25, 'city':'Hyd'}
#Access
print(user['city'])
#print(user['name']) # in case if key is not present we will get error
print(user.get('name')) # we can use get to avoid error
print(user.get('age'))
print(user.get('name', 'unknown')) 

# Checks
user = {'id':1, 'age':25, 'city':'Hyd'}
print('age' in user)
print('name' in user)
print('name' not in user)

# View Object

user = {'id':1, 'age':25, 'city':'Hyd'}
print(user.keys())     # to get only key details from dict, structure of data
print(user.values())   # to get only values from dict
print(user.items())    # to get both together in the form of list of tuples so that we can do the loop,transformation and other
print(user)

# Looping
user = {'id':1, 'age':25, 'city':'Hyd'}
for u in user:
    #print(u)
    print(u, user[u])

for key,values in user.items():
    print(key,values)  # Smart way

# Add , Remove and Update

user = {'id':1, 'age':25, 'city':'Hyderabad'}
user['name'] = 'Ram'  # to add new pair in dict
user['age'] = 30      # to update the existing value
user.update({'age':55, 'city':'Pune'}) # to update multiples values in dict
print(user)

user = {'id':1, 'age':25, 'city':'Hyderabad'}
#user.pop('age')
#print(user)
#age = user.pop('age')
#age = user.pop('salary') # we will get error if by mistake we use wrong key to avoid this
#age = user.pop('salary', 'not found')
#print('Removed Items', age)

#user.pop() # we can not use this 1 argument is required so instead of this we can use below
user.popitem() # it will remove the last value from dict
print(user)

# Creation of Dict

user = {'id':None, 
        'age':None, 
        'city': None,
        'name': None
        }

# if we have same value for all the keys so instead of this we can use

user = dict.fromkeys(['id', 'age', 'city', 'name'], None)
print(user)
user['age'] = 25
print(user)


# Dict - Real world application
# 1 use case: Database or API records
# Representing a single row from a DB or API

row = {
    'id': 101,
    'name': 'Krishn',
    'country': 'Bharat',
    'age': 25,
    'status': 'Always Active'
}
print(row)

# 2 use case: Mapping Translations to Friendly Values

status_map = {
    '01': 'open',
    '02': 'In Progress',
    '03': 'Completed'
}

print(status_map)

# 3 use case: Mapping Abbreviations

country_map = {
    'IN': 'india',
    'US': 'United State',
    'FR': 'France'
}

print(country_map)

# 4 use case: Config and Environment Data
# Storing environment variables & Configurations

system_conn = {
    'DB_HOST': 'prod-db.company.com',
    'DB_PORT':  5432,
    'DB_USER': 'admin_user',
    'DB_NAME': 'analytics_warehouse',
}

# 4 use case: ETL & Pipeline settings
etl_config = {
    'DEBUG_MODE': False,                     # Turn verbose logging on/off
    'BATCH_SIZE': 500,                       # How many row to process per batch
    'LOG_LEVEL': 'INFO',                     # Logging Verbosity
    'SOURCE_PATH': 'data/bronze/',           # where raw files lives
    'TARGET_PATH': 'data/silver/',           # where cleaned files go
    'RETRY_COUNT': 3,                        #
    'FAIL_ON_ERROR': False,
    'VALIDATE_SCHEMA': True,
    'SUPPORTED_FORMATS': ['csv', 'parquet'],
    'RUN_ENVIRONMENT': 'production'

}



# 5 use case: Metadata




# Challenges
# Keep only string values & convert them to upper case

user = {'id':1, 'name':'Ram', 'age':25, 'city':'Hyderabad'}
user_str = {
    k: v.upper()# Expression 
    for k, v in user.items()# Loop
    if isinstance(v, str)# Filter
}
print(user_str)