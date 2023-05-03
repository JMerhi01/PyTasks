# New movie ratings

age = input("Please enter your age: ")

# Age check if 1-117
while not age.isdigit() or int(age) < 1 or int(age) > 117:
    age = input("Please input an age between 1 and 117: ")

age = int(age)
#
if age < 12:
    print("You can only watch movies rated Universal")
elif age < 15:
    print("You can watch movies rated Universal and PG")
elif age < 18:
    print("You can watch movies rated Universal, PG, and 12")
elif age == 18:
    print("You can watch movies rated Universal, PG, 12, and 15, and 18")
else:
    print("You can watch movies rated Universal, PG, 12, 15, and 18")