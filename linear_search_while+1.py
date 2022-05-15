def linear_search(sequince, element):
    i = 0
    sequince.append(element)
    while(sequince[i] != element):
        i += 1
    if(i == (len(sequince) - 1)):
        return -1
    else:
        return i


sequince = [4, 8, 0, 23, 7, 1, 6, 14, 83, 5, 11, 2, 3]

try:
    element = int(input())
except:
    element = 7

print(linear_search(sequince, element))