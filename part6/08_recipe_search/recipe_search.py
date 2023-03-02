def load_recipes(filename: str) -> dict:
    recipes = {}
    with open(filename) as r:
        recipe = None
        for i in r:
            line = i.strip()
            if not recipe:
                recipe = line
                recipes[recipe] = []
                continue
            if not line:
                recipe = None
                continue
            recipes[recipe].append(line)
    return recipes


def search_by_name(filename: str, word: str) -> list:
    result = []
    recipes = load_recipes(filename)
    for recipe in recipes:
        if word in recipe.lower():
            result.append(recipe)
    return result


def search_by_time(filename: str, prep_time: int) -> list:
    result = []
    recipes = load_recipes(filename)
    for recipe in recipes:
        if int(recipes[recipe][0]) <= prep_time:
            result.append(f"{recipe}, preparation time {recipes[recipe][0]} min")
    return result


def search_by_ingredient(filename: str, ingredient: str) -> list:
    result = []
    recipes = load_recipes(filename)
    for recipe in recipes:
        if ingredient in recipes[recipe]:
            result.append(f"{recipe}, preparation time {recipes[recipe][0]} min")
    return result


if __name__ == "__main__":
    pass