# In python first latter of True and False should be always capital latter
# --------  Boolean Expression - Values -----------
'''print(True)
print(False)
print(type(True))

# --------  Boolean Expression - Functions -----------
# bool(value) function
print(bool(123))
print(bool("Hi"))
print(bool())
print(bool(""))
print(bool(0))
print(bool(None))

# any(value) and all(value) functions
email = ""
#phone = "8989-76-1089"
phone = ""
username = ""
# Use case - while sign-up into any website the registration can be allow 
# if any of the field is filled
print(any([email,phone,username]))

email = "sbt@gmail.com"
phone = "8989-76-1089"
username = ""
#username = "sbt"
# Use case - while sign-up into any website the registration can be allow 
# only if all field are filled
print(any([email,phone,username])) # For any()
print(all([email,phone,username])) # For all()

# isinstance(value,type) function
print(isinstance(123, int))
print(isinstance(True, str))

# Methods
print("Hello".endswith("o"))
print("Hello".startswith("o"))

# --------  Boolean Expression - Comparison Operators -----------

print(10 == 10)
print(10 != 10)
print(7 > 5)
print(7 >= 5)
print(7 < 5)
print(7 <= 5)

print("a" < "b")
print("a" == "b")
print("a" == "A")

# Chained Comparison - it evaluates from left to right, checking each condition one by one

print(1 < 4 < 5)
print(5 < 4 < 7)

# Is age between 18 to 30

#age = 20
#age = 18
age = 17
age = 31
print(18 <= age <= 30)

# --------  Boolean Expression - Logical Operators -----------
# and, or and not

print(5 > 1 and 7 < 5)
print(5 > 1 and 7 > 5)

print(5 > 1 or 7 < 5)
print(5 < 1 or 7 < 5)

# Use Case - Check if the system is under pressure
# During high use
cpu_usage = 70
memory_usage = 95
print(cpu_usage > 90 or memory_usage > 90) # True means it will send the alerts
# Now the system is cooling down
cpu_usage = 70
memory_usage = 50
print(cpu_usage > 90 or memory_usage > 90)  # False means we do not have alerts

# Use Case - Checking user credentials before login
email = True
password = False
print(email and password)

email = True
password = True
print(email and password)

print(not 5 > 2)
print(not True)
print(not False)
print(not not False)

name = ""
print(not name)
print(not 0)

# Allow access only if the user is logged in 
# or they are a guest 
# but they must not be banned

is_logged_in = True
is_guest = False
is_banned = False
print(is_logged_in or is_guest and not is_banned)

# Logged in and Guest must be belongs together 
is_logged_in = True
is_guest = False
is_banned = True
print((is_logged_in or is_guest) and not is_banned)

# Challenges
# 1. Check if a user's name is not empty and the age is grater than or equal to 18

user = True
age = 17
print((bool("user"), age >= 18))'''

# 2. Check the password is at least 8 character long and dose not contains spaces
# 3. Check if user's email is not empty, contains @ and ends with .com
# 4. Check if a username is a string, i snot None and longer than 5 characters
# 5. Check if if the user is either admin or moderator, and either they are not banned or they have verified their email


# Membership and Identity Operators
# in and not in operators

print("o" in "python")
print("o" not in "python")
print("s" in "python")
print("s" not in "python")

print(3 in [1,2,3,4,5])
print(3 not in [1,2,3,4,5])

# Validate that the domain is not on the banned list
domain = "gmail.com"
banned_domain = ["spam.com","fake.org","bot.net"]
print(domain not in banned_domain)

domain = "spam.com"
banned_domain = ["spam.com","fake.org","bot.net"]
print(domain not in banned_domain)

# Identity Operators

x = ["a","b","c"]
y = ["a","b","c"]
print(x==y)
print(x is y)

x = ["a","b","c"]
y = x
print(x==y)
print(x is y)

x = 5
y = 5
print(x==y)
print(x is y)

# Validate the email address it must be filled in and not empty

email = ""
print(email != "")

email = "sbt@.com"
print(email != "")

email = None
print(email is not None and email != "")