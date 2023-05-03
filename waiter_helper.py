# Making the lists

starters = ["Hummus", "Chicken Strips", "Chicken Wings"]
mains = ["Chicken Burger", "Beef Burger", "Lobster"]
desserts = ["Cheesecake", "Sticky Toffee", "Chocolate Brownie"]

# Displaying the menu
print("Welcome to JafsCafe!")
print("This is the menu!")

print("starters")
print(starters)
print("mains")
print(mains)
print("desserts")
print(desserts)

import random
random_number = random.randint(1, 99)

order = []
for i in range(1, 4):
    if i == 1:
        response = input("What would you like to order? ")
    else:
        response = input("What else would you like to order? ")
    order.append(response)

if order:
    print("You have ordered:")
    for item in order:
        print(item)
    print("Thank you! Your order number is")
    print(random_number)
else:
    print("You didn't order anything.")
