import os

# **********# for testing purposes #**********#


def print_recipe_details(recipe, recipe_details):
    for recipe_detail in recipe_details:
        detail = getattr(recipe, 'get_'+recipe_detail)()
        if recipe_detail == "title":
            print(f"Recipe Title: {detail}")
        elif recipe_detail == "ingredients":
            print(f"Ingredients: {check_if_list_or_string(detail)}")
        elif recipe_detail == "instructions":
            print(f"Instructions: {check_if_list_or_string(detail)}")
        elif recipe_detail == "cooking_time":
            print(f"This recipe takes {detail} minutes to cook")
        elif recipe_detail == "dietary_info":
            print(f"Dietary Information: {check_if_list_or_string(detail)}")
        elif recipe_detail == "equipment":
            print(f"Equipment Needed: {check_if_list_or_string(detail)}")
        else:
            print(f"Invalid recipe detail: {recipe_detail}")


def check_if_list_or_string(value):
    if type(value) == list:
        return '\n'.join(value)
    else:
        return value
# **********# till here for testing purposes #**********#


class RecipeManager:
    _instance = None

    # Initialize the RecipeManager class with an empty list of recipes
    # This is a singleton class, so only one instance of this class can be created
    def __new__(cls):
        if cls._instance is None:  # Check if an instance of this class has already been created
            cls._instance = super().__new__(cls)  # If not, create an instance
            cls._instance.recipes = []
        return cls._instance

    def add_recipe(self, recipe):
        self.recipes.append(recipe)  # Add a recipe to the list of recipes

    def get_all_recipes(self):
        return self.recipes  # Return all recipes

    # Get recipes by a specific attribute
    def get_recipes_by_attributes(self, recipe_attribute, recipe_value):
        results = []  # Initialize an empty list to store matching recipes
        for recipe in self.recipes:  # Iterate over each recipe in the list
            if type(getattr(recipe, recipe_attribute)) == list:
                # If the attribute is a list, check if the value is present in the list
                if recipe_value in getattr(recipe, recipe_attribute):
                    results.append(recipe)
            else:
                # Otherwise, directly compare the attribute value with the given value
                if getattr(recipe, recipe_attribute) == recipe_value:
                    # If the attribute value matches the given value, add the recipe to the list of matching recipes
                    results.append(recipe)
        if len(results) == 0:
            return None  # If no matching recipes found, return None
        return results  # Return the matching recipes

    # Helper functions to search recipes by specific attributes
    def get_recipe_by_title(self, recipe_title):
        return self.get_recipes_by_attributes("title", recipe_title.title())

    def get_recipes_by_ingredients(self, recipe_ingredients):
        return self.get_recipes_by_attributes("ingredient_list", recipe_ingredients)

    def get_recipes_by_cooking_time(self, recipe_cooking_time):
        return self.get_recipes_by_attributes("cooking_time", recipe_cooking_time)

    def get_recipes_by_dietary_info(self, recipe_dietary_info):
        return self.get_recipes_by_attributes("dietary_info", recipe_dietary_info)

    def get_recipes_by_equipment(self, recipe_equipment):
        return self.get_recipes_by_attributes("equipment_list", recipe_equipment)

    # **********# to be completed #**********#
    # Get recipes by a combination of attributes
    def get_recipes_by_attributes_combination(self, recipe_attributes, recipe_values):
        recipes = []
        for recipe in self.recipes:
            # Iterate over each recipe in the list
            for i, recipe_attribute in enumerate(recipe_attributes):
                # Check if the attribute is a list
                if type(getattr(recipe, recipe_attribute)) == list:
                    # Check if the value is present in the list
                    if recipe_values[i] in getattr(recipe, recipe_attribute):
                        # If the value is present, add the recipe to the list of matching recipes
                        recipes.append(recipe)
                else:
                    # Otherwise, directly compare the attribute value with the given value
                    if getattr(recipe, recipe_attribute) == recipe_values[i]:
                        # If the attribute value matches the given value, add the recipe to the list of matching recipes
                        recipes.append(recipe)
        # Remove duplicate recipes from the list
        if len(recipes) == 0:
            return None
        return recipes

    # Update a recipe by its title with a new recipe

    def update_recipe(self, recipe_title, new_recipe):
        # recipe_selected = recipe.curselection()
        for recipe in self.recipes:
            # Find the recipe with the matching title and update its attributes
            if recipe.get_title() == recipe_title:
                recipe.set_title(new_recipe.title)
                recipe.set_ingredients(new_recipe.ingredient_list)
                recipe.set_instructions(new_recipe.instruction_list)
                recipe.set_cooking_time(new_recipe.cooking_time)
                recipe.set_dietary_info(new_recipe.dietary_info)
                break

    # Update specific attribute of a recipe
    def update_recipe_attribute(self, recipe_attribute, recipe_name, new_value):
        for recipe in self.recipes:
            # Find recipe with matching title
            if recipe.get_title() == recipe_name.title():

                print(
                    f"Updating {recipe_attribute} of {recipe_name} to {new_value}\n")
                # Update the attribute with the new value
                getattr(recipe, 'set_'+recipe_attribute)(new_value)
                break

    # Helper functions to update specific attributes of a recipe
    def update_recipe_title(self, recipe_title, new_title):
        self.update_recipe_attribute("title", recipe_title, new_title)

    def update_recipe_ingredients(self, recipe_title, new_ingredients):
        self.update_recipe_attribute(
            "ingredients", recipe_title, new_ingredients)

    def update_recipe_instructions(self, recipe_title, new_instructions):
        self.update_recipe_attribute(
            "instructions", recipe_title, new_instructions)

    def update_recipe_cooking_time(self, recipe_title, new_cooking_time):
        self.update_recipe_attribute(
            "cooking_time", recipe_title, new_cooking_time)

    def update_recipe_dietary_info(self, recipe_title, new_dietary_info):
        self.update_recipe_attribute(
            "dietary_info", recipe_title, new_dietary_info)

    def update_recipe_equipment(self, recipe_title, new_equipment):
        self.update_recipe_attribute(
            "equipment", recipe_title, new_equipment)

    # Delete a recipe by its title
    def delete_recipe(self, recipe_title):
        for recipe in self.recipes:
            if recipe.get_title() == recipe_title.title():
                self.recipes.remove(recipe)  # Remove the recipe from the list
                break

    # get recipe details
    def get_recipe(self, recipe, recipe_attributes=["title", "ingredients", "instructions", "cooking_time", "dietary_info", "equipment"]):
        return recipe.get_recipe_details(recipe_attributes)

        # print(recipe.get_details(recipe_attributes))
        # print("\n")
        # print(recipe)
        # return recipe.get_details(recipe_attributes)

    # def save_recipes_to_file(self):
    #     with open("recipes.txt", "w") as file:
    #         for recipe in self.recipes:
    #             file.write(recipe.get_details() + "\n")

    #     def save_recipes(self):
    #     for recipe in self.recipes:
    #         filename = os.path.join(recipe_folder_path, f"{recipe.get_title()}.txt")
    #         with open(filename, 'w') as file:
    #             file.write(f"{recipe.get_title()}\n")
    #             file.write(f"{recipe.get_ingredients()}\n")
    #             file.write(f"{recipe.get_instructions()}\n")
    #             file.write(f"{recipe.get_cooking_time()}\n")
    #             file.write(f"{recipe.get_dietary_info()}\n")

    # def load_recipes_from_file(self):
    #     with open("recipes.txt", "r") as file:
    #         for line in file:
    #             recipe_details = line.split(",")
    #             recipe_title = recipe_details[0]
    #             recipe_ingredients = recipe_details[1]
    #             recipe_instructions = recipe_details[2]
    #             recipe_cooking_time = recipe_details[3]
    #             recipe_dietary_info = recipe_details[4]
    #             recipe_equipment = recipe_details[5]
    #             recipe = Recipe(recipe_title, recipe_ingredients, recipe_instructions,
    #                             recipe_cooking_time, recipe_dietary_info, recipe_equipment)
    #             self.recipes.append(recipe)

    # **********# for testing purposes #**********#

    def print_recipes(self, recipes, recipe_attributes=["title", "ingredients", "instructions", "cooking_time", "dietary_info", "equipment"]):
        for recipe in recipes:
            # Iterate through each recipe in the 'recipes' list.
            print_recipe_details(recipe, recipe_attributes)
            # Call the 'print_recipe_details' function to print the details of the current recipe.
            # Print a new line after printing the details of each recipe.
            print("\n")
    # **********# for testing purposes #**********#
