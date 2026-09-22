# Question 2 - Your First Toolbox
# Function 1 - double
def double(number):
    return(number*2)
print(double(7))
print(double(10))

# Function 2 - is_pass
def is_pass(score):
    if score >= 50:
        return "True"
    return "False"
print(is_pass(80))
print(is_pass(20))


# Function 3 - greet
def greet(name, greeting="Hello"):
   return greeting + ", " + name + "!"

print(greet("Amina", " Hello"))
print(greet("Brian", " Habari"))
