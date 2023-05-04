# Fizzbuzz
# 3 == 0 so test the condition that if c is a multiple of the chosen number
# % modulo gives back the remainder of the division so if the % is 0 then
# there is no remainder and c is divisible by the number

for c in range(1, 101):
    if c % 3 == 0 and c % 5 == 0:
        print("FizzBuzz")
    elif c % 3 == 0:
        print("Fizz")
    elif c % 5 == 0:
        print("Buzz")
    else:
        print(c)