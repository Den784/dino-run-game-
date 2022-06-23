from variables import *
from efects import *

class Button:  # класс кнопок
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactiv_color = ('#DF64BD')
        self.activ_color = ('#DF38B1')

    def draw_button(self, x, y, message, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(display, self.activ_color, (x, y, self.width, self.height))

            if click[0] == 1:
                #pygame.mixer.Sound.play(click_sound)
                pygame.time.delay(300)
                if action == quit:
                    pygame.quit()
                    quit()
                else:
                    action()

        else:
            pygame.draw.rect(display, self.inactiv_color, (x, y, self.width, self.height))

        print_text(message=message, x=x + 10, y=y + 10, font_color=(0, 0, 0), font_size=font_size)