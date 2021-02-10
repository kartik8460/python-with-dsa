class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def info(self):
        return "{} {}".format(self.fname, self.lname)

    def superClassmethod(self):
        print('{} {}'.format(self.fname, self.lname))


class Student(Person):
    def __init__(self, fname, lname, schoolname, classname, rollno):
        super().__init__(fname, lname)
        # self.fname = fname
        # self.lname = lname
        self.schoolname = schoolname
        self.classname = classname
        self.rollno = rollno

    def info(self):
        return "{} {} {} {} {}".format(self.fname, self.lname, self.schoolname, self.classname, self.rollno)


p1 = Person('Mandeep', 'Saini')

s1 = Student('Kartik', 'Gupta', 'SDA', '12th', 15)

print('********************************************************')
p1.superClassmethod()
s1.superClassmethod()
print('********************************************************')
print(p1.info())
print(s1.info())
print('********************************************************')
