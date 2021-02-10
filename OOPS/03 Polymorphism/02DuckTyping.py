class Pycharm:
    def execute(self):
        print('Compiling')
        print('Running')


class Vscode:
    def execute(self):
        print('Eslint Check')
        print('Prettier Check')
        print('Compiling')
        print('Running')


class Laptop:
    def code(self, ide):
        ide.execute()


lap1 = Laptop()
print('*********************************************')
py = Pycharm()
lap1.code(py)
print('*********************************************')
vs = Vscode()
lap1.code(vs)
print('*********************************************')
