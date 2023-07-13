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
            
