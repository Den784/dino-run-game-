from variables import *

def print_text(message, x, y, font_color, font_type='Bg/txt.ttf',
               font_size=30):  # создание текста его размера и шрифта3

    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))