print("WELCOME TO THE OMEGA STORES!")
print("#" * 40)
item = input("What item you want to buy? ")
price = float(input(f"What is the price of the {item}? "))
quantity = int(input(f'How many {item} do you want to purchase?'))
result = f"""Added {quantity} {item}s to the cart
Sub Total: N{quantity * price}
"""
print(result)
