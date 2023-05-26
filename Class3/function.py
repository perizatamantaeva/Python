discount = 0
sales_tax = 0.08

def tax_func(price):
    taxes = price * 0.08
    return taxes

def discount_func (price, discount):
    discount_sum = price * (discount/100)
    return discount_sum
price = int(input("Enter the price: "))

tax = tax_func(price)

if price > 100:
    discount = discount_func(price, 10)
total_price = price - discount + tax
print(f"Your total price is: {total_price}")