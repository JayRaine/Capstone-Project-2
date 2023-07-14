class Recipe:
    def __init__(self, recipe_title, ingredient_list, instruction_list, cooking_time, dietary_info):
        self.title = recipe_title
        self.ingredient_list = ingredient_list
        self.instruction_list = instruction_list
        self.cooking_time = cooking_time
        self.dietary_info = dietary_info

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

    # Function for setting the instructions
    def set_instructions(self, instruction_list):
        self.instruction_list = instruction_list

    def get_instructions(self):  # Function for retrieving the instructions
        return self.instruction_list

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

    def get_details(self):  # Function for displaying all of the information in the recipe
        print(f"Recipe: {self.title} \n"
              f"Dietary information: {self.dietary_info} \n"
              f"This recipe takes {self.cooking_time} minutes to cook")
        print("The ingredients are: " +
              ', '.join(self.ingredient_list).capitalize())
        length = len(self.instruction_list)
        for i in range(length):
            i = int(i)
            print(f"{i + 1}. {self.instruction_list[i].capitalize()}")
