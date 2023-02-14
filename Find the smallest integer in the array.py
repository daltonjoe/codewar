def find_smallest_int(arr):
    arr.sort()
    return arr[0]

print(find_smallest_int([0, 1-2**64, 2**64]))    