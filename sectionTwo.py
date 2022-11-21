#DATA TYPES
#Subscripting
#Always start counting from zero

#print("Hello"[4])

#TYPE CHECKING/CONVERSION

#type check - int
#a = 123
#print(type(a))

#type conversion
#a = str(123)
#print(type(a))

#a = float(123)
#print(type(a))

#DATA TYPE 
#Instructions
#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

#Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

#stage 1

#two_digit_number = input("Type a two digit")
#print(type("two_digit_number"))

#stage 2

#first_digit = two_digit_number[0]
#second_digit = two_digit_number[0]

#height = input("enter your height in m: ")
#weight = input("enter your weight in kg: ")

#1st stage using exponent operator
#bmi = int(weight) / float(height) ** 2
#print(bmi)

#2nd stage using exponent operator
#bmi = int(weight) / float(height) ** 2
#bmi_as_int = int(bmi)
#print(bmi_as_int)

#NUMBER MANIPULATION 

#round function in different places etc
#print(round(8 / 3, 4))

#Floor // division means dividing and rounding down to the nearest integer.
#print(8 // 2)

#F-strings provide a concise and convenient way to embed python expressions 
#inside string literals for formatting. 

#score = 0
#height = 1.8
#isWinning = True

#Using f-String for individual variables
#print(f"your score is {isWinning}")

#Using f-String for ALL variables
#print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")


#CODE CHALLENGE
#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

#Input always create strings
#If you want to maths input, remeber to do TYPE CONVERSION.

#age = input("What is your age ")

#Convert input age as int.
#age_as_int = int(age)
#years_remaining = 90 - age_as_int
#days_remaining = years_remaining * 365
#weeks_remaining =  years_remaining * 52
#months_remaining = years_remaining * 12 

#print(months_remaining)

#message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
#print(message)

#PROJECT ONE

#Welcome to the tip calculator
#What was the total bill? $150.00
#What percentage tip would you like to give? 10,12,or 15? 12
#How many people to split the bill? 7
#Each person should pay: $19.93

#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person pay (150.00 / 5 ) * 1.12 = 33.6
#Round the result to 2 decimal places = 33.60

#This is the welcome page
print("Welcome to the tip calculator")

#Bill will have to be converted bc input should out float
bill = float(input("What was the total bill? $"))

#Remember not to add % sign on your code
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

people = int(input("How many people to split the  bill?"))

#bill_with_tip = tip / 100 * bill + bill

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
#This is the round number final amount
final_amount = round(bill_per_person, 2)
#This is rounding number to 2 decimal places in python
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
