# Calculating Body Mass Index (height / divided by weight squared) using imperial measurements.
# If using metric measurements (i.e. meters and kilograms) change "inches" to "m" and "lbs" to "kg" and remove the * 703

height = float(input("Please enter your height in inches: "))
weight = float(input("Please enter your weight in lbs: "))

result = (weight / height ** 2) * 703
BMI = round(result,2)
# print(format(BMI,".2f"))
if BMI >= 40:
  print(f"Your BMI is {BMI} and you are very obese.")
elif 30 <= BMI <= 39:
  print(f"Your BMI is {BMI} and you are obese.")
elif 25 <= BMI <= 29:
  print(f"Your BMI is {BMI} and you are overweight.")
elif 19 <= BMI <= 24:
  print(f"Your BMI is {BMI} and you are normal weight.")
else:
  print(f"Your BMI is {BMI} and you are underweight.")
