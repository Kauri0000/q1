#1. Create a class called calculator
#2. Create a function in the class for each mathematical operation: Addition, Multiplication, Division, Subtraction
#3. Outside of your class definition, create an instance of your calculator class
#4. Call each function in your calculator class and store each output into a variable. Use any values for arguments.
#5. Print all your variables to the console



class calculator:

    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b    
    
    def divide(self, a, b):
        return a / b
    
calc = calculator()
    
print(" Input your 2 values")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
add_result = calc.add(a, b)
subtract_result = calc.subtract(a, b)
multiply_result = calc.multiply(a, b)
divide_result = calc.divide(a, b)

print("Addition Result:", add_result)
print("Subtraction Result:", subtract_result)
print("Multiplication Result:", multiply_result)
print("Division Result:", divide_result)