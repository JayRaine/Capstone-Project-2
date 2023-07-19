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

class RecipeManager:
    def __init__(self):
        self.recipes = []  # Initialize an empty list to store recipes

    def add_recipe(self, recipe):
        self.recipes.append(recipe)  # Add a recipe to the list of recipes

    def get_all_recipes(self):
        return self.recipes  # Return all recipes

    # Get recipes by a specific attribute
    def get_recipes_by_attributes(self, recipe_attribute, recipe_value):
        recipes = []  # Initialize an empty list to store matching recipes
        for recipe in self.recipes:  # Iterate over each recipe in the list
            if type(getattr(recipe, recipe_attribute)) == list:
                # If the attribute is a list, check if the value is present in the list
                if recipe_value in getattr(recipe, recipe_attribute):
                    recipes.append(recipe)
            else:
                # Otherwise, directly compare the attribute value with the given value
                if getattr(recipe, recipe_attribute) == recipe_value:
                    # add the recipe to the list of matching recipes
                    recipes.append(recipe)
        if len(recipes) == 0:
            return None  # If no matching recipes found, return None
        return recipes  # Return the list of matching recipes

    # Helper functions to search recipes by specific attributes
    def get_recipe_by_title(self, recipe_title):
        return self.get_recipes_by_attributes("title", recipe_title)

    def get_recipes_by_ingredients(self, recipe_ingredients):
        return self.get_recipes_by_attributes("ingredient_list", recipe_ingredients)

    def get_recipes_by_cooking_time(self, recipe_cooking_time):
        return self.get_recipes_by_attributes("cooking_time", recipe_cooking_time)

    def get_recipes_by_dietary_info(self, recipe_dietary_info):
        return self.get_recipes_by_attributes("dietary_info", recipe_dietary_info)

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
    def update_recipe_attribute(self, recipe_attribute, recipe_value, new_value):
        for recipe in self.recipes:
            # Find recipes where the specified attribute matches the given value
            if getattr(recipe, recipe_attribute) == recipe_value:
                # Update the attribute with the new value
                setattr(recipe, recipe_attribute, new_value)
                break

    # Helper functions to update specific attributes of a recipe
    def update_recipe_title(self, recipe_title, new_title):
        self.update_recipe_attribute("title", recipe_title, new_title)

    def update_recipe_ingredients(self, recipe_title, new_ingredients):
        self.update_recipe_attribute(
            "ingredient_list", recipe_title, new_ingredients)

    def update_recipe_instructions(self, recipe_title, new_instructions):
        self.update_recipe_attribute(
            "instruction_list", recipe_title, new_instructions)

    def update_recipe_cooking_time(self, recipe_title, new_cooking_time):
        self.update_recipe_attribute(
            "cooking_time", recipe_title, new_cooking_time)

    def update_recipe_dietary_info(self, recipe_title, new_dietary_info):
        self.update_recipe_attribute(
            "dietary_info", recipe_title, new_dietary_info)

    # Delete a recipe by its title
    def delete_recipe(self, recipe_title):
        for recipe in self.recipes:
            if recipe.get_title() == recipe_title:
                self.recipes.remove(recipe)  # Remove the recipe from the list
                break

    # This function prints the details of recipes by iterating over a list of recipes.
    def print_recipes(self, recipes, recipe_details):
        
        # Iterate through each recipe in the 'recipes' list.
        for recipe in recipes: 
            
            # Call the 'print_recipe_details' function to print the details of the current recipe.
            print_recipe_details(recipe, recipe_details)
            
            # Print a new line after printing the details of each recipe.
            print("\n")
        


