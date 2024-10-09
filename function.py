#recursive function
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 3
print("The factorial of", num, "is", factorial(num))


#anonymous/lambda function
# Python code to illustrate the cube of a number
def cube(x): return x*x*x

cube_v2 = lambda x : x*x*x

print(cube(7))
print(cube_v2(7))


#generator function
# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1            
    yield 2            
    yield 3            
 
# Driver code to check above generator function
for value in simpleGeneratorFun(): 
    print(value)

def fib(limit):
    a, b = 0, 1
    while b < limit:
        yield b
        a, b = b, a + b

# Create a generator object
x = fib(200)

# Iterate over the generator object and print each value
for i in x:
    print(i)


#user defined function
def evenOdd( x ): 
    if (x % 2 == 0): 
        print("even")
    else: 
        print("odd")
  
# Driver code 
evenOdd(2) 
evenOdd(3)


#High order function
# Python program to illustrate functions 
# can be passed as arguments to other functions 
def shout(text): 
    return text.upper() 
  
def whisper(text): 
    return text.lower() 
  
def greet(func): 
    # storing the function in a variable 
    greeting = func("Hi, I am created by a function \
    passed as an argument.") 
    print(greeting)  
  
greet(shout) 
greet(whisper)


#built-in functions
# Function to calculate speed
def cal_speed(dist, time):
    print(" Distance(km) :", dist)
    print(" Time(hr) :", time)
    return dist / time

# Function to calculate distance traveled
def cal_dis(speed, time):
    print(" Time(hr) :", time)
    print(" Speed(km / hr) :", speed)
    return speed * time

# Function to calculate time taken
def cal_time(dist, speed):
    print(" Distance(km) :", dist)
    print(" Speed(km / hr) :", speed)
    return dist / speed


# Driver Code
# Calling function cal_speed()
print(" The calculated Speed(km / hr) is :",
      cal_speed(abs(45.9), abs(-2)))
print("")

# Calling function cal_dis()
print(" The calculated Distance(km) :",
      cal_dis(abs(-62.9), abs(2.5)))
print("")

# Calling function cal_time()
print(" The calculated Time(hr) :",
      cal_time(abs(48.0), abs(4.5)))


#dict() function
my_dict = dict(name="Alice", age=25, city="New York")
print(my_dict) 


