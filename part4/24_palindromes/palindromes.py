def main():
    while True:
        get_string = input("Please type in a palindrome: ")
        if palindromes(get_string):
            print(f"{get_string} is a palindrome!")
            break
        else:
            print("that wasn't a palindrome")


def palindromes(string: str) -> bool:
    return string[::-1] == string


main()