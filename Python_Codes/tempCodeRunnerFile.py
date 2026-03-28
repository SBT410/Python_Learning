def calculate_discount(price, rate):
    """ Calculate the final price after applying a discount. """
    final_price = price - (price * rate/100)
    return final_price

print(calculate_discount(80, 20))