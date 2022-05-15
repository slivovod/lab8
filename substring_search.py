def substring_search(text, pattern):
    i = -1
    j = 0
    while((j < len(pattern)) and i < (len(text) - len(pattern))):
        j = 0
        i += 1
        while(j < len(pattern) and pattern[j] == text[i + j]):
            j += 1
    if(j == len(pattern)):
        return i
    else:
        return -1

text = "It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout."
pattern = input()
if(len(pattern) < 1):
    pattern = "will"
print(substring_search(text, pattern))