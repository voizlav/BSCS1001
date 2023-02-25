def histogram(string: str):
    result = {}
    
    for letter in string:
        if letter not in result:
            result[letter] = ""
        result[letter] += "*"
    
    for k, i in result.items():
        print(k, i) 


if __name__ == "__main__":
    histogram("test")