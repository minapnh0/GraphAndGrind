menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]

iced_tea = [tea for tea in menu if "Iced" in tea ]

print(iced_tea)


lenght_tea = [tea for tea in menu if len(tea)<10]
print(lenght_tea)