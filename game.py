import numpy as np
import copy

from pygame.time import Clock

from global_variable import *
from Wall import Wall
from Tank import PlayerTank, VragTank, Tank
from GUI import *

if android:
    import sdl2


class Map:
    def __init__(self):
        self.poligon = np.zeros((count_cell_height, count_cell_width, 2),
                                dtype=object)  # Матрица игрового поля (1й параметр - ID объекта(0 - объекта нет), 2 параметр координаты объекта)
        print("y = ", count_cell_height, "x =", count_cell_width)

        listoftank.append(PlayerTank(self, 1,
                                     2))  # Создаем игрока, он всегда первый в списке #Передаем ссылку на себя, чтобы получить доступ к данным  игрового поля

        k = 30  # Количество вражеских танков
        for i in range(0, k):
            a = random.randint(0, count_cell_height - 1)
            b = random.randint(0, count_cell_width - 1)
            if not (self.poligon[a][b][0] in [5, 6]):
                listoftank.append(VragTank(self, b, a))

        self.wall = Wall(self)  # Создаем стены


def Update():
    map.wall.Update()  # Обновляем позицию стен

    i = 0
    while i < len(listoftank):  # Обновляем позиции танков
        listoftank[i].Update()
        i += 1


def run_game():
    game = True
    while game:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
        display.fill((0, 0, 0))  # Закрашиваем черным фон

        if android:
            ControlForAndroid()
            pressed = pg.mouse.get_pressed()
            if pressed[0]:
                listoftank[0].MoveAndroid(pg.mouse.get_pos())

        i = 0
        while i < len(listoftank):
            listoftank[i].MoveNew()  # Двигаем танки
            i += 1


        Interface(listoftank[0].bull.patron, len(listoftank) - 1)


        Update()  # Обновляем объекты
        pg.display.update()  # Обновляем экран
        clock.tick(FPS)  # Количество кадров в секундку (скорость цикла)


clock = pg.time.Clock()  # Создание задержки
map = Map()  # Создание карты
run_game()  # Запуск игры
