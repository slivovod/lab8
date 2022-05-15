def binary_search(sequince, element):
    sequince.sort()
    low = 0
    high = len(sequince) - 1
    mid = (low + high) // 2
    while(element != sequince[mid] and low < high):
        if(element > sequince[mid]):
            low = mid + 1
        else: # that mean what elif(element < sequince[mid]):
            high = mid - 1
        mid = (low + high) // 2
    if(sequince[mid] == element):
        return mid
    else:
        return -1

sequince = [4, 64, 8, 0, 23, 7, 1, 74, 20, 18,  6, 15, 83, 5, 11, 2, 3, 14, 55]

try:
    element = int(input())
except:
    element = 8

sequince.sort()
print(sequince)
print(binary_search(sequince, element))