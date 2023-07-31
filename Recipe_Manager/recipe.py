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

    # Function for setting the equipment needed
    def set_equipment(self, equipment):
        self.equipment_list = equipment

    # Function for getting the equipment
    def get_equipment(self):
        return self.equipment_list

    # def get_detail(self, detail):
    #     if type(details) == str:
    #         details = [details]
    #     match detail:
    #         case "title":
    #             return self.get_title()
    #         case "ingredients":
    #             return self.get_ingredients()
    #         case "instructions":
    #             return self.get_instructions()
    #         case "cooking_time":
    #             return self.get_cooking_time()
    #         case "dietary_info":
    #             return self.get_dietary_info()
    #         case "equipment":
    #             return self.get_equipment()
    #         case _:
    #             print("Invalid detail type entered")
    #             return None

    def get_recipe_details(self, details=['title', 'ingredients', 'instructions', 'cooking_time', 'dietary_info', 'equipment']):
        details_dict = {}
        if type(details) == str:
            details = [details]
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
                case _:
                    print("Invalid detail type entered")
        return details_dict

    # def get_recipe_to_preview(self, details):
    #     details_dict = {}
    #     if type(details) == str:
    #         details = [details]
    #     for detail in details:
    #         match detail:
    #             case "title":
    #                 f"Recipe Title: {detail}"
    #             case "ingredients":
    #                 details_dict["ingredients"] = self.get_ingredients()
    #             case "instructions":
    #                 details_dict["instructions"] = self.get_instructions()
    #             case "cooking_time":
    #                 details_dict["cooking_time"] = self.get_cooking_time()
    #             case "dietary_info":
    #                 details_dict["dietary_info"] = self.get_dietary_info()
    #             case "equipment":
    #                 details_dict["equipment"] = self.get_equipment()
    #             case _:
    #                 print("Invalid detail type entered")
    #     return details_dict
