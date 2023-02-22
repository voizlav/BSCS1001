def all_the_longest(items: list) -> list:
    return [i for i in items if len(i) == max(len(x) for x in items)]

if __name__ == "__main__":
    print(all_the_longest(["adele", "mark", "dorothy", "tim", "hedy", "richard"]))