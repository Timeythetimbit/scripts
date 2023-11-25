"""
U3S4E1CustomLibary
By Timbo
Done By Oct 24
"""
import colorama

def healthbar():
    hp = int(input("What is your HP?\n"))
    maxhp = int(input("What is your max HP?\n"))
    totalhp = maxhp - hp
    print("|" + colorama.Back.GREEN + hp * " " + colorama.Back.RESET + totalhp * "-" + "|")
    print(hp, "/", maxhp)
healthbar()