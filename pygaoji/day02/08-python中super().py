class Car(object):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def run(self):
        print("车在跑")

    def stop(self):
        print("车在停")


class ElectricCar(Car):

    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def run(self):
        print("电车在跑")

    def stop(self):
        print("电车在停")


tesla = ElectricCar("tesla", "model s", 100)
tesla.run()
print(tesla.brand)
print(tesla.model)
print(tesla.battery)