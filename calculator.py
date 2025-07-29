first= float(input("enter the first number: "))
second= float(input("enter the second number:"))
operation= input("chose an operation (+, -, *, /): ")
if operation == "+":
    result = first + second
    print("the answer is:", result)
elif operation == "-":
    result = first - second
    print("the answer is:", result)
elif operation =="*":
    result = first * second 
    print("the answer is:", result)
elif operation == "/":
    if second == 0:
        print("you can't divide by zero!")
    else:
        result = first / second
        print("the answer is:", result)
else:
    print("that's not a valid operation!")
    