#Dictionary 

chai_order = dict(type = "Masala Chai", size = "Large", Sugar = 2)
print(f"Chai Order : {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"
print(f"Recipe base: {chai_recipe["base"]}")
print(f"Recipe Liquid: {chai_recipe["liquid"]}")

del chai_recipe["liquid"]
print(f"Chai Recipe: {chai_recipe}")

print(f"Is sugar in chai order: {"Sugar" in chai_order}")

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}
print(f"Order details (keys): {chai_order.keys()}")
print(f"Order details (values): {chai_order.values()}")
print(f"Chai order (items): {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Last item: {last_item}")

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)
print(f"Updated chai recipe: {chai_recipe}")

customer_note = chai_recipe.get("size", "No Note")
print(f" Customer note is: {customer_note}")

