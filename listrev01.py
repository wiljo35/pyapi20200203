#!/usr/bin/python3

def main():
    anotheremptylist = []

    ## this will throw an ERROR
    ## the extend method expects exactly one argument
    anotheremptylist.extend('10.0.0.1', 'retro_game_server')

    print(anotheremptylist)

    if__name__ == "__main__":
