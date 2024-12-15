
def fun(file = 'example'):
    for i in open(file, 'r', encoding="utf-8"):
        print(i)
try:
    fun()
except FileNotFoundError:
    print('Файла нет!')
