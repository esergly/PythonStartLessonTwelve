my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_list = open("111.txt", "a+") #имя файла такое, чтобы он оказался в начале директории
num_list.write(str(my_list))
num_list.close()