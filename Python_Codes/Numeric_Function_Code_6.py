#****************------- Numeric Functions Types ----------***************

# type()
'''x = 5
y = 5.5
z = 2 + 3j

print(type(x))
print(type(y))
print(type(z))

# int()
x = "55"
print(type(x))
print(x * 5)
x = int(x)
print(type(x))
print(x * 5)

#float()
x = 3.14
print(int(x))
print(float(x))
x = 3
print(float(x))
x = "3.14"
print(float(x))

# complex()
x = 2
y = 3
print(complex(x,y))'''


#****************------- Numeric Functions Math Operators  ----------***************

'''print(2 + 3)
print(10 - 5)
print(3 * 5)
print(5 / 2)
print(5 // 2) # Floor Division - It divides two numbers and result will be round down
print(5 % 2)  # Remainder - the leftover part after division to check if a no is even
print(5 ** 5) # Exponentiation - It raises a no to the power of another no


x = 2
#y = x + 3
#print (y)
x += 3 # Shortcut method
print (x)
x -= 1
print (x)
x *= 3
print (x)
x /= 2
print (x)'''

#****************------- Numeric Functions - Rounding Numbers  ----------***************

# To Measure Distance & Size
'''print (abs (2- 10)) # It returns the absolute(Non-Negative) value of a number

# Rounding No
import math # To use math module in our code we need to import, it is not build- in function
price = 89.767079
print(round(price)) # It is handy in Data Analysis to clean up no for reports or save space
print(round(price,2))
print(math.floor(price)) # 
print(math.ceil(price))  # Perfect for Data Engineering like splitting data into batches 
print(math.trunc(price)) # if you have already imported math use math.trunc() its make your intent clear.
print(int(price))''' # if you not using math already just use int() its simple and build-in


#****************------- Numeric Functions - Random ----------***************

'''import random   # Use it to generate test data (dummy) for like - ID, age or prices
print(random.random())
print(random.randint(2,10))'''

#****************------- Numeric Functions - Validation ----------***************

x = 5.0
print(x.is_integer())
y = 5.5
print(y.is_integer())

x = 50
print(isinstance(x,int))
x = 50.55
print(isinstance(x,int))
print(isinstance(x,float))

# Challenge - Generate a random integer between 1 - 100 and also check if result is an even no

import random 
x = random.randint(1,100) % 2
print(x)

