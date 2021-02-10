class Person:
    country = 'India' # class Variable

    def compare(self, obj):
        if self.age == obj.age:
            return True
        else:
            False


person1 = Person()
person2 = Person()

person1.name = 'Kartik' # instance/object variable
person2.name = 'Shubham'  # instance/object variable
person1.age = 22
person2.age = 22

print(person1.name)
print(person1.age)
print(person2.name)
print(person2.age)
print(person2.name)
print(person1.country)
print(person2.country)
Person.country = 'USA'
print(person1.country)
print(person2.country)

print(person1.compare(person2))
