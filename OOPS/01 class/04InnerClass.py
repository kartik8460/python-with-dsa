class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lp = self.Laptop()

    def show(self):
        print('Name : ', self.name)
        print('Rollno : ', self.rollno)

    class Laptop:
        def __init__(self):
            self.brand = 'HP'
            self.cpu = 'Ryzen 7'
            self.ram = '16 GB'

        def show(self):
            print('Brand : ', self.brand)
            print('CPU : ', self.cpu)
            print('RAM : ', self.ram)


print('********************************************')
s1 = Student('Kartik', 865)
s1.show()
print('********************************************')
lap1 = s1.Laptop()
lap1.show()
print('********************************************')
lap2 = Student.Laptop()
lap2.show()
print('********************************************')
s1.lp.show()
print('********************************************')
