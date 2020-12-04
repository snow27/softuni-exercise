command = input()
total_price = 0.0

while True:
    if command == "special" or command == "regular":
        break
    given_price = float(command)
    if given_price < 0:
        print("Invalid price!")
    else:
        total_price += given_price
    command = input()

if total_price == 0:
    print("Invalid order!")
else:
    taxes = total_price * 0.2
    price_with_tax = total_price + taxes
    if command == "special":
        price_with_tax -= price_with_tax * 0.1
    print(f"Congratulations you've just bought a new computer!\n"
          f"Price without taxes: {total_price:.2f}$\n"
          f"Taxes: {taxes:.2f}$\n"
          f"-----------\n"
          f"Total price: {price_with_tax:.2f}$")
