def formatted(floats: list) -> list:
    return [f"{i:.2f}" for i in floats]


if __name__ == "__main__":
    print(formatted([1.234, 0.3333, 0.11111, 3.446]))