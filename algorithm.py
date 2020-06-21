import pygame, random

def get_best(squares):
    num = 0
    best_choice = random.randint(0, 8)
    found = False
    for i in range(1, 4):
        if squares[num].clicked == squares[num + 1].clicked == 1:
            if squares[num + 2].clicked == 0:
                best_choice = num + 2
                found = True
                break
        elif squares[num].clicked == squares[num + 2].clicked == 1:
            if squares[num + 1].clicked == 0:
                best_choice = num + 1
                found = True
                break
        elif squares[num + 1].clicked == squares[num + 2].clicked == 1:
            if squares[num].clicked == 0:
                best_choice = num
                found = True
                break
        num += 3

    num = 0
    for i in range(1, 4):
        if not found:
            if squares[num].clicked == squares[num + 3].clicked == 1:
                if squares[num + 6].clicked == 0:
                    best_choice = num + 6
                    found = True
                    break
            elif squares[num].clicked == squares[num + 6].clicked == 1:
                if squares[num + 3].clicked == 0:
                    best_choice = num + 3
                    found = True
                    break
            elif squares[num + 3].clicked == squares[num + 6].clicked == 1:
                if squares[num].clicked == 0:
                    best_choice = num
                    found = True
                    break
            num += 1

    if not found:
        if squares[0].clicked == squares[4].clicked == 1:
            if squares[8].clicked == 0:
                best_choice = 8
                found = True
        if squares[4].clicked == squares[8].clicked == 1:
            if squares[0].clicked == 0:
                best_choice = 0
                found = True
        if squares[0].clicked == squares[8].clicked == 1:
            if squares[4].clicked == 0:
                best_choice = 4
                found = True
        if squares[2].clicked == squares[4].clicked == 1:
            if squares[6].clicked == 0:
                best_choice = 6
                found = True
        if squares[4].clicked == squares[6].clicked == 1:
            if squares[2].clicked == 0:
                best_choice = 2
                found = True
        if squares[2].clicked == squares[6].clicked == 1:
            if squares[4].clicked == 0:
                best_choice = 4
                found = True

    num = 0
    for i in range(1, 4):
        if squares[num].clicked == squares[num + 1].clicked == 2:
            if squares[num + 2].clicked == 0:
                best_choice = num + 2
                found = True
                break
        elif squares[num].clicked == squares[num + 2].clicked == 2:
            if squares[num + 1].clicked == 0:
                best_choice = num + 1
                found = True
                break
        elif squares[num + 1].clicked == squares[num + 2].clicked == 2:
            if squares[num].clicked == 0:
                best_choice = num
                found = True
                break
        num += 3

    num = 0
    for i in range(1, 4):
        if squares[num].clicked == squares[num + 3].clicked == 2:
            if squares[num + 6].clicked == 0:
                best_choice = num + 6
                found = True
                break
        elif squares[num].clicked == squares[num + 6].clicked == 2:
            if squares[num + 3].clicked == 0:
                best_choice = num + 3
                found = True
                break
        elif squares[num + 3].clicked == squares[num + 6].clicked == 2:
            if squares[num].clicked == 0:
                best_choice = num
                found = True
                break
        num += 1

    if squares[0].clicked == squares[4].clicked == 2:
        if squares[8].clicked == 0:
            best_choice = 8
            found = True
    if squares[4].clicked == squares[8].clicked == 2:
        if squares[0].clicked == 0:
            best_choice = 0
            found = True
    if squares[0].clicked == squares[8].clicked == 2:
        if squares[4].clicked == 0:
            best_choice = 4
            found = True
    if squares[2].clicked == squares[4].clicked == 2:
        if squares[6].clicked == 0:
            best_choice = 6
            found = True
    if squares[4].clicked == squares[6].clicked == 2:
        if squares[2].clicked == 0:
            best_choice = 2
            found = True
    if squares[2].clicked == squares[6].clicked == 2:
        if squares[4].clicked == 0:
            best_choice = 4
            found = True

    if found and squares[best_choice].clicked != 0:
        print("something's gone terribly wrong")
        best_choice = random.randint(0, 8)
    return best_choice
    
    