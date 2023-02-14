

# An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

# Example: (Input --> Output)

# "Dermatoglyphics" --> true
# "aba" --> false
# "moOse" --> false (ignore letter case)

#  test.assert_equals(is_isogram("Dermatoglyphics"), True )
#         test.assert_equals(is_isogram("isogram"), True )
#         test.assert_equals(is_isogram("aba"), False, "same chars may not be adjacent" )
#         test.assert_equals(is_isogram("moOse"), False, "same chars may not be same case" )
#         test.assert_equals(is_isogram("isIsogram"), False )
#         test.assert_equals(is_isogram(""), True, "an empty string is a valid isogram" )


# SET Method
# initializing list
from types import MethodDescriptorType


lis1 = [ 3, 4, 1, 4, 5 ]
 
# initializing tuple
# tup1 = (3, 4, 1, 4, 5)
 
# # Printing iterables before conversion
# print("The list before conversion is : " + str(lis1))
 
# print("The tuple after conversion is : " + str(set(tup1)))

# COUNT Method
# points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

# x = points.count(9)--------->2

def is_isogram(string):
    string = string.lower()
    letters = {letter: string.count(letter) for letter in string}
    if set(letters.values()) == {1} or set(letters.values()) == set():
        return True
    else:
        return False
     
print(is_isogram("isIsogram"))