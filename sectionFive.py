# FOR LOOP
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)

#fruits = ["Apple", "Peach", "Pear"]
#or john in fruits:
  #print(john)
  #print(john + "pie") #Inside for loop will print as many times as possible
  #print(fruits)
#print(fruits) # outside for loop

#Loop through the letters in the word "banana":
#for code in "I love Python":
  #print(code)

#Exercise 1 - Average Height

#Instructions
#You are going to write a program that calculates the average student height from a List of heights.
#e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
#The average height can be calculated by adding all the heights together and dividing by the total number of heights.
#e.g.
#180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
#There are a total of 7 heights in student_heights
#1146 ÷ 7 = 163.71428571428572
#Average height rounded to the nearest whole number = 164
#Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

#student_heights = input("Input a list of students height ")

#for n in range(0, len(student_heights)):
  #student_heights[n] = int(student_heights[n])
#print(student_heights)

#total_height = 0
#for height in student_heights:
  #total_height += (height)
#print(total_height)

#number_of_students = 0
#for student in student_heights:
  #number_of_students += 1
#print(number_of_students)

#number_of_coders = 0
#for coder in student_heights:
  #number_of_coders += 1
#print(number_of_coders)


#Exercise 2 - High Score
#Instructions
#You are going to write a program that calculates the highest score from a List of scores.
#e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
#Important you are not allowed to use the max or min functions. The output words must match the example. i.e
# highest score in the class is: x
#Example Input

#student_scores= [78, 65, 89, 86, 55, 91, 64, 89]

#highest_score = 0
#for score in student_scores:
  #if score > highest_score:
    #highest_score = score
#print(f"The highest score in the class is: {highest_score}")

# FOR LOOP AND RANGE FUNCTION

# Range b/w 1-10 will print number from 1-9
# Range b/w 1-11 will print number from 1-10
#for number in range (1,10):
  #print(number)

# Range stepping by numbers 1,11, 3
#for number in range (1,10, 3):
 # print(number)

#Exercise 3 - Adding Even Numbers
#Instructions
#You are going to write a program that calculates the sum of all the even numbers from 1 to 100. Thus, the first even number would be 2 and the last one is 100:

#i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100

#Important, there should only be 1 print statement in your console output. It should just print the final total and not every step of the calculation.

#Hint - There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.

#total = 0
#for numbers in range(2, 101, 2):
  #total += numbers
#print(total)

#Exercise 4 - FizzBuzz
#Instructions
#You are going to write a program that automatically prints the solution to the FizzBuzz game.
#Your program should print each number from 1 to 100 in turn.
#When the number is divisible by 3 then instead of printing the number it should print "Fizz".
#When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz

#for number in range(1,101):
  #if number % 3 == 0 and number % 5 ==0:
    #print("FizzBuzz")
  #elif number % 3 == 0:
   #print("Fizz")
  #elif number % 5 == 0:
    #print("Buzz")
  #else: 
    #print(number)


#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#password = ""

#for char in range(1, nr_letters + 1):
  #password += random.choice(letters)

#for char in range(1, nr_symbols + 1):
  #password += random.choice(symbols)

#for char in range(1, nr_numbers + 1):
  #password += random.choice(numbers)

#print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")