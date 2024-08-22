class Tool(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


t1 = Tool('斧子')
t2 = Tool('榔头')
print(Tool.get_count())
