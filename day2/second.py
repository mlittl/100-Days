# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
float(height)
float(weight)

height2 = float(height)*float(height)
BMI = int(weight) / height2

int_BMI = int(BMI)

print(int_BMI)