while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    function = int(input("Function: "))
    if function == 1:
        entry = input("Diary entry: ")
        with open("diary.txt", "a") as d:
            d.write(entry + "\n")
        print("Diary saved")
    elif function == 2:
        print("Entries:")
        with open("diary.txt") as d:
            for i in d:
                print(i)
    elif function == 0:
        print("Bye now!")
        break