is_boiling= True
stri_count = 6
total_actions = is_boiling + stri_count # Upcasting
print (f"Total actions {total_actions}")

milk_present = 0
print (f"Is there milk? {bool(milk_present)}")

milk_presented = "milk"
print (f"Is there milk? {bool(milk_presented)}")

water_hot = True
tea_added = False

can_serve = water_hot and tea_added
print (f"Can serve Chai? {can_serve}")


