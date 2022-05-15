def linear_search(sequince, element):
    for i in range(len(sequince)):
        if(sequince[i] == element):
            return i
    return -1

sequince = [-2, 0, 3, 5, 7, 8, 11, 18, 24]
#element = 5

try:
    element = int(input())
except:
    element = 5
    
print(linear_search(sequince, element))