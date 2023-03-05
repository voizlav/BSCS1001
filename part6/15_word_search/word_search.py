def load_words(filename: str) -> list:
    result = []
    with open(filename) as f:
        for i in f:
            result.append(i.strip())
    return result


def find_words(search_term: str) -> list:
    result = []
    words = load_words("words.txt")
    if "*" in search_term:
        if search_term.startswith("*"):
            for word in words:
                result.append(word) if word.endswith(search_term[1:]) else None
        if search_term.endswith("*"):
            for word in words:
                result.append(word) if word.startswith(search_term[:-1]) else None
    elif "." in search_term:
        for word in words:
            if len(word) == len(search_term):
                for i in range(len(word)):
                    if "." == search_term[i]:
                        result.append(word) if i == len(word) - 1 else None
                        continue
                    if word[i] == search_term[i] and i == len(word) - 1:
                            result.append(word)
                    if word[i] != search_term[i]:
                        break
    else:
        for word in words:
            if search_term == word:
                result.append(word)
                break
    
    return result



if __name__ == "__main__":
    print(find_words("*vokes"))
    print(find_words("ca."))
    print(find_words("t.st"))