from variables import *
from cobjects import *
from buttons import *
from efects import *
import random
import time

def current_milli_time():  # ускорение
    return round(time.time() * 1000)

def game_menu():  # создание игрового меню с кнопками
    global scores
    scores = 0
    menu_background = pygame.image.load('Bg/MenuBg.jpg')
    start_btn = Button(288, 70)
    quit_btn = Button(100, 70)
    #play_music_btn = Button(288, 70)
    #stop_music_btn = Button(288, 70)
    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.blit(menu_background, (0, 0))
        print_text('Dino Run Game', 230, 50, font_color=(0, 0, 0), font_size=50)
        start_btn.draw_button(270, 200, 'Start game', start_game, 45)
        # 1111 play_music_btn.draw_button(270, 300, 'Play music', play_music, 45)
        # 1111 stop_music_btn.draw_button(270, 400, 'Stop music', stop_music, 45)
        #   play_music_btn.draw_button(270, 300, 'Play music', 45)
        #   stop_music_btn.draw_button(270, 400, 'Stop music', 45)
        quit_btn.draw_button(350, 300, 'Quit', quit, 40)
        #   quit_btn.draw_button(358,300,'Quit',quit,50)
        #   play_music_btn.draw_button(270,400,'Play music',play_music,50)
        #   stop_music_btn.draw_button(270,500,'Stop music',stop_music,50)
        pygame.display.update()
        clock.tick(60)

def start_game():  # запуск игры из игрового меню (функция кнопки 'Start game')
    global scores, time_speed, make_jump, jump_count, usr_y

    while game_cycle():  # цикл для запуска игры
        scores = 0
        time_speed = 4
        make_jump = False
        jump_count = 30
        usr_y = display_height - usr_height - 95


#def stop_music():
#    pygame.mixer.music.pause()
#
#def play_music():
#    pygame.mixer.music.unpause()
#    pygame.mixer.music.load(str(random.randrange(1, 5)) + '.mp3')
#    pygame.mixer.music.set_volume(0.6)
#    pygame.mixer.music.play(1)


def game_cycle():  # игровой цикл (запуск игры)
    global make_jump, time_speed, night, flag, array
    #pygame.mixer.music.play(-1)

    if night == True and flag == 255:
        night == False
        flag = 0
        print(night,flag)
        print(night, flag)

    game = True
    cactus_arr = []
    create_cactus_arr(cactus_arr)

    land = pygame.image.load('Bg/land.jpg')
    cloud = open_random_objects()

    #    need_input = False
    #    input_text = ''

    while game:

        time_check = current_milli_time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            '''
            if need_input and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    need_input = False
                    input_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    pass
                else:
                    input_text += event.unicode   
            '''

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            make_jump = True

        if keys[pygame.K_ESCAPE]:
            pause()

        if keys[pygame.K_TAB]:
            #pygame.mixer.music.stop()
            game_menu()

        if make_jump:
            jump()

            #     print(len(cactus_arr))

        count_scores(cactus_arr)

        if scores % 11 == 0 and scores != 0 and not night:
            land = pygame.image.load('Bg/Land2.jpg')
            flag = 255
            night = True
            print(night, flag)
            
        elif scores % 24 == 0 and scores != 0 and night and night:
            land = pygame.image.load('Bg/land.jpg')
            flag = 0
            night = False
            print(night, flag)

        display.blit(land, (0, 0))
        print_text('Scores: ' + str(scores),
                    600, 10, font_color=(flag, flag, flag))
        print_text('Press TAB to exit menu ',
                    550, 40, font_color=(flag, flag, flag), font_size=20)
        draw_array(cactus_arr)
        move_objects(cloud)
        draw_dino()

        if check_collision(cactus_arr):
            #pygame.mixer.music.stop()
            #pygame.mixer.Sound.play(fall_sound)
            game = False

        if current_milli_time() - time_check > 0:
            time_speed += 0.0001

        #       print_text(input_text, 500, 400)

        pygame.display.update()
        clock.tick(75)
    return game_over()


def jump():  # прыжок
    global usr_y, make_jump, jump_count, dino_img
    if jump_count >= -30:
        if jump_count == -30:
            pass
    #        pygame.mixer.Sound.play(fall_sound)

        usr_y -= jump_count / 2.5
        jump_count -= 1
    #   dino_img=[0]
    else:
        jump_count = 30
        make_jump = False


def create_cactus_arr(array):  # отрисовка модели кактуса
    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Object(display_width + 20, height, width, img, a))

    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Object(display_width + 300, height, width, img, a))

    choice = random.randrange(0, 3)
    img = cactus_img[choice]
    width = cactus_options[choice * 2]
    height = cactus_options[choice * 2 + 1]
    array.append(Object(display_width + 600, height, width, img, a))


