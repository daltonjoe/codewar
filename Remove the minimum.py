def remove_smallest(numbers):
    index=numbers.index(min(numbers,default=0))
    numbers.pop(index)
    return numbers
print(remove_smallest([1, 2, 3, 1, 1]))