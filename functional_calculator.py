# Functional Calculator

# Functions
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def modulo(num1, num2):
    return num1 % num2

def cm_to_m(num):
    return num / 100

def m_to_feet(num):
    return num * 3.28084

# Displaying the menu
print("Select what you'd like to do.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Modulo")
print("6. Convert cm to m")
print("7. Convert m to feet")

# The Input
while True:
    choice = input("Enter choice(1/2/3/4//6/7): ")
# Float to convert input for numbers in to floating numbers
    if choice in ('1', '2', '3', '4', '5',):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

# After they pick the number they want and add the numbers
# if and elif and else to check which one they picked and depending...
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    elif choice == '5':
        print(num1, "%", num2, "=", modulo(num1, num2))
    elif choice == '6':
        cm = float(input("Enter length in centimeters: "))
        m = cm_to_m(cm)
        print(cm, "cm =", m, "m")
    elif choice == '7':
        m = float(input("Enter length in meters: "))
        feet = m_to_feet(m)
        print(m, "m =", feet, "ft")
# picked choice with num1 and num2 and print statement.
# If they misstype something then make an error message
    else:
        print("Invalid Input")
