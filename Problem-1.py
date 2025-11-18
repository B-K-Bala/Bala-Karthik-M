# Problem-1.py
# First problem - Simple Calcluaator using class - class name Calculator 
# For Double i imported double from matplotlib.pylab
# Inputs : a --> double , b --> double , c --> string

from matplotlib.pylab import double


class calcultor:
    def __init__(self,a,b):
        self.a =a

        self.b=b

    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b  
    def mul(self):
        return self.a * self.b
    def div(self):
        if self.b==0:
            return f"Cannot Divide the {self.a} by zero"
        return self.a / self.b
    
if __name__ == "__main__":
    a=double(input("Enter first number: "))
    b=double(input("Enter second number: "))
    operation=input("Enter operation (add,sub,mul,div): ")

    cal = calcultor(a,b)
    if operation == "add":
        print(f"Addition {a} {operation} {b} :",cal.add())
    elif operation == "sub":
        print(f"Subtraction {a} {operation} {b} :",cal.sub())
    elif operation == "mul":
        print(f"Multiplication {a} {operation} {b} :",cal.mul())
    elif operation == "div":
        print(f"Division {a} {operation} {b} :",cal.div())
    else:
        print("Unknown operation")
        
     

        
