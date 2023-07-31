import tkinter as tk
from recipe_manager import RecipeManager
from view_recipe_ui import create_recipe_preview

selected_label = None


def create_view_all_recipes_preview(parent):
    recipe_manager = RecipeManager()
    # recipe_manager.load_recipes_from_file()

    def preview_recipe(parent, recipe):
        global selected_label
        selected_label = None
        for widget in parent.winfo_children():
            widget.destroy()
        create_recipe_preview(parent, recipe)

    def delete_recipe(parent, recipe):
        global selected_label
        selected_label = None
        recipe_manager.delete_recipe(recipe)
        for widget in parent.winfo_children():
            widget.destroy()
        create_view_all_recipes_preview(parent)

    def select_recipe(event):
        # Deselect the previously selected label
        global selected_label
        if selected_label is not None:
            selected_label.config(bg="#eb8806")

        # Set the background color of the newly selected label
        selected_label = event.widget
        selected_label.config(bg="yellow")

        # Store the selected recipe in a variable or perform any desired actions
        selected_recipe = selected_label["text"]
        preview_button.pack()
        delete_button.pack()

    all_recipes = recipe_manager.get_all_recipes()
    if all_recipes:  # If there are no recipes
        for recipe in all_recipes:
            for key, value in recipe_manager.get_recipe(recipe, 'title').items():
                preview_text = f"{key}: {value}"
            label = tk.Label(
                parent,
                text=preview_text,
                width=50,
                height=2,
                bg="#eb8806",
                relief="flat",
                cursor="hand2",
                foreground="blue",
                font=("Arial", 12)
            )
            label.pack(anchor="center", pady=10, padx=20)
            # Bind the select_recipe function to the click event
            label.bind("<Button-1>", lambda event: select_recipe(event))

        preview_button = tk.Button(
            parent,
            width=10,
            height=1,
            text="Preview",
            bg="#eb8806",
            foreground="black",
            font=("Arial", 12),
            command=lambda recipe=recipe: preview_recipe(parent, recipe)
        )

        delete_button = tk.Button(
            parent,
            text="Delete",
            bg="#eb8806",
            foreground="white",
            font=("Arial", 12),
            command=lambda recipe=recipe: delete_recipe(parent, recipe)
        )
    else:
        label = tk.Label(
            parent,
            text="No recipes found",
            width=50,
            height=2,
            bg="#eb8806",
            relief="flat",
            foreground="blue",
            font=("Arial", 12)
        )
        label.pack(anchor="center", pady=10, padx=20)
