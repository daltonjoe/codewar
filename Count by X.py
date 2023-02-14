
# Create a function with two arguments that will return an array of the first (n) multiples of (x).
# Assume both the given number and the number of times to count will be positive numbers greater than 0.
# Return the results as an array (or list in Python, Haskell or Elixir).
# Examples:
# count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
# count_by(2,5) #should return [2,4,6,8,10]


def count_by(x, n):
    list=[]
    while x+1 <= n+1:
        for i in range(n):
            a=(i+1)*x
            list.append(a)
        return list

    while x > n:
        for i in range(n):
            a=(i+1)*(x)
            list.append(a)
        return list    

    for i in range(n):
        list.append(x*(i+x))
    return list
        



print(count_by(8,14))