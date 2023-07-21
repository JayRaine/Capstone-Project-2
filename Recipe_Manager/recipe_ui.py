from recipe import Recipe  # Import the Recipe class from recipe.py
from recipe_manager import RecipeManager # Import the RecipeManager class from recipe_manager.py
from recipes import recipes  # Import the 'recipes' dictionary from recipes.py
import tkinter as tk


#initiallize
window = tk.Tk()
window.title("Recipe Management System")
window.geometry('1000x725')
window.eval("tk::PlaceWindow . center") # Window will open on centre of the screeen
bg_colour = "#59656F" # Setting a variable to colour
bg_colour2="#cdd1cd"

# Dividing the window in 2 parts 

frame_left = tk.Frame(window, 
                  width=300, 
                  height=7250, 
                  background=bg_colour,
                  relief="flat")
frame_left.grid(row=0, column=0)
frame_left.pack_propagate(False) #background colour to all page

frame_right = tk.Frame(window, 
                  width=700, 
                  height=725, 
                  background=bg_colour2,
                  relief="flat")
frame_right.grid(row=0, column=1)
frame_right.pack_propagate(False) #background colour to all page

#frame_right widgets
# logo_img = ImageTk.PhotoImage(Image.open('logo.png').convert('RGB'))
# logo_widget = tk.Label(frame_right, image = logo_img) # converting to widget, tkinter doesn't have an specific
# logo_widget.image = logo_img
# logo_widget.pack() #place widget in frame

#Instructions widget
tk.Label(frame_left,
         text="Recipe Management System",
         background=bg_colour, # Setting label background colour
         foreground="white", # Setting text colour 
         font=("TkMenuFont", 20) # Setting font type and size
         ).pack() # Pack method to organise

# Initialize recipe manager
recipe_manager = RecipeManager()
#****** In progress*******
def add_recipe():
 print("Hello")
#     recipe_title = recipe_title.get()
#     ingredients = recipe_ingredients.get().split(',')
#     instructions = recipe_instructions.get("1.0", tk.END).split('\n')
#     cooking_time = recipe_cooking_time.get()
#     dietary_info = recipe_dietary_info.get()
#     recipe_equipament = recipe_equipament.get()

#     recipe = Recipe(title, ingredients, instructions, cooking_time, dietary_info)
# recipe_manager.add_recipe(recipe)
def get_all_recipes():
 print("Hello")

def update_recipe():
 print("Hello")

def delete_recipe():
 print("Hello")

# Buttons widget
# Button to add a new recipe
add_button = tk.Button(
    frame_left,
    width=15, 
    height=1,
    text="Add a new recipe", # Text shown on button
    font= ("TkMenuFont", 15), # Setting font type and size
    background= "pink", # Setting button background colour
    foreground="black", # Setting text colour 
    cursor="hand2", # Change the cursor to the hand
    activebackground= "#badee2", # Changes background colour when cursor click
    activeforeground= "black", # Changes font colour when cursor click
    command=add_recipe() # Function which runs every time the button is pressed
).pack()

# Button to view all recipes
get_all_button = tk.Button(
    frame_left,
    width=15, 
    height=1,
    text="View all recipes", # Text shown on button
    font= ("TkMenuFont", 15), # Setting font type and size
    background= "pink", # Setting button background colour
    foreground="black", # Setting text colour 
    cursor="hand2", # Change the cursor to the hand
    activebackground= "#badee2", # Changes background colour when cursor click
    activeforeground= "black", # Changes font colour when cursor click
    command=get_all_recipes() # Function which runs every time the button is pressed
).pack()

#Button to edit a recipe
update_button = tk.Button(
    frame_left,
    width=15, 
    height=1,
    text="Update a recipe", # Text shown on button
    font= ("TkMenuFont", 15), # Setting font type and size
    background= "pink", # Setting button background colour
    foreground="black", # Setting text colour 
    cursor="hand2", # Change the cursor to the hand
    activebackground= "#badee2", # Changes background colour when cursor click
    activeforeground= "black", # Changes font colour when cursor click
    command=update_recipe() # Function which runs every time the button is pressed
).pack()

#Button to delete a recipe
delete_button = tk.Button(
    frame_left,
    width=15, 
    height=1,
    text="Delete a recipe", # Text shown on button
    font= ("TkMenuFont", 15), # Setting font type and size
    background= "pink", # Setting button background colour
    foreground="black", # Setting text colour 
    cursor="hand2", # Change the cursor to the hand
    activebackground= "#badee2", # Changes background colour when cursor click
    activeforeground= "black", # Changes font colour when cursor click
    command=delete_recipe() # Function which runs every time the button is pressed
).pack()

#run
window.mainloop() #displays app until the user closes it

