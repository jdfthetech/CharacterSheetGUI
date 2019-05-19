import os

class character(object):
    character = ""

    def __init__(self):
        self.character = "Character Name"

    def print_character(self):
        print(self.character)

obj = character()
char1 = character()
char2 = character()


obj.print_character()

char1.print_character()

