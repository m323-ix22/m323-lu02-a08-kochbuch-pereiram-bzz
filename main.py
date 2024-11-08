import json


def adjust_recipe(orig_rec, num_people):
    """
    Adjusts the recipe based on the number of people.

    Parameters:
        orig_rec (dict): The original recipe.
        num_people (int): The number of people to adjust the recipe for.

    Returns:
        dict: The adjusted recipe.
    """
    adjusted_ingredients = {}
    original_servings = orig_rec['servings']
    factor = num_people / original_servings

    for ingredient, amount in orig_rec['ingredients'].items():
        adjusted_ingredients[ingredient] = amount * factor

    adjust_rec = {
        'title': orig_rec['title'],
        'ingredients': adjusted_ingredients,
        'servings': num_people
    }
    return adjust_rec


def load_recipe(json_string):
    """
    Loads a recipe from a JSON string.

    Parameters:
        json_string (str): The JSON string containing the recipe.

    Returns:
        dict: The recipe as a Python dictionary.
    """
    return json.loads(json_string)


if __name__ == '__main__':
    recipe_json = ('{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, '
                   '"Minced Meat": 500}, "servings": 4}')
    original_recipe = load_recipe(recipe_json)
    adjusted_recipe = adjust_recipe(original_recipe, 8)
    print(f"Original Recipe: {original_recipe}")
    print(f"Adjusted Recipe: {adjusted_recipe}")
