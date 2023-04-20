# Name: Nicole Price
# email: pricenm@mail.uc.edu
# Assignment Title: Assignment 04
# Course: IS 4010
# Semester/Year: Spring 2023
# Brief Description: 
# Citations: 
# Anything else that's relevant: 

# create_fruit_list
# This is a module of functions we can call

def create_fruit_list(filename):
    '''
    Read a comma-delimited file and return a list built from the elements in the file
    :param fileName: The file to process
    :return The list that was read and processed
    '''   
    fruitFile = open(filename, "r") # The default directory here is the Src folder. 
    buffer = fruitFile.readline()
#   print(buffer)

#   Make a list out of the comma-delimited data
    fruits = buffer.split(",")
#   fruits is a list now but it's dirty
#   print(fruits)

#   We need to remove tabs and leading/trailing spaces
    fruit_list = []                             # Create an empty list
    for f in fruits:                            # What data type is f ?
        clean_fruit = f.strip()                 # Research strip()
#       print ("<" + clean_fruit + ">")         # Print with delimiters so we see if the string is cleaned up
        fruit_list.append(clean_fruit)
    
#   Now we have a clean list of fruits
#   print(fruit_list)
    return (fruit_list)