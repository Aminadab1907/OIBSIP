'''This is a script that calculates the Body Mass Index of an individual when
he/she adds their height and weight and the appropriate obesity level is given
back to the user.'''


# Ask the user to input their height and weight
weight = float(input("Enter your weight in Kilograms:   "))
height = float(input("Enter your height in meters:  "))

# Define a function to calculate BMI from User Input
def bmiCalculator(height,weight):
    bmi = weight / (height * height)
    return round(bmi,2)


# print the bmi on the screen
bmi_result =  bmiCalculator(height,weight)
print("Your BMI is ",bmi_result)



""" BMI CLASSIFICATION TABLE
BMI	                Weight Status
--------------      ---------------
Below 18.5	        Underweight
18.5 – 24.9	        Healthy Weight
25.0 – 29.9	        Overweight
30.0 and Above	    Obesity
"""

#A fucntion to classify BMI result into the above categories

def bmiClassify(result):
    if (result >= 30):
        return 'Obesity'
    elif (result < 30 and result >=25):
        return 'Overweight'
    elif (result < 35 and result >=18.5):
        return 'Healthy Weight'
    else:
        return 'Underweight'


print ("Your BMI Classification is ",bmiClassify(bmi_result))










