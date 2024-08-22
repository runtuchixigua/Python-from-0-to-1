class GasolineCar():
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def run_with_gasoline(self):
        print("正在以汽油形式行驶")


class ElectricCar():
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    def run_with_electricity(self):
        print("正在以电形式行驶")


class HybridCar(GasolineCar, ElectricCar):
    def __init__(self, brand, model, battery):
        GasolineCar.__init__(self, brand, model)
        ElectricCar.__init__(self, brand, model, battery)




byd = HybridCar("BYD", "e6", 100)
print(byd.brand)
print(byd.model)
print(byd.battery)
byd.run_with_gasoline()
byd.run_with_electricity()
print(HybridCar.__mro__)