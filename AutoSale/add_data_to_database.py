import csv
import sqlite3


class DataBase:
    def __init__(self, db_path: str):
        """
        Подключиться к базе данных и создать таблицы
        :param db_path: нужен для подключения к базе данных
        """
        self.base = sqlite3.connect(db_path)
        self.cur = self.base.cursor()
        if self.base:
            print('Database connected OK!')

    def add_new_brand_and_model(self, brand: str, model):
        self.cur.execute('INSERT OR IGNORE INTO cars_model_and_brand_cars(brand, model) VALUES(?, ?)', (model, brand,))
        self.base.commit()

    def add_new_brand(self, brand: str):
        self.cur.execute('INSERT OR IGNORE INTO cars_brands_cars(brand) VALUES(?)', (brand,))
        self.base.commit()



db = DataBase('db.sqlite3')

csv_file_name = 'cars.csv'

with open(csv_file_name, 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for car in spamreader:
        brand = car[0]
        model = car[1]

        db.add_new_brand_and_model(brand=brand, model=model)


with open(csv_file_name, 'r') as csvfile:
    arr = []
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for car in spamreader:
        if car[0] in arr:
            pass
        else:
            arr.append(car[0])
            db.add_new_brand(brand=car[0])

