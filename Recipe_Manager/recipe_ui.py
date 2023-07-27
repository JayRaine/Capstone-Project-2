from recipe import Recipe  # Import the Recipe class from recipe.py
# Import the RecipeManager class from recipe_manager.py
from recipe_manager import RecipeManager
from recipes import recipes  # Import the 'recipes' dictionary from recipes.py
from tkinter import *
import tkinter as tk # Importing Python GUI Tkinter Module


window = tk.Tk() # Create a window object
window.title("Recipe Management System") # Name shown on our window
window.geometry('1000x700') # Window size
window.resizable(width=False, height=False)
# window.rowconfigure(0, minsize=500, weight=1)
# window.columnconfigure(1, minsize=500, weight=1)
bg_colour = "#949494"  # Gray color
bg_colour2 = "white"

# Initialize recipe manager
recipe_manager = RecipeManager()

# Function to display the selected recipe
def selected_recipe():
    for selected_recipe in recipes_list.curselection():
        recipes_list.bind("Selected", selected_recipe) 
#well we gotta bind the selection to the listbox when you select a recipe haven't we?

###### TEST
def func():
    print("Hello")

# Dividing window in 2 frames
# Left frame
frm_left = tk.Frame(window, width=400, height=300,relief="flat") 
frm_left.grid(row=0, column=0, sticky="NSEW") # Pack the information and shows it on window, and position it

# Right frame
frm_right = tk.Frame(window, width=600, height=400, relief="flat") 
frm_right.grid(row=0, column=1, sticky="N") # Pack the information and shows it on window, and position it

# Page title
lbl_header = tk.Label(frm_left, text="Recipe Management System",fg="black", font=("TkMenuFont", 20))
lbl_header.grid(row=0, column=0, sticky="W", pady=15, padx=15)  # Pack the information and shows it on window, and position it

# Button to add a new recipe
btn_add = tk.Button(frm_left, width=15, height=1, text="Add a new recipe", font=("TkMenuFont", 15), cursor="hand2", relief="flat", command= func()#command=recipe_manager.add_recipe(recipes)
                    )
btn_add.grid(row=1, column=0, sticky="W", pady=20, padx=50)

# List box that you can select the recipe and it will show up on the right side and you can update this recipe or delete
# Creating list of all recipes
recipes_listbox=tk.Listbox(frm_left, width= 30, height=30)
recipes_listbox.grid(row=2, column=0, sticky="W", pady=5, padx=10)

#Scrollbar on recipes_listbox on right side
recipes_scrollbar = tk.Scrollbar(frm_left, orient= "vertical", command=recipes_listbox.yview) 
recipes_scrollbar.grid(row=2, column=0,sticky="E")

recipes_listbox.config(yscrollcommand=recipes_scrollbar.set)

######## NEEDS TO GET THE INFORMATION FROM DICTIONARY

recipes_dic={"a", "b", "c", "d", "a", "b", "c", "d", "a", "b", "c", "d", "a", "b", "c", "d", "a", "b", "c", "d", "a", "b", "c", "d", "a", "b", "c", "d", "a", "b", "c", "d", "a", "b", "c", "d", "a", "b", "c", "d"}

# Adding list of recipes on recipes_list and trying to displaying on recipe_listbox ordened
recipes_list=recipes_dic
for recipe in recipes_list:
    recipes_listbox.insert(END, recipe)
#sorted_recipes=sorted(recipes_list.items(), key=lambda x:x[1], reverse=True)
#for recipe in sorted_recipes:
#    recipes_listbox.insert(END, recipe)

# Title text box
lbl_recipe_title=tk.Label(frm_right,text="Title", font=("TkMenuFont", 15))
txt_recipe_title= tk.Entry(frm_right, width=25, bg=bg_colour2, fg= "black")
txt_recipe_title.grid(row=1, column=2,pady=10, sticky="N")
lbl_recipe_title.grid(row=1, column=1, pady=10, sticky="N")

# Cooking time text box
lbl_cooking_time=tk.Label(frm_right, text="Cooking time", font=("TkMenuFont", 15))
txt_cooking_time=tk.Entry(frm_right, width=25, bg=bg_colour2, fg= "black" )
txt_cooking_time.grid(row=2, column=2, pady=10, sticky="N")
lbl_cooking_time.grid(row=2, column=1, pady=10, sticky="N")

# Dietary text box
lbl_dietary=tk.Label(frm_right,text="Dietary", font=("TkMenuFont", 15))
txt_dietary=tk.Entry(frm_right, width=25, bg=bg_colour2, fg= "black" )
txt_dietary.grid(row=3, column=2, pady=10, sticky="N")
lbl_dietary.grid(row=3, column=1, pady=10, sticky="N")

# Equipament text box
lbl_equipament=tk.Label(frm_right,text="Equipament", font=("TkMenuFont", 15))
txt_equipament=tk.Entry(frm_right, width=25, bg=bg_colour2, fg= "black" )
txt_equipament.grid(row=4, column=2, pady=10, sticky="N")
lbl_equipament.grid(row=4, column=1, pady=10, sticky="N")

# Ingredients text box
lbl_ingredients=tk.Label(frm_right, text="Ingredients", font=("TkMenuFont", 15))
txt_ingredients=tk.Text(frm_right, width=40, height=15,bg=bg_colour2,fg= "black" )
txt_ingredients.grid(row=7, column=2, sticky="S")
lbl_ingredients.grid(row=6, column=2, sticky="S")

#Instructions text box
lbl_instructions=tk.Label(frm_right, text="Instructions", font=("TkMenuFont", 15))
txt_instructions=tk.Text(frm_right, width=40, height=15, bg=bg_colour2, fg= "black")
txt_instructions.grid(row=9, column=2, sticky="S")
lbl_instructions.grid(row=8, column=2, sticky="S")

# Button to save new recipe
btn_save_recipe = tk.Button(frm_right, width=15, height=1, text="Save new recipe", font=("TkMenuFont", 15), cursor="hand2", relief="flat", command= func() #command=recipe_manager.add_recipe(recipes)
)
btn_save_recipe.grid(row=2, column=3, padx=70, sticky="S")
                            
# Button to edit the selected recipe
btn_update = tk.Button(frm_right, width=15, height=1, text="Update this recipe", font=("TkMenuFont", 15), cursor="hand2", command= func() #command= recipe_manager.update_recipe(new_recipe=Recipe.curselection()) #recipe_manager.update_recipe(recipes)#update_recipe(title, attribute)
)
btn_update.grid(row=3, column=3, padx=70, sticky="S")

# Button to delete a recipe
btn_delete = tk.Button(frm_right, width=15, height=1, text="Delete this recipe", font=("TkMenuFont", 15), cursor="hand2", command= func() #command= recipe_manager.delete_recipe(recipes) #recipe_manager.delete_recipe(recipes) #RecipeManager(delete_recipe)
)
btn_delete.grid(row=4, column=3, padx=70, sticky="S")

# run
window.mainloop()  # Run the event loop, displays app until the user closes it
