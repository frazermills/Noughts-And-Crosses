import pygame

pygame.init()

HEIGHT = 500
WIDTH = 400
size = (WIDTH, HEIGHT)

game_settings = {
    "draw": False,
    "winner": None,
    "player": "x"
}

colours = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "GREY": (105,105,105),
    "LIGHT_GREY": (211,211,211),
    "RED":(255, 0, 0),
    "GREEN": (0, 255, 0),
    "YELLOW": (255, 255, 0)
}

config = {
    "text_colour": colours["WHITE"],
    "button_colour": colours["RED"],
    "menu_mode": "start",
    "fps": 30,
    "winner": None,
    "line_colour": colours["RED"],
    "img_scale": (80, 80),
    "font": pygame.font.Font(None, 30)
    
}
