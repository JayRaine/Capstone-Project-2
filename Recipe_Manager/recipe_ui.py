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
                       height=7250,
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
         width=25,  # Setting label width
         height=3,
         text="Recipe Management System",
         background=bg_colour,  # Setting label background colour
         foreground="white",  # Setting text colour
         font=("TkMenuFont", 13)  # Setting font type and size
         ).pack()  # Pack method to organise


recipe1 = Recipe(**recipes['egg_recipe'])


# Initialize recipe manager
recipe_manager = RecipeManager()
# ****** In progress*********#

# Create a list to store ingredients
ingredients_list = []

# function to add ingredients to the list of ingredients and update the preview


def add_ingredients():
    ingredients_list.append(ingredients.get())
    # Call the update_preview() function to update the preview
    update_preview()

# function to update the preview


def update_preview():
    # Update the text attribute of the label with the current list of ingredients
    preview_ingredients.config(
        text="Ingredients: " + ', '.join(ingredients_list).capitalize())


def add_recipe():
    recipe_title = title.get()
    ingredients_list = ingredients.get()
    instructions_list = instructions.get()
    cooking_time = cookingTime.get()
    dietary_info = dietaryInfo.get()
    recipe_equipament_list = recipe_equipament.get()
    recipe = Recipe(recipe_title, ingredients_list, instructions_list,
                    cooking_time, dietary_info, recipe_equipament_list)
    recipe_manager.add_recipe(recipe)


def get_all_recipes():
    all_recipes = recipe_manager.get_all_recipes()
    recipe_manager.print_recipes(all_recipes)


#     get recipe functions that are available
#     recipe1 = recipe_manager.get_recipe_by_title(recipe_title)
#     all_recipes_with_ingredients... = recipe_manager.get_recipe_by_ingredients(ingredients)
#     all_recipes_with_instructions... = recipe_manager.get_recipe_by_instructions(instructions)
#     all_recipes_with_cooking_time... = recipe_manager.get_recipe_by_cooking_time(cooking_time)
#     all_recipes_with_dietary_info... = recipe_manager.get_recipe_by_dietary_info(dietary_info)
#     all_recipes_with_recipe_equipament... = recipe_manager.get_recipe_by_equipament(recipe_equipament)


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
#    delete recipe function that is available
recipe_manager.delete_recipe('egg_recipe')


def delete_recipe():
    print("Hello")


# input widget
# Title
tk.Label(frame_right,
         text="Title",  # Text shown on label
         background=bg_colour2,  # Setting label background colour
         foreground="black",  # Setting text colour
         font=("TkMenuFont", 15)  # Setting font type and size
         ).pack()  # Pack method to organise
# Entry widget for title input
title = tk.Entry(frame_right,
                 width=50,
                 background="white",  # Setting label background colour
                 foreground="black",  # Setting text colour
                 font=("TkMenuFont", 15)  # Setting font type and size
                 )
title.pack()  # Pack method to organise

# Ingredients
tk.Label(frame_right,
         width=50,  # Setting label width
         height=1,
         text="Ingredients",  # Text shown on label
         background=bg_colour2,  # Setting label background colour
         foreground="black",  # Setting text colour
         font=("TkMenuFont", 15)  # Setting font type and size
         ).pack()  # Pack method to organise
# Entry widget for ingredients input
ingredients = tk.Entry(frame_right,
                       width=50,
                       background="white",  # Setting label background colour
                       foreground="black",  # Setting text colour
                       font=("TkMenuFont", 15)  # Setting font type and size
                       )
ingredients.pack()  # Pack method to organise

# add ingredients button
add_ingredients_button = tk.Button(
    frame_right,
    width=15,
    height=1,
    text="Add ingredients",  # Text shown on button
    font=("TkMenuFont", 15),  # Setting font type and size
    background="pink",  # Setting button background colour
    foreground="black",  # Setting text colour
    cursor="hand2",  # Change the cursor to the hand
    activebackground="#badee2",  # Changes background colour when cursor click
    activeforeground="black",  # Changes font colour when cursor click
    # Function which runs every time the button is pressed
    command=add_ingredients
)
add_ingredients_button.pack()


# preview ingredients on screen
preview_ingredients = tk.Label(frame_right,
                               width=50,
                               height=1,
                               text="",  # Text shown on label
                               background=bg_colour2,  # Setting label background colour
                               foreground="black",  # Setting text colour
                               # Setting font type and size
                               font=("TkMenuFont", 15)
                               )
preview_ingredients.pack()  # Pack method to organise

# Instructions
tk.Label(frame_right,
         width=50,  # Setting label width
         height=1,
         text="Instructions",  # Text shown on label
         background=bg_colour2,  # Setting label background colour
         foreground="black",  # Setting text colour
         font=("TkMenuFont", 15)  # Setting font type and size
         ).pack()  # Pack method to organise
# Entry widget for instructions input
instructions = tk.Entry(frame_right,
                        width=50,
                        background="white",  # Setting label background colour
                        foreground="black",  # Setting text colour
                        font=("TkMenuFont", 15)  # Setting font type and size
                        )
instructions.pack()  # Pack method to organise

# Cooking time
tk.Label(frame_right,
         width=50,  # Setting label width
         height=1,
         text="Cooking time",  # Text shown on label
         background=bg_colour2,  # Setting label background colour
         foreground="black",  # Setting text colour
         font=("TkMenuFont", 15)  # Setting font type and size
         ).pack()  # Pack method to organise
# Entry widget for cooking time input
cookingTime = tk.Entry(frame_right,
                       width=50,
                       background="white",  # Setting label background colour
                       foreground="black",  # Setting text colour
                       font=("TkMenuFont", 15)  # Setting font type and size
                       )
cookingTime.pack()  # Pack method to organise

# Dietary info
tk.Label(frame_right,
         width=50,  # Setting label width
         height=1,
         text="Dietary info",  # Text shown on label
         background=bg_colour2,  # Setting label background colour
         foreground="black",  # Setting text colour
         font=("TkMenuFont", 15)  # Setting font type and size
         ).pack()  # Pack method to organise
# Entry widget for dietary info input
dietaryInfo = tk.Entry(frame_right,
                       width=50,
                       background="white",  # Setting label background colour
                       foreground="black",  # Setting text colour
                       font=("TkMenuFont", 15)  # Setting font type and size
                       )
dietaryInfo.pack()  # Pack method to organise

# Recipe equipament
tk.Label(frame_right,
         width=50,  # Setting label width
         height=1,
         text="Recipe equipament",  # Text shown on label
         background=bg_colour2,  # Setting label background colour
         foreground="black",  # Setting text colour
         font=("TkMenuFont", 15)  # Setting font type and size
         ).pack()  # Pack method to organise
# Entry widget for recipe equipament input
recipe_equipament = tk.Entry(frame_right,
                             width=50,
                             background="white",  # Setting label background colour
                             foreground="black",  # Setting text colour
                             # Setting font type and size
                             font=("TkMenuFont", 15)
                             )
recipe_equipament.pack()  # Pack method to organise


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
    command=add_recipe
)
add_button.pack()

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
    command=get_all_recipes
)
get_all_button.pack()

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
    # command=recipe_manager.delete_recipe('egg_recipe')
).pack()

# run
window.mainloop()  # displays app until the user closes it
