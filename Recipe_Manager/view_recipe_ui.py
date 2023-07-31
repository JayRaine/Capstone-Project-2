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
    label_font_1 = ("Arial", 14, "bold")

    frame_style = ttk.Style()
    frame_style.configure("Custom.TLabelframe", background="#e6f1ff",
                          borderwidth=0, foreground="red", )

    header_style = ttk.Style()
    header_style.configure("Custom.TLabelheader",
                           borderwidth=0, font=label_font_1, foreground="blue", )

    label_style = ttk.Style()
    label_style.configure("Custom.TLabel2",
                          borderwidth=0, font=label_font, foreground="black", )

    details_maping = {}
    for key, value in recipe_manager.get_recipe(recipe).items():
        match key:
            case "title":
                details_maping["Recipe Title"] = value.capitalize()
            case "ingredient_list":
                details_maping["Ingredients"] = convert_to_string(
                    value).capitalize()
            case "instruction_list":
                details_maping["Instructions"] = convert_to_string(
                    value).capitalize()
            case "cooking_time":
                details_maping["Cooking Time"] = f"This recipe takes {str(value)} minutes to cook"
            case "dietary_info":
                details_maping["Dietary Information"] = convert_to_string(
                    value).capitalize()
            case "equipment":
                details_maping[
                    "Equipment_list"] = f"Equipment needed {convert_to_string(value).capitalize()}"
            case _:
                raise ValueError("Invalid detail type entered")

    for key, value in details_maping.items():
        label_frame = ttk.LabelFrame(
            frame, style="Custom.TLabelframe")
        label_frame.pack(anchor="center",
                         fill="x", expand=True,)
        header = ttk.Label(
            label_frame, text=key, borderwidth=0, font=label_font_1, foreground="blue")
        header.pack(anchor="center", pady=10, padx=20)
        preview_text = value
        label = ttk.Label(
            label_frame, text=preview_text, borderwidth=0, font=label_font, foreground="black")
        label.pack(anchor="center", pady=10, padx=20)

        # label_frame = ttk.LabelFrame(
        #     frame, text=key.capitalize(), style="Custom.TLabelframe")
        # label_frame.pack(anchor="center", pady=10, padx=20,
        #                  fill="x", expand=True,)
        # label = ttk.Label(
        #     label_frame, text=preview_text, font=label_font, style="Custom.TLabel")
        # label.pack(anchor="center", pady=10, padx=20)
