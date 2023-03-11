def convert(my_list, my_function):
    return [my_function(i) for i in my_list]


def to_euro(number):
    return f"{number} €"


if __name__ == "__main__":
    my_list = [2, 3, 4, -5, "test", 1.333334, -3.4567, True]
    euros = convert(my_list, to_euro)
    print(euros)