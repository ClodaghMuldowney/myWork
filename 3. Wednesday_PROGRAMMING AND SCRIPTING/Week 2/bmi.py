weight = int(input("Enter Weight kg: "))
height= int(input("Enter Height cm: "))
HeightInMetres= (height/100)
bmi= (weight/HeightInMetres)/HeightInMetres
BMI = round(bmi, 1)

print("your BMI is {}".format(BMI))
