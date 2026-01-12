#Simple Function
#Create a function that: Takes a name as parameter,  Prints a greeting message

def greet(name):
    print(f"Welcome {name}, Have a good day")
    
name = str(input("Please enter your name: "))
greet(name)



# Add Two Numbers
# Create a function that: Takes two numbers Returns their sum, Print the returned value

def sum(n1, n2):
    return n1+n2

n1 = int(input("Please enter the first number: "))
n2 = int(input("Please enter the second number: "))
add = sum(n1,n2)
print(f"{n1} + {n2} = {add}")




# Check Even or Odd
# Create a function that: Takes a number, Prints whether it is even or odd

def check(n):
    if (n%2==0):
        print(f"{n} is an even number!")
    else:
        print(f"{n} is an odd number!")


n = int(input("Please eneter the number: "))
check(n)




# Factorial (Recursion)
# Create a recursive function to: Calculate factorial of a number

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
n = int(input("please enetr a number: "))
f = factorial(n)
print(f"The factorial of {n} is: {f}")