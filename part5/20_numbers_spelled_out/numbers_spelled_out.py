def dict_of_numbers():
    numbers = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "Thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety"
    }

    for i in range(0, 100):
        if i not in numbers:
            numbers[i] = f"{numbers[i - i % 10]}-{numbers[i % 10]}"
        numbers[i] = numbers[i].lower()
    
    return numbers


if __name__ == "__main__":
    test = dict_of_numbers()
    print(test[30])