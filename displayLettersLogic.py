import pygame
from button import Button

def prepare_buttons():
    
    return button_arr

displayed_letter = []

def update_player_picks(character, button_arr, screen):
    displayed_letter.append(button_arr[ord(character) - 64])
    startx = 0
    for letter in displayed_letter:
        letter.setLocation(startx, 0)
        letter.draw(screen)
        startx += letter.getImage().get_width()
    