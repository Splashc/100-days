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

#Final - Tip Calculator
print("WELCOME TO MONEY calculator")
bill = float(input("WHAT YOU PAY $ "))
tip = int(input("HOW much Do you tip in %? "))
people = int(input("How much people pay the bill? "))

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print(f"EVERYONE PAY: ${final_amount}")
