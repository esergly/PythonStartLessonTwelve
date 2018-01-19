file = open("111.txt", "r")
text = str(file.readlines())
count = 0
for i in range(len(text)):
    if text[i] == "а":
        count += 1
print('В тексте буква "a" встречается ' + str(count) + ' раз.')
file.close()
