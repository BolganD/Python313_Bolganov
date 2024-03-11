class Student:
    def __init__(self, name):
        self.name = name
        self.i = self.Infor()

    def show_infor(self):
        print(f'{self.name} => {self.i.m}, {self.i.p}, {self.i.me}')

    class Infor:
        def __init__(self):
            self.m = 'HP'
            self.p = 'i7'
            self.me = '16'


show_students = Student('Roman')
show_students.show_infor()
