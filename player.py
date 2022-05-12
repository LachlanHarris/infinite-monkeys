class player:
    monkeys_amount = 0
    dollars = 0
    monkey_wage = 1
    modifier = 1
    name = ""
    DPS = 0
    MPS = 0
    letters = 130000 #number of letters in hamlet
    possible_key_strokes = 88 #number of keys on a typewriter
    incrementers_base_costs = [10,50,100,250,500,1000,1500]
    incrementers_costs = [10,50,100,250,500,1000,1500]
    incrementers_increase_value = [1,5,10,25,50,100,150]
    incrementers = [0,0,0,0,0,0,0]
    
    #not in use, could be used to gradually reveal purchase options
    incrementer_unlocked = [(True,200),(False,1000),(False,5000),(False,50000),(False,100000),(False,1000000),(False,10000000)]

    def __init__(self,value,name):
        self.monkeys_amount = value
        self.name = name

    def check_unlocks(self,tier):
        if self.incrementer_unlocked[tier][0] == True:
            return True
        elif self.incrementer_unlocked[tier][1] < self.monkeys_amount:
            self.incrementer_unlocked[tier][0] = True
        else:
            return False


