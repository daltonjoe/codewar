
def is_uppercase(inp):
    list_inp=list(inp)
    

    for i in list_inp:
       
        if i.isalpha() == True:
        
            if i == i.lower():
                return False
            elif type(i)==type("!"):
                return True
            else:
                return True
        else:
            return True   


# import re
# def is_uppercase(inp):
#     if inp.upper() == inp:
#         return True
#     elif re.match('[a-z]',inp) != None:
#         return False
#     else:
#         return False


inp="!"
print(is_uppercase(inp))           

