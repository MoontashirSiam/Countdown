import pygame
from pyvidplayer import Video
from button import Button
import lettersRound
import lettersDict

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

player_letters = []
player_answer = []

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Countdown")

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.set_volume(0.1)

countdown_clock = pygame.mixer.Sound("countdownclock.mp3")
countdown_clock.set_volume(0.06)

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

vid = Video("Intro1.mp4")
vid.set_size((800, 600))

def intro():
    run = True
    time_start = pygame.time.get_ticks()
    print(time_start)
    time_end = time_start + 32000
    while run:

        vid.draw(screen, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    vid.close()
                    main_menu()
        if(pygame.time.get_ticks() > time_end):
            vid.close()
            print(pygame.time.get_ticks())
            print(time_end)
            main_menu()
        
        pygame.display.update()

    pygame.quit()

def main_menu():
    scale = 0.4
    pygame.mixer.music.play(-1)
    start_img = pygame.image.load("images/button_start.png").convert_alpha()
    start_button = Button(SCREEN_WIDTH / 2 - start_img.get_width() * scale / 2, SCREEN_HEIGHT / 2 - start_img.get_height() * scale / 2 - 150, start_img, scale)
    
    run = True
    while run:

        screen.fill((25, 80, 160))
        if start_button.draw(screen):
            letters_round_one()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()

    pygame.quit()

consonant_img = pygame.image.load("images/button_consonant.png").convert_alpha()
consonant_button = Button(SCREEN_WIDTH / 2 - consonant_img.get_width() * 0.4 / 2, SCREEN_HEIGHT / 2 - consonant_img.get_height() * 0.4 / 2 + 75, consonant_img, 0.4, None)
vowel_img = pygame.image.load("images/button_vowel.png").convert_alpha()
vowel_button = Button(SCREEN_WIDTH / 2 - vowel_img.get_width() * 0.4 / 2, SCREEN_HEIGHT / 2 - vowel_img.get_height() * 0.4 / 2 + 175, vowel_img, 0.4, None)

a_img = pygame.image.load("images/button_a.png").convert_alpha()
b_img = pygame.image.load("images/button_b.png").convert_alpha()
c_img = pygame.image.load("images/button_c.png").convert_alpha()
d_img = pygame.image.load("images/button_d.png").convert_alpha()
e_img = pygame.image.load("images/button_e.png").convert_alpha()
f_img = pygame.image.load("images/button_f.png").convert_alpha()
g_img = pygame.image.load("images/button_g.png").convert_alpha()
h_img = pygame.image.load("images/button_h.png").convert_alpha()
i_img = pygame.image.load("images/button_i.png").convert_alpha()
j_img = pygame.image.load("images/button_j.png").convert_alpha()
k_img = pygame.image.load("images/button_k.png").convert_alpha()
l_img = pygame.image.load("images/button_l.png").convert_alpha()
m_img = pygame.image.load("images/button_m.png").convert_alpha()
n_img = pygame.image.load("images/button_n.png").convert_alpha()
o_img = pygame.image.load("images/button_o.png").convert_alpha()
p_img = pygame.image.load("images/button_p.png").convert_alpha()
q_img = pygame.image.load("images/button_q.png").convert_alpha()
r_img = pygame.image.load("images/button_r.png").convert_alpha()
s_img = pygame.image.load("images/button_s.png").convert_alpha()
t_img = pygame.image.load("images/button_t.png").convert_alpha()
u_img = pygame.image.load("images/button_u.png").convert_alpha()
v_img = pygame.image.load("images/button_v.png").convert_alpha()
w_img = pygame.image.load("images/button_w.png").convert_alpha()
x_img = pygame.image.load("images/button_x.png").convert_alpha()
y_img = pygame.image.load("images/button_y.png").convert_alpha()
z_img = pygame.image.load("images/button_z.png").convert_alpha()

letter_scale = 0.4
a_button = Button(0, 0, a_img, letter_scale)
b_button = Button(0, 0, b_img, letter_scale)
c_button = Button(0, 0, c_img, letter_scale)
d_button = Button(0, 0, d_img, letter_scale)
e_button = Button(0, 0, e_img, letter_scale)
f_button = Button(0, 0, f_img, letter_scale)
g_button = Button(0, 0, g_img, letter_scale)
h_button = Button(0, 0, h_img, letter_scale)
i_button = Button(0, 0, i_img, letter_scale)
j_button = Button(0, 0, j_img, letter_scale)
k_button = Button(0, 0, k_img, letter_scale)
l_button = Button(0, 0, l_img, letter_scale)
m_button = Button(0, 0, m_img, letter_scale)
n_button = Button(0, 0, n_img, letter_scale)
o_button = Button(0, 0, o_img, letter_scale)
p_button = Button(0, 0, p_img, letter_scale)
q_button = Button(0, 0, q_img, letter_scale)
r_button = Button(0, 0, r_img, letter_scale)
s_button = Button(0, 0, s_img, letter_scale)
t_button = Button(0, 0, t_img, letter_scale)
u_button = Button(0, 0, u_img, letter_scale)
v_button = Button(0, 0, v_img, letter_scale)
w_button = Button(0, 0, w_img, letter_scale)
x_button = Button(0, 0, x_img, letter_scale)
y_button = Button(0, 0, y_img, letter_scale)
z_button = Button(0, 0, z_img, letter_scale)

button_arr = [a_button, b_button, c_button, d_button, e_button, 
    f_button, g_button, h_button, i_button, j_button,
    k_button, l_button, m_button, n_button, o_button,
    p_button, q_button, r_button, s_button, t_button,
    u_button, v_button, w_button, x_button, y_button,
    z_button]

displayed_buttons = []
answer_buttons = [0 for i in range(9)]
answer_order = []

def letters_round_one():
    global player_letters
    run = True
    consonant_button.setAction(add_consonant)
    vowel_button.setAction(add_vowel)
    while run:
        screen.fill((25, 80, 160))
        consonant_button.draw(screen)       
        vowel_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        if(len(player_letters)):
            length = 0
            for letter in player_letters:
                length += button_arr[ord(letter) - 65].getImage().get_width()
            start_letters = SCREEN_WIDTH // 2 - length // 2
            for button in displayed_buttons:
                button.setLocation(start_letters, 100)
                button.draw(screen)
                start_letters += button.getImage().get_width()

        pygame.display.update()

    pygame.quit()

answers_start = 0

def letters_round_two():
    run = True
    global answers_start
    round_start = pygame.time.get_ticks()
    round_end = round_start + 31500
    length = 0
   
    for letter in player_letters:
        length += button_arr[ord(letter) - 65].getImage().get_width()
    start_letters = SCREEN_WIDTH // 2 - length // 2
    answers_start = start_letters
    for button in displayed_buttons:
        button.setLocation(start_letters, SCREEN_HEIGHT // 2 + 50)
        button.setOrigin(start_letters)
        start_letters += button.getImage().get_width()
    # button = displayed_buttons[0]
    # button.setLocation(start_letters, SCREEN_HEIGHT // 2 + 50)
    # button.setOrigin(start_letters)
    # button.setAction(moveLetter)
    
    # displayed_buttons[1].setLocation(start_letters, SCREEN_HEIGHT // 2 - displayed_buttons[0].getImage().get_height() - 50)
    # displayed_buttons[1].draw(screen)

    displayed_buttons[0].setAction(move_letter_one)
    displayed_buttons[1].setAction(move_letter_two)
    displayed_buttons[2].setAction(move_letter_three)
    displayed_buttons[3].setAction(move_letter_four)
    displayed_buttons[4].setAction(move_letter_five)
    displayed_buttons[5].setAction(move_letter_six)
    displayed_buttons[6].setAction(move_letter_seven)
    displayed_buttons[7].setAction(move_letter_eight)
    displayed_buttons[8].setAction(move_letter_nine)
    while run:
        countdown_clock.play()
        screen.fill((25, 80, 160))
        
        
        for button in displayed_buttons:
            if(button):
                button.draw(screen)
        for button in answer_buttons:
            if(button):
                
                button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if(pygame.time.get_ticks() >= round_end):
            letters_round_three()
        pygame.display.update()

    pygame.quit()

def letters_round_three():
    run = True
    countdown_clock.stop()
    pygame.mixer.music.play(-1)
    while run:

        screen.fill((25, 80, 160))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()

    pygame.quit()

def main_game():
    run = True
    while run:

        screen.fill((25, 80, 160))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()

    pygame.quit()

def add_consonant():
    global player_letters
    player_letters = lettersRound.generateLetter(letters=player_letters, choice='C')
    vowel_count = lettersRound.getVowelCount(letters=player_letters)
    displayed_buttons.append(button_arr[ord(player_letters[-1]) - 65].duplicate())
    print(player_letters)
    if(len(player_letters) - vowel_count == 6):
        consonant_button.setAction(None)
        consonant_button.setImage(pygame.image.load("images/button_consonant_disabled.png").convert_alpha(), 0.4)
    if(len(player_letters) == 9):
        consonant_button.setImage(pygame.image.load("images/button_consonant_disabled.png").convert_alpha(), 0.4)
        vowel_button.setImage(pygame.image.load("images/button_vowel_disabled.png").convert_alpha(), 0.4)
        consonant_button.draw(screen)       
        vowel_button.draw(screen)
        length = 0
        for letter in player_letters:
            length += button_arr[ord(letter) - 65].getImage().get_width()
            start_letters = SCREEN_WIDTH // 2 - length // 2
        for button in displayed_buttons:
            button.setLocation(start_letters, 100)
            button.draw(screen)
            start_letters += button.getImage().get_width()
        pygame.mixer.music.fadeout(3000)
        pygame.display.update()
        pygame.time.delay(3000)
        letters_round_two()

def add_vowel():
    global player_letters
    global button_arr
    player_letters = lettersRound.generateLetter(letters=player_letters, choice='V')
    vowel_count = lettersRound.getVowelCount(letters=player_letters)
    displayed_buttons.append(button_arr[ord(player_letters[-1]) - 65].duplicate())
    print(player_letters)
    if(vowel_count == 5):
        vowel_button.setAction(None)
        vowel_button.setImage(pygame.image.load("images/button_vowel_disabled.png").convert_alpha(), 0.4)
    if(len(player_letters) == 9):
        consonant_button.setImage(pygame.image.load("images/button_consonant_disabled.png").convert_alpha(), 0.4)
        vowel_button.setImage(pygame.image.load("images/button_vowel_disabled.png").convert_alpha(), 0.4)
        consonant_button.draw(screen)       
        vowel_button.draw(screen)
        length = 0
        for letter in player_letters:
            length += button_arr[ord(letter) - 65].getImage().get_width()
        start_letters = SCREEN_WIDTH // 2 - length // 2
        for button in displayed_buttons:
            button.setLocation(start_letters, 100)
            button.draw(screen)
            start_letters += button.getImage().get_width()
        pygame.mixer.music.fadeout(3000)
        pygame.display.update()
        pygame.time.delay(3000)
        letters_round_two()

def move_letter_one():
    if(displayed_buttons[0].getLocation()[1] > SCREEN_HEIGHT // 2):
        displayed_buttons[0].setLocation(displayed_buttons[0].getOrigin(), SCREEN_HEIGHT // 2 - displayed_buttons[0].getImage().get_height() - 50)
    else:
        displayed_buttons[0].setLocation(displayed_buttons[0].getOrigin(), SCREEN_HEIGHT // 2 + 50)

def move_letter_two():
    if(displayed_buttons[1].getLocation()[1] > SCREEN_HEIGHT // 2):
        displayed_buttons[1].setLocation(displayed_buttons[1].getOrigin(), SCREEN_HEIGHT // 2 - displayed_buttons[1].getImage().get_height() - 50)
    else:
        displayed_buttons[1].setLocation(displayed_buttons[1].getOrigin(), SCREEN_HEIGHT // 2 + 50)

def move_letter_three():
    if(displayed_buttons[2].getLocation()[1] > SCREEN_HEIGHT // 2):
        displayed_buttons[2].setLocation(displayed_buttons[2].getOrigin(), SCREEN_HEIGHT // 2 - displayed_buttons[2].getImage().get_height() - 50)
    else:
        displayed_buttons[2].setLocation(displayed_buttons[2].getOrigin(), SCREEN_HEIGHT // 2 + 50)

def move_letter_four():
    if(displayed_buttons[3].getLocation()[1] > SCREEN_HEIGHT // 2):
        displayed_buttons[3].setLocation(displayed_buttons[3].getOrigin(), SCREEN_HEIGHT // 2 - displayed_buttons[3].getImage().get_height() - 50)
    else:
        displayed_buttons[3].setLocation(displayed_buttons[3].getOrigin(), SCREEN_HEIGHT // 2 + 50)

def move_letter_five():
    global answers_start
    if(displayed_buttons[4]):
        answer_buttons[4] = displayed_buttons[4]
        answer_buttons[4].setLocation(answers_start,SCREEN_HEIGHT // 2 - answer_buttons[4].getImage().get_height() - 50)
        answers_start += answer_buttons[4].getImage().get_width()
        answer_order.append(4)
        displayed_buttons[4] = 0
    else:
        displayed_buttons[4] = answer_buttons[4]
        answers_start = answer_buttons[4].getLocation()[0]
        answer_buttons[4] = 0
        start_val = answer_order.index(4)
        answer_order.pop(start_val)
        for i in range(start_val, len(answer_order)):
            val = answer_order[i]
            answer_buttons[val].setLocation(answers_start,SCREEN_HEIGHT // 2 - answer_buttons[val].getImage().get_height() - 50)
            answers_start += answer_buttons[val].getImage().get_width()
        displayed_buttons[4].setLocation(displayed_buttons[4].getOrigin(), SCREEN_HEIGHT // 2 + 50)

def move_letter_six():
    global answers_start
    if(displayed_buttons[5]):
        answer_buttons[5] = displayed_buttons[5]
        answer_buttons[5].setLocation(answers_start,SCREEN_HEIGHT // 2 - answer_buttons[5].getImage().get_height() - 50)
        answers_start += answer_buttons[5].getImage().get_width()
        answer_order.append(5)
        displayed_buttons[5] = 0
    else:
        displayed_buttons[5] = answer_buttons[5]
        answers_start = answer_buttons[5].getLocation()[0]
        answer_buttons[5] = 0
        start_val = answer_order.index(5)
        answer_order.pop(start_val)
        print(answer_order)
        for i in range(start_val, len(answer_order)):
            val = answer_order[i]
            answer_buttons[val].setLocation(answers_start,SCREEN_HEIGHT // 2 - answer_buttons[val].getImage().get_height() - 50)
            answers_start += answer_buttons[val].getImage().get_width()

        displayed_buttons[5].setLocation(displayed_buttons[5].getOrigin(), SCREEN_HEIGHT // 2 + 50)

def move_letter_seven():
    if(displayed_buttons[6].getLocation()[1] > SCREEN_HEIGHT // 2):
        displayed_buttons[6].setLocation(displayed_buttons[6].getOrigin(), SCREEN_HEIGHT // 2 - displayed_buttons[6].getImage().get_height() - 50)
    else:
        displayed_buttons[6].setLocation(displayed_buttons[6].getOrigin(), SCREEN_HEIGHT // 2 + 50)

def move_letter_eight():
    if(displayed_buttons[7].getLocation()[1] > SCREEN_HEIGHT // 2):
        displayed_buttons[7].setLocation(displayed_buttons[7].getOrigin(), SCREEN_HEIGHT // 2 - displayed_buttons[0].getImage().get_height() - 50)
    else:
        displayed_buttons[7].setLocation(displayed_buttons[7].getOrigin(), SCREEN_HEIGHT // 2 + 50)

def move_letter_nine():
    if(displayed_buttons[8].getLocation()[1] > SCREEN_HEIGHT // 2):
        displayed_buttons[8].setLocation(displayed_buttons[8].getOrigin(), SCREEN_HEIGHT // 2 - displayed_buttons[8].getImage().get_height() - 50)
    else:
        displayed_buttons[8].setLocation(displayed_buttons[8].getOrigin(), SCREEN_HEIGHT // 2 + 50)
        
        

intro()