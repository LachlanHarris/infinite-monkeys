
from tkinter import *
from tkinter import ttk
from tkinter.tix import *
from tkinter.tix import Balloon

import math
import player
import GUI


WINDOW_SIZE = "720x480"
GAME_TITLE = "Infinite Monkeys"

def handle_click_button(event):
    player1.monkeys_amount += (1 * player1.modifier)

#computes DPS and adds DPS to monkeys
def compute_monkey_wage_addition():
    DPS = player1.monkey_wage * player1.monkeys_amount
    player1.dollars += DPS
    player1.DPS = DPS
    game_window.after(1000, compute_monkey_wage_addition)

#computes MPS and adds MPS to monkeys
def compute_auto_per_increment():
    MPS = 0
    for i in range(len(player1.incrementers)):
        MPS += (player1.incrementers[i] * player1.incrementers_increase_value[i])
    player1.monkeys_amount += MPS
    player1.MPS = MPS
    game_window.after(1000,compute_auto_per_increment)

def compute_monkey_odds():
    monkey_odds = str(player1.possible_key_strokes) + "^" +  str(player1.letters)
    return monkey_odds

#updates the gui
def GUI_update_tick():
    current_monkeys_display.configure(text = "Monkeys currently typing: " + str(player1.monkeys_amount))
    monkey_odds_value.configure(text = "Current odds of typing Hamlet: " + compute_monkey_odds() + "    roughly equivilant to " +  " NOT IMPLEMENTED ")

    #formats the money into comma seperated format eg. 1000 -> $1,000
    money.configure(text = "${:,}".format(player1.dollars))

    #these update slower since they are linked to the 1 second game tick in the functions that compute monkey and money per tick
    current_MPS_display.configure(text = "Monkeys per second: " + str(player1.MPS))
    current_DPS_display.configure(text = "Dollars per second: " + "${:,}".format(player1.DPS))

    #updates costs for incrementers
    first_auto_cost_display.configure(text = "${:,}".format(player1.incrementers_costs[0]) + "  you own: " + str(player1.incrementers[0]))
    second_auto_cost_display.configure(text = "${:,}".format(player1.incrementers_costs[1]) + "  you own: " + str(player1.incrementers[1]))
    third_auto_cost_display.configure(text = "${:,}".format(player1.incrementers_costs[2]) + "  you own: " + str(player1.incrementers[2]))
    fourth_auto_cost_display.configure(text = "${:,}".format(player1.incrementers_costs[3]) + "  you own: " + str(player1.incrementers[3]))
    fifth_auto_cost_display.configure(text = "${:,}".format(player1.incrementers_costs[4]) + "  you own: " + str(player1.incrementers[4]))
    sixth_auto_cost_display.configure(text = "${:,}".format(player1.incrementers_costs[5]) + "  you own: " + str(player1.incrementers[5]))
    
    game_window.after(100, GUI_update_tick)
    

player1 = player.player(0 ,"test")

game_window = Tk()
game_window.geometry(WINDOW_SIZE)
game_window.title(GAME_TITLE)

#rows 1 and 2
#display information
current_monkeys_display = ttk.Label()
current_monkeys_display.grid(column=2, row=1, pady= 5)

current_MPS_display = ttk.Label()
current_MPS_display.grid(column=2, row=2 , pady = 5)

monkey_odds_value = ttk.Label(text = "monkey odds: ")
monkey_odds_value.grid(column=4, row=1, padx= 15)

money = ttk.Label(text = "$")
money.grid(column=3, row=1, padx= 15)

current_DPS_display = ttk.Label()
current_DPS_display.grid(column=3, row=2 , pady= 15)




buy_monkey_button = ttk.Button(text = "Hire a new monkey")
buy_monkey_button.bind("<Button-1>", handle_click_button)
buy_monkey_button.grid(column=2, row= 3, pady= 5)

buy_monkey_tip = Balloon(initwait = 10)
buy_monkey_tip.bind_widget(buy_monkey_button, balloonmsg = "click this button to increase monkey count by 1")

buttons = []
displays = []

first_auto_button , first_auto_tip, first_auto_cost_display = GUI.incrementor_button_constructor("Monkey Advertisment", 0 , "increases MPS (monkeys per second) by " + str(player1.incrementers_increase_value[0]), player1)
second_auto_button, second_auto_tip, second_auto_cost_display = GUI.incrementor_button_constructor("Monkey Recruiter", 1, "increases MPS (monkeys per second) by " + str(player1.incrementers_increase_value[1]), player1)
third_auto_button, third_auto_tip, third_auto_cost_display = GUI.incrementor_button_constructor("Monkey Marketing", 2, "increases MPS (monkeys per second) by " + str(player1.incrementers_increase_value[2]), player1)
fourth_auto_button, fourth_auto_tip, fourth_auto_cost_display = GUI.incrementor_button_constructor("Monkey Peer Recruitment", 3, "increases MPS (monkeys per second) by " + str(player1.incrementers_increase_value[3]), player1)
fifth_auto_button, fifth_auto_tip, fifth_auto_cost_display = GUI.incrementor_button_constructor("Monkey Managment", 4, "increases MPS (monkeys per second) by " + str(player1.incrementers_increase_value[4]), player1)
sixth_auto_button, sixth_auto_tip, sixth_auto_cost_display = GUI.incrementor_button_constructor("Monkey Mass Media", 5, "increases MPS (monkeys per second) by " + str(player1.incrementers_increase_value[5]), player1)

game_window.after(100, GUI_update_tick)
game_window.after(1000, compute_monkey_wage_addition)
game_window.after(1000, compute_auto_per_increment)
game_window.mainloop()
