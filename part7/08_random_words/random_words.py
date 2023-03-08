from random import shuffle


def load_words(filename: str):
    result = []
    with open(filename) as f:
        for i in f:
            result.append(i.strip())
    return result


def words(n: int, beginning: str):
    result = []
    words = load_words("words.txt")
    for word in words:
        if word.startswith(beginning):
            result.append(word)
    if len(result) < n:
        raise ValueError("not enough words beginning with the", beginning)
    shuffle(result)
    return [word for word in result[:n]]


if __name__ == "__main__":
    word_list = words(3, "ca")
    for word in word_list:
        print(word)