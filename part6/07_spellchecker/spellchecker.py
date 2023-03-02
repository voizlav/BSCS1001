word_list = []
get_string = input("Write text: ").split()

with open("wordlist.txt") as w:
    for i in w:
        word_list.append(i.strip())

result = []
for word in get_string:
    if word.lower() not in word_list:
        result.append(f"*{word}*")
        continue
    result.append(word)

print(" ".join(result))