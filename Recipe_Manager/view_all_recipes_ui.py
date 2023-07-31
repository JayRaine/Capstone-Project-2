import tkinter as tk
from recipe_manager import RecipeManager
from view_recipe_ui import create_recipe_preview


def create_view_all_recipes_preview(parent):
    recipe_manager = RecipeManager()

    def preview_recipe(parent, recipe):
        for widget in parent.winfo_children():
            widget.destroy()
        create_recipe_preview(parent, recipe)

    all_recipes = recipe_manager.get_all_recipes()

    for recipe in all_recipes:
        for key, value in recipe_manager.get_recipe(recipe, 'title').items():
            preview_text = f"{key}: {value}"
            label = tk.Button(
                parent,
                text=preview_text,
                width=50,
                height=2,
                bg="#eb8806",
                relief="flat",
                cursor="hand2",
                foreground="blue",
                activebackground="#eb8806",
                activeforeground="white",
                font=("Arial", 12),
                command=lambda recipe=recipe: preview_recipe(parent, recipe)
            )
            label.pack(anchor="center", pady=10, padx=20)

    # def preview_recipe_details(self, detail):
    #         match detail:
    #             case "title":
    #                  return f"Recipe Title: {detail}"
    #             case "ingredients":
    #                 return f"Ingredients:\n{self.check_if_list_or_string(self.get_ingredients())}"
    #             case "instructions":
    #                 return f"Instructions:\n{self.check_if_list_or_string(self.get_instructions())}"
    #             case "cooking_time":
    #                 f"This recipe takes {detail} minutes to cook"
    #             case "dietary_info":
    #                 f"Dietary information:\n{self.check_if_list_or_string(self.get_dietary_info())}"
    #             case "equipment":
    #                 f"Equipment needed:\n{self.check_if_list_or_string(self.get_equipment())}"
    #             case _:
    #                 print("Invalid detail type entered")
    #                 return None

    # def check_if_list_or_string(value):
    #     match type(value):
    #         case list:
    #             return '\n'.join(value)
    #         case _:
    #             return value
