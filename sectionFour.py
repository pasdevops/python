# RANDOMISATION
# Random is a python module with lots of functions
# Codes can be splitted into different modules for differebt functions


#import random

#Random integer
#random_integer = random.randint(1,10)
#print(random_integer)

# Random float
# random_float = random.random()
# print(random_float)

# Expanding random numbers 
# random_float * 5
# print(random_float)

# love_score = random.randint(1,100)
# print(f"Your love score is {love_score}")



# Exercise 1 - Heads or Tails
# Instructions
# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
#There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.
# e.g. 1 means Heads 0 means Tails

#import random

#random_side = random.randint(0,1)
#if random_side == 1:
  #print("Heads")
#else:
  #print("Tails")

# LIST DATA STRUCTURE

#POSITIVE INDEXING
#state_of_america = ["Delaware","Penslvania","Illionis"]
#print(state_of_america[0])

#NEGATIVE INDEXING
#state_of_america = ["Delaware","Penslvania","Illionis"]
#print(state_of_america[-2])

#CHANGE LIST IN CODE
#state_of_america[1] = "DELAWEARE"
#print(state_of_america)

#ADDING FUNCTION TO LIST - append
#states_of_america = "Pencilvenia"
#states_of_america.append("Londoner")
#print(states_of_america)

#ADDING FUNCTION TO LIST - extend 
#states_of_america = "Pencilvenia"
#states_of_america.extend("Londoner")
#print(states_of_america)


#Exercise 2 - Banker Roulette
#Instructions
#You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

#Important: You are not allowed to use the choice() function.

#Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name

#names_string = input("Give me everybody's names, separated by a comma.")
#names = names_string.split(",")


#num_items = len(names)

#random_choice = random.randint(0, num_items -1)
#person_who_will_pay = names[choice_name]
#print(person_who_will_pay + "is going to buy the meal today.")

# INDEX ERROR

# Index error is of going beyond range. 

#states_of_america = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "illinois"]
#print(len(states_of_america[14]))

# NESTED LIST - List within a list

#dirty_dozen = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "illinois"]
#print(len(dirty_dozen))

#fruits = ["Celery", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware"]
#vegetables = ["Spinach", "Georgia", "Hawaii", "Idaho", "illinois"]

#dirty_dozen = [fruits, vegetables]
#print(dirty_dozen)