file = open("111.txt", "r")
text = file.readlines()
file.close()
temp = text[0].split()
count = 0
result = []
char = list(temp[-1])
for i in range(len(char)):
    if char[-1] == "." or ":" or ";" or "!" or "?":
        char[-1] = ''
        if i > 0:
            char[0] = char[0] + char[i]
del temp[-1]
temp.append(char[0])
for element in temp:
    if len(element) == count:
        result.append(element)
    if len(element) > count:
        count = len(element)
        result.clear()
        result.append(element)
print(result)
