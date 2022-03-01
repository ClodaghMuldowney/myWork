Grade = int(input('Input %: '))
if (Grade < 40):
    print("Fail")
elif (Grade >=40) and (Grade <= 49):
    print("Pass")
elif (Grade >=50) and (Grade <= 59) :
    print("Merit 2")
elif (Grade >=60) and (Grade <= 69) :
    print("Merit 1")
elif (Grade>=70) :
    print("Distinction")