
class UserAccount():

    def __init__(self, username: str = 'User', email: str = '', passowrd: str = ''):
        self.username = username
        self.email = email
        self.__password = passowrd

    def set_password(self, new_password: str):
        self.__password = new_password

    def check_password(self, password):
        return self.__password == password

me = UserAccount(username ='Terrapod', email= 'n123@yandex.ru')

me.set_password('123456')

print(me.check_password('123456'))