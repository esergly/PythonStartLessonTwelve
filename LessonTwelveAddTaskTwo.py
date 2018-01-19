# Первый способ чтения
with open("1.txt", "r") as one:
    one_contents = one.readlines()
# Второй способ чтения
two = open("2.txt", "r")
two_contents = two.readlines()
two.close()
result = []
line_one = one_contents[0].split(" ")
line_two = two_contents[0].split(" ")
for i in range(len(line_one)):
    for j in range(len(line_two)):
        if line_two[j] == line_one[i]:
            result.append(line_one[i])
with open("result.txt", "w") as result_file:
    for element in result:
        result_file.write(element+" ")


