import pygame
from settings import *

class Grid:
    def __init__(self, screen, line_colour, x_img, o_img):
        
        self.screen = screen
        self.arr = [[None] * 3, [None] * 3, [None] * 3]

        self.player_x = x_img
        self.player_o = o_img

        self.col = None
        self.row = None

        self.line_colour = line_colour
        self.line_width = 7

        self.is_clicked = False
        self.reset = False
        
        
    def setup(self):
        self.screen.fill(colours["WHITE"])

        pygame.draw.line(self.screen, self.line_colour, (WIDTH / 3, 0),(WIDTH / 3, (HEIGHT - 100)), self.line_width)
        pygame.draw.line(self.screen, self.line_colour, (WIDTH / 3 * 2, 0), (WIDTH / 3 * 2, (HEIGHT - 100)), self.line_width)

        pygame.draw.line(self.screen, self.line_colour, (0, (HEIGHT - 100) / 3), (WIDTH, (HEIGHT - 100) / 3), self.line_width)
        pygame.draw.line(self.screen, self.line_colour, (0, (HEIGHT - 100) / 3 * 2), (WIDTH, (HEIGHT - 100) / 3 * 2), self.line_width)

    def check_draw(self):
        draw_flag = 0

        for i, row in enumerate(self.arr):
            if None not in row:
                draw_flag += 1

        if draw_flag == 3:
            game_settings["draw"] = True
        
        player = game_settings["player"]
        
        if game_settings["winner"] == None: 
            self.message = "{0}'s Turn".format(player.upper())
            
        else:
            if player == "x":
                self.message = "O Wins!"
            else:
                self.message = "X Wins"

            self.reset = True

        if game_settings["draw"]:
            self.message = "It's a draw!"
            self.reset = True


    def render_text(self):
        text = config["font"].render(self.message, 1, colours["WHITE"])
        self.screen.fill(colours["BLACK"], (0, 400, 500, 100))
        text_rect = text.get_rect(center=(WIDTH/2, 450))
        self.screen.blit(text, text_rect)
        pygame.display.update()
        

    def get_location_input(self):
        x, y = pygame.mouse.get_pos()

        if (x < WIDTH / 3):
            self.col = 1
        elif (x < WIDTH / 3 * 2):
            self.col = 2
        elif (x < WIDTH):
            self.col = 3
        else:
            self.col = None

        if (y < (HEIGHT - 100) / 3):
            self.row = 1
        elif (y < (HEIGHT - 100) / 3 * 2):
            self.row = 2
        elif y < (HEIGHT - 100):
            self.row = 3
        else:
            self.__row = None

        self.check_rules()

    def check_rules(self):
        if self.row and self.col and self.arr[self.row - 1][self.col - 1] is None:

            self.draw()

    def draw(self):
        if self.row == 1:
            x_pos = 30
        elif self.row == 2:
            x_pos = (WIDTH / 3) + 30
        elif self.row == 3:
            x_pos = (WIDTH / 3 * 2) + 30

        if self.col == 1:
            y_pos = 30
        elif self.col == 2:
            y_pos = ((HEIGHT - 100) / 3) + 30
        elif self.col == 3:
            y_pos = ((HEIGHT - 100) / 3 * 2) + 30

        if game_settings["player"] == "x":
            self.screen.blit(self.__player_x, (y_pos, x_pos))
            self.arr[self.row - 1][self.col - 1] = game_settings["player"]
            game_settings["player"] = "o"
        else:
            self.screen.blit(self.player_o, (y_pos, x_pos))
            self.arr[self.row - 1][self.col - 1] = game_settings["player"]
            game_settings["player"] = "x"

    def check_win(self):

        for row in range(0,3):

            if self.arr[row][0] == self.arr[row][1] == self.arr[row][2] and (self.arr[row][0] != None):
                pygame.draw.line(self.screen, colours["RED"], (0, (row + 1) * ((HEIGHT - 100) / 3 ) - ((HEIGHT - 100) / 6)),
                                 (WIDTH, (row + 1) * ((HEIGHT - 100) / 3) - ((HEIGHT - 100) / 6)), 4)

                game_settings["winner"] = self.arr[row][0]

        for i in range(0, 3):

            col = [self.arr[j][i] for j in range(0, 3)]

            if col[0] == col[1] == col[2] and col[0] != None:
                pygame.draw.line(self.screen, colours["RED"], ((i + 1) * WIDTH / 3 - WIDTH / 6, 0),
                                 ((i + 1) * WIDTH / 3 - WIDTH / 6, (HEIGHT - 100)), 4)

                game_settings["winner"] = self.arr[i][0]

        if self.arr[0][0] == self.arr[1][1] == self.arr[2][2] and self.arr[0][0] != None:
            pygame.draw.line(self.screen, colours["RED"], (50, 50), (350, 350), 4)
            game_settings["winner"] = self.arr[0][0]

        if self.arr[0][2] == self.arr[1][1] == self.arr[2][0] and self.arr[0][2] != None:
            pygame.draw.line(self.screen, colours["RED"], (50, 350), (350, 50), 4)
            game_settings["winner"] = self.arr[0][2]

    def check_reset(self):
        if self.reset_flag:
            self.reset = True
