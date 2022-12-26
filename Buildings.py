import csv

class InvalidBuilding(Exception):
    pass

class Building:
    def __init__(self, storey, height, width, name):
        self.storey = storey
        self.height = height
        self.width = width
        self.name = name

    def to_tuple(self):
        return self.storey, self.height, self.width, self.name

    @classmethod
    def from_tuple(cls, data):
        return cls(*data)

    def __str__(self):
        return f'Building: Storeys:{self.storey}, Height:{self.height}, Width:{self.width}, Name:{self.name}'

opt = input("Что вы хотите сделать?\n1. Прочитать данные из файла\n2. Записать данные в файл\n")
if opt == '1':
    with open('Building.csv', 'rt') as f:
        csv_reader = csv.reader(f)
        buildings_csv = [Building.from_tuple(row) for row in csv_reader]
        print('Кол-во домов: ', len(buildings_csv))
        for building in buildings_csv:
            print(building)
elif opt == '2':
    x = input("Введите кол-во этажей: ")
    y = input("\nВведите высоту здания: ")
    z = input("\nВведите ширину здания: ")
    n = input("\nВведите название здания: ")
    try:
        building = Building(int(x), int(y), int(z), n) # NOTE ЭТО ПЛОХО
    except ValueError:
        print('Вводите только числовые значения для кол-ва этажей, длины и ширины!')
    else:
        with open('Building.csv', 'a', newline='') as f: 
            if int(x) > 0 and int(y) > 0 and int(z) > 0:
                csv_writer = csv.writer(f)
                csv_writer.writerow([building.storey, building.height, building.width, building.name])
                print('Дом успешно создан!')
            else:
                print('Ошибка!!!!!!!!!!!!!!!!')
# else:
#     raise Exception("Пожалуйста, выберите 1 или 2 вариант.\n")
else:
    print('Пожалуйста, выберите 1 или 2 вариант.')
