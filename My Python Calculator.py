
operation = input("please enter the calculation symbol (sum : + , minus : - , product : * , division : / , Quadratic equation : 01 , heron's formula : 02 , cos formula : 03 , Compound Interest : 04 , Sigma(Sum) : 05 , prime number checking : 06 )")

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
    num2 = 0
    while num2 == 0:
        num2 = float(input("please enter the second number:"))
        if num2 == 0:
            print("The second number cannot be zero cuz you cannot divide by zero.")
    result = num1 / num2

elif operation == "01" :
    num1 = float(input("please enter the first number:"))
    num2 = float(input("please enter the second number:"))
    num3 = float(input("please enter the third number:"))
    dalta = num2**2 - 4*num1*num3
    root1 = (-num2 + (num2**2 - 4*num1*num3)**0.5) / (2*num1)
    root2 = (-num2 - (num2**2 - 4*num1*num3)**0.5) / (2*num1)

elif operation == "02" :
    num1 = 0
    num2 = 0
    num3 = 0
    while num1 <= 0:
        num1 = float(input("please enter the first number:"))
        if num1 <= 0:
            print("Length of triangle must be a positive number.")
    while num2 <= 0:
        num2 = float(input("please enter the second number:"))
        if num2 <= 0:
            print("Length of triangle must be a positive number.")
    while num3 <= 0:
        num3 = float(input("please enter the third number:"))
        if num3 <= 0:
            print("Length of triangle must be a positive number.")
    if (num1 + num2 <= num3) or (num1 + num3 <= num2) or (num2 + num3 <= num1):
        print("The triangle is not possible.")
        exit()
    s = (num1 + num2 + num3)/2
    area = (s*(s-num1)*(s-num2)*(s-num3))**0.5

elif operation == "03" :
    num1 = 0
    num2 = 0
    angle = 0
    while num1 <= 0:
        num1 = float(input("please enter the first number:"))
        if num1 <= 0:
            print("Length of triangle must be a positive number.")
    while num2 <= 0:
        num2 = float(input("please enter the second number:"))
        if num2 <= 0:
            print("Length of triangle must be a positive number.")
    while angle <= 0:
        angle = float(input("please enter the angle:"))
        if angle <= 0:
            print("Angle of triangle must be a positive number.")
    
    c = (num1**2 + num2**2 - 2*num1*num2*math.cos(math.radians(angle)))**0.5
    
    if num1 + num2 <= c or c + num1 <= num2 or c + num2 <= num1:
        print("The triangle is not possible.")
        exit()

elif operation == "04" :
    principal = 0

    while principal <= 0:
        principal = float(input("Enter the principal amount: "))
        if principal <= 0:
            print("The principal amount must be a positive number.")

    interest_rate = 0

    while interest_rate <= 0:
        interest_rate = float(input("Enter the interest rate (in %) per year: "))
        if interest_rate <= 0:
            print("interest_rate must be positive number.")

    time = 0

    while time <= 0:
        time = float(input("Enter the time (in year): "))
        if time <= 0:
            print("Time must be positive number.")
       
    calme = input("How does it calculate (annually, quarterly, halfyear):")

    if calme == "annually":
        ans = principal * (1 + interest_rate/100) ** time

    elif calme == "quarterly":
        ans = principal * (1 + interest_rate/400) ** (time * 4)

    elif calme == "halfyear":
        ans = principal * (1 + interest_rate/200) ** (time * 2)

    else:
        print("Plz make sure you enter the correct inputs.")

elif operation == "05" :
    Starting_index = 0
    Final_index = 0
    
    while Starting_index <= 0:
        Starting_index = int(input("Enter the starting index:"))
        if Starting_index <= 0:
            print("Starting index must be a positive number.")
    
    while Final_index <= 0:
        Final_index = int(input("Enter the final index:"))
        if Final_index <= 0:
            print("Final index must be a positive number.")

    while Starting_index > Final_index:
        print("Final index must be greater than starting index.")
        Final_index = int(input("Enter the final index:"))
    ans05 = 0

    for x in range(Starting_index, Final_index + 1, 1):
        ans05 += x
    
elif operation == "06" :
    num = 0

    while num <= 1:
        num = int(input("Enter a number: "))
        if num <= 1:
            print("num must be greater than 1")
        elif num == 2:
            print("Prime")
        else:
            for x in range(2, num):
                if num % x == 0:
                    print("Not Prime")
                    break
                else:
                    print("Prime")
                    break
    exit()
else:
    print("please enter the correct symbol")
    exit()

if operation == "01":
    if {dalta} == 0:
        print({dalta})
        print("The equation has one real root only.")
        print(f"The root of the equation is {root1}")

    elif {dalta} < 0:
        print({dalta})
        print("The equation has no real root.")
    
    else:
        print({dalta}) 
        print("The equation has two real roots.")
        print(f"The roots of the equation are {root1} and {root2}")

elif operation == "02":
    print(f"The area of the triangle is {area}")

elif operation == "03":
    print(f"The length is {round(c,2)}")

elif operation == "04":
    interest = ans - principal

    print(f"The new total amount of money is $ {round(ans,2)} , the interest is ${round(interest,2)}")

elif operation == "05":
    print(f"The sum is {ans05}")

else:
    print("ANS is",{round(result,2)})
