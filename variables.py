import pygame

night = False
flag = 0

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('My game')

#pygame.mixer.music.load(
#    'F:\програмирование\Python\курс\game\структурырование попытка номер 2\Sounds/3.mp3')
#pygame.mixer.music.set_volume(0.3)
#
#fall_sound = pygame.mixer.Sound(
#    'F:\програмирование\Python\курс\game\структурырование попытка номер 2\Sounds/Bdish.wav')
#click_sound = pygame.mixer.Sound(
#    'F:\програмирование\Python\курс\game\структурырование попытка номер 2\Sounds/button.wav')

icon = pygame.image.load('Bg/геймпад.png')
pygame.display.set_icon(icon)

cactus_img = [pygame.image.load('Objects/Cactus0.png'), pygame.image.load('Objects/Cactus1.png'),
              pygame.image.load('Objects/Cactus2.png')]
cactus_options = [69, 449, 37, 410, 40, 420]

cloud_img = [pygame.image.load('Objects/Cloud0.png'), 
            pygame.image.load('Objects/Cloud1.png')]

dino_img = [pygame.image.load('Dino/Dino0.png'), pygame.image.load('Dino/Dino1.png'),
            pygame.image.load('Dino/Dino2.png'),
            pygame.image.load('Dino/Dino3.png'), pygame.image.load('Dino/Dino4.png')]

img_counter = 0

scores = 0
max_scores = 0
max_abov = 0

a = 4
b = 2
time_check = 0
time_speed = 4

usr_width = 60
usr_height = 100
usr_x = display_width // 3
usr_y = display_height - usr_height - 100

cactus_width = 20
cactus_height = 70
cactus_x = display_width - 50
cactus_y = display_height - cactus_height - 100

clock = pygame.time.Clock()
make_jump = False
jump_count = 30