def separate_list(numbers: list):
    positive, negative = [], []
    for number in numbers:
        if number == 0:
            continue
        positive.append(number) if number > 0 else negative.append(number)  
    return (positive, negative)


if __name__ == "__main__":
    numbers = [1, -1, 2, -3, 5, -1, 1, 1, 9, 0]
    numbers1, numbers2 = separate_list(numbers)
    print(numbers1)
    print(numbers2)