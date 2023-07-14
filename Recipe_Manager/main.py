from recipe import Recipe

egg_recipe = {
    'cooking_time': 10,
    'recipe_title': "egg",
    'dietary_info': "egg",
    'ingredient_list': ["egg", "water", "pan"],
    'instruction_list': ["boil water", "put egg in water", "wait 10 minutes", "egg is cooked"]
}
egg = Recipe(**egg_recipe)

egg.get_details()
