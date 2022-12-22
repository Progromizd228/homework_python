class InvalidBuilding(Exception):
    pass

class Building:
    def __init__(self, storey, height, width, name):
        self.storey = storey
        self.height = height
        self.width = width
        self.name = name
        if not self.is_valid():
            raise InvalidBuilding

    def show(self):
        return self.storey, self.height, self.width, self.name

    def is_valid(self):
        if self.storey > 0 and self.height > 0 and self.width > 0:
            return True
        
        if not all([isinstance(side, (float, int)) for side in self.show()]):
            return False

opt = input("Что вы хотите сделать?\n1. Прочитать данные из файла\n2. Записать данные в файл\n")
if int(opt) == 1:
    f = open("Building.txt", "r")
    print(f.read())
elif int(opt) == 2:
    x = input("Введите кол-во этажей: ")
    y = input("\nВведите высоту здания: ")
    z = input("\nВведите ширину здания: ")
    n = input("\nВведите название здания: ")
    try:
        if all(isinstance(vars, (float, int)) for vars in [int(x), int(y), int(z)]):
            building = Building(int(x), int(y), int(z), n)
            f = open("Building.txt", "a")
            f.write("Ваше здание:" + str(building.show()) + "\n")
    except ValueError:
        print('Нужно вводить число, зачтите задание пж')
else:
    raise Exception("Пожалуйста, выберите 1 или 2 вариант.\n")