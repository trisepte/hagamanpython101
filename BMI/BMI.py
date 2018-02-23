
from gpiozero import RGBLED 
from time import sleep
from colorama import Fore
from colorama import init

led = RGBLED(16, 20, 21)
init()

print("Welcome to BMI Calculator!")

height = float(input("Please enter your height (in inches): "))

weight = int(input("Please enter your weight (in pounds): "))

height_meter = height*0.025

weight_kilo = weight*0.45

bmi = weight_kilo / ( height_meter ** 2 )

if bmi <= 18.5:
    print(Fore.RED + "Your BMI is ", bmi," which means you are underweight. ")
    led.color = (1, 0, 0) # red
    
elif bmi > 18.5 and bmi < 25:
    print(Fore.GREEN + "Your BMI is ", bmi," which means you are normal. ")
    led.color = (0, 1, 0) # green

elif bmi > 25 and bmi < 30:
    print(Fore.YELLOW + "Your BMI is ", bmi," which means you are overweight. ")
    led.color = (1, 0.411765, 0) # orange

elif bmi > 30:
    print(Fore.RED + "Your BMI is ", bmi," which means you are obese. ")
    led.color = (1, 0, 0) # red
    
else:
    print("There was an error with your input. ")

sleep(5)
