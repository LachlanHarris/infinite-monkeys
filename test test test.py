
from tkinter import *
from tkinter import ttk
import math

WINDOW_SIZE = "720x480"
GAME_TITLE = "Infinite Monkeys"

class player:
    monkeys_amount = 0
    dollars = 0
    monkey_wage = 1
    modifier = 1
    name = ""
    letters = 130000 #number of letters in hamlet
    possible_key_strokes = 88 #number of keystrokes on a typewriter
    incrementers_base_costs = [10,50,100,250,500,1000,1500]
    incrementers_costs = [10,50,100,250,500,1000,1500]
    incrementers_increase_value = [1,5,10,25,50,100,150]
    incrementers = [0,0,0,0,0,0,0]

    def __init__(self,value,name):
        self.monkeys_amount = value
        self.name = name

def handle_click_first_incrementer(event):
    incremental_button_handler(0)

def handle_click_second_incrementer(event):
    incremental_button_handler(1)

def handle_click_third_incrementer(event):
    incremental_button_handler(2)

def handle_click_fourth_incrementer(event):
    incremental_button_handler(3)

def handle_click_fifth_incrementer(event):
    incremental_button_handler(4) 

def incremental_cost_modifier(tier):
    player1.incrementers_costs[tier] = math.floor(player1.incrementers_base_costs[tier] * (1.5** player1.incrementers[tier]))

def incremental_button_handler(tier):
    if player1.dollars >= player1.incrementers_costs[tier]:
        player1.incrementers[tier] += 1
        player1.dollars -= player1.incrementers_costs[tier]
        incremental_cost_modifier(tier)

def handle_click_button(event):
    player1.monkeys_amount += (1 * player1.modifier)

def compute_monkey_wage_addition():
    player1.dollars += player1.monkey_wage * player1.monkeys_amount
    game_window.after(1000, compute_monkey_wage_addition)

def compute_auto_per_increment():
    for i in range(len(player1.incrementers)):
        player1.monkeys_amount += (player1.incrementers[i] * player1.incrementers_increase_value[i])
    game_window.after(1000,compute_auto_per_increment)

def compute_monkey_odds():
    monkey_odds = str(player1.possible_key_strokes) + "^" +  str(player1.letters)
    return monkey_odds

#updates the gui
def game_tick():
    player_value.configure(text = "Monkeys currently typing: " + str(player1.monkeys_amount))
    monkey_odds_value.configure(text = "Current odds of typing Hamlet: " + compute_monkey_odds())
    #formats the money into comma seperated format eg. 1000 -> $1,000
    money.configure(text = "${:,}".format(player1.dollars))
    
    game_window.after(100, game_tick)
    

player1 = player(0 ,"test")

game_window = Tk()
game_window.geometry(WINDOW_SIZE)
game_window.title(GAME_TITLE)

player_value = ttk.Label()
player_value.grid(column=1, row=1, pady= 5)

monkey_odds_value = ttk.Label(text = "monkey odds: ")
monkey_odds_value.grid(column=2, row=1, padx= 15)

money = ttk.Label(text = "$")
money.grid(column=3, row=1, padx= 15)

main_button = ttk.Button(text = "Hire a new monkey")
main_button.bind("<Button-1>", handle_click_button)
main_button.grid(column=1, row= 2, pady= 5)

first_auto = ttk.Button(text = "Monkey advertisment")
first_auto.bind("<Button-1>", handle_click_first_incrementer)
first_auto.grid(column=1, row= 3, pady= 5)

second_auto = ttk.Button(text = "Monkey Recruiter")
second_auto.bind("<Button-1>", handle_click_second_incrementer)
second_auto.grid(column=1, row= 4, pady= 5)

third_auto = ttk.Button(text = "Monkey Marketing")
third_auto.bind("<Button-1>", handle_click_third_incrementer)
third_auto.grid(column=1, row= 5, pady= 5)

fourth_auto = ttk.Button(text = "Monkey peer recruitment")
fourth_auto.bind("<Button-1>", handle_click_fourth_incrementer)
fourth_auto.grid(column=1, row= 6, pady= 5)

game_window.after(100, game_tick)
game_window.after(1000, compute_monkey_wage_addition)
game_window.after(1000, compute_auto_per_increment)
game_window.mainloop()
