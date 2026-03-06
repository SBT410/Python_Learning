 # Indentation in conditional statements- spaces after the condition
'''if score >= 90 :
   print("A")

def greet(name):
   print("Ram", name)

for i in range(3):
   print("Loop", i)


def check_even(number):
   if number % 2 == 0:
      print("Even Number")
   else:
      print("Odd Number")

#----------------------------------------------------
# if statement
#score = 100
score = 50
if score >= 90 :
     print("A")
     print("Great Job")

# if-else statement
score = 50
if score >= 90 :
     print("A")
else:
     print("F")

# elif statement
score = 95
project_submitted = True
if score >= 90:
     print("A")
elif score >= 80:
     print("B")
elif score >= 70:
     print("C")
elif score >= 60:
     print("D")
else:
     print("F")


# Nested if statement
score = 95
project_submitted = True
if score >= 90:
     if project_submitted:
          print("A+")
     else:
          print("A")
elif score >= 80:
     print("B")
elif score >= 70:
     print("C")
elif score >= 60:
     print("D")
else:
     print("F")


# Connecting conditions- Logical Operators
score = 95
project_submitted = False
if score >= 90 and project_submitted:
     print("A+")
elif score >= 90:
     print("A")
elif score >= 80:
     print("B")
elif score >= 70:
     print("C")
elif score >= 60 or project_submitted:
     print("D")
else:
     print("F")


# Independent if-else conditions

score = 50
project_submitted = True
if score >= 90:
     print("High Score")
else:
     print("Low Score")

if project_submitted:
     print("Project is submitted")
else:
     print("Project is not submitted")

# Challenge

# Email must not be empty
# Email must contains a '.' and one '@' symbol
# Email must ends with '.com', '.org', or '.net'
# Email must not be longer than 254 characters
# Email must start and end with a latter or digit

email = "sbtriptahi@gmail.com#"
#email = "   "
email = email.strip()
# Email must not be empty
if email == "":
    print("Email can not be empty.")
# Email must contains a '.' and only one '@' symbol
elif not('.' in email and '@' in email):
    print("Email must contain . and'@'")
# Email must contains only one '@' symbol
elif email.count("@") != 1:
    print("Email must contains only one '@' symbol")
    # Email must ends with '.com', '.org', or '.net'
elif not email.endswith(('.com','.org','.net')) :
    print("Email must ends with .com, .org or .net")
# Email must not be longer than 254 characters
elif len(email) > 555:
    print("Email must not be longer than 254 characters")
# Email must start and end with a latter or digit
elif not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a latter or digit")
else:
    print("Email is valid.")

# if we add something at the end of email code is ending on 3rd condition 
# so for that we need to use 
# with independent if statement

#email = "sbtriptahi@@gmail.com#"
email = "sbtriptahi@gmail.com"
valid = True
#email = "   "
email = email.strip()
# Email must not be empty
if email == "":
    print("Email can not be empty.")
# Email must contains a '.' and only one '@' symbol
if not('.' in email and '@' in email):
    print("Email must contain . and'@'")
    valid = False
# Email must contains only one '@' symbol
if email.count("@") != 1:
    print("Email must contains only one '@' symbol")
    valid = False
    # Email must ends with '.com', '.org', or '.net'
if not email.endswith(('.com','.org','.net')) :
    print("Email must ends with .com, .org or .net")
    valid = False
# Email must not be longer than 254 characters
if len(email) > 555:
    print("Email must not be longer than 254 characters")
    valid = False
# Email must start and end with a latter or digit
if not (email[0].isalnum() and email[-1].isalnum()):
    print("Email must start and end with a latter or digit")
    valid = False
if valid:
    print("Email is valid.")


# Challenge

# Password must not be empty
# Password must be at least 8 characters long
# Password must include at least 1 uppercase and 1 lowercase
# Password must not be same as email
# Password must not contains any spaces
# Password must start and end with a latter or digit







# inline if (Ternary Operators) statement - it is only for simple logics
#score = 100
score = 50
if score >= 90 :
     print("A")
     print("Great Job")

# Inline example

score = 55
print("A" if score >= 90 else "F")

score = 55
grade = "A" if score >= 90 else "F"
print(grade)


score = 95
project_submitted = True
if score >= 90:
     print("A")
elif score >= 80:
     print("B")
else:
    print("F")

# Inline example
score = 65
grade = "A" if score >= 90 else "B" if score >= 80 else "F"
print(grade)


# Case - Match
# Convert the full country name into 2-latter abbreviations

country = "India"
if country == "India":
    print("IN")
elif country == "United States":
    print("US")
elif country == "Egypt":
    print("EG")
elif country == "Germany":
    print("DE")
else:
    print("Unknown Country")


# Using Match Case
# Can be used only for matching value we can not use any operators

country = "USA"
match country:
    case "United State" | "USA":
        print("US")
    case "India":
        print("IN")
    case "Egypt":
        print("EG")
    case "Germany":
        print("DE")
    case _:
        print("Unknown Country")'''