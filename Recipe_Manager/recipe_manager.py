import recipes as recipes_dict
import os 
current_directory = os.getcwd()
recipe_folder_path = os.path.join(current_directory, "saved recipes")
if not os.path.exists(recipe_folder_path):
    os.mkdir(recipe_folder_path)
# The is the Recipe class
class Recipe:
    def __init__(self, recipe_title, ingredient_list, instruction_list, cooking_time, dietary_info, equipment_list):
        self.title = recipe_title.title()
        self.ingredient_list = ingredient_list
        self.instruction_list = instruction_list
        self.cooking_time = cooking_time
        self.dietary_info = dietary_info
        self.equipment_list = equipment_list

    # Function for setting the name of the recipe and forcing user input to title case
    def set_title(self, recipe_title):
        self.title = recipe_title.title()

    def get_title(self):  # Function for retrieving the name of the recipe
        return self.title

    # Function for setting the list of ingredients
    def set_ingredients(self, ingredient_list):
        self.ingredient_list = ingredient_list

    def get_ingredients(self):  # Function for retrieving the ingredient list
        return self.ingredient_list

    def get_ingredients_file(self):
        return ', '.join(self.ingredient_list)
    
    # Function for setting the instructions
    def set_instructions(self, instruction_list):
        self.instruction_list = instruction_list

    def get_instructions(self):  # Function for retrieving the instructions
        return self.instruction_list

    def get_instructions_file(self):
        return ', '.join(self.instruction_list)
    # Function for setting the cooking time
    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time

    def get_cooking_time(self):  # Function for retrieving the cooking time
        return self.cooking_time

    # Function for setting the dietary info
    def set_dietary_info(self, dietary_info):
        self.dietary_info = dietary_info.capitalize()

    def get_dietary_info(self):  # Function for retrieving the dietary info
        return self.dietary_info

    # Function for setting the equipment needed
    def set_equipment(self, equipment):
        self.equipment_list = equipment

    # Function for getting the equipment
    def get_equipment(self):
        return self.equipment_list
    
    def get_equipment_file(self):
        return ', '.join(self.equipment_list)

    def get_details(self, details):
        details_dict = {}
        for detail in details:
            match detail:
                case "title":
                    details_dict["title"] = self.get_title()
                case "ingredients":
                    details_dict["ingredients"] = self.get_ingredients()
                case "instructions":
                    details_dict["instructions"] = self.get_instructions()
                case "cooking_time":
                    details_dict["cooking_time"] = self.get_cooking_time()
                case "dietary_info":
                    details_dict["dietary_info"] = self.get_dietary_info()
                case "equipment":
                    details_dict["equipment"] = self.get_equipment()
        return details_dict


class RecipeManager:
    def __init__(self):

        
        self.recipes = []  # Initialize an empty list to store recipes
        
        i = 0
        while i < len(recipes_dict.recipes):
            recipe = Recipe(**recipes_dict.recipes[i])
            self.add_recipe(recipe)
            i = i + 1

  
    def add_recipe(self, recipe):
        self.recipes.append(recipe)  # Add a recipe to the list of recipes        
        self.save_recipe_to_file()

    # This seems to be an infinate loop
        # temp = {
        # 'cooking_time': recipe.get_cooking_time(),
        # 'recipe_title': recipe.get_title(),
        # 'dietary_info': recipe.get_dietary_info(),
        # 'ingredient_list': recipe.get_ingredients(),
        # 'instruction_list': recipe.get_instructions(),
        # 'equipment_list': recipe.get_equipment()
        # }
        # recipes_dict.recipes.append(temp)
    
    def get_all_recipes(self):
        return self.recipes  # Return all recipes
    
    def get_recipe(self, recipe_index): # Return a recipe via the index
        if recipe_index >= 0 and recipe_index < len(self.recipes):
            return self.recipes[recipe_index]
        else:
            return None

    def check_if_list_or_string(value):
        if type(value) == list:
            return '\n'.join(value)
        else:
            return value

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
        #recipe_selected = recipe.curselection()
        for recipe in self.recipes:
            # Find the recipe with the matching title and update its attributes
            if recipe.get_title() == recipe_title:
                recipe.set_title(new_recipe.title)
                recipe.set_ingredients(new_recipe.ingredient_list)
                recipe.set_instructions(new_recipe.instruction_list)
                recipe.set_cooking_time(new_recipe.cooking_time)
                recipe.set_dietary_info(new_recipe.dietary_info)
                break

    def update_recipe_ui(self, recipe_index, new_recipe):
        if recipe_index >= 0 and recipe_index < len(self.recipes):
            self.recipes[recipe_index] = new_recipe
        self.save_recipe_to_file()
        self.save_recipes_to_dict()

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
    
    def delete_recipe_index(self, recipe_index):
        if recipe_index >= 0 and recipe_index < len(self.recipes):
            del self.recipes[recipe_index]

    # This function prints the details of recipes by iterating over a list of recipes.
    # def print_recipes(self, recipes, recipe_attributes):
    #     # Iterate through each recipe in the 'recipes' list.
    #     for recipe in recipes:
    #         # Call the 'print_recipe_details' function to print the details of the current recipe.
    #         print_recipe_details(recipe, recipe_attributes)
    #         # Print a new line after printing the details of each recipe.
    #         print("\n")



    
    def save_recipe_to_file(self):
        for recipe in self.recipes:
            filename = os.path.join(recipe_folder_path, f"{recipe.get_title()}.txt")
            with open(filename, 'w') as f:
                f.write(f"{recipe.get_title()}\n")
                f.write(f"{recipe.get_ingredients_file()}\n")
                f.write(f"{recipe.get_instructions_file()}\n")
                f.write(f"{recipe.get_cooking_time()}\n")
                f.write(f"{recipe.get_dietary_info()}\n")
                f.write(f"{recipe.get_equipment_file()}")

    # Attempting to save recipe to dictionary, seems to crash during runtime
    def save_recipes_to_dict(self):
        pass

        
        #     temp = {
        #         'cooking_time': recipe.get_cooking_time(),
        #         'recipe_title': recipe.get_title(),
        #         'dietary_info': recipe.get_dietary_info(),
        #         'ingredient_list': recipe.get_ingredients(),
        #         'instruction_list': recipe.get_instructions(),
        #         'equipment_list': recipe.get_equipment()
        #         }
        #     recipes_dict.recipes.append(temp)
    
    def load_recipe_from_file(self, filename):
        if filename.endswith('txt'):
                with open(filename) as recipe_file:
                    lines = recipe_file.readlines()
                    if len(lines) == 6:
                        title = lines[0].strip()
                        ingredients = [ingredient.strip() for ingredient in lines[1].split(",")]
                        instructions = [instruction.strip() for instruction in lines[2].split(",")]
                        cooking_time = lines[3].strip()
                        dietary_info = lines[4].strip()
                        equipment = [item.strip() for item in lines[5].split(",")]
                        recipe = Recipe(title, ingredients, instructions, cooking_time, dietary_info, equipment)
                        self.add_recipe(recipe)



#   on load if recipe_title = recipe_title.txt
#   pass
#   otherwise, load
#
#  from Tkinter import Tk     # from tkinter import Tk for Python 3.x
#  from tkinter.filedialog import askopenfilename

# Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
# filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
# print(filename)
# #
# #
#
#