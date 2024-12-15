
open('user_file', 'a').write(input('Введите текст: ') + '\n')
for i in open('user_file', 'r'):
    print(i)