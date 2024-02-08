"""This is a script that calculates the Body Mass Index of an individual when
he/she adds their height and weight and the appropriate obesity level is given
back to the user.
----------------------------BMI CLASSIFICATION TABLE---------------------------
     BMI	          Weight Status
--------------      ---------------
Below 18.5	        Underweight
18.5 – 24.9	        Healthy Weight
25.0 – 29.9	        Overweight
30.0 and Above	    Obesity
--------------------------------******----------------------------------------

Tallest ever recorded human to walk on Earth  - 2.72m
Shortest ever recorded human to walk on Earth - 55 cm (0.55m)
Heaviest ever recorded human to live on Earth - 650kg


*** Here we will create a GUI for our BMI Calculator using "ttkbootstrap" package
as it's more customized and more attractive than vanilla tkinter.

N.B - It requires installing the ttkbootstrap package in your system
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkbootstrap import Style


# Define a Function to take user input and calculate BMI
def calculate_bmi():
    try:
        # Accept user input in the provided boxes
        weight = float(weight_input.get())
        height = float(height_input.get())

        # Ensure weight and height fall within valid ranges (0-650 kg and 0-2.72 meters).
        # Raise a ValueError if either is outside the valid range.
        if not (0 < weight <= 650) or not (0.54 < height <= 2.72):
            raise ValueError("WEIGHT must be between 0 and 650 Kilograms, and HEIGHT must be between 0.54 and 2.72 "
                             "meter")

        # This is executed as long as we have received the correct data
        bmi = round(weight / (height * height), 2)  # Calculate the BMI and round it to two decimal place
        bmi_result_label.config(text=f"Your BMI is {bmi}",
                                foreground='green')  # This sets the text displayed on the screen to include the
        # calculated BMI value.
        bmi_classification_label.config(text=f"Your BMI Classification is '{bmi_classify(bmi)}'",
                                        foreground='green')  # This displays the BMI classification based on the result.

    # If an error occurs
    # This displays the value error obtained in a pop-up error messagebox
    except ValueError as ve:
        messagebox.showerror("Error", str(ve))  # The value error message from above is displayed here
        bmi_result_label.config(text="", foreground='black')  # Reset text color to black for error
        bmi_classification_label.config(text="", foreground='black')


# This i the function to classify the BMI Result to the appropriate categories
def bmi_classify(result):
    if result >= 30:
        return 'Obesity'
    elif 30 > result >= 25:
        return 'Overweight'
    elif 25 > result >= 18.5:
        return 'Healthy Weight'
    else:
        return 'Underweight'


# ---GUI is created using the code snippets below---

# Create a Tkinter GUI window
root = tk.Tk()  # This initializes a Tkinter window instance.
root.title("BMI Calculator")  # This is the title for the GUI Window
style = Style(theme="cyborg")  # This is optional and can be changed to other themes
icon_image = tk.PhotoImage(file="bmilogo2.png") # A custom logo png for the BMI App that is shown in the window title
root.iconphoto(True, icon_image)

# Create input fields for the height, weight, and name
container = ttk.Frame(root, padding=20)  # This creates a frame widget named container inside the root window
# which is used to organize and group other widgets.
container.pack(expand=True, fill="none")  # This makes it expandable in both directions (horizontally and
# vertically) to fill available space.

# creates a label and an entry field for the user's name within the container frame.
name_label = ttk.Label(container, text="Name:")
name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
name_entry = ttk.Entry(container)
name_entry.grid(row=0, column=1, padx=10, pady=5)


# creates a label and an entry field for the user's weight within the container frame.
weight_label = ttk.Label(container, text="Weight(kg):")
weight_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
weight_input = ttk.Entry(container)
weight_input.grid(row=1, column=1, padx=10, pady=5)


# creates a label and an entry field for the user's height within the container frame.
height_label = ttk.Label(container, text="Height(m):")
height_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
height_input = ttk.Entry(container)
height_input.grid(row=2, column=1, padx=10, pady=5)


# creates a button widget to calculate BMI within the container frame
calculate_button = ttk.Button(container, text="Calculate BMI", command=calculate_bmi) # A button is defined which
# when clicked executes the calculate_bmi function when pressed
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10) # This places the button under the entry fields


# creates two label widgets to display the BMI result and its classification within the container frame
bmi_result_label = ttk.Label(container, text="", foreground='black')  # Initialize text color as black and initial
# text is set to an empty string
bmi_result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

bmi_classification_label = ttk.Label(container, text="", foreground='black')  # Initialize text color as black and
# initial text is set to an empty string
bmi_classification_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

# Run the Tkinter event loop
root.mainloop()