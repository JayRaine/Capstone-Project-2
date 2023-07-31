# Import necessary modules
from recipe_manager import *
from tkinter.filedialog import askopenfilename
import tkinter as tk
from tkinter import *

# This is the main class for the recipe management system
class RecipeManagementApp:
    def __init__(self, manager):
        # Initialize the RecipeManagementApp
        self.manager = manager
        self.selected_index = None
        self.window = tk.Tk()
        self.window.title("Recipe Manager")
        self.window.geometry('1100x750')
        self.window.resizable(width=False, height=False) # user can't resize the window

        # Dividing window into two frames
        # Left frame
        self.frm_left = tk.Frame(self.window, width=400, height=300, relief=FLAT)
        self.frm_left.grid(row=0, column=0, sticky="NSEW")

        # Right frame
        self.frm_right = tk.Frame(self.window, width=600, height=400, relief=FLAT)
        self.frm_right.grid(row=0, column=1, sticky="N")

        # Page title
        self.lbl_header = tk.Label(self.frm_left, text="Recipe Manager", fg="black", font=("TkMenuFont", 20))
        self.lbl_header.grid(row=0, column=0, sticky="W", pady=15, padx=15)

        # Button to add a new recipe
        self.btn_add = tk.Button(self.frm_left, width=15, height=1, relief=tk.RAISED, text="Clear entry boxes", font=("TkMenuFont", 15), cursor="hand2", command=self.clear_entry_boxes)
        self.btn_add.grid(row=1, column=0, sticky="W", pady=20, padx=100)

        # List box that displays the recipes
        self.recipes_listbox = tk.Listbox(self.frm_left, width=59, height=35)
        self.recipes_listbox.grid(row=2, column=0, sticky="W", pady=5, padx=10)
        self.recipes_listbox.bind('<<ListboxSelect>>', self.selected_recipe)

        # Scrollbar for the recipes_listbox
        self.recipes_scrollbar = tk.Scrollbar(self.frm_left, orient="vertical", command=self.recipes_listbox.yview)
        self.recipes_scrollbar.grid(row=2, column=0, sticky="E")
        self.recipes_listbox.config(yscrollcommand=self.recipes_scrollbar.set)

        # Title text box
        self.lbl_recipe_title = tk.Label(self.frm_right, text="Title", font=("TkMenuFont", 15))
        self.txt_recipe_title = tk.Entry(self.frm_right, width=25, bg="white", fg="black")
        self.txt_recipe_title.grid(row=1, column=2, pady=10, sticky="N")
        self.lbl_recipe_title.grid(row=1, column=1, pady=10, sticky="N")

        # Cooking time text box
        self.lbl_cooking_time = tk.Label(self.frm_right, text="Cooking time", font=("TkMenuFont", 15))
        self.txt_cooking_time = tk.Entry(self.frm_right, width=25, bg="white", fg="black")
        self.txt_cooking_time.grid(row=2, column=2, pady=10, sticky="N")
        self.lbl_cooking_time.grid(row=2, column=1, pady=10, sticky="N")

        # Dietary text box
        self.lbl_dietary = tk.Label(self.frm_right, text="Dietary", font=("TkMenuFont", 15))
        self.txt_dietary = tk.Entry(self.frm_right, width=25, bg="white", fg="black")
        self.txt_dietary.grid(row=3, column=2, pady=10, sticky="N")
        self.lbl_dietary.grid(row=3, column=1, pady=10, sticky="N")

        # Equipment text box
        self.lbl_equipment = tk.Label(self.frm_right, text="Equipment", font=("TkMenuFont", 15))
        self.txt_equipment = tk.Entry(self.frm_right, width=25, bg="white", fg="black")
        self.txt_equipment.grid(row=4, column=2, pady=10, sticky="N")
        self.lbl_equipment.grid(row=4, column=1, pady=10, sticky="N")

        # Ingredients text box
        self.lbl_ingredients = tk.Label(self.frm_right, text="Ingredients", font=("TkMenuFont", 15))
        self.txt_ingredients = tk.Text(self.frm_right, width=40, height=15, bg="white", fg="black")
        self.txt_ingredients.grid(row=7, column=2, sticky="S")
        self.lbl_ingredients.grid(row=6, column=2, sticky="S")

        # Instructions text box
        self.lbl_instructions = tk.Label(self.frm_right, text="Instructions", font=("TkMenuFont", 15))
        self.txt_instructions = tk.Text(self.frm_right, width=40, height=15, bg="white", fg="black")
        self.txt_instructions.grid(row=9, column=2, sticky="S")
        self.lbl_instructions.grid(row=8, column=2, sticky="S")

        # Button to save new recipe
        self.btn_save_recipe = tk.Button(self.frm_right, relief=tk.RAISED, width=15, height=1, text="Save new recipe", font=("TkMenuFont", 15), cursor="hand2", command=self.add_recipe)
        self.btn_save_recipe.grid(row=2, column=3, padx=70, sticky="S")

        # Button to edit the selected recipe
        self.btn_update = tk.Button(self.frm_right, width=15, height=1,relief=tk.RAISED, text="Update this recipe", font=("TkMenuFont", 15), cursor="hand2", command=self.update_recipe)
        self.btn_update.grid(row=3, column=3, padx=70, sticky="S")

        # Button to delete a recipe
        self.btn_delete = tk.Button(self.frm_right, width=15, height=1, relief=tk.RAISED, text="Delete this recipe", font=("TkMenuFont", 15), cursor="hand2", command=self.delete_recipe)
        self.btn_delete.grid(row=4, column=3, padx=70, sticky="S")

        # Button to import a recipe
        self.btn_delete = tk.Button(self.frm_right, width=15, height=1, relief=tk.RAISED, text="Import recipe", font=("TkMenuFont", 15), cursor="hand2", command=self.load_recipe)
        self.btn_delete.grid(row=5, column=3, padx=70, sticky="S")

        # Refreshing the listbox and importing recipes from text files
        self.load_from_folder()


    def clear_entry_boxes(self):
        # Clear the entry boxes
        self.txt_recipe_title.delete(0, tk.END)
        self.txt_cooking_time.delete(0, tk.END)
        self.txt_dietary.delete(0, tk.END)
        self.txt_equipment.delete(0, tk.END)
        self.txt_ingredients.delete('1.0', tk.END)
        self.txt_instructions.delete('1.0', tk.END)

    # Function to display the selected recipe
    def selected_recipe(self, event):
        # Get the index of the selected recipe in the listbox
        selected_index = self.recipes_listbox.curselection()
        if selected_index:
            self.selected_index = selected_index[0]
            # Update the displayed recipe details in the right frame
            self.update_displayed_recipe()

    def update_displayed_recipe(self):
        # Check if a recipe is selected
        if self.selected_index is not None:
            # Get the selected recipe from the manager
            recipe = self.manager.get_recipe(self.selected_index)
            if recipe:
                # Clear existing entry boxes
                self.clear_entry_boxes()
                # Set other entry boxes with recipe details
                self.txt_recipe_title.insert(tk.END, recipe.get_title())
                self.txt_cooking_time.insert(tk.END, recipe.get_cooking_time())
                self.txt_dietary.insert(tk.END, recipe.get_dietary_info())
                self.txt_equipment.insert(tk.END, ', '.join(recipe.get_equipment()))
                self.txt_ingredients.insert(tk.END, '\n'.join(recipe.get_ingredients()))
                self.txt_instructions.insert(tk.END, '\n'.join(recipe.get_instructions()))

    # Function to delete the selected recipe
    def delete_recipe(self):
        if self.selected_index is not None:
            # Delete the recipe from the manager based on the selected index
            self.manager.delete_recipe_index(self.selected_index)
            # Refresh the recipe list in the listbox
            self.refresh_recipe_list()
            # Clear the entry boxes and reset selected_index
            self.clear_entry_boxes()
            self.selected_index = None

    # Refreshes the recipe list in the listbox
    def refresh_recipe_list(self):
        # Clear existing recipes from the listbox
        self.recipes_listbox.delete(0, tk.END)
        # Get all recipes from the manager and add them to the listbox
        recipes = self.manager.get_all_recipes()
        for recipe in recipes:
            self.recipes_listbox.insert(tk.END, recipe.get_title())
            
    # Function to add a new recipe based on the data entered in the entry boxes
    def add_recipe(self):
        title = self.txt_recipe_title.get()
        ingredients = self.txt_ingredients.get("1.0", tk.END)
        instructions = self.txt_instructions.get("1.0", tk.END)
        cooking_time = self.txt_cooking_time.get()
        dietary_info = self.txt_dietary.get()
        equipment = self.txt_equipment.get()
        # Create a new Recipe instance and add it to the manager
        recipe = Recipe(title, [ingredient.strip() for ingredient in ingredients.split("\n")],
                        [instruction.strip() for instruction in instructions.split("\n")],
                        cooking_time, dietary_info, [equip.strip() for equip in equipment.split(",")])
        self.manager.add_recipe(recipe)
        # Refresh the recipe list in the listbox
        self.refresh_recipe_list()
        # Clear the entry boxes and reset selected_index
        self.clear_entry_boxes()
        self.selected_index = None
    
    # Function to update the selected recipe with the data entered in the entry boxes
    def update_recipe(self):
        if self.selected_index is not None:
            title = self.txt_recipe_title.get()
            ingredients = self.txt_ingredients.get("1.0", tk.END)
            instructions = self.txt_instructions.get("1.0", tk.END)
            cooking_time = self.txt_cooking_time.get()
            dietary_info = self.txt_dietary.get()
            equipment = self.txt_equipment.get()
            # Create an updated Recipe instance with the new data
            updated_recipe = Recipe(title, [ingredient.strip() for ingredient in ingredients.split("\n")],
                                    [instruction.strip() for instruction in instructions.split("\n")],
                                    cooking_time, dietary_info, [equip.strip() for equip in equipment.split(",")])
            # Update the recipe in the manager
            self.manager.update_recipe_ui(self.selected_index, updated_recipe)
            # Refresh the recipe list in the listbox
            self.refresh_recipe_list()

    # Function to load a recipe from a file
    def load_recipe(self):
        # Ask the user to select a file and get the filename
        filename = tk.filedialog.askopenfilename()
        # Load the recipe from the selected file and add it to the manager
        self.manager.load_recipe_from_file_selected(filename)
        # Refresh the recipe list in the listbox
        self.refresh_recipe_list()

    def load_from_folder(self):
        self.manager.load_recipes_from_folder()
        self.refresh_recipe_list()


# Create a RecipeManager instance and pass it to the app
recipe_manager = RecipeManager()  # You should initialize this with your specific implementation
app = RecipeManagementApp(recipe_manager)

# Run the event loop, display the app until the user closes it
app.window.mainloop()
