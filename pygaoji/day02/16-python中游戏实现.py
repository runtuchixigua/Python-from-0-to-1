class Game(object):
    """
    Game类代表一个游戏，玩家可以开始游戏、显示帮助和显示排名。
    """

    # 初始化游戏实例时设置玩家名称
    def __init__(self, name):
        self.player_name = name

    # 定义一个类变量来记录最高分数
    top_score = 0

    # 静态方法，用于显示游戏帮助信息
    @staticmethod
    def show_help():
        """
        显示游戏的帮助信息，包括游戏的基本操作和选项。
        """
        print(
            """
            1. 显示帮助
            2. 开始游戏
            3. 退出游戏
            """
        )

    # 类方法，用于显示当前的最高分数排名
    @classmethod
    def show_rank(cls):
        """
        显示当前游戏的最高分数排名。
        """
        print(cls.top_score)

    # 实例方法，用于开始游戏
    def start_game(self):
        """
        开始游戏，展示游戏规则，然后游戏结束。
        """
        print("开始游戏")
        print("游戏规则")
        print("游戏结束")

# 直接调用类方法显示当前最高分数排名
Game.show_rank()
