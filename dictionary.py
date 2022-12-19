#Dictionary in Python

#programming_dictionary = {
  #"Bug": "An error in a program that prevents the program from running as expected.", 
  #"Function": "A piece of code that you can easily call over and over again.",

#}
#Retrieveing items from dictionary.
#print(programming_dictionary["Bug"])


#Adding new items to dictionary
#programming_dictionary["Loop"] = "This is the start of the Python journey." 
#print(programming_dictionary)

#Create an empty dictionary
#empty_dictionary = {}

#Wipe an existing dictionary
#programming_dictionary ={}
#print(programming_dictionary)

#Edit an item in a dictionary
#programming_dictionary["Bug"] = "A month in your computer"
#print(programming_dictionary)

#loop through a dictionary
#for key in programming_dictionary:
  #print(key)
  #print(programming_dictionary[key])

#GRADING PROGRAME TASKS

#Instructions
#You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.

#Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.

#DO NOT modify lines 1-7 to change the existing student_scores dictionary.

#DO NOT write any print statements.

#This is the scoring criteria:

#Scores 91 - 100: Grade = "Outstanding"
#Scores 81 - 90: Grade = "Exceeds Expectations"
#Scores 71 - 80: Grade = "Acceptable"
#Scores 70 or lower: Grade = "Fail"

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
#Create an empty dictionary called student_grades.
#student_grades = {}

# Write your code below to add the grades 
#for student in student_scores:
  #print(student)

#Create an empty dictionary called student_grades.
student_grades = {}

# Write your code below to add the grades 
#for student in student_scores:
  #score = student_scores[student]
  #if score > 90:
    #student_grades[student] = "Outstanding"
  #elif score > 80:
    #student_grades[student] = "Exceed Expectation"
  #elif score > 70:
    #student_grades[student] = "Acceptable"
  #else:
    #student_grades[student] = "Fail"
  
  #print(student_grades)
  
# NESTING IN DICTIONARY

#Nesting
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a list in a Dictionary
travel_log = [
  {
"country": "France",
"Germany": ["Paris", "Lile", "Dijon"],
"total_visits": 12
},
{
 "country": "Germany",
 "cities_visited": ["Berlin", "Harmburg", "Stugart"],
 "total visit": 5
},
]


from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

bids = {}
bidding_finished = false


while not bidding_finished
  name = input("What is your name")
  price = input("What is your bid? $")
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
  if should_continue == "no:"
    bidding_finished = True
elif should_continue == "yes":
  clear()













