#User input of % grade
percentage = float(input("Enter the percentage: "))

#round the float down
import math
percentage = math.floor(percentage)

#stipulations for grades
if (percentage < 40):
    print("Fail")
elif (percentage >=40) and (percentage <= 49):
    print("Pass")
elif (percentage >=50) and (percentage <= 59) :
    print("Merit 2")
elif (percentage >=60) and (percentage <= 69) :
    print("Merit 1")
elif (percentage>=70) :

    print("Distinction")
