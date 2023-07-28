def print_recipe_details(recipe, recipe_details):
    for recipe_detail in recipe_details:
        detail = getattr(recipe, 'get_'+recipe_detail)()
        match recipe_detail:
            case "title":
                print(f"Recipe Title: {detail}")
            case "ingredients":
                print("The ingredients are: \n" +
                      ', '.join(detail).capitalize())
            case "instructions":
                print("The instructions are: ")
                for i, instruction in enumerate(detail):
                    print(f"{i + 1}. {instruction.capitalize()}")
            case "cooking_time":
                print(f"This recipe takes {detail} minutes to cook")
            case "dietary_info":
                print(f"Dietary information: {detail}")
            case "equipment":
                print("The equipment needed is: \n" +
                      ', '.join(detail).capitalize())


class RecipeManager:
    def __init__(self):
        self.recipes = []  # Initialize an empty list to store recipes

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

    # This function prints the details of recipes by iterating over a list of recipes.
    def print_recipes(self, recipes, recipe_attributes=["title", "ingredients", "instructions", "cooking_time", "dietary_info", "equipment"]):
        # Iterate through each recipe in the 'recipes' list.
        for recipe in recipes:
            # Call the 'print_recipe_details' function to print the details of the current recipe.
            print_recipe_details(recipe, recipe_attributes)
            # Print a new line after printing the details of each recipe.
            print("\n")
