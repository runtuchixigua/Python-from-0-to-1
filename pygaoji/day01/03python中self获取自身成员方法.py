class Car(object):
    """
    Car类表示汽车的模型。
    """

    def run(self):
        """
        run方法表示汽车的运行行为。
        """
        print("run")  # 输出"run"，模拟汽车运行的状态

    def work(self):
        """
        work方法表示汽车的工作行为，其中包含了调用run方法的行为。
        """
        self.run()  # 调用run方法，使汽车开始运行

bmw = Car()  # 创建一个Car类的实例，表示一辆宝马汽车
bmw.work()  # 调用实例的work方法，让这辆宝马汽车开始工作
