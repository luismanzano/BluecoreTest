# MIX POTIONS CHALLENGE

def mix_potions(potions):
    volume = 0
    ingredients = {}
    for potion in potions:
        volume += potion["volume"]

    for i, potion in enumerate(potions):
        for ingredient in potion["ingredients"]:
            if ingredient in ingredients:
                ingredients[ingredient] += potion['ingredients'][ingredient] * potion["volume"]
            else:
                ingredients[ingredient] = potion['ingredients'][ingredient] * potion["volume"]

    for ingredient in ingredients:
        ingredients[ingredient] /= volume

    return {
        "volume": volume,
        "ingredients": ingredients
    }

# THIS IS A BRUTE FORCE ALGORITHM I BELIEVE I COULD HAVE SIMPLIFIED IT WITH A BIT MORE TIME

if __name__ == '__main__':
    test = [
        {
            "volume": 100,
            "ingredients": {"ingredient1":50, "ingredient2":20, "ingredientA": 500}
        },
        {
            "volume": 300,
            "ingredients": {"ingredient1":150, "ingredientA":300, "ingredientB": 950, }
        }
    ]

    print(mix_potions(test))
