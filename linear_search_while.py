def linear_search(sequince, element):
    i = 0
    while(i < len(sequince) and sequince[i] != element):
        i += 1
    if(i == len(sequince)):
        return -1
    else:
        return sequince[i], i


sequince = [4, 8, 0, 23, 1, 6, 14, 83, 5, 11]

try:
    element = int(input())
except:
    element = 6

print(linear_search(sequince, element))