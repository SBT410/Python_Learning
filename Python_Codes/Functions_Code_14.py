# User Define Functions
# If we create a user define functions it is easy to change
#  Change fast 
# Safer(Low Risk) 
# Smaller & clean 
# Easy to read and understand 
# Modular 
# Collaboration 

def make_tea ():
    print('Start the Gas stove')
    print('Make raw tew')
    print('Add Milk')
    print('Enjoy It')


print('Wake up')
make_tea()
print('Working for a while')
make_tea()
make_tea()


def clean_name():
    names = '  krisHn  '
    print(names.strip().lower())

clean_name() # this we can if we have only one value to change but we in our data we need to change multiple values

# For Multiple Values which we can change with argument dynamically 

def clean_name(names):
    print(names.strip().lower())

clean_name('RADHE  ')
clean_name('  krisHn  ')
clean_name()     # fi we pass this we will get error
clean_name('')   # Instead of above we can pass this

# Local & Global Variables
def clean_name(names):                # Parameter
    cleaned = names.strip().lower()
    print('Raw:', names)   # Local Variable
    print('Cleaned:', cleaned)

clean_name('  RADHE  ')
#print('Raw:', names) # we can not access local variable outside the function definition

# Global Variables

#case_rule = 'lower'  # Global Variable
case_rule = 'n/a'  # Global Variable

def clean_name(names):                # Parameter
    cleaned = names.strip()
    if case_rule == 'lower':
        cleaned = cleaned.lower()
    print('Cleaned:', cleaned)

clean_name('  RadhE  ')
print('The Rule is:', case_rule)  # # we can access global variable anywhere in function

# Building cleaned full name

def clean_name(first_name, last_name, country):                # Parameter
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + ' ' + last

    print(full_name, 'from', country)

clean_name('  RadhE  ', 'KRISHN  ', 'Bharat')


# Positional and Keyword Argument

def clean_name(first_name, last_name, country):                # Parameter
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + ' ' + last
    print(full_name, 'from', country)

# Positional Argument
clean_name('Bharat','  RadhE  ', 'KRISHN  ')

# Keyword Argument
clean_name(first_name = '  RadhE  ', last_name = 'KRISHN  ', country = 'ind')
clean_name(country = 'ind', first_name = '  RadhE  ', last_name = 'KRISHN  ') # even if we change the position of argument still result will not change

# Mixed Argument
clean_name('  RadhE  ', last_name = 'KRISHN  ', country = 'ind') # Allowed
clean_name('  RadhE  ', 'KRISHN  ', country = 'ind') # Allowed
# clean_name(first_name = '  RadhE  ','KRISHN  ', country = 'ind')  # we can not start with Keyword Argument always start with Positional Argument
#clean_name('  RadhE  ',last_name = 'KRISHN  ','ind') # Not allowed

# Default Parameter

#def clean_name(first_name, last_name, country = 'n/a'):  # Allowed
#def clean_name(first_name, last_name = 'n/a', country):   # Not allowed
def clean_name(first_name, last_name = 'n/a', country = 'n/a'):   # Allowed
    first = first_name.strip().lower()
    last = last_name.strip().lower()
    full_name = first + ' ' + last
    print(full_name, 'from', country)

# Positional Argument
clean_name('Bharat','  RadhE  ', 'KRISHN  ')
# Keyword Argument
clean_name(country = 'ind', first_name = '  RadhE  ', last_name = 'KRISHN  ')
# Mixed Argument
clean_name('  RadhE  ', last_name = 'KRISHN  ', country = 'ind')
# Default
clean_name('Ram', 'Chandra')


# *args **kwargs
# Calculate a total of multiple values

def  total (a=0, b=0, c=0, d=0): # we have to define 0 for each parameter
    print(a + b + c)

total(1, 2)
total(1, 2, 3)
total(1, 2, 3, 4)  # we don't know how many values are coming
#......          # this is not the smart way if we have multiple values

# *args 
def  total (*args):    # if we use *args no need to define 0 for each parameter
    print(type(args))
    print(sum(args))

total(1, 2)
total(1, 2, 3)
total(1, 2, 3, 4)   # We can use *args if we have multiple values


# **kwargs
# Create the user profile 
def create_user (**kwargs):
    print(type(kwargs))
    print(kwargs)

create_user(first_name = 'ram',
            last_name = 'chandra',
            age = 25,
            country = 'Ayodhya') # we can use kwargs only with key value pairs.

create_user(name = 'sita',
            country = 'Avadh')

# Return

def clean_name(names):                # Parameter
    cleaned = names.strip().lower()
    return cleaned  # if we don't use return we will get None in the output

cln_name = clean_name('  RADHE  ')
print(cln_name)

# Example 
def clean_name(names):     
    if not names:
        return None
    else:
        cleaned = names.strip().lower()
        return cleaned

cln_name = clean_name('  RADHE  ')
#cln_name = clean_name('')
print(cln_name)

# Multiple return values
def clean_name(names):     
        lo_cleaned = names.strip().lower()
        up_cleaned = names.strip().upper()
        return lo_cleaned, up_cleaned

cln_name = clean_name('  RADHE  ')
print(type(cln_name))
print(cln_name)

# Example 
def clean_name(names):     
        lo_cleaned = names.strip().lower()
        up_cleaned = names.strip().upper()
        return lo_cleaned, up_cleaned

lo_name, up_name = clean_name('  RADHE  ')
print(lo_name)
print(up_name)