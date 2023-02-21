values = [1, 2, 3, 4, 5]

while True:
    get_index = int(input("Index: "))
    if get_index == -1:
        break
    new_value = int(input("New value: "))
    values[get_index] = new_value
    print(values)