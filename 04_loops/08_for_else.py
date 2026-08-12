staff = [("Nina", 16), ("Zara", 17), ("Tina", 15)]

for name, age in staff:
    if age <=18 :
        print(f"{name} : {age} is eligible to manage the staff ")
        break
else:
    print(f"No one is eligible to manage the staff")

