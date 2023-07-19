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
        return details_dict

    # # Function for printing the recipe details
    # def print_recipes(self, details):
    #     recipe_dict = self.get_details(details)
    #     for detail in recipe_dict:
    #         match detail:
    #             case "title":
    #                 print(f"Recipe: {detail}")
    #             case "ingredients":
    #                 print("The ingredients are: " +
    #                       ', '.join(detail).capitalize())
    #             case "instructions":
    #                 for i, instruction in enumerate(detail):
    #                     print(f"{i + 1}. {instruction.capitalize()}")
    #             case "cooking_time":
    #                 print(f"This recipe takes {detail} minutes to cook")
    #             case "dietary_info":
    #                 print(f"Dietary information: {detail}")

    # def get_details(self):
    #     print(f"Recipe: {self.title}")
    #     print(f"Dietary information: {self.dietary_info}")
    #     print(f"This recipe takes {self.cooking_time} minutes to cook")
    #     print("The ingredients are: " +
    #           ', '.join(self.ingredient_list).capitalize())
    #     for i, instruction in enumerate(self.instruction_list):
    #         print(f"{i + 1}. {instruction.capitalize()}")
