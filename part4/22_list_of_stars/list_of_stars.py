def list_of_stars(items: list) -> str:
    for i in items:
        print("*" * i)


if __name__ == "__main__":
    list_of_stars([1])