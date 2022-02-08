weight = input("Enter your mass in Kilograms: ")
height = input("Enter your height in metres: ")
bmi = (float(weight)/(float(height)*float(height)))
if bmi < 18.5:
    print("Underweight")
elif (18.5 < bmi < 25):
    print("Normal")
elif (25 < bmi < 30):
    print("Overweight")
elif bmi > 30:
    print("Obesity")

