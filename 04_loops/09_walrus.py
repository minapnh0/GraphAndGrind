# -------Walrus
value = 13
remainder = value % 5

if remainder:
    print(f"Not divisible, remainder is {remainder}")


# -------Walrus
if remainder:= value % 5:
    print(f"Not divisible, remainder is {remainder}")

# available_sizes = ["small", "medium", "large"]
# if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
#     print (f"serving {requested_size}")
# else:
#     print(f"Size is not available - {requested_size}")


# ------
flavors = ["masala", "ginger", "lemon", "mint"]
while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available")
print(f"You choose {flavor} chai")



