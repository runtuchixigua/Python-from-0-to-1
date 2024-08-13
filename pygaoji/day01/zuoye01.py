class Phone:
    def kaiji(self):
        print('kaiji')

    def guanji(self):
        print('guanji')

    def takephoto(self):
        print('takephoto')


class Computer():
    def coding(self):
        print('coding')

    def lookmedia(self):
        print('lookmedia')


computer = Computer()
computer.brand = 'huashuo'
computer.price = 1200
computer.coding()
computer.lookmedia()


class Engineer:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print('work')

    def __str__(self):
        return f"Name: {self.name}, Salary: {self.salary}"


eng = Engineer('tom', 20000)
print(eng)

