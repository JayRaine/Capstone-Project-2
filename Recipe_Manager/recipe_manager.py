
class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def update_recipe(self, recipe_title, new_recipe):
        for recipe in self.recipes:
            if recipe.get_title() == recipe_title:
                recipe.set_title(new_recipe.title)
                recipe.set_ingredients(new_recipe.ingredient_list)
                recipe.set_instructions(new_recipe.instruction_list)
                recipe.set_cooking_time(new_recipe.cooking_time)
                recipe.set_dietary_info(new_recipe.dietary_info)
                break
