
def is_uppercase(inp):
    list=[]
    
    for x in (str(inp)):
        list.append(x)
    

    index = 0
    while index < len(list):
        element = list[index]
        if element == element.lower():
            index += 1
            return True
        else:    
            return True       
        
        # BITMEDI


inp="hello I AM DONALD"
print(is_uppercase(inp))           

