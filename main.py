import pygame, classes, random, algorithm

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Noughts and Crosses")

squares = []
turn = 1

end = False
cpu = "yes"

def set_up():
    global turn, end
    x_offset = 0
    y_offset = 0
    if len(squares) == 0:
        for row in range(1, 4):
            for spot in range(1, 4):
                squares.append(classes.square(x_offset, y_offset, x_offset / 200))
                x_offset += 200
            x_offset = 0
            y_offset += 200

    for square in squares:
        square.clicked = 0

    end = False
    turn = 1

def click(point):
    global turn
    for square in squares:
        if square.rect.collidepoint(point) and square.clicked < 1:
            square.click(turn)
            turn_change()

def turn_change():
    global turn
    turn += 1
    if turn == 3:
        turn = 1

def win_check():
    if squares[4].clicked > 0:
        if squares[3].clicked == squares[4].clicked == squares[5].clicked:
            return squares[4].clicked
        if squares[1].clicked == squares[4].clicked == squares[7].clicked:
            return squares[4].clicked
        if squares[0].clicked == squares[4].clicked == squares[8].clicked:
            return squares[4].clicked
        if squares[6].clicked == squares[4].clicked == squares[2].clicked:
            return squares[4].clicked
    if squares[0].clicked > 0:
        if squares[0].clicked == squares[1].clicked == squares[2].clicked:
            return squares[0].clicked
        if squares[0].clicked == squares[3].clicked == squares[6].clicked:
            return squares[0].clicked
    if squares[8].clicked > 0:
        if squares[6].clicked == squares[7].clicked == squares[8].clicked:
            return squares[8].clicked
        if squares[2].clicked == squares[5].clicked == squares[8].clicked:
            return squares[8].clicked

    for square in squares:
        if square.clicked == 0:
            return 0
    return 3

def ai():
    global turn
    while True:
        choice = algorithm.get_best(squares)
        if squares[choice].clicked < 1:
            squares[choice].click(2)
            turn_change()
            break

def draw_window():
    global win
    win.fill((0, 0, 0))
    for square in squares:
        square.draw(win)

    pygame.display.update()

set_up()
run = True
while run:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not end:
                click(pygame.mouse.get_pos())

    if end:
        pygame.time.wait(1000)
        set_up()

    if win_check() == 1:
        end = True
        print("Crosses Wins!")
    elif win_check() == 2:
        end = True
        print("Noughts Wins!")
    elif win_check() == 3:
        end = True
        print("Draw!")

    draw_window()

    if cpu == "yes":
        if turn == 2 and not end:
            pygame.time.wait(200)
            ai()


pygame.quit()