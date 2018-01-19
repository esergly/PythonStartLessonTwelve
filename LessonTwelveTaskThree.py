# Вариант 1
i = ''
while i != 'quit':
    notepad = open("111.txt", "a+")
    text = input('Введите текст для сохранения: \n')
    notepad.write(text)
    notepad.close()
    i = input('Желаете продолжить? Если да, нажмите Enter, если нет - наберите "quit": \n')

# Вариант 2
i = ''
text = []
while i != 'quit':
    text.append(input('Введите текст для сохранения: \n'))
    i = input('Желаете продолжить? Если да, нажмите Enter, если нет - наберите "quit": \n')
notepad = open("111.txt", "a+")
for j in range(len(text)):
    notepad.write(text[j])
    notepad.write('\n')
notepad.close()

