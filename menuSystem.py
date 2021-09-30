import pygame

class StartMenu:
    def __init__(self, screen, font, text_colour, button_colour):
        self.screen = screen
        self.font = font
        self.text_colour = text_colour
        self.button_colour = button_colour
        self.click = False
        self.button_width = 150
        self.button_height = 75
        self.option = None
        self.buttons_xy = None
        self.button_objects = None
        self.button_command = ["Quit Game", "Start Game"]
        self.title = "Tic Tac Toe - by Frazer Mills"

    def setup(self):
        pygame.display.set_caption("{0}".format(self.title))
        self.screen.fill((0,0,0))
        
    def draw_text(self, text, x, y):
        textobj = self.font.render(text, 1, self.text_colour)
        textrect = textobj.get_rect()
        textrect.center = (x, y)
        self.screen.blit(textobj, textrect)

    def get_button_objects(self):
        self.buttons_xy = [
            ((self.screen.get_width() // 2) - (self.button_width // 2), (self.screen.get_width() // 2) - i)
            for i in range(-100, 100, 100)
        ]

        self.button_objects = {
            f"{0}".format(button {i}): pygame.Rect(self.buttons_xy[i][0], self.buttons_xy[i][1], self.button_width, self.button_height)
            for i, button in enumerate(self.buttons_xy)
        }

    def check_collisions(self):
        mousex, mousey = pygame.mouse.get_pos()
        
        if self.button_objects[f"button 0"].collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[0]
                
        elif self.button_objects["button 1"].collidepoint((mousex, mousey)):
            if self.click:
                self.option = self.button_command[1]
                
        
    def display_buttons(self):
        
        for i, button_object in enumerate(self.button_objects):
            pygame.draw.rect(self.screen, self.button_colour, self.button_objects[button_object])
        
        self.draw_text("{0}".format(self.title), self.screen.get_width() // 2, self.screen.get_height() // 4)
        self.draw_text("{0}".format(self.button_command[0]), self.buttons_xy[0][0] + 75, self.buttons_xy[0][1] + 35)
        self.draw_text("{0}".format(self.button_command[1]), self.buttons_xy[1][0] + 75, self.buttons_xy[1][1] + 35)

        pygame.display.update()

    def is_clicked(self):
        self.click = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                    
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == True:
                    self.click = True
