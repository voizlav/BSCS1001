def everything_reversed(items: list) -> list:
    return [i[::-1] for i in items][::-1]


if __name__ == "__main__":
    print(everything_reversed(["Hi", "there", "example", "one more"]))