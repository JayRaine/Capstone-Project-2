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
# Print all recipes
recipe_manager.print_recipes(all_recipes, ['cooking_time',
                                           'dietary_info', 'ingredients', 'instructions', 'equipment'])  # Print details of the first recipe in the list


# Get the recipes from the recipe manager (returns a list)

# Get the recipe with the title "egg"
egg_recipe = recipe_manager.get_recipe_by_title(
    "egg")
# Get all 10 minute recipes
ten_min_recipes = recipe_manager.get_recipes_by_cooking_time(
    10)

# Print the details of the egg recipe
recipe_manager.print_recipes(egg_recipe, ['cooking_time',
                                          'dietary_info', 'ingredients', 'instructions', 'equipment'])
# Print all 10 minute recipes
recipe_manager.print_recipes(ten_min_recipes, ['cooking_time',
                                               'dietary_info', 'ingredients', 'instructions', 'equipment'])


# update recipe functions by attributes
recipe_manager.update_recipe_cooking_time("egg", 20)
recipe_manager.update_recipe_dietary_info("egg", "egg is good for you")
recipe_manager.update_recipe_ingredients("egg", ["egg", "water", "salt"])
recipe_manager.update_recipe_instructions(
    "egg2", ["boil water", "add egg", "add salt"])
recipe_manager.update_recipe_equipment("egg", ["pot", "spoon", "whisker"])
recipe_manager.update_recipe_title("egg", "scrambled egg")

# get the new recipe
egg_recipe2 = recipe_manager.get_recipe_by_title("scrambled egg")

# print the new recipe
recipe_manager.print_recipes(egg_recipe2, ['cooking_time',
                                           'dietary_info', 'ingredients', 'instructions', 'equipment'])

# delete recipe
recipe_manager.delete_recipe("scrambled egg")

# print all recipes again showing that scrabled egg is deleted
print("All recipes after deleting scrambled egg")
recipe_manager.print_recipes(all_recipes, ['cooking_time',
                                           'dietary_info', 'ingredients', 'instructions', 'equipment'])
