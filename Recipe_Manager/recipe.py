class Recipe(): # Creating the recipe class
    
    def __init__(self, recipe_name, recipe_ingredients, recipe_instructions, recipe_cooking_time, recipe_dietary_info): # Constructor for new recipes        
        self.title = recipe_name.title()
        self.ingredients = recipe_ingredients
        self.instructions = recipe_instructions
        self.cooking_time = recipe_cooking_time
        self.dietary_info = recipe_dietary_info.capitalize()

    def set_title(self, recipe_name): # Function for setting the name of the recipe and forcing user input to title case
        self.title = recipe_name.title()
    
    def get_title(self): # Function for retrieving the name of the recipe
        return self.title
    
    def set_ingredients(self, recipe_ingredients): # Function for setting the list of ingredients
        self.ingredients = recipe_ingredients

    def get_ingredients(self): # Function for retrieving the ingredient list
        return self.ingredients
    
    def set_instructions(self, recipe_instructions): # Function for setting the instructions
        self.instructions = recipe_instructions

    def get_instructions(self): # Function for retrieving the instructions
        return self.instructions
    
    def set_cooking_time(self, recipe_cooking_time): # Function for setting the cooking time
        self.cooking_time = recipe_cooking_time

    def get_cooking_time(self): # Function for retrieving the cooking time
        return self.cooking_time
    
    def set_dietary_info(self, recipe_dietary_info): # Function for setting the dietary info
        self.dietary_info = recipe_dietary_info.capitalize()

    def get_dietary_info(self): # Function for retrieving the dietary info
        return self.dietary_info

    def get_details(self): # Function for displaying all of the information in the recipe
        print(f"Recipe: {self.title} \n"
              f"Dietary information: {self.dietary_info} \n"
              f"This recipe takes {self.cooking_time} minutes to cook")
        print("The ingredients are: " + ', '.join(self.ingredients).capitalize())        
        length = len(self.instructions)
        for i in range(length):
            i = int(i)
            print(f"{i + 1}. {self.instructions[i].capitalize()}")
            

class Recipe_manager(Recipe): # Creating Recipe_manager class that inherits all functions in Recipe class
    
    def new_recipe(self): # Function to add new recipes
        recipe_name = input("Please enter the name of the recipe: ")
        dietary_info = input("Please enter the calories per serving: ") # Asking the user for the recipe details
        cook_time = input("Please enter the cook time for this recipe: ")
        ingredients = []
        instructions = []
        n = int(input("Please enter the number of ingredients: "))
        for i in range(0, n):
            item = input("Please enter an ingredient: ")
            ingredients.append(item)
        n = int(input("Please enter how many steps there are in the recipe: "))
        for i in range(0, n):
            step = input("Please enter the next instruction: ")
            instructions.append(step)
        
         # = Recipe(recipe_name, ingredients, instructions, cook_time, dietary_info)
