import math

#question 7
def calculate_sphere_volume():
    diameter = float(input("Enter the diameter of the sphere: "))
    radius = diameter / 2
    volume = (4 / 3) * math.pi * radius**3
    print(f"The volume of the sphere is approximately {volume:.2f} cubic units.")
    return volume

calculate_sphere_volume()

#question 8
def interest(prnc, time=2, rate=0.10):
    return prnc * time * rate

print(interest(6100, 1))  
print(interest(5000, rate=0.05))  
print(interest(5000, 3, 0.12))  
print(interest(time=4, prnc=5000))  

#question 11
print(math.add(1, 2))

#question 12
from math import subtract
print(subtract(2, 1))
from math import *
print(subtract(2, 1))
from math import add
print(add(1, 1))

#question 18
from math import factorial
print(factorial(5)) 

#question 20
import statistics

heights = {'Rishabh': 5.9, 'Anna': 5.5, 'Rinku': 6.1, 'Tapish': 6.0, 'Ajay': 7.2}
height_values = list(heights.values())

average_height = statistics.mean(height_values)
median_height = statistics.median(height_values)

print(f"Average Height: {average_height}")
print(f"Median Height: {median_height}")

#question 21
import random

def guess_number():
    number = random.randint(1, 9)
    guess = int(input("Guess a number between 1 and 9: "))
    if guess == number:
        print("Correct!")
    else:
        print(f"Wrong! The number was {number}.")

guess_number()





