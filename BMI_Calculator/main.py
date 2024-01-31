'''This is a script that calculates the Body Mass Index of an individual when
he/she adds their height and weight and the appropriate obesity level is given
back to the user.'''


# Ask the user to input their height and weight
weight = float(input("Enter your weight in Kilograms:   "))
height = float(input("Enter your height in meters:  "))

# Define a function to calculate BMI from User Input
def bmiCalculator(height,weight):
    bmi = weight / (height * height)
    return (bmi)


# print the bmi on the screen
print(bmiCalculator(height,weight))






