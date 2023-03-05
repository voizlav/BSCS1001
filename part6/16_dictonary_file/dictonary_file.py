
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    option = int(input("Function: "))
    if option == 1:
        fin_word = input("The word in Finnish: ")
        eng_word = input("The word in English: ")
        with open("dictionary.txt", "a") as d:
            d.write(f"{fin_word} - {eng_word}\n")
        print("Dictionary entry added")
    if option == 2:
        search_term = input("Search term: ")
        words = []
        with open("dictionary.txt") as d:
            for i in d:
                words.append(i.strip())
        for word in words:
            if search_term in word:
                print(word)
    if option == 3:
        print("Bye!")
        break