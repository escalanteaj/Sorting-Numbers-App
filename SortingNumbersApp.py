import tkinter as tk
from tkinter import ttk
import random
import time
from sorting_algorithms import bubble_sort, insertion_sort, quick_sort, merge_sort, selection_sort, radix_sort

# Global color variables
BACKGROUND_COLOR = "#2b2d42"
LABEL_BACKGROUND_COLOR = "#d90429"
TEXT_COLOR = "#FFFFFF"
BUTTON_COLOR = "#8d99ae"

# Create the main application window
root = tk.Tk()
root.title("Sorting Numbers App")
root.geometry("500x800")
root.configure(bg=BACKGROUND_COLOR)

# Define a global variable to store random numbers
RANDOM_NUMBERS = []

# Function to generate and display random numbers
def generate_random_numbers():
    global RANDOM_NUMBERS
    RANDOM_NUMBERS = [random.randint(1, 777) for _ in range(100)]
    numbers_label.config(text="Random Numbers List:\n" + ", ".join(map(str, RANDOM_NUMBERS)))

# Function to sort and display numbers
def sort_numbers():
    global RANDOM_NUMBERS
    selected_sort = selected_algorithm.get()

    if not RANDOM_NUMBERS:
        generate_random_numbers()
        
    start_time = time.time()

    if selected_sort == "Bubble Sort":
        sorted_numbers = bubble_sort(RANDOM_NUMBERS)
    elif selected_sort == "Insertion Sort":
        sorted_numbers = insertion_sort(RANDOM_NUMBERS)
    elif selected_sort == "Quick Sort":
        sorted_numbers = quick_sort(RANDOM_NUMBERS)
    elif selected_sort == "Merge Sort":
        sorted_numbers = merge_sort(RANDOM_NUMBERS)
    elif selected_sort == "Selection Sort":
        sorted_numbers = selection_sort(RANDOM_NUMBERS)
    elif selected_sort == "Radix Sort":
        sorted_numbers = radix_sort(RANDOM_NUMBERS)
    else:
        sorted_numbers = []
        
    end_time = time.time()
    sorting_duration = end_time - start_time

    # Display sorted numbers with line breaks for better visibility
    result_label.config(text="Sorted Numbers:\n" + ", ".join(map(str, sorted_numbers)))
    
    # Update the sorting time label
    sorting_time_label.config(text=f"Sorting Time: {sorting_duration:.6f} seconds")

# Create labels using the pack manager with padding
app_name_label = tk.Label(root, text="Sorting Numbers App", font=("Helvetica", 16), fg=TEXT_COLOR, bg=LABEL_BACKGROUND_COLOR)
app_name_label.pack(pady=10, fill='x')

generate_button = tk.Button(root, text="Generate Numbers", command=generate_random_numbers, bg=BUTTON_COLOR, fg=TEXT_COLOR, height=2, width=20)
generate_button.pack(pady=10)

numbers_label = tk.Label(root, text="Random Numbers List:", font=("Helvetica", 12), fg=TEXT_COLOR, bg=LABEL_BACKGROUND_COLOR, wraplength=400, justify="left")
numbers_label.pack(pady=10)

sort_label = tk.Label(root, text="Sort Using:", font=("Helvetica", 12), fg=TEXT_COLOR, bg=LABEL_BACKGROUND_COLOR)
sort_label.pack(pady=10, fill='x')

# Create a Combobox for sorting algorithms
sorting_algorithms = ["Bubble Sort", "Insertion Sort", "Quick Sort", "Merge Sort", "Selection Sort", "Radix Sort"]
selected_algorithm = tk.StringVar()
algorithm_combobox = ttk.Combobox(root, textvariable=selected_algorithm, values=sorting_algorithms)
selected_algorithm.set(sorting_algorithms[0])
algorithm_combobox.pack(pady=10)

sort_button = tk.Button(root, text="Sort", command=sort_numbers, bg=BUTTON_COLOR, fg=TEXT_COLOR, height=2, width=20)
sort_button.pack(pady=10)

result_label = tk.Label(root, text="Sorted Numbers:", font=("Helvetica", 12), fg=TEXT_COLOR, bg=LABEL_BACKGROUND_COLOR, wraplength=400, justify="left")
result_label.pack(pady=10)

# Create a label to display the time sorting time
sorting_time_label = tk.Label(root, text="Sorting Time: N/A", font=("Helvetica", 12), fg=TEXT_COLOR, bg=LABEL_BACKGROUND_COLOR)
sorting_time_label.pack(pady=10)

# Function to reset the app
def reset_app():
    numbers_label.config(text="Random Numbers List:")
    result_label.config(text="Sorted Numbers:")
    sorting_time_label.config(text="Sorting Time: N/A")
    selected_algorithm.set(sorting_algorithms[0])

reset_button = tk.Button(root, text="Reset", command=reset_app, bg=BUTTON_COLOR, fg=TEXT_COLOR, height=2, width=20)
reset_button.pack(pady=10)

root.mainloop()