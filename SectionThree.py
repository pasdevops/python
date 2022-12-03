#COMAPRISON OPERATOR 

#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))

#if statement syntax
#use semi colon at the end 
#use indetation on the print line
#else should under "if line" 
#Add a colon afer the "else"
#use another indentation after "else"

#GREATER THAN
#if height > 120:
  #print("You can ride the rollercoaster")
#else:
  #print("Sorry, you have to grow taller before you can ride.")

#LESS THAN
#if height < 120:
 #print("You can ride the rollercoaster")
#else:
  #print("Sorry, you have to grow taller before you can ride.")

#GREATER THAN OR EQUAL TO
#if height >= 120:
  #print("You can ride the rollercoaster")
#else:
  #print("Sorry, you have to grow taller before you can ride.")


#ODD OR EVEN NUMBER
#Instructions
#Write a program that works out whether if a given number is an odd or even number.
#Even numbers can be divided by 2 with no remainder.
#e.g. 86 is even because 86 ÷ 2 = 43
#43 does not have any decimal places. Therefore the division is clean.
#e.g. 59 is odd because 59 ÷ 2 = 29.5
#29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.
#The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.

#number = int(input("Which number do you want to check?" ))

#modulo and comparison operator
#if number % 2 == 0:
  #print("This is a even number")
#else:
  #print("This is an odd number")

#NESTED IF STATEMENT AND ELIF STATEMENT

#if height >= 120:
  #print("You can ride the rollercoaster!")
  #age = int(input("What is your age? "))
#Nested if statement SHOULD live in if statement 
#if the age is not less than 12 PRINT pay $5
#if age < 12:
  #print("Please pay $5.")
#You can add ELIF b/w if and ELSE can be represented as ELSEIF
#You can add as many ELIF as you want in a block of if condition.
#elif age <= 18:
  #print("Please pay $7.")
#elif age <= 18:
  #print("Please pay $7.") 
#else: 
  #print("Please pay $12.")


#BMI CALCULATOR PROJECT

#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
#The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
#The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
#Warning you should convert the result to a whole number.

#Under 18.5 they are underweight
#Over 18.5 but below 25 they have a normal weight
#Over 25 but below 30 they are overweight
#Over 35 but below 35 they are obese
#Above 35 they are clinically obese

#ARITHMETIC OPERATORS

# MODULES = returns the remainder of dividing two numbers %

# EXPONENTIATION = raises a number to a power 
# e.g. 
# x = 2
# y = 5
# Same as 2*2*2*2*2

# FLOOR DIVISION = rounds the results down to the nearest whole number
# e.g.
# x = 15
# y = 2
# (x // y) = 7

#height = float(input("enter your height in m: "))
#weight = float(input("enter your weight in kg: "))

#bmi = round(weight / height ** 2)
#if bmi >18.5:
#print(f"Your bmi is {bmi}, you are underweight.")
#elif bmi <25:#
  #print(f"Your bmi is {bmi}, you have normal weight.")
#elif bmi <30:
  #print(f"Your bmi is {bmi}, you are overweight.")
#elif bmi <35:
  #print(f"Your bmi is {bmi}, you are obese.")
#else: 
  #print(f"Your bmi is {bmi}, you are clinically obese.")


#LEAP YEAR PROJECT

#year = int(input("Which year do you want to check? "))

#if year % 4 == 0:
  #if year % 100 == 0:
    #if year % 400 == 0:
      #print("Leap year")
    #else: 
      #print("Not a leap year")
  #else:
      #print("Leap year.")
#else:
  #print("Not a leap year.")


# MULTIPLE IF STATEMET PROJECT

#print("Welcome to the rollercoaster!")
#height = int(input("What is your height in cm? "))
#bill = 0

#if height >= 120:
  #print("You can ride the rollercoaster!")
  #age = int(input("What is your age? "))
  #if age < 12:
    #bill = 5
    #print("Child tickets are $5.")
  #elif age <= 18:
    #bill = 7
    #print("Youth tickets are $7. ")
  #else: 
    #bill = 12
    #print("Adult tickets are $12.")

  #wants_photo = input("Do you want a photo taken? Y or N. ")
  #if wants_photo == "Y":
    #bill += 3
  #print(f"Your final bill is ${bill}")

#else: 
  #print("Sorry, you have to grow taller before you can ride.")
  #What is the use of += in Python?
#+= adds a number to a variable, changing the variable itself in the process


#Exercise 4 - Pizza Order Practice
#Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

#Based on a user's order, work out their final bill.
#Small Pizza: $15
#Medium Pizza: $20
#Large Pizza: $25
#Pepperoni for Small Pizza: +$2
#Pepperoni for Medium or Large Pizza: +$3
#Extra cheese for any size pizza: + $1

#print("Welcome to Python Pizza Deliveries!")
#size = input("What size pizza do you want? S,M or L")
#add_pepperoni = input("Do you want pepperoni? Y or N")
#extra_cheese = input("Do want extra cheese? Y or N"Y)

#bill = 0

#if size == "S" :
 #bill += 15
# += adds another value with the variable's value and assigns the new value to the variable.
#elif size == "M" :
  #bill += 20
#elif size == "L" :
  #bill += 25
# add a nested if statement

#if add_pepperoni == "Y":
  #if size == "S":
    #bill += 2
  #else:
   #bill += 3
#if extra_cheese == "Y": 
  #bill += 1

#print(f"Your final bill is ${bill}")


# Exercise 5 - Love Calculator

#Instructions
#You are going to write a program that tests the compatibility between two people.
#To work out the love score between two people:
#Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#Then check for the number of times the letters in the word LOVE occurs. 
#Then combine these numbers to make a 2 digit number.
#For Love Scores less than 10 or greater than 90, the message should be:

#print("Welcome to the Love Calculator")
#name1 = input("What is your name? \n")
#name2 = input("What is their name? \n")

#combine_string = name1 + name2
#lower_case_string = combine_string.lower()

#t = lower_case_string.count("t")
#r = lower_case_string.count("r")
#u = lower_case_string.count("u")
#e = lower_case_string.count("e")

#true = t + r + u + e

#l = lower_case_string.count("l")
#o = lower_case_string.count("o")
#v = lower_case_string.count("v")
#e = lower_case_string.count("e")

#love = l + o + v + e

#love_score = int(str(true) + str(love))

#print(love_score)

#if (love_score <10) or (love_score> 90):
  #print(f"Your love score is {love_score}, you go together like coke and menthos")

#elif(love_score >= 40) and (love_score <= 50):
  #print(f"Your score is {love_score}, you are alright together.")
#else: 
  #print(f"Your score is {love_score}")
