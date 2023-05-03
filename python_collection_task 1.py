# Defining the list
cool_things = ["Super Computer", "Luxury Home", "Custom Mobile", "Fastest Internet", "Tesla"]

# Checking it's type
print(cool_things)
print(type(cool_things))

# Printing the first element
print(cool_things[0])

# Printing the second element
print(cool_things[1])

# Printing the last element using negative indexing
print(cool_things[-1])

# Replacing the first element
cool_things[0] = "Private Island"

# Replacing something in the list
cool_things[2] = "Bat Mobile"
print(cool_things)

# Adding something new to the list
cool_things.append("Gamer Den")
print(cool_things)

# Remove a specific item from the list
cool_things.remove("Tesla")
print(cool_things)

# Removing the last item from the list
cool_things.pop()
print(cool_things)