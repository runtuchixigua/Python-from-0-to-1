class Sweetpotato(object):
    def __init__(self):
        self.cooked_time = 0
        self.cooked_state = '妈妈生的'
        self.condiments = []

    def cook(self, time):
        self.cooked_time += time
        if self.cooked_time < 3:
            self.cooked_state = '生的'
        elif self.cooked_time < 5:
            self.cooked_state = '半生不熟'
        elif self.cooked_time < 8:
            self.cooked_state = '熟了'
        else:
            self.cooked_state = '糊了老弟'

    def add_condiments(self, condiment):
        self.condiments.append(condiment)

    def __str__(self):
        return f'地瓜的状态是{self.cooked_state}, 添加的佐料有{self.condiments}'

    def __del__(self):
        print('地瓜被吃光了')

digua = Sweetpotato()
digua.cook(1)
digua.add_condiments('辣椒')
print(digua)

digua.cook(100)
digua.add_condiments('芥末')
print(digua)