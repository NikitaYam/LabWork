
def dog():
    return 'Гав-гав'

def cat():
    return 'Мяу-мяу'

def easy_num(n):
    if n != 1:
        flag = True
        for i in range(2, n // 2):
            if n % i == 0:
                flag = False
    else:
        flag = False
    return flag