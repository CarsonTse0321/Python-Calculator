#This is a python calculator for some simple calculations

operation = input("please enter the calculation symbol (sum : + , minus : - , product : * , division : / , Quadratic equation : 01 , heron's formula : 02 , cos formula : 03 , Compound Interest : 04 )")

import math

if operation == "+" :
    num1 = float(input("please enter the first number:"))
    num2 = float(input("please enter the second number:"))
    result = num1 + num2

elif operation == "-" :
    num1 = float(input("please enter the first number:"))
    num2 = float(input("please enter the second number:"))
    result = num1 - num2

elif operation == "*" :
    num1 = float(input("please enter the first number:"))
    num2 = float(input("please enter the second number:"))
    result = num1 * num2

elif operation == "/" :
    num1 = float(input("please enter the first number:"))
    num2 = float(input("please enter the second number:"))
    result = num1 / num2

elif operation == "01" :
    num1 = float(input("please enter the first number:"))
    num2 = float(input("please enter the second number:"))
    num3 = float(input("please enter the third number:"))
    root1 = (-num2 + (num2**2 - 4*num1*num3)**0.5) / (2*num1)
    root2 = (-num2 - (num2**2 - 4*num1*num3)**0.5) / (2*num1)

elif operation == "02" :
    num1 = float(input("please enter the first number:"))
    num2 = float(input("please enter the second number:"))
    num3 = float(input("please enter the third number:"))
    s = (num1 + num2 + num3)/2
    area = (s*(s-num1)*(s-num2)*(s-num3))**0.5

elif operation == "03" :
    num1 = float(input("please enter the first number:"))
    num2 = float(input("please enter the second number:"))
    angle=float(input("please enter the angle in degrees:"))
    c = (num1**2 + num2**2 - 2*num1*num2*math.cos(math.radians(angle)))**0.5

elif operation == "04" :
    principal = float(input("Enter the principal: "))

    interest_rate = float(input("Enter the interest rate (in %): "))

    time = float(input("Enter the time (in year): "))

    calme = input("How does it calculate (annually, quarterly, halfyear):")

    if calme == "annually":
        ans = principal * (1 + interest_rate/100) ** time

    elif calme == "quarterly":
        ans = principal * (1 + interest_rate/400) ** (time * 4)

    elif calme == "halfyear":
        ans = principal * (1 + interest_rate/200) ** (time * 2)

    else:
        print("Plz make sure you enter the right inputs.")
        quit()

else:
    print("please enter the correct symbol")
    exit()

if operation == "01":
    print(f"The roots of the equation are {root1} and {root2}")

elif operation == "02":
    print(f"The area of the triangle is {area}")

elif operation == "03":
    print(f"The length is {round(c,2)}")

elif operation == "04":
    interest = ans - principal

    print(f"The new total amount of money is $ {round(ans,2)} , the interest is ${round(interest,2)}")

else:
    print("ANS is",{round(result,2)})