def find_radius(array):  # красиво спавнит кактусы
    maximum = max(array[0].x, array[1].x, array[2].x)

    if maximum < display_width:
        radius = display_width
        if radius - maximum < 50:
            radius += 280
    else:
        radius = maximum

    choice = random.randrange(0, 5)
    if choice == 0:
        radius += random.randrange(10, 15)
    else:
        radius += random.randrange(250, 400)
    return radius


def draw_array(array):  # создание кактусов
    for cactus in array:
        check = cactus.move()
        if not check:
            radius = find_radius(array)

            choice = random.randrange(0, 3)
            img = cactus_img[choice]
            width = cactus_options[choice * 2]
            height = cactus_options[choice * 2 + 1]

            cactus.return_self(radius, height, width, img)


def open_random_objects():  # отрисовка камней и облаков

    choice = random.randrange(0, 2)
    img_of_clud = cloud_img[choice]
    cloud = Object(display_width, 100, 10, img_of_clud, b)

    return cloud


def move_objects(cloud):  # рандомное изображение камней и облаков

    check = cloud.move()
    if not check:
        choice = random.randrange(0, 2)
        img_of_cloud = cloud_img[choice]
        cloud.return_self(display_width, random.randrange(45, 180), cloud.width, img_of_cloud)


def draw_dino():  # рисует динозавра
    global img_counter

    if img_counter == 25:
        img_counter = 0

    if jump_count == 30:
        display.blit(dino_img[img_counter // 5], (usr_x, usr_y))
        img_counter += 1

    elif jump_count >= -30:
        display.blit(dino_img[0], (usr_x, usr_y))

def pause():  # пауза
    global flag
    paused = True

    pygame.mixer.music.pause()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text('Paused, press RETURN to continue', 120, 280, font_color=(flag, flag, flag))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()
        clock.tick(15)
    pygame.mixer.music.unpause()


def check_collision(barriers):  # физика кактусов
    for barrier in barriers:
        if barrier.y == 449:
            if not make_jump:
                if barrier.x <= usr_x + usr_width - 22 <= barrier.x + barrier.width:
                    return True
            elif jump_count >= 0:
                if usr_y + usr_height - 5 >= barrier.y:
                    if barrier.x <= usr_x + usr_width - 22 <= barrier.x + barrier.width:
                        return True
            else:
                if usr_y + usr_height - 10 >= barrier.y:
                    if barrier.x <= usr_x <= barrier.x + barrier.width:
                        return True
        else:
            if not make_jump:
                if barrier.x <= usr_x + usr_width + 5 <= barrier.x + barrier.width:
                    return True
            elif jump_count == 10:
                if usr_y + usr_height - 5 >= barrier.y:
                    if barrier.x <= usr_x + usr_width - 5 <= barrier.x + barrier.width:
                        return True
            elif jump_count <= 1:
                if usr_y + usr_height - 2 >= barrier.y:
                    if barrier.x <= usr_x + 13 <= barrier.x + barrier.width:
                        return True
            elif jump_count >= 1:
                if usr_y + usr_height - 2 >= barrier.y:
                    if barrier.x <= usr_x + usr_width - 22 <= barrier.x + barrier.width:
                        return True
            else:
                if usr_y + usr_height - 3 >= barrier.y:
                    if barrier.x <= usr_x + usr_width + 5 <= barrier.x + barrier.width:
                        return True

    return False


def count_scores(barriers):  # счетчик очков
    global scores, max_abov

    above_cactus = 0

    if -20 <= jump_count <= 25:
        for barrier in barriers:
            if usr_y + usr_height - 5 <= barrier.y:
                if barrier.x <= usr_x <= barrier.x + barrier.width:
                    above_cactus += 1
                elif barrier.x <= usr_x + usr_width <= barrier.x + barrier.width:
                    above_cactus += 1
        max_abov = max(max_abov, above_cactus)
    else:
        if jump_count == -30:
            scores += max_abov
            max_abov = 0


def game_over():  # окончание игры если ударился об кактус
    global scores, max_scores
    if scores > max_scores:
        max_scores = scores

    stopped = True
    while stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text('Game Over, press RETURN to play again, ESC to exit', 25, 250, font_color=(flag, flag, flag),
                   font_size=27)
        print_text('Max scores:' + str(max_scores), 290, 320, font_color=(flag, flag, flag))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            return True

        if keys[pygame.K_ESCAPE]:
            return False

        pygame.display.update()
        clock.tick(15)