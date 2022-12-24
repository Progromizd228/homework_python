import csv

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

opt = input("Что вы хотите сделать?\n1. Прочитать данные из файла\n2. Записать данные в файл\n")
if int(opt) == 1:
    with open('Building', 'rt') as f:
        csv_reader = csv.reader(f)
        for line in csv_reader:
            print('Name: {0}\nStoreys: {1}\nHeight: {2}\nWidth: {3}\n'.format(line[3], line[0], line[1], line[2]))
elif int(opt) == 2:
    x = input("Введите кол-во этажей: ")
    y = input("\nВведите высоту здания: ")
    z = input("\nВведите ширину здания: ")
    n = input("\nВведите название здания: ")
    try:
        building = Building(int(x), int(y), int(z), n)
    except ValueError:
        print('Нужно вводить число, зачтите задание пж')
    else:
        with open("Building", "a") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow([building.storey, building.height, building.width, building.name])
else:
    raise Exception("Пожалуйста, выберите 1 или 2 вариант.\n")
