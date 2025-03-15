from global_variable import *

font = pg.font.Font(None, 50) #Шрифт
batton_up = font.render('Up', True, (180, 60, 0)) #Кнопка
battonUPcoord = [1850, 500, 200, 200]

batton_down = font.render('Down', True, (180, 60, 0)) #Кнопка
battonDOWNcoord = [1850, 900, 200, 200]

batton_right = font.render('Right', True, (180, 60, 0)) #Кнопка
battonRIGHTcoord = [700, 900, 200, 200]

batton_left = font.render('Left', True, (180, 60, 0)) #Кнопка
battonLEFTcoord = [200, 900, 200, 200]

batton_fire = font.render('FIRE', True, (180, 60, 0)) #Кнопка
battonFIREcoord = [1850, 200, 200, 200]

def Interface(patron, count_vrag):
    pul = font.render("Патронов: " + str(patron), True, (180, 60, 0))  # Кнопка
    vrag = font.render("Осталось врагов: " + str(count_vrag), True, (180, 60, 0))  # Кнопка

    display.blit(pul, (500, 870))
    display.blit(vrag, (900, 870))


def ControlForAndroid():
    pg.draw.rect(display, (100, 9, 0), battonUPcoord)
    pg.draw.rect(display, (100, 9, 0), battonDOWNcoord)
    pg.draw.rect(display, (100, 9, 0), battonRIGHTcoord)
    pg.draw.rect(display, (100, 9, 0), battonLEFTcoord)
    pg.draw.rect(display, (100, 9, 0), battonFIREcoord)
    display.blit(batton_up, battonUPcoord)
    display.blit(batton_down, battonDOWNcoord)
    display.blit(batton_right, battonRIGHTcoord)
    display.blit(batton_left, battonLEFTcoord)
    display.blit(batton_fire, battonFIREcoord)
