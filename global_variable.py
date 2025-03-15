import pygame as pg
import random

try:
    import android
except ImportError:
    android=None

pg.init() #Инициализация библиотеки

grid = 30 #Размер одной клетки

display_width = 1900 # Ширина дисплея
display_height = 910 # Высота дисплея

display = pg.display.set_mode((display_width, display_height)) #Инициализация рабочего окна
pg.display.set_caption('Tanks') # Заголовок игры

offset_display = 50 #Смещение от края окна

max_width = display_width - offset_display * 2 #Количество клеток по ширине
offset_width = offset_display #Смещение от начала слева
max_height = display_height - offset_display * 2 #Количество клеток по высоте
offset_height = offset_display #Смещение от начала сверху


tank_grid = 26 #Размер танка

count_cell_width = max_width // grid
count_cell_height = max_height // grid

FPS = 60 #Кадры в секунду


block_coll = [] #Матрица столкновений блоков с танками

tank_coll_ID = [] #Матрица сопоставлений танков с их id
tank_coll = [] #Матрица столкновений танков с танками
listoftank = [] #Список живых танков