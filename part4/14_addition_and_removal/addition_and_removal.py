result = []

while True:
    print("The list is now", result)
    control = input("a(d)d, (r)emove or e(x)it: ")

    if control == "d":
        result.append(len(result) + 1)
    elif control == "r":
        result.pop()
    elif control == "x":
        print("Bye!")
        break
