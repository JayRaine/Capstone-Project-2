from recipe import Recipe  # Import the Recipe class from recipe.py
# Import the RecipeManager class from recipe_manager.py
from recipe_manager import RecipeManager
from recipes import recipes  # Import the 'recipes' dictionary from recipes.py

recipe_manager = RecipeManager()  # Create an instance of the RecipeManager class

# Create a Recipe instance using the 'egg_recipe' dictionary from recipes.py
recipe_instance = Recipe(**recipes['egg_recipe'])

# Add the created recipe to the recipe manager
recipe_manager.add_recipe(recipe_instance)




# Get all recipes from the recipe manager
all_recipes = recipe_manager.get_all_recipes()
for recipe in all_recipes:  # Iterate over each recipe
    print(recipe.get_details(['title', 'cooking_time',
                              'dietary_info', 'ingredients', 'instructions']))  # Print details of each recipe

# Get the recipe with the title "egg" from the recipe manager (returns a list)
egg_recipe = recipe_manager.get_recipe_by_title("egg")
# Print the details of the egg recipe in the list
recipe_manager.print_recipes(egg_recipe, ['cooking_time',
                                 'dietary_info', 'ingredients', 'instructions']) # Print details of the first recipe in the list

# update recipe functions by attributes
recipe_manager.update_recipe_title("egg", "egg2")
recipe_manager.update_recipe_cooking_time("egg", 20)
recipe_manager.update_recipe_dietary_info("egg2", "egg2")
recipe_manager.update_recipe_ingredients("egg2", ["egg2", "water2", "pan2"])
recipe_manager.update_recipe_instructions("egg2", ["boil water2", "put egg2 in water2", "wait 20 minutes", "egg2 is cooked"])

egg_recipe2 = recipe_manager.get_recipe_by_title("egg2")
recipe_manager.print_recipes(egg_recipe2, ['cooking_time',
                                 'dietary_info', 'ingredients', 'instructions']) # 
print(egg_recipe2[0].get_details(['title', 'cooking_time',
                                'dietary_info', 'ingredients', 'instructions']))
# patatoes_recipe = {
#     'cooking_time': 10,
#     'recipe_title': "patatoes",
#     'dietary_info': "patatoes",
#     'ingredient_list': ["patatoes", "water", "pan"],
#     'instruction_list': ["boil water", "put patatoes in water", "wait 10 minutes", "patatoes is cooked"]

# }
# egg.get_details()


