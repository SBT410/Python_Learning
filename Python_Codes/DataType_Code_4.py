# Datatypes

'''a = 10 #integer
b = 3.14 #float
c = "Hello, World!" #string
d = 'Hi' #string
e = "1234" #string
f = True #boolean
g = False #boolean
h = None #NoneType
i = "" #blank string it is not same as None
j= " " #empty space it is string value with one or more space it is not same as None'''


#***Functions*****

text = 'Hi'
number = 55
#print(text)
#print(number)
print(type(text))
print(type(number))
print(len(text))
#print(len(number)) #len() function is used to find the length of a string, list, tuple, etc. It cannot be used with numbers.

#***Methods*****

'''text = 'hi'
number = 55
print(text.upper())
#number.upper() #number is an integer and it does not have the upper() method. The upper() method is used to convert a string to uppercase. It cannot be used with numbers.
print(number.bit_length()) #number is an integer and it has the bit_length() method. The bit_length() method is used to find the number of bits required to represent an integer in binary. It cannot be used with strings.
#print(text.bit_length()) #text is a string and it does not have the bit_length() method. The bit_length() method is used to find the number of bits required to represent an integer in binary. It cannot be used with strings.
'''

# Challenge: Create a variable of each data type and print their types and values.

age = 30 #integer
height = 5.9 #float
name = "Shashi" #string
is_student = True #boolean
a = None #NoneType
print("Age:", age, "Type:", type(age), age.bit_length())
print("Height:", height, "Type:", type(height), height.__str__())
print("Name:", name, "Type:", type(name), len(name))
print("Is Student:", is_student, "Type:", type(is_student), is_student.__str__())
print("a:", a, "Type:", type(a), a.__str__() if a is not None else "NoneType does not have __str__ method")
