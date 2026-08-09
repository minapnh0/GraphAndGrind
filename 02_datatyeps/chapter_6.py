# String - Immutable

chai_type= "Giner Chai"
Customer_name = "Parya"
print (f"order for {Customer_name} :{chai_type} please! ")


chai_description = "Aromatic & Bold"
print(f"Every Second Char: {chai_description[0:8:2]}")
print(f"First Word: {chai_description[:8]}")
print(f"Last Word: {chai_description[11:]}")
print(f"Revers :{chai_description[::-1]}")

label_text = "مينا"
encoded_label = label_text.encode("utf-8")
print(f"Non encoded label:{label_text}")
print(f"encoded label:{encoded_label}")

decoded_label= encoded_label.decode("utf-8")
print(f"decoded label:{decoded_label}")
