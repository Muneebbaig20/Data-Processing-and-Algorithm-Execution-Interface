


import tkinter as tk
from tkinter import filedialog, messagebox
import random
import math
import os




class Coordinate:
    def __init__(self, horizontal, vertical):
      
        self.horizontal = horizontal
       
        self.vertical = vertical


# Function to calculate the distance between two coordinates
def calculate_distance(coord1, coord2):
   
    return math.sqrt((coord1.horizontal - coord2.horizontal) ** 2 + (coord1.vertical - coord2.vertical) ** 2)


# Brute-force method to find the closest pair of coordinates
def exhaustive_search(coordinates):
    
    min_distance = float('inf')
 
    for i in range(len(coordinates)):
      
        for j in range(i + 1, len(coordinates)):
       
            min_distance = min(min_distance, calculate_distance(coordinates[i], coordinates[j]))
    return min_distance


# Divide-and-conquer approach to find the closest pair of coordinates
def find_nearest_neighbors(coordinates):
    if len(coordinates) <= 3:

        return exhaustive_search(coordinates)
    

    midpoint = len(coordinates) // 2

    left_min = find_nearest_neighbors(coordinates[:midpoint])

    right_min = find_nearest_neighbors(coordinates[midpoint:])

    return min(left_min, right_min)



def multiply_large_numbers(multiplier, multiplicand):
    if multiplier < 10 or multiplicand < 10:
        return multiplier * multiplicand

    length = max(len(str(multiplier)), len(str(multiplicand)))

    half_length = length // 2

    ten_power_half = 10 ** half_length


    high_multiplier = multiplier // ten_power_half
    low_multiplier = multiplier % ten_power_half
    high_multiplicand = multiplicand // ten_power_half
    
    low_multiplicand = multiplicand % ten_power_half

    high_product = multiply_large_numbers(high_multiplier, high_multiplicand)
    
    low_product = multiply_large_numbers(low_multiplier, low_multiplicand)
    
    cross_product = multiply_large_numbers(high_multiplier + low_multiplier, high_multiplicand + low_multiplicand) - high_product - low_product

    return high_product * ten_power_half * ten_power_half + (cross_product * ten_power_half) + low_product



# Function to generate random input for coordinate and multiplication files
def generate_input_files(file_type, file_number, size):
    filename = f"{file_type}_input_{file_number}.txt"

    with open(filename, 'w') as file:
        if file_type == "coordinate":
            for _ in range(size):

                file.write(f"{random.randint(-1000, 1000)} {random.randint(-1000, 1000)}\n")
        elif file_type == "multiplication":
            for _ in range(size):

                file.write(f"{random.randint(1, 100000)} {random.randint(1, 100000)}\n")

    messagebox.showinfo("Info", f"{filename} generated successfully!")




# Function to calculate the closest pair distance from a file

def calculate_nearest_neighbors_from_file(filename):
    
    coordinates = []
    with open(filename, 'r') as file:
        for line in file:
            x, y = map(int, line.strip().split())

            coordinates.append(Coordinate(x, y))

    coordinates.sort(key=lambda coord: coord.horizontal)

    closest_distance = find_nearest_neighbors(coordinates)

    messagebox.showinfo("Result", f"Closest Pair Distance: {closest_distance}")



# Function to perform large-scale multiplication from a file

def perform_large_scale_multiplication_from_file(filename):
    result_text = ""
    with open(filename, 'r') as file:
      
        for line in file:
            num1, num2 = map(int, line.strip().split())
            product = multiply_large_numbers(num1, num2)
           
            result_text += f"Multiplication Result for {num1} and {num2}: {product}\n"

    messagebox.showinfo("Result", result_text)



def main():
    root = tk.Tk()
    root.title("Algorithm GUI")


    def generate_file():

        file_type = file_type_var.get()
        file_number = file_number_entry.get()
        size = int(size_entry.get())

        generate_input_files(file_type, file_number, size)


    def open_and_run_algorithm():
      
        filename = filedialog.askopenfilename(title="Select Input File", filetypes=[("Text files", "*.txt")])
        if filename:

            algorithm_choice = algorithm_var.get()

            if algorithm_choice == "Closest Pair":
                calculate_nearest_neighbors_from_file(filename)

            elif algorithm_choice == "Integer Multiplication":
                perform_large_scale_multiplication_from_file(filename)

            else:
                messagebox.showerror("Error", "Please select a valid algorithm")


    # File generation options

    tk.Label(root, text="Generate Input File").grid(row=0, column=0, columnspan=2)
    file_type_var = tk.StringVar(value="coordinate")
  
    tk.Radiobutton(root, text="Coordinate", variable=file_type_var, value="coordinate").grid(row=1, column=0)
    
    tk.Radiobutton(root, text="Multiplication", variable=file_type_var, value="multiplication").grid(row=1, column=1)


    tk.Label(root, text="File Number:").grid(row=2, column=0)
    file_number_entry = tk.Entry(root)

    file_number_entry.grid(row=2, column=1)


    tk.Label(root, text="Size:").grid(row=3, column=0)
    size_entry = tk.Entry(root)

    size_entry.grid(row=3, column=1)

    tk.Button(root, text="Generate File", command=generate_file).grid(row=4, column=0, columnspan=2, pady=5)

    

    tk.Label(root, text="Select Algorithm").grid(row=5, column=0, columnspan=2)
    
    algorithm_var = tk.StringVar(value="Closest Pair")
   
    tk.Radiobutton(root, text="Closest Pair", variable=algorithm_var, value="Closest Pair").grid(row=6, column=0)
   
    tk.Radiobutton(root, text="Integer Multiplication", variable=algorithm_var, value="Integer Multiplication").grid(row=6, column=1)


    tk.Button(root, text="Open and Run Algorithm", command=open_and_run_algorithm).grid(row=7, column=0, columnspan=2, pady=10)

    root.mainloop()


if __name__ == "__main__":

    main()
