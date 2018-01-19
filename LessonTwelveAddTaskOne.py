from operator import itemgetter
with open("result.txt", "r+") as work_data:
    line = work_data.read().split('\n')
myString = ''.join(line)  # собираем список в строку, убирая служебные символы
myString = ''.join(myString.split())  # удаляем из строки пробелы
result = {}
my_list = list(myString)
# Используем метод из решения 3-ей задачи 8-ой лекции
for i in my_list:
    count = result.get(i)
    if count:
        result[i] = count + 1
    else:
        result[i] = 1
res = sorted(result.items(), key=itemgetter(1))
res.reverse()
print(res)
