def sum_cubes(n):
    # your code here
    list=[]
    cubed=[]
    for i in range(n):
        list.append(i+1)

    for i in list:
        cubed.append(pow(i,3))
        
    return sum(cubed)
    

print(sum_cubes(3))