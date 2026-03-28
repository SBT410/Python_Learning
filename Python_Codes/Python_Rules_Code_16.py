# Bad Style Code

def DiskPrint(p, r):
    print('calculating discount')
    p = p - (p * r/100)
    print(p)

DiskPrint(80, 20)

# Proper Formatted Code

# def disk_print(p, r): # Function name should be meaningful, 
# Parameter name should describe their values, 
# use Docstring to describe what this function dose

def calculate_discount(price: float, rate: float) -> float: # Datatype is just a hint for developer (Human) it will not cast or change any datatype
    """ Calculate the final price after applying a discount. 
        Args:
            price (float): Original Product Price.
            rate (float): Discount Rate as numbers (20 for 20%).
        Return:
            final_price (float): Final price after applying discount.
    """
    final_price = price - (price * rate/100)
    return final_price

print(calculate_discount(80, 20))
#help(calculate_discount) # To check the description of code

