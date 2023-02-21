get_number = int(input("Please type in a positive integer: "))

for i in range(-get_number, get_number + 1):
    if i == 0:
        continue
    print(i)