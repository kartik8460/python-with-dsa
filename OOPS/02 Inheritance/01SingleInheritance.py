class PhoneOne:
    def feature1(self):
        print('Flagship Processor')

    def feature2(self):
        print('512 GB Storage')


class PhoneTwo(PhoneOne):
    def feature3(self):
        print('108 MP Camera')

    def feature4(self):
        print('AMOLED Screen')


print('*******************************')

print('Phone One')
p1 = PhoneOne()
p1.feature1()
p1.feature2()
# p1.feature3() # Error
# p1.feature4() # Error

print('*******************************')

print('Phone Two')
p2 = PhoneTwo()
p2.feature1()
p2.feature2()
p2.feature3()
p2.feature4()

print('*******************************')
