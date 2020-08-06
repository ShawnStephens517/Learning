print("Would you like to find cost of a specified number or an order?")
print("Type NUMBER for specific or ORDER for an order")
answer = input(" ").upper()

if answer == "NUMBER":
    amount_high = input("How Many 16GB would you like")
    total_high = int(amount_high) * 145
    print(total_high)

    amount_low = input("How Many 8GB would you like")
    total_low = int(amount_low) * 84
    print(total_high)
    
elif answer == "ORDER":

    print("Calculating.....")

    order_number = 15

    total_high = order_number * 145

    total_low = order_number * 84

    print(f"""An order would cost:
          ${total_low} for 8GB
               or
          ${total_high} for 16GB""")
