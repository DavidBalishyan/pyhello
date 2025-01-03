# Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food (lowercase q to quit): ")
    if food == "q":
        break
    price = float(input("Enter a price: "))
    foods.append(food)
    prices.append(price)
    total += price

print("---- Cart ----")
for i in range(len(foods)):
    print(f"{foods[i]}: ${prices[i]}")
print(f"Total: ${total}")