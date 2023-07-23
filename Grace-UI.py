import tkinter as tk

self.window = tk.Tk{}

self.window.geometry{""}
self.window.configure(bg="#7A316F")
self.window.title(Recipe_manager)

self.search_label = tk.Label(self.window, text="Search Recipe", bg="#CD6688")
self.search_label.grid(column=0, row=0, padx=5)

self.search_entry = tk.Entry(master=self.window, width=40)
self.search_entry.grid(column=1, row=0, padx=10, pady=20)

self.search_button = tk.Button(self.window, text="search", highlightbackground="",
                               command=self._run_search_query)
self.search_button.grid(column=2, row=0, padx=10)


# recipe getting fron tk
def __get_ingredients(self, recipe):
    ingredients = tk.Text(master=self.window, height=20,
                          width=20, bg="#AED8CC")
    ingredients.grid(column=1, row=6, pady=10)
    ingredients.delete("1.0", tk.END)

    if recipe == None:
        ingredients.insert(tk.END, "Error!, Recipe not found")
        return

    ingredients.insert(tk.END, "\n" + recipe.label + "n")
    for ingredient in recipe_ingredient_names:
        ingredients.insert(tk.END, "\n" + ingredient)


img = Image.open
img = img.resize(RECIPE_IMAGE_WIDTH, RECIPE_IMAGE_HEIGHT)
Image = ImageTk.PhotoImage(img)


self.recipe_link_button = tk.button(self.window, text="link to Recipe", highlightbackground="#461959",
                                    command=self: __open_recipe_link)

self.recipe_link_button.grid(column=1, row 7, padx=5)
