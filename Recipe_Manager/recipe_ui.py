from recipe import Recipe  # Import the Recipe class from recipe.py
# Import the RecipeManager class from recipe_manager.py
from recipe_manager import RecipeManager
from recipes import recipes  # Import the 'recipes' dictionary from recipes.py
import tkinter as tk


# initiallize
window = tk.Tk()
window.title("Recipe Management System")
window.geometry('1000x725')
# Window will open on centre of the screeen
window.eval("tk::PlaceWindow . center")
bg_colour = "#59656F"  # Setting a variable to colour
bg_colour2 = "#cdd1cd"

# Dividing the window in 2 parts

frame_left = tk.Frame(window,
                      width=300,
                      height=7250,
                      background=bg_colour,
                      relief="flat")
frame_left.grid(row=0, column=0)
frame_left.pack_propagate(False)  # background colour to all page

frame_right = tk.Frame(window,
                       width=700,
                       height=725,
                       background=bg_colour2,
                       relief="flat")
frame_right.grid(row=0, column=1)
frame_right.pack_propagate(False)  # background colour to all page

# frame_right widgets
# logo_img = ImageTk.PhotoImage(Image.open('logo.png').convert('RGB'))
# logo_widget = tk.Label(frame_right, image = logo_img) # converting to widget, tkinter doesn't have an specific
# logo_widget.image = logo_img
# logo_widget.pack() #place widget in frame

# Instructions widget
tk.Label(frame_left,
         text="Recipe Management System",
         background=bg_colour,  # Setting label background colour
         foreground="white",  # Setting text colour
         font=("TkMenuFont", 20)  # Setting font type and size
         ).pack()  # Pack method to organise

recipe_1 = {
    'cooking_time': 60,
    'recipe_title': "chicken",
    'dietary_info': "chicken",
    'ingredient_list': ["chicken", "water", "pan"],
    'instruction_list': ["boil water", "put chicken in water", "wait 60 minutes", "chicken is cooked"],
    'equipment_list': ["pan", "knife", "spoon"]
}

recipe1 = Recipe(**recipe_1)


# Initialize recipe manager
recipe_manager = RecipeManager()
# ****** In progress*********#
#     add recipe function that is available
#     recipe1 = recipe_manager.add_recipe(recipe)

#     get recipe functions that are available
#     recipe1 = recipe_manager.get_recipe_by_title(recipe_title)
#     all_recipes_with_ingredients... = recipe_manager.get_recipe_by_ingredients(ingredients)
#     all_recipes_with_instructions... = recipe_manager.get_recipe_by_instructions(instructions)
#     all_recipes_with_cooking_time... = recipe_manager.get_recipe_by_cooking_time(cooking_time)
#     all_recipes_with_dietary_info... = recipe_manager.get_recipe_by_dietary_info(dietary_info)
#     all_recipes_with_recipe_equipament... = recipe_manager.get_recipe_by_equipament(recipe_equipament)

#     get all recipes function available
# all_recipes = recipe_manager.get_all_recipes()

# #     update recipe functions that are available
# update_recipe = recipe_manager.update_recipe(recipe_title, recipe)
# update_recipe_ingredients = recipe_manager.update_recipe_by_ingredients(
#     recipe_title, ingredients)
# update_recipe_instructions = recipe_manager.update_recipe_by_instructions(
#     recipe_title, instructions)
# update_recipe_cooking_time = recipe_manager.update_recipe_by_cooking_time(
#     recipe_title, cooking_time)
# update_recipe_dietary_info = recipe_manager.update_recipe_by_dietary_info(
#     recipe_title, dietary_info)
# update_recipe_equipament = recipe_manager.update_recipe_by_equipament(
#     recipe_title, recipe_equipament)


def delete_recipe():
    print("Hello")


# Buttons widget
# Button to add a new recipe
add_button = tk.Button(
    frame_left,
    width=15,
    height=1,
    text="Add a new recipe",  # Text shown on button
    font=("TkMenuFont", 15),  # Setting font type and size
    background="pink",  # Setting button background colour
    foreground="black",  # Setting text colour
    cursor="hand2",  # Change the cursor to the hand
    activebackground="#badee2",  # Changes background colour when cursor click
    activeforeground="black",  # Changes font colour when cursor click
    # Function which runs every time the button is pressed
    command=recipe_manager.add_recipe(recipe1)
).pack()

# Button to view all recipes
get_all_button = tk.Button(
    frame_left,
    width=15,
    height=1,
    text="View all recipes",  # Text shown on button
    font=("TkMenuFont", 15),  # Setting font type and size
    background="pink",  # Setting button background colour
    foreground="black",  # Setting text colour
    cursor="hand2",  # Change the cursor to the hand
    activebackground="#badee2",  # Changes background colour when cursor click
    activeforeground="black",  # Changes font colour when cursor click
    # Function which runs every time the button is pressed get_all_recipes and prints on screen
    command=recipe_manager.get_all_recipes()
).pack()

# Button to edit a recipe
update_button = tk.Button(
    frame_left,
    width=15,
    height=1,
    text="Update a recipe",  # Text shown on button
    font=("TkMenuFont", 15),  # Setting font type and size
    background="pink",  # Setting button background colour
    foreground="black",  # Setting text colour
    cursor="hand2",  # Change the cursor to the hand
    activebackground="#badee2",  # Changes background colour when cursor click
    activeforeground="black",  # Changes font colour when cursor click
    # Function which runs every time the button is pressed
    # command=update_recipe(title, attribute)
).pack()

# Button to delete a recipe
delete_button = tk.Button(
    frame_left,
    width=15,
    height=1,
    text="Delete a recipe",  # Text shown on button
    font=("TkMenuFont", 15),  # Setting font type and size
    background="pink",  # Setting button background colour
    foreground="black",  # Setting text colour
    cursor="hand2",  # Change the cursor to the hand
    activebackground="#badee2",  # Changes background colour when cursor click
    activeforeground="black",  # Changes font colour when cursor click
    # Function which runs every time the button is pressed
    # command=delete_recipe(recipe_title)
).pack()

# run
window.mainloop()  # displays app until the user closes it
