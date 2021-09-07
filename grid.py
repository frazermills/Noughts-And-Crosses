import pygame
from settings import *

class Grid:
    def __init__(self, screen, line_colour, x_img, o_img):
        
        self.__screen = screen
        self.__arr = [[None] * 3, [None] * 3, [None] * 3]

        self.__player_x = x_img
        self.__player_o = o_img

        self.__col = None
        self.__row = None

        self.__line_colour = line_colour
        self.__line_width = 7

        self.__is_clicked = False
        self.__reset = False

    @property
    def Is_clicked(self):
        return self.__is_clicked

    @Is_clicked.setter
    def Is_clicked(self, value):
        self.__is_clicked = value

    @property
    def Reset(self):
        return self.__reset

    @Reset.setter
    def Reset(self, value):
        self.__reset = value

    def setup(self):
        self.__screen.fill(colours["WHITE"])

        pygame.draw.line(self.__screen, self.__line_colour, (WIDTH / 3, 0),(WIDTH / 3, (HEIGHT - 100)), self.__line_width)
        pygame.draw.line(self.__screen, self.__line_colour, (WIDTH / 3 * 2, 0), (WIDTH / 3 * 2, (HEIGHT - 100)), self.__line_width)

        pygame.draw.line(self.__screen, self.__line_colour, (0, (HEIGHT - 100) / 3), (WIDTH, (HEIGHT - 100) / 3), self.__line_width)
        pygame.draw.line(self.__screen, self.__line_colour, (0, (HEIGHT - 100) / 3 * 2), (WIDTH, (HEIGHT - 100) / 3 * 2), self.__line_width)

    def check_draw(self):
        draw_flag = 0

        for i, row in enumerate(self.__arr):
            if None not in row:
                draw_flag += 1

        if draw_flag == 3:
            game_settings["draw"] = True
        
        player = game_settings["player"]
        
        if game_settings["winner"] == None: 
            self.__message = f"{player.upper()}'s Turn"
            
        else:
            if player == "x":
                self.__message = f"O Wins!"
            else:
                self.__message = f"X Wins"

            self.__reset = True

        if game_settings["draw"]:
            self.__message = "It's a draw!"
            self.__reset = True


    def render_text(self):
        text = config["font"].render(self.__message, 1, colours["WHITE"])
        self.__screen.fill(colours["BLACK"], (0, 400, 500, 100))
        text_rect = text.get_rect(center=(WIDTH/2, 450))
        self.__screen.blit(text, text_rect)
        pygame.display.update()
        

    def get_location_input(self):
        x, y = pygame.mouse.get_pos()

        if (x < WIDTH / 3):
            self.__col = 1
        elif (x < WIDTH / 3 * 2):
            self.__col = 2
        elif (x < WIDTH):
            self.__col = 3
        else:
            self.__col = None

        if (y < (HEIGHT - 100) / 3):
            self.__row = 1
        elif (y < (HEIGHT - 100) / 3 * 2):
            self.__row = 2
        elif y < (HEIGHT - 100):
            self.__row = 3
        else:
            self.__row = None

        self.check_rules()

    def check_rules(self):
        if self.__row and self.__col and self.__arr[self.__row - 1][self.__col - 1] is None:

            self.draw()

    def draw(self):
        if self.__row == 1:
            x_pos = 30
        elif self.__row == 2:
            x_pos = (WIDTH / 3) + 30
        elif self.__row == 3:
            x_pos = (WIDTH / 3 * 2) + 30

        if self.__col == 1:
            y_pos = 30
        elif self.__col == 2:
            y_pos = ((HEIGHT - 100) / 3) + 30
        elif self.__col == 3:
            y_pos = ((HEIGHT - 100) / 3 * 2) + 30

        if game_settings["player"] == "x":
            self.__screen.blit(self.__player_x, (y_pos, x_pos))
            self.__arr[self.__row - 1][self.__col - 1] = game_settings["player"]
            game_settings["player"] = "o"
        else:
            self.__screen.blit(self.__player_o, (y_pos, x_pos))
            self.__arr[self.__row - 1][self.__col - 1] = game_settings["player"]
            game_settings["player"] = "x"

    def check_win(self):

        for row in range(0,3):

            if self.__arr[row][0] == self.__arr[row][1] == self.__arr[row][2] and (self.__arr[row][0] != None):
                pygame.draw.line(self.__screen, colours["RED"], (0, (row + 1) * ((HEIGHT - 100) / 3 ) - ((HEIGHT - 100) / 6)),
                                 (WIDTH, (row + 1) * ((HEIGHT - 100) / 3) - ((HEIGHT - 100) / 6)), 4)

                game_settings["winner"] = self.__arr[row][0]

        for i in range(0, 3):

            col = [self.__arr[j][i] for j in range(0, 3)]

            if col[0] == col[1] == col[2] and col[0] != None:
                pygame.draw.line(self.__screen, colours["RED"], ((i + 1) * WIDTH / 3 - WIDTH / 6, 0),
                                 ((i + 1) * WIDTH / 3 - WIDTH / 6, (HEIGHT - 100)), 4)

                game_settings["winner"] = self.__arr[i][0]

        if self.__arr[0][0] == self.__arr[1][1] == self.__arr[2][2] and self.__arr[0][0] != None:
            pygame.draw.line(self.__screen, colours["RED"], (50, 50), (350, 350), 4)
            game_settings["winner"] = self.__arr[0][0]

        if self.__arr[0][2] == self.__arr[1][1] == self.__arr[2][0] and self.__arr[0][2] != None:
            pygame.draw.line(self.__screen, colours["RED"], (50, 350), (350, 50), 4)
            game_settings["winner"] = self.__arr[0][2]

    def check_reset(self):
        if self.__reset_flag:
            self.__reset = True
