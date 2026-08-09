#Tuples -Immutable

spices = ("salt", "cloves", "safron")
(spice1, spice2, spice3) = spices
print(f"Main Spices: {spice1}, {spice2}, {spice3}")

ginger_ratio , salt_ratio = 2,3
print(f"Ratio Ginger is: {ginger_ratio}, Ratio salt is:{salt_ratio}")

ginger_ratio , salt_ratio = salt_ratio, ginger_ratio
print(f"Ratio Ginger is: {ginger_ratio}, Ratio salt is:{salt_ratio}")

# membership testing
(print(f"Is safron is in spices? {"safron" in spices}"))
(print(f"Is paprica is in spices? {"paprica" in spices}"))
print(f"Is cloves in spoces? {"cloves" in spices}")