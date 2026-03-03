#**********------- Types  -------************

'''name = "Shashi"
print(type(name))
age = 30
print(type(age))
#print('Your age is' + age) #This will give an error because we cannot concatenate a string and an integer. We need to convert the integer to a string first.
print('Your age is ' + str(age)) #This will work because we have converted the
age = age + 5 # this is valid coz we are adding integers
print (age)
age = str(age) # we change the datatype from int to str
print (type(age))
#age = age + 5 # this is not valid coz now the age is string and we can not add str with int'''


#**********------- Math  -------************

'''password = "55555s"
password = "55555sbt"
password = "  55555sbt"
print(len(password))

if len(password) < 8:
    print("Your password id too short")

text = """
Python is easy to learn.
Python is powerful.
python is very imp for Data Engineers.
"""
# Python is case-sensitive thats why we got count as 2 if change the 3rd line into Python we will get count as 3.
print(text.count("Python"))'''

#**********------- Transformations -------************

'''price = "4545,55"
print(price.replace(",","."))
mobile = "8989-76-1089"
print(mobile.replace("-",""))
price = "$5,454.55"
print(price.replace("$",""))
print(price.replace("$","").replace(",",""))

#Challenge
#Convert the below no without any special characters
phone = "+91 (8989) 76-1089"
print(phone.replace("+","00").replace("(","").replace(")","").replace("-","").replace(" ",""))'''

# Join String

'''first_name = "Radhe"
last_name = "Krishn"
print(first_name+last_name)
print(first_name+" ",last_name)
full_name = first_name + last_name
print(full_name)
full_name = first_name + " " +last_name
print(full_name)

path = "C:/Users/Shashi/"
file = "report.csv"
full_path = path + file
print(full_path)'''

# F-String

'''name = "Krishn"
age = 25
is_god = True
#print("My name is "+ name + ", I am " + str(age) + " years old, and god status is " + str(is_god) + ".")
print(f"My name is {name}, I am {age} years old, and god status is {is_god}.")
print(f"2 + 3 = {2 + 3}")
#print(f"{this is me}")
print(f"{{this is me}}")'''

# split()

'''stamp = "2026-02-15 15:45"
print(stamp.split(" "))
date = "2026-02-15"
print(date.split("-"))
csv_file = "1410,Shashi,India,29-12-1989,M"
print(csv_file.split(","))'''

# String Repetition

'''print("ha" * 5)
print("========================")
print("=" * 55)
#if you want to change
print("#" * 55)'''

# Data Extraction- Indexing

'''text = "Python"
# Extract the 1st character
print(text[0])
print(text[-6])
# Extract the last character
print(text[5])
print(text[-1])
# Extract the mid character
print(text[3])
print(text[-3])

# Data Extraction- Slicing
date = "2026-02-15"
# Extract the year
print(date[0:4])
print(date[:4])
# Extract the month
print(date[5:7])
# Extract the day
print(date[8:])
print(date[-2:])'''


#**********------- Cleaning -------************

#Data Cleansing - Clean or Remove Spaces

'''text = "  Radhe".lstrip()
print(text)
text = "Radhe  ".rstrip()
print(text)
text = "  Radhe  ".strip()
print(text)
text = "###Radhe###".strip("#")
print(text)

#Detect Extra spaces Data Quality check
#text = "  Radhe"
text = "Radhe"
print(len(text))
print(len(text.strip()))
no_of_spaces = (len(text)) - (len(text.strip()))
is_clean = (len(text)) == (len(text.strip()))
print("No. of spaces: ",no_of_spaces)
print("Is my data clean? ",is_clean)'''


#Data Cleansing - Clean Cases or Case Conversion

'''text = "python PROGRAMMING"
print(text.lower())
print(text.upper())
#Use case Clean Data for Matching
search = "Email".lower()
data = "emAil".lower()
print(search == data)
#With spaces
search = "Email ".lower().strip()
data = " emAil".lower().strip()
print(search == data)

# Advanced Challenge

# Messy String - Input
# "968-Radha, (D@t@ Engineer);; 27y  "
# Clean String - Output
# name: radha | role: data engineer | age: 27
name = "968-Radha"
role = "(D@t@ Engineer);;"
age = "27y  "
print(f"name: {name.lower().replace("-","").replace("968","")} | role: {role.lower().replace("@","a").replace("(","").replace(")","").replace(";","")}| age: {age.lower().strip().replace("y","")}")'''

#**********------- Searching -------************

'''phone = "+91-8989-76-1089"
print(phone.startswith("+91"))

email = "sbtripathi@outlook.com"
print(email.endswith("gmail.com"))

file = "data_backup.csv"
print(file.endswith(".csv"))

email = "sbtripathi@outlook.com"
print("@" in email)
url = "https://api.data.com/v1/about"
print("/api" in url)

phone1 = "+91-8989-7610-89"
phone2 = "00-8989-7610-89"
print(phone1[4:])
print(phone2[3:])

print(phone1.replace("-","")[3:])
print(phone2.replace("-","")[2:])

print(phone1.find("-"))

print(phone1[phone1.find("-"):])
print(phone2[phone2.find("-"):])

print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])'''


#**********------- Validating -------************
country = "INDIA"
print(country.isalpha())
country = "INDIA1"
print(country.isalpha())
mobile = "8989761089"
print(mobile.isnumeric())
mobile = "8989761089"
print(mobile.isnumeric())
value = "3.14"
print(value.isnumeric())