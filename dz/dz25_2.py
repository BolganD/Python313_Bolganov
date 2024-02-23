class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def name(self):
        return self.__name

    @property
    def old(self):
        return self.__old

    @name.setter
    def name(self, changing_name):
        if isinstance(changing_name, str):
            self.__name = changing_name
        else:
            print('Введите корректное имя')

    @old.setter
    def old(self, changing_old):
        if isinstance(changing_old, int):
            self.__old = changing_old
        else:
            print('Возраст задается только числами')

    @name.deleter
    def name(self):
        print('Удаление имени...')
        del self.__name

    @old.deleter
    def old(self):
        print('Удаление возраста...')
        del self.__old


person_1 = Person('Igor', 51)
print(person_1.__dict__)
print(person_1.name)
print(person_1.old)
person_1.name = 'Sergey'
print(person_1.name)
del person_1.old
print(person_1.__dict__)