class Food(object):
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price

    def __str__(self):
        return f"食物名称:{self.name}，价格是{self.price}"

