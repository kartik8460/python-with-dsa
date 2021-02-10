name = ("Navin", "Kiran", "Harsh", "Navin")
comps = ("Dell", "Apple", "MS")

print('******************************************************************')

zipped = dict(zip(name, comps))
print(zipped)

print('******************************************************************')

zipped = tuple(zip(name, comps))
print(zipped)

print('******************************************************************')

zipped = list(zip(name, comps))
print(zipped)

print('******************************************************************')

zipped = zip(name, comps)
print(zipped)

for (a, b) in zipped:
    print(a, ':', b)

print('******************************************************************')
