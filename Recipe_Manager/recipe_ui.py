
import tkinter as tk
from PIL import ImageTk, Image
import os  # Used to get the current working directory


from recipe import Recipe
from recipe_manager import RecipeManager
from recipes import recipes  # Import the 'recipes' dictionary from recipes.py

# Import the functions from the other UI files
from add_recipe_ui import create_add_recipe_preview
from view_all_recipes_ui import create_view_all_recipes_preview
from update_recipe_ui import create_update_recipe_preview
from search_recipe_ui import create_search_recipe_preview


# Change the current working directory to the directory of this file
current_directory = os.getcwd()

recipe_manager = RecipeManager()
recipe_manager.load_recipes_from_file()


def switch_preview(preview_type):
    # Remove the current right-side content
    for widget in frame_right.winfo_children():
        widget.destroy()

    if preview_type == "Add Recipe":
        create_add_recipe_preview(frame_right)
    elif preview_type == "View All Recipes":
        create_view_all_recipes_preview(frame_right)
    elif preview_type == "Update Recipe":
        create_update_recipe_preview(frame_right)
    elif preview_type == "search_recipe":
        create_search_recipe_preview(frame_right)


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

# Adding a logo to the left frame
logo = ImageTk.PhotoImage(Image.open(
    current_directory + "/Recipe_Manager/logo.png"))
logo_label = tk.Label(frame_left, image=logo, width=200, height=150)
logo_label.pack(pady=10)


# Adding buttons to the left frame
preview_options = ["Add Recipe", "View All Recipes",
                   "Update Recipe", "search_recipe"]
for option in preview_options:

    tk.Button(frame_left, text=option,
              width=15,
              height=3,
              background="#d1163c",
              foreground="white",
              cursor="hand2",
              activebackground="#badee2",
              activeforeground="black",
              font=("TkMenuFont", 13, "bold"),
              command=lambda opt=option: switch_preview(opt)).pack(pady=5)


frame_right = tk.Frame(window,
                       width=700,
                       height=7250,
                       background=bg_colour2,
                       relief="flat")
frame_right.grid(row=0, column=1)
frame_right.pack_propagate(False)  # background colour to all page

# Initialize with the first preview option
switch_preview(preview_options[0])


# Initialize recipe manager
recipe_manager = RecipeManager()
# ****** In progress*********#


def get_all_recipes():  # function to get all recipes from the recipe manager
    all_recipes = recipe_manager.get_all_recipes()
    print(all_recipes)
    # * in the meantime just prints all recipes should be changed to display in the UI *#
    recipe_manager.print_recipes(all_recipes)


# *    get recipe functions that are available * #
#     recipe1 = recipe_manager.get_recipe_by_title(recipe_title)
#     all_recipes_with_ingredients... = recipe_manager.get_recipe_by_ingredients(ingredients)
#     all_recipes_with_instructions... = recipe_manager.get_recipe_by_instructions(instructions)
#     all_recipes_with_cooking_time... = recipe_manager.get_recipe_by_cooking_time(cooking_time)
#     all_recipes_with_dietary_info... = recipe_manager.get_recipe_by_dietary_info(dietary_info)
#     all_recipes_with_recipe_equipament... = recipe_manager.get_recipe_by_equipament(recipe_equipament)


# *     update recipe functions that are available *#
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
#    delete recipe function that is available
# delete_recipe = recipe_manager.delete_recipe(recipe_title)


def delete_recipe():
    print("Hello")


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
    # command=recipe_manager.delete_recipe('egg_recipe')
).pack()


# run
window.mainloop()  # Run the event loop, displays app until the user closes it
