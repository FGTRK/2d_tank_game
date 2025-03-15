from global_variable import *

class Wall:
    ID = 1 #Идентификатор стены
    chance_wall = 2  # Шанс появления стены

    def __init__(self, map): #Конструктор
        self.Wall_img = pg.image.load('Sprite/wall.png').convert() #Загружаем изображение стены
        self.map = map  #Передаем ссылку на карту

        i = 0
        while i < count_cell_height:
            j = 0
            while j < count_cell_width:
                # Заполнение матрицы
                w_gen = random.randint(0, self.chance_wall)
                if (w_gen == 0) and (self.map.poligon[i][j][0] == 0):
                    self.map.poligon[i][j][0] = self.ID #Присваиваем ID в матрице
                    self.map.poligon[i][j][1] = self.Wall_img.get_rect(topleft=(offset_width + grid * j, offset_height + grid * i)) #Присваиваем координаты в матрице объектов
                    block_coll.append(self.Wall_img.get_rect(topleft=(offset_width + grid * j, offset_height + grid * i))) #Добавляем объект в матрицу столкновений
                 #   display.blit(self.Wall_img, (self.map.poligon_object[i][j].x, self.map.poligon_object[i][j].y)) #Рисуем стены по координатам
                j += 1
            i += 1

    def Update(self):
        i = 0
        while i < count_cell_height:
            j = 0
            while j < count_cell_width:
                if self.map.poligon[i][j][0] == Wall.ID:
                    display.blit(self.Wall_img, (self.map.poligon[i][j][1].x, self.map.poligon[i][j][1].y))  # Рисуем стены по координатам
                j += 1
            i += 1
