# Title: 'main.py'
# Date: 2.8.21
# Python version: 3.9.5
# Author: Frazer Mills

import pygame
import time
import menuSystem
import grid
from settings import *

def menu_handler(menu_mode, screen, text_font, text_colour, button_colour):
    in_menu = True

    while in_menu:

        if menu_mode == "start":
            start_menu = menuSystem.StartMenu(screen, text_font, text_colour, button_colour)
            start_menu.setup()

            while start_menu.option == None:
                start_menu.get_button_objects()
                start_menu.check_collisions()
                start_menu.display_buttons()
                start_menu.is_clicked()

                if start_menu.option == "Start Game":
                    print("Start game")
                    in_menu = False
                    
                elif start_menu.option == "Button":
                    print("Button clicked")

                elif start_menu.option == "Quit Game":
                    pygame.quit()
                    quit()
            

def event_handler(game_grid):
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            game_grid.is_clicked = True
            game_grid.get_location_input()        

def image_setup():
    x_img_file = pygame.image.load("pics/X.png")
    o_img_file = pygame.image.load("pics/O.png")

    x_img = pygame.transform.scale(x_img_file, config["img_scale"])
    o_img = pygame.transform.scale(o_img_file, config["img_scale"])

    return x_img, o_img

def reset_game(game_grid):
    del game_grid

    game_settings["draw"] = False
    game_settings["winner"] = None
    game_settings["player"] = "x"
    
    time.sleep(3)

def main():
    pygame.init()

    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    text_font = pygame.font.SysFont("Arial", 20)
    x_img, o_img = image_setup()

    menu_handler(config["menu_mode"], screen, text_font, config["text_colour"], config["button_colour"])

    line_colour = colours["BLACK"]
    game_grid = grid.Grid(screen, line_colour, x_img, o_img)
    
    game_grid.setup()
    
    while not game_grid.reset:
        event_handler(game_grid)
        
        game_grid.check_draw()
        game_grid.render_text()

        game_grid.check_win()
        game_grid.check_draw()

        pygame.display.update()

    reset_game(game_grid)
    


if __name__ == "__main__":
    while True:
        main()
