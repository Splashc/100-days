# Exercise 1 - Data Types
two_digit_number = input("Type a two digit number: ")

first = int(two_digit_number[0])
second = int(two_digit_number[1])

print(first + second)

# Exercise 2 - BMI Calculator
Height = input("enter your height in m: \n")
Weight = input("enter your weight in kg: \n")

Weight_int = int(Weight)
Height_float = float(Height)

bmi = Weight_int / Height_float ** 2
bmi = Weight_int / (Height_float * Height_float)
bmi_as_int = int(bmi)
print(bmi_as_int)

#Exercise 3 - Life in Weeks
Age = input("What is your current age? \n")

Years = 90 - int(Age)
Months = round(Years * 12)
Weeks = round(Years * 52)
Days = round(Years * 365)

print(f"You have {Days} days, {Weeks} weeks, and {Months} months left.")
