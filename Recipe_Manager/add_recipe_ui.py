import tkinter as tk
import os
from recipe import Recipe
from recipe_manager import RecipeManager


def create_add_recipe_preview(parent):

    recipe_manager = RecipeManager()
    # ****** In progress*********#

    # Create a list to store ingredients
    ingredientsList = []
    # Create a list to store instructions
    instructionsList = []
    # Create a list to store dietary information
    dietaryInfoList = []
    # Create a list to store equipment
    equipmentList = []

    # functions to add attribute [ingredient, instruction etc] and update the preview

    def add_ingredients():
        ingredientsList.append(ingredients.get())
        ingredients.delete(0, "end")  # Clear the input field
        # Call the update_preview() function to update the preview
        update_ingrediants_preview()

    def add_instructions():
        instructionsList.append(instructions.get())
        instructions.delete(0, "end")  # Clear the input field
        # Call the update_preview() function to update the preview
        update_instructions_preview()

    def add_dietary_info():
        dietaryInfoList.append(dietaryInfo.get())
        dietaryInfo.delete(0, "end")  # Clear the input field
        # Call the update_preview() function to update the preview
        update_dietary_info_preview()

    def add_equipment():
        equipmentList.append(recipe_equipament.get())
        recipe_equipament.delete(0, "end")  # Clear the input field
        # Call the update_preview() function to update the preview
        update_equipment_preview()

    # functions to update the preview after adding ingredients or instructions etc

    def update_ingrediants_preview():
        # Update the text attribute of the label with the current list of ingredients
        preview_ingredients.config(
            text="Ingredients: " + ', '.join(ingredientsList).capitalize())

    def update_instructions_preview():
        # Update the text attribute of the label with the current list of instructions
        preview_instructions.config(
            text="Instructions: " + ', '.join(instructionsList).capitalize())

    def update_dietary_info_preview():
        # Update the text attribute of the label with the current list of dietary information
        preview_dietary_info.config(
            text="Dietary Information: " + ', '.join(dietaryInfoList).capitalize())

    def update_equipment_preview():
        # Update the text attribute of the label with the current list of equipment
        preview_equipment.config(
            text="Equipment: " + ', '.join(equipmentList).capitalize())

    def add_recipe():  # function to add recipe to the recipe manager
        title = recipe_title.get()
        ingredients_list = ingredientsList.copy()
        instructions_list = instructions.get("1.0", "end-1c")
        cooking_time = cookingTime.get()
        dietary_info = dietaryInfoList.copy()
        recipe_equipament_list = equipmentList.copy()

        # Create a recipe object
        recipe = Recipe(title, ingredients_list, instructions_list,
                        cooking_time, dietary_info, recipe_equipament_list)
        # Add the recipe to the recipe manager
        recipe_manager.add_recipe(recipe)

        # Clear the input fields
        recipe_title.delete(0, "end")
        ingredients.delete(0, "end")
        instructions.delete("1.0", "end")
        cookingTime.delete(0, "end")
        dietaryInfo.delete(0, "end")
        recipe_equipament.delete(0, "end")
        # Clear the preview
        preview_ingredients.config(text="Ingredients: ")
        preview_instructions.config(text="Instructions: ")
        preview_dietary_info.config(text="Dietary Information: ")
        preview_equipment.config(text="Equipment: ")
        # clear the lists
        ingredientsList.clear()
        instructionsList.clear()
        dietaryInfoList.clear()
        equipmentList.clear()

    # input widget

    # Title
    tk.Label(parent,
             text="Title",  # Text shown on label
             background="#cdd1cd",  # Setting label background colour
             foreground="black",  # Setting text colour
             font=("TkMenuFont", 15)  # Setting font type and size
             ).pack()  # Pack method to organise
    # Entry widget for title input
    recipe_title = tk.Entry(parent,
                            width=50,
                            background="white",  # Setting label background colour
                            foreground="black",  # Setting text colour
                            # Setting font type and size
                            font=("TkMenuFont", 15)
                            )
    recipe_title.pack()  # Pack method to organise

    # Ingredients
    tk.Label(parent,
             width=50,  # Setting label width
             height=1,
             text="Ingredients",  # Text shown on label
             background="#cdd1cd",  # Setting label background colour
             foreground="black",  # Setting text colour
             font=("TkMenuFont", 15)  # Setting font type and size
             ).pack()  # Pack method to organise
    # Entry widget for ingredients input
    ingredients = tk.Entry(parent,
                           width=50,
                           background="white",  # Setting label background colour
                           foreground="black",  # Setting text colour
                           # Setting font type and size
                           font=("TkMenuFont", 15)
                           )
    ingredients.pack()  # Pack method to organise

    # add ingredients button
    add_ingredients_button = tk.Button(
        parent,
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
    preview_ingredients = tk.Label(parent,
                                   width=50,
                                   height=1,
                                   text="",  # Text shown on label
                                   background="#cdd1cd",  # Setting label background colour
                                   foreground="black",  # Setting text colour
                                   # Setting font type and size
                                   font=("TkMenuFont", 15)
                                   )
    preview_ingredients.pack()  # Pack method to organise

    # Instructions
    tk.Label(parent,
             width=50,  # Setting label width
             height=1,
             text="Instructions",  # Text shown on label
             background="#cdd1cd",  # Setting label background colour
             foreground="black",  # Setting text colour
             font=("TkMenuFont", 15)  # Setting font type and size
             ).pack()  # Pack method to organise
    # Entry widget for instructions input
    instructions = tk.Text(parent,
                           width=50,
                           height=4,
                           background="white",  # Setting label background colour
                           foreground="black",  # Setting text colour
                           # Setting font type and size
                           font=("TkMenuFont", 15)
                           )
    instructions.pack()  # Pack method to organise

    # add instructions button
    # add_instructions_button = tk.Button(
    #     parent,
    #     width=15,
    #     height=1,
    #     text="Add instructions",  # Text shown on button
    #     font=("TkMenuFont", 15),  # Setting font type and size
    #     background="pink",  # Setting button background colour
    #     foreground="black",  # Setting text colour
    #     cursor="hand2",  # Change the cursor to the hand
    #     activebackground="#badee2",  # Changes background colour when cursor click
    #     activeforeground="black",  # Changes font colour when cursor click
    #     # Function which runs every time the button is pressed
    #     command=add_instructions
    # )
    # add_instructions_button.pack()

    # preview instructions on screen
    preview_instructions = tk.Label(parent,
                                    width=50,
                                    height=1,
                                    text="",  # Text shown on label
                                    background="#cdd1cd",  # Setting label background colour
                                    foreground="black",  # Setting text colour
                                    # Setting font type and size
                                    font=("TkMenuFont", 15)
                                    )
    preview_instructions.pack()  # Pack method to organise

    # Cooking time
    tk.Label(parent,
             width=50,  # Setting label width
             height=1,
             text="Cooking time",  # Text shown on label
             background="#cdd1cd",  # Setting label background colour
             foreground="black",  # Setting text colour
             font=("TkMenuFont", 15)  # Setting font type and size
             ).pack()  # Pack method to organise
    # Entry widget for cooking time input
    cookingTime = tk.Entry(parent,
                           width=50,
                           background="white",  # Setting label background colour
                           foreground="black",  # Setting text colour
                           # Setting font type and size
                           font=("TkMenuFont", 15)
                           )
    cookingTime.pack()  # Pack method to organise

    # Dietary info
    tk.Label(parent,
             width=50,  # Setting label width
             height=1,
             text="Dietary info",  # Text shown on label
             background="#cdd1cd",  # Setting label background colour
             foreground="black",  # Setting text colour
             font=("TkMenuFont", 15)  # Setting font type and size
             ).pack()  # Pack method to organise
    # Entry widget for dietary info input
    dietaryInfo = tk.Entry(parent,
                           width=50,
                           background="white",  # Setting label background colour
                           foreground="black",  # Setting text colour
                           # Setting font type and size
                           font=("TkMenuFont", 15)
                           )
    dietaryInfo.pack()  # Pack method to organise

    # add dietary info button
    add_dietary_info_button = tk.Button(
        parent,
        width=15,
        height=1,
        text="Add dietary info",  # Text shown on button
        font=("TkMenuFont", 15),  # Setting font type and size
        background="pink",  # Setting button background colour
        foreground="black",  # Setting text colour
        cursor="hand2",  # Change the cursor to the hand
        activebackground="#badee2",  # Changes background colour when cursor click
        activeforeground="black",  # Changes font colour when cursor click
        # Function which runs every time the button is pressed
        command=add_dietary_info
    )
    add_dietary_info_button.pack()

    # preview dietary info on screen
    preview_dietary_info = tk.Label(parent,
                                    width=50,
                                    height=1,
                                    text="",  # Text shown on label
                                    background="#cdd1cd",  # Setting label background colour
                                    foreground="black",  # Setting text colour
                                    # Setting font type and size
                                    font=("TkMenuFont", 15)
                                    )
    preview_dietary_info.pack()  # Pack method to organise

    # Recipe equipament
    tk.Label(parent,
             width=50,  # Setting label width
             height=1,
             text="Recipe equipament",  # Text shown on label
             background="#cdd1cd",  # Setting label background colour
             foreground="black",  # Setting text colour
             font=("TkMenuFont", 15)  # Setting font type and size
             ).pack()  # Pack method to organise
    # Entry widget for recipe equipament input
    recipe_equipament = tk.Entry(parent,
                                 width=50,
                                 background="white",  # Setting label background colour
                                 foreground="black",  # Setting text colour
                                 # Setting font type and size
                                 font=("TkMenuFont", 15)
                                 )
    recipe_equipament.pack()  # Pack method to organise

    # add recipe equipament button
    add_recipe_equipament_button = tk.Button(
        parent,
        width=15,
        height=1,
        text="Add equipament",  # Text shown on button
        font=("TkMenuFont", 15),  # Setting font type and size
        background="pink",  # Setting button background colour
        foreground="black",  # Setting text colour
        cursor="hand2",  # Change the cursor to the hand
        activebackground="#badee2",  # Changes background colour when cursor click
        activeforeground="black",  # Changes font colour when cursor click
        # Function which runs every time the button is pressed
        command=add_equipment
    )
    add_recipe_equipament_button.pack()

    # preview recipe equipament on screen
    preview_equipment = tk.Label(parent,
                                 width=50,
                                 height=1,
                                 text="",  # Text shown on label
                                 background="#cdd1cd",  # Setting label background colour
                                 foreground="black",  # Setting text colour
                                 # Setting font type and size
                                 font=("TkMenuFont", 15)
                                 )
    preview_equipment.pack()  # Pack method to organise

    # add recipe button
    add_recipe_button = tk.Button(
        parent,
        width=15,
        height=1,
        text="Add recipe",  # Text shown on button
        font=("TkMenuFont", 15),  # Setting font type and size
        background="pink",  # Setting button background colour
        foreground="black",  # Setting text colour
        cursor="hand2",  # Change the cursor to the hand
        activebackground="#badee2",  # Changes background colour when cursor click
        activeforeground="black",  # Changes font colour when cursor click
        # Function which runs every time the button is pressed
        command=add_recipe
    )
    add_recipe_button.pack()

    # preview recipe on screen
    preview_recipe = tk.Label(parent,
                              width=50,
                              height=1,
                              text="",  # Text shown on label
                              background="#cdd1cd",  # Setting label background colour
                              foreground="black",  # Setting text colour
                              # Setting font type and size
                              font=("TkMenuFont", 15)
                              )
    preview_recipe.pack()  # Pack method to organise
