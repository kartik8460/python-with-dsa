class Student:
    school = 'Seventh-Day Adventist Higher Secondary School'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1+self.m2+self.m3) / 3

    def get_m1(self):
        return self.m1

    def set_m1(self, m):
        self.m1 = m

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def info():
        print('This is a Student Class .. in abc module')


s1 = Student(50, 60, 40)
s2 = Student(50, 90, 20)

print(s1.avg())
print(s2.avg())

print(Student.getSchool())

s1.info()
