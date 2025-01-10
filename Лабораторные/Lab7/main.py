

class Employee():

    def __init__(self, name: str, id: str):
        self.name = name
        self.id = id

    def get_info(self):
        return [self.name, self.id]


class Manager(Employee):

    def __init__(self, name: str, id: str, department: str):
        self.dep = department
        Employee.__init__(self, name=name, id=id)

    def get_info(self):
        return super().get_info() + [self.dep]

    def manage_project(self):
        print(f'{self.name}: Проект в разработке...')


class Technician(Employee):

    def __init__(self, name: str, id: str, specialization: str):
        self.spec = specialization
        Employee.__init__(self, name=name, id=id)

    def perform_maintenance(self):
        print(f"{self.name}: Ведутся тех. обслуживания...")


class TechManager( Manager, Technician):

    def __init__(self, name: str, id: str, specialization: str, department:str):
        self.employee = []
        Technician.__init__(self, name = name, id = id, specialization=specialization)
        Manager.__init__(self, name=name, id = id, department= department)

    def get_info(self):
        return [self.name, self.id, self.spec, self.dep] 

    def add_employee(self, name:str, id:str):
        self.employee.append(Employee(name=name, id=id))

    def get_team_info(self):
        return self.employee

print('-'*100)

a = TechManager(name= 'Лёха', id="1284R762H9238DK-POP", specialization= 'Разработчик', department= 'Разработка')
a.add_employee(name='Роман', id='1234')
a.add_employee(name='Серёга', id='5678')
a.add_employee(name='Фердинант', id='9999')

b = a.get_info()
for i in b:
    print(i, end= '| ')
print('', end='\n')
a.manage_project()
a.perform_maintenance()
b = a.get_team_info()
print(f'Команда сотрудника {a.name}: ')
for i in b:
    print('   ',i.name, i.id)

print('-'*100)

l = Employee(name= 'Dimon', id = '1231')
d = Manager(name = 'Simon', id = '6543', department='Uborka')
s = Technician(name = 'Limon', id='7890', specialization='Uborshcick')

print(l.get_info())

print('-'*100)

print(d.get_info())
d.manage_project()

print('-'*100)

print(s.get_info())
s.perform_maintenance()
