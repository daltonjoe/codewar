def divisible_by(numbers, divisor):
    list =[]
    for i in numbers:
        if i % divisor == 0:
            list.append(i)
        else:
            pass
    return list        







print(divisible_by([0,1,2,3,4,5,6,7,8,9,10], 2))