from select import select


class Book():
    def __init__(self):
        self.name = 'Заводной Апельсин'
        self.author = 'Энтони Бёрджесс'
        self.year = '1962'

    def get_info(self):
        return {'name':self.name, 'author':self.author, 'year':self.year}

    # Здесь побаловался
    def set_info(self, a:str, b:str, c:int):
        self.name = a
        self.author = b
        self.year = c

a = Book()
book = a.get_info()
print(f'{book['name']} - {book['author']}| {book['year']} год')

# Здесь побаловался
print("")

a.set_info("Мечтают ли андроиды об электроовцах", 'Филип К. Дик', 1986)
book = a.get_info()
print(f'{book['name']} - {book['author']}| {book['year']} год')