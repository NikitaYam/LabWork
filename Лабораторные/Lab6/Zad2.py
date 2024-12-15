

class Vehicle():

    def __init__(self, make: str, model: str):
        self.make = make
        self.model = model

    def get_info(self):
        return  {'make':self.make, 'model':self.model}

class Car(Vehicle):

    def __init__(self, make: str, model: str, fuel_type: str):
        self.fuel_type = fuel_type
        super().__init__(make=make, model=model)

    def get_info(self):
        #return  {'make':self.make, 'model':self.model, 'fuel_type':self.fuel_type}
        a = super().get_info()
        a['fuel_type'] = self.fuel_type
        return a

v = Vehicle('BMW', 'T-1')
info = v.get_info()
print(f'Марка - {info['make']}; Модель - {info['model']}')

c = Car(make = 'BMW', model='T-1', fuel_type='Disell')
info = c.get_info()
print(f'Марка - {info['make']}; Модель - {info['model']}; Тип топлива - {info['fuel_type']}')


