from __future__ import annotations
from typing import Iterable
import gradio as gr
from gradio.themes.base import Base
from gradio.themes.utils import colors, fonts, sizes

# Define Seafoam theme
class Seafoam(Base):
    def __init__(
        self,
        *,
        primary_hue: colors.Color | str = colors.emerald,
        secondary_hue: colors.Color | str = colors.blue,
        neutral_hue: colors.Color | str = colors.blue,
        spacing_size: sizes.Size | str = sizes.spacing_md,
        radius_size: sizes.Size | str = sizes.radius_md,
        text_size: sizes.Size | str = sizes.text_lg,
        font: fonts.Font | str | Iterable[fonts.Font | str] = (
            fonts.GoogleFont("Quicksand"),
            "ui-sans-serif",
            "sans-serif",
        ),
        font_mono: fonts.Font | str | Iterable[fonts.Font | str] = (
            fonts.GoogleFont("IBM Plex Mono"),
            "ui-monospace",
            "monospace",
        ),
    ):
        super().__init__(
            primary_hue=primary_hue,
            secondary_hue=secondary_hue,
            neutral_hue=neutral_hue,
            spacing_size=spacing_size,
            radius_size=radius_size,
            text_size=text_size,
            font=font,
            font_mono=font_mono,
        )
        super().set(
            body_background_fill="repeating-linear-gradient(45deg, *primary_200, *primary_200 10px, *primary_50 10px, *primary_50 20px)",
            body_background_fill_dark="repeating-linear-gradient(45deg, *primary_800, *primary_800 10px, *primary_900 10px, *primary_900 20px)",
            button_primary_background_fill="linear-gradient(90deg, *primary_300, *secondary_400)",
            button_primary_background_fill_hover="linear-gradient(90deg, *primary_200, *secondary_300)",
            button_primary_text_color="white",
            button_primary_background_fill_dark="linear-gradient(90deg, *primary_600, *secondary_800)",
            slider_color="*secondary_300",
            slider_color_dark="*secondary_600",
            block_title_text_weight="600",
            block_border_width="3px",
            block_shadow="*shadow_drop_lg",
            button_shadow="*shadow_drop_lg",
            button_large_padding="32px",
        )

# Create Seafoam theme instance
seafoam = Seafoam()

# Sorting algorithms
def selection_sort(arr):
    """Sort the array using selection sort algorithm."""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def insertion_sort(arr):
    """Sort the array using insertion sort algorithm."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge_sort(arr):
    """Sort the array using merge sort algorithm."""
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

def sort_array(arr, algorithm):
    """Sort the array based on the selected algorithm."""
    arr = list(map(int, arr.split(',')))  # Convert string input to a list of integers
    if algorithm == "Selection Sort":
        sorted_arr = selection_sort(arr.copy())
    elif algorithm == "Insertion Sort":
        sorted_arr = insertion_sort(arr.copy())
    elif algorithm == "Merge Sort":
        sorted_arr = merge_sort(arr.copy())
    else:
        sorted_arr = arr
    return ', '.join(map(str, sorted_arr))

# Create the Gradio interface with Seafoam theme
with gr.Blocks(theme=seafoam) as demo:
    gr.Markdown("# Sorting Algorithm Visualizer")
    
    with gr.Row():
        array_input = gr.Textbox(label="Enter array (comma-separated)", placeholder="e.g., 5, 2, 9, 1, 5, 6")
        algorithm = gr.Dropdown(label="Select Sorting Algorithm", choices=["Selection Sort", "Insertion Sort", "Merge Sort"])
    
    with gr.Row():
        sort_button = gr.Button("Sort Array")
    
    sorted_output = gr.Textbox(label="Sorted Array")
    
    sort_button.click(fn=sort_array, inputs=[array_input, algorithm], outputs=sorted_output)

# Launch the Gradio app
demo.launch()
