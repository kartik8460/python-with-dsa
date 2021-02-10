class A:
    def __init__(self):
        print('Class A Init')

    def method1(self):
        print('Method 1 from class - A')


class B:
    def __init__(self):
        super().__init__()
        print('Class B Init')

    def method1(self):
        print('Method 1 from class - B')


class C(A, B):
    def __init__(self):
        super().__init__()  # A is given the preference as it is Inherited first(before B)
        print('Class C init')

    def callMethod(self):
        super().method1()


c = C()
c.callMethod()
