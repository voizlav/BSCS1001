phonebook = {}

while True:
    option = int(input("command (1 search, 2 add, 3 quit): "))

    if option == 1:
        name = input("Name: ")

        if name not in phonebook:
            print("no number")
            continue
        for i in phonebook[name]:
            print(i)
    
    if option == 2:
        name = input("Name: ")
        number = input("Number: ")

        if name not in phonebook:
            phonebook[name] = []
        phonebook[name].append(number)

        print("ok!")
    
    if option == 3:
        print("quitting...")
        break