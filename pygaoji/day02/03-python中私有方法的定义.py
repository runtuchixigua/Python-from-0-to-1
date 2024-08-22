class ATM(object):
    def __card(self):
        print('请输入卡号')
    def __password(self):
        print('请输入密码')

    def __authrize(self):
        print('验证成功')


    def __input(self):
        print('请输入金额')
    
    def withdraw(self):
        self.__card()
        self.__password()
        self.__authrize()
        self.__input()

atm = ATM()
atm.withdraw()
