import tkinter as tk
from tkinter import ttk
from recipe_manager import RecipeManager


def convert_to_string(value):
    if type(value) == list:
        return '\n'.join(value)
    else:
        return value


def create_recipe_preview(parent, recipe):
    recipe_manager = RecipeManager()

    frame = ttk.LabelFrame(parent, borderwidth=0)
    frame.pack(anchor="center", pady=10, padx=20, fill="x")

    label_font = ("Arial", 12)
    label_frame_font = ("Arial", 14, "bold")

    frame_style = ttk.Style()
    frame_style.configure("Custom.TLabelframe", background="#e6f1ff",
                          borderwidth=0, font=label_frame_font, foreground="red", )
    label_style = ttk.Style()
    label_style.configure("Custom.TLabel",
                          borderwidth=0, font=label_font, foreground="blue", )

    for key, value in recipe_manager.get_recipe(recipe).items():
        match key:
            case "title":
                preview_text = f"Recipe Title: \n{convert_to_string(value).capitalize()}"
            case "ingredients":
                preview_text = f"Ingredients:\n{convert_to_string(value).capitalize()}"
            case "instructions":
                preview_text = f"Instructions:\n{convert_to_string(value).capitalize()}"
            case "cooking_time":
                preview_text = f"This recipe takes {str(value)} minutes to cook"
            case "dietary_info":
                preview_text = f"Dietary information:\n{convert_to_string(value).capitalize()}"
            case "equipment":
                preview_text = f"Equipment needed:\n{convert_to_string(value).capitalize()}"
            case _:
                raise ValueError("Invalid detail type entered")

        label_frame = ttk.LabelFrame(
            frame, text=key.capitalize(), style="Custom.TLabelframe")
        label_frame.pack(anchor="center", pady=10, padx=20,
                         fill="x", expand=True,)
        label = ttk.Label(
            label_frame, text=preview_text, font=label_font, style="Custom.TLabel")
        label.pack(anchor="center", pady=10, padx=20)
