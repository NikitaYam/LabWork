import math
import datetime

for i in range(1, 10):
    print(math.sqrt(i))

print('')
d = datetime.datetime.now()
print(f'time: {d.hour}:{d.minute}:{d.second}')
print(f'date: {d.day}.{d.month}.{d.year}')
