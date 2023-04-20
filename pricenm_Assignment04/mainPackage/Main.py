# Name: Nicole Price
# email: pricenm@mail.uc.edu
# Assignment Title: Assignment 04
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: 
# Citations: Multiple SO references
# Anything else that's relevant: 

# main.py
# This is our entry point.

from functionPackage.create_fruit_list import create_fruit_list

myList = create_fruit_list("fruits.txt")
# add a fruit to the list
myList.append("pink lady apple")
print(myList)
# convert the list to a set call the set myFruitSet and print it
myFruitSet = set(myList) # the set is unordered
print(myFruitSet)
# write an if/else to compare the length of the set with the length of the list
# print a message either way ex: set is longer than list, etc.
if len(myFruitSet) <= len(myList):
    print("The set is longer than the list")
else:
    print("The list is longer than the set")
# second option to fulfill the above request
if len(myList) == len(myFruitSet):
    print("List and set are the same length")
else:
    print("List and set are not the same length")
# sort the list in alpha order ascending into a new list called mySortedList
mySortedList = sorted(myList)
print(mySortedList)
# use list comprehension to create a  new list from myList
# the fruits must be capitalized
myCapitalizedList = [n.title() for n in myList]
print(myCapitalizedList)
# example for line 38 of alternate myCapitalizedlist = [x.capitalize() for x in myList]
# use list comprehension to build a new list
# should have all the fruits that start with A
myAFruits = [i for i in myList if i[0].lower() == 'a']
print(myAFruits)
# example for line 43 myAFruits = [fruit for fruit in myList if fruit.startswith("a")]
# write a for loop that iterates 5 iterations
# print should be inside the loop, print one random fruit from list
import random
for i in range(0,5):
    print(random.choice(myList))
