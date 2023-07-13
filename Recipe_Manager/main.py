from recipe import Recipe

cook_time = 10
recipe_name = "egg"
dietary_info = "egg"
ingredient_list = ["egg", "water", "pan"]
instruction_list = ["boil water", "put egg in water", "wait 10 minutes", "egg is cooked"]
egg = Recipe(recipe_name, ingredient_list, instruction_list, cook_time, dietary_info)

egg.get_details()
