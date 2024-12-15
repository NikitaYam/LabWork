import my_module as myd
from my_package import matemaica as m
from my_package import my_module as my

### Проверка модуля my_module
print(myd.dog())
print('')

print(myd.cat())
print('')

print(myd.easy_num(631))
print('')

### Проверка модулей пакета my_package
a = 1
b = 8

print('{} + {} ='.format(a,b), m.sum(a,b))
print('{} - {} ='.format(a,b),m.raz(a,b))
print('{} * {} ='.format(a,b),m.poizv(a,b))
print('{} / {} ='.format(a,b), m.delen(a,b))
print('')
print(my.cat())
