print("Welcome to BMI Calculator!")

height = float(input("Please enter your height (in inches): "))

weight = int(input("Please enter your weight (in pounds): "))

height_meter = height*0.025

weight_kilo = weight*0.45

bmi = weight_kilo / ( height_meter ** 2 )

if bmi <= 18.5:
    print("Your BMI is ", bmi," which means you are underweight. ")

elif bmi > 18.5 and bmi < 25:
    print("Your BMI is ", bmi," which means you are normal. ")

elif bmi > 25 and bmi < 30:
    print("Your BMI is ", bmi," which means you are overweight. ")

elif bmi > 30:
    print("Your BMI is ", bmi," which means you are obese. ")

else:
    print("There was an error with your input. ")
