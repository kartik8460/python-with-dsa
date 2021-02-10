class PhoneOne:
    def feature1(self):
        print('Flagship Processor')

    def feature2(self):
        print('512 GB Storage')


class PhoneTwo(PhoneOne):
    def feature3(self):
        print('Fast Charging')

    def feature4(self):
        print('5G')


class PhoneThree(PhoneTwo):
    def feature5(self):
        print('108 MP Camera')

    def feature6(self):
        print('AMOLED Screen')


print('*******************************')
print('Phone One')
print('*******************************')
p1 = PhoneOne()
p1.feature1()
p1.feature2()
# p1.feature3() # Error
# p1.feature4() # Error

print('*******************************')
print('Phone Two')
print('*******************************')
p2 = PhoneTwo()
p2.feature1()
p2.feature2()
p2.feature3()
p2.feature4()

print('*******************************')
print('Phone Three')
print('*******************************')
p3 = PhoneThree()
p3.feature1()
p3.feature2()
p3.feature3()
p3.feature4()
p3.feature5()
p3.feature6()
print('*******************************')
