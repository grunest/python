""" This module does nothing really """
def add_it_up(x, y):
    """ Adds two numbers """
    return int(x) + int(y)

one_number = input("Enter a number: ")
second_number = input("Enter another number: ")
print ("The sume of the two numbers is: " + str(add_it_up(int(one_number), int(second_number))))
print ("This is another change")
