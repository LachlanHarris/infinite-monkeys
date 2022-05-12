from logging import raiseExceptions
from tkinter import *
from tkinter import ttk
from tkinter.tix import *
from tkinter.tix import Balloon

import math

def incremental_cost_modifier(tier, player):
    player.incrementers_costs[tier] = math.floor(player.incrementers_base_costs[tier] * (1.5** player.incrementers[tier]))

def incremental_button_handler(event, tier, player):
    if player.dollars >= player.incrementers_costs[tier]:
        player.incrementers[tier] += 1
        player.dollars -= player.incrementers_costs[tier]
        incremental_cost_modifier(tier, player)

def incrementor_button_constructor(text_string, tier , tip_message, player):
    if tier > len(player.incrementers):
        raise IndexError('Tried to access a tier of incrementor that doesnt exist')

    button = ttk.Button(text = text_string , command = lambda : incremental_button_handler(None, tier, player) )
    button.bind("<Button-1>", lambda event: incremental_button_handler(event, tier, player))

    tip = Balloon(initwait =  10)
    tip.bind_widget(button, balloonmsg = tip_message)

    display = ttk.Label()

    #displays the description and button on the row equal to the tier + 4 (rows 1-3 are data and the +1 button)
    display.grid(column=1, row= (tier+4), padx= 15 )
    button.grid(column=2, row= (tier+4), pady= 5 )

    return button, tip, display


def draw_unlocked_buttons(player,buttons,displays):
    pass