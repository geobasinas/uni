import cmath
import math

a = int(input("Dose timh gia ton a: "))
b = int(input("Dose timh gia ton b: "))
c = int(input("Dose timh gia ton c: "))

if a % 2 == 0:
    discriminant = b**2 - 4 * a * c
    if discriminant >= 0:
        solution1 = (-b + math.sqrt(discriminant)) / (2 * a)
        solution2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Riza 1:", solution1)
        print("Riza 2:", solution2)
        if solution1 > solution2:
            print("Megalyterh lysh einai:", solution1)
        else:
            print("Megalyterh lysh einai:", solution2)
    elif discriminant == 0:
        solution = -b / (2 * a)
        print("H exisosi exei mia pragmatiki riza:", solution)
    else:
        print("H exisosi den exei pragmatikes rizes alla exei duo fantasitkes rizes")
        riza1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        riza2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        print("Riza 1:", riza1)
        print("Riza 2:", riza2)
        if riza1.real > riza2.real:
            print("H megalyterh lysh einai:", riza1)
        else:
            print("H megalyterh lysh einai:", riza2)
else:
    average = (a + b + c) / 3
    print("O mesos oros tvn a, b kai c einai:", average)
  
