
class Car:
    def __init__(self, brand, model, color, engine, year):
        self.brand = brand
        self.model = model
        self.color = color
        self.engine = engine
        self.year = year
    
    def drive(self):
        print(self.brand, self.model, "is moving")

my_car = Car('BMW', 'M5', 'green', '2.0', 2001)
fav_teachers_car = Car('Nissan', 'Tiida', 'gold', '1.5', 2011)

