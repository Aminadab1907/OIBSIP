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
--------------------------------******-----------------------------------------

Tallest ever recorded human to walk on Earth - 2.72m
Shortest ever recorded human to walk on Earth - 55 cm (0.55m)
Heaviest ever recorded human to live on Earth - 650kg
"""


# Define a function to receive user data
def user_input():
    # Ask the user for their name for a personalized interaction
    name = (input("Please enter your name:   ")).capitalize()

    # Input validation for weight
    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            if 0 < weight <= 650:
                break
            else:
                print("Please enter a weight between 0 and 650 kilograms.")
        except ValueError:
            print("Please enter a valid number for weight.")

    # Input validation for height
    while True:
        try:
            height = float(input("Enter your height in meters: "))
            if 0 < height <= 2.72:
                break
            else:
                print("Please enter a height between 0 and 2.72 meters.")
        except ValueError:
            print("Please enter a valid number for height.")

    return height, weight, name


# Define a function to calculate BMI from User Input
def bmiCalculator(height, weight):
    # BMI is the quotient of the individual's weight divided by the square of their height
    bmi = weight/ (height*height)
    return round(bmi, 2)  # Round the BMI Result to two decimal places


# Define a function to classify BMI result into the above categories
def bmiClassify(result):
    if result >= 30:
        return 'Obesity'
    elif 30 > result >= 25:
        return 'Overweight'
    elif 25 > result >= 18.5:
        return 'Healthy Weight'
    else:
        return 'Underweight'


# Main script
height, weight, name = user_input()

# Calculate BMI
bmi_result = bmiCalculator(height, weight)

# Print the BMI result and classification
print("Dear", name, ",\nYour BMI is ", bmi_result)
print("Your BMI Classification falls into '", bmiClassify(bmi_result), "' category.")
