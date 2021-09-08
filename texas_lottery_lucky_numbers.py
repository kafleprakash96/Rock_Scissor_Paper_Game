import random

class PowerMegaLottoCash5:
    def __init__(self):
        self.lower = 1
        self.upper = 75

    def getRandom(self):
        return random.randint(self.lower,self.upper)
    
    def randomNumber(self):
        self.a1=self.getRandom()
        self.a2=self.getRandom()
        self.a3=self.getRandom()
        self.a4=self.getRandom()
        self.a5=self.getRandom()
        self.a6=self.getRandom()

    def Powerball(self):
        self.randomNumber()
        print(f"The lucky numbers for Powerball this week are {self.a1},{self.a2},{self.a3},{self.a4},{self.a5} with powerplay {random.randint(1,26)}")


    def MegaMillion(self):
        self.upper = 75
        self.randomNumber()
        print(f"The lucky number for Megamillion this week are {self.a1},{self.a2},{self.a3},{self.a4},{self.a5} with megaplier {random.randint(1,24)}")
    
    def cashFive(self):
        self.upper = 35
        self.randomNumber()
        print(f"The lucky Cash5 number for this week are {self.a1},{self.a2},{self.a3},{self.a4},{self.a5}")
    
    def Lotto(self):
        self.upper = 54
        self.randomNumber()
        print(f"The lucky Lotto number for this week are {self.a1},{self.a2},{self.a3},{self.a4},{self.a5},{self.a6}")

class Daily4Pick3:
        def __init__(self):
            self.a7=random.randint(0,999)
            self.a8=random.randint(0,9999)

        def Pick3(self):
            if self.a7<=9:
                print(f"The lucky numbers for Pick3 this week is 00{self.a7} with fireball {random.randint(0,9)}")
            elif self.a7>=9 and self.a7<=99:
                print(f"The lucky numbers for Pick3 this week is 0{self.a7} fireball {random.randint(0,9)}")
            else:
                print(f"The lucky numbers for Pick3 this week is {self.a7} fireball {random.randint(0,9)}")
        
        def Daily4(self):
            if self.a8<10:
                print(f"The lucky number for Daily 4 this week is 000{self.a8} with fireball {random.randint(0,9)}")
            elif self.a8>10 and self.a8<100:
                print(f"The lucky number for Daily 4 this week is 00{self.a8} with fireball {random.randint(0,9)}")
            elif self.a8>10 and self.a8<100:
                print(f"The lucky number for Daily 4 this week is 0{self.a8} with fireball {random.randint(0,9)}")
            else:
                print(f"The lucky number for Daily 4 this week is {self.a8} with fireball {random.randint(0,9)}")


p1 = PowerMegaLottoCash5()
p2 = Daily4Pick3()

p2.Pick3()
p2.Daily4()
p1.Powerball()
p1.MegaMillion()
p1.cashFive()
p1.Lotto()
