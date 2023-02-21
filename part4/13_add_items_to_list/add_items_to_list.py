items = []
items_number = int(input("How many items: "))

for i in range(items_number):
    item = int(input(f"Item {i + 1}: "))
    items.append(item)

print(items)