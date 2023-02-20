def find_uniq(arr):
    for i in arr:
 
        if arr[int(i)]==arr[int(i+1)]:
            
            # print(arr[int(i+1)])
            pass
        else:
            return arr[int(i+1)]

print(find_uniq([ 1, 1, 1, 2, 1, 1 ]))