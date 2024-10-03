def classattendance():
    print('class attendance is low')
classattendance()

def car():
    print('this car is a vw golf')
car()

def medicine():
    print('the goverment is replacing NHIF')
medicine()

def greet():
 print('welcome to Kenya')
greet()

def add_numbers(a, b):
    return a+b
result = add_numbers(3,5)
print (result)

def sub_numbers(a, b):
    return a-b
result = sub_numbers(8,5)
print (result)

def mult_numbers(a, b):
    return a*b
result = mult_numbers(3,5)
print (result)

def div_numbers(a, b):
    return a/b
result = div_numbers(35,5)
print (result)


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

#anonymous function
# Python code to illustrate the cube of a number
# using lambda function
def cube(x): return x*x*x

cube_v2 = lambda x : x*x*x

print(cube(7))
print(cube_v2(7))