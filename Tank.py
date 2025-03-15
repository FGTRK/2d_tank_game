from global_variable import *
if android:
    from GUI import *

class Tank:
    count = 0 #Переменная для генерации id конкретного танка

    def __init__(self, map, dir, ID, x, y): #Конструктор
        self.x = x  # Координата X в матрице
        self.y = y  # Координата Y в матрице

        self.Pl_img_default = pg.image.load(dir)

        self.Pl_img = self.Pl_img_default.convert_alpha() #Загружаем изображение танка (convert для ускорения работы)
        self.Pl_up = pg.transform.rotate(self.Pl_img, 90)
        self.Pl_down = pg.transform.rotate(self.Pl_img, -90)
        self.Pl_right = self.Pl_img
        self.Pl_left = pg.transform.flip(self.Pl_img, 1, 0)
        self.rotate = self.Pl_right #Начальный поворот

        self.map = map

        # Спавн танка
        self.map.poligon[self.y][self.x][0] = ID # Присваиваем ID в матрице
        self.coord = self.Pl_img.get_rect(topleft=(
            offset_height + grid * self.x + 2, offset_width + grid * self.y + 2))  # Реальные координаты на поле

        self.IDTank = Tank.count #Идентификатор конкретного танка
        tank_coll_ID.append(self.IDTank)
        Tank.count += 1
        tank_coll.append(self.coord) #Добавляем положение танка

      #  display.blit(self.rotate, (self.coord.x, self.coord.y))  # Рисуем танк по координатам

        self.direction = [1, 1]  # 0 0 вверх, 0 1 влево, 1 0 вниз, 1 1 вправо, Третья - переменная отвечает за предварительный разворот

        self.patron = 40 #Количество патронов (максимальное)
        self.bull = Bullet(self.patron) #Создаем патроны
        self.cooldown = 10 #Перезарядка

    """
    def __del__(self):
        print(self.IDTank, " - был уничтожен")
    """


    def Update(self):
        self.bull.Move(self.map.poligon)
        self.bull.Update()
        display.blit(self.rotate, (self.coord.x, self.coord.y))  # Рисуем танк по координатам

    def Move(self, Space, Up, Dowm, Right, Left):

        self.cooldown -= 1
        if Space and self.cooldown <= 0:  # Стрельба
           self.bull.Add_patron(self.coord, self.direction)
           self.cooldown = 40 #Обновляем кулдаун

        # Обработка клавиши вперед
        elif Up:
            if self.direction == [0, 0]: #Проверка на поворот танка
                self.coord.y -= 1 #Проверяем на столкновение вперед на - 1 значение
                tank_coll[tank_coll_ID.index(self.IDTank)] = self.Pl_img.get_rect(topleft=(0, 0)) #Обнуляем позицию нашего танка, чтобы его не было в матрице столкновений танков
                if not (self.coord.y >= offset_height and self.coord.collidelist(block_coll) == -1 and self.coord.collidelist(tank_coll) == -1):
                    self.coord.y += 1
                tank_coll[tank_coll_ID.index(self.IDTank)] = self.coord
            else:
                # Поворт спрайта
                self.rotate = self.Pl_up
                self.direction = [0, 0]

        # Обработка клавиши назад
        elif Dowm:
            if self.direction == [1, 0]:
                self.coord.y += 1
                tank_coll[tank_coll_ID.index(self.IDTank)] = self.Pl_img.get_rect(topleft=(0, 0))
                if not (self.coord.bottom < max_height + offset_height and self.coord.collidelist(block_coll) == -1 and self.coord.collidelist(tank_coll) == -1):
                    self.coord.y -= 1
                tank_coll[tank_coll_ID.index(self.IDTank)] = self.coord
            else:
                self.rotate = self.Pl_down
                self.direction = [1, 0]

        # Обработка клавиши вправо
        elif Right:
            if self.direction == [1, 1]:
                self.coord.x += 1
                tank_coll[tank_coll_ID.index(self.IDTank)] = self.Pl_img.get_rect(topleft=(0, 0))
                if not (self.coord.right < max_width + offset_width and self.coord.collidelist(block_coll) == -1 and self.coord.collidelist(tank_coll) == -1):
                    self.coord.x -= 1
                tank_coll[tank_coll_ID.index(self.IDTank)] = self.coord
            else:
                self.rotate = self.Pl_right
                self.direction = [1, 1]

        # Обработка клавиши влево
        elif Left:
            if self.direction == [0, 1]:
                self.coord.x -= 1
                tank_coll[tank_coll_ID.index(self.IDTank)] = self.Pl_img.get_rect(topleft=(0, 0))
                if not (self.coord.x >= offset_width and self.coord.collidelist(block_coll) == -1 and self.coord.collidelist(tank_coll) == -1):
                    self.coord.x += 1
                tank_coll[tank_coll_ID.index(self.IDTank)] = self.coord
            else:
                self.rotate = self.Pl_left
                self.direction = [0, 1]



class PlayerTank(Tank):
    ID = 5 #Идентификатор танка игрока
    dir_to_image = 'Sprite/PlayerTank.png'  # Путь, название к изображению танка

    def __init__(self, map, x, y): #Конструктор
        Tank.__init__(self, map, PlayerTank.dir_to_image, PlayerTank.ID, x, y) #Инициализируем основные переменные

    def MoveNew(self):
        keys = pg.key.get_pressed()  # Получаем кортеж нажатых клавиш
        self.Move(keys[pg.K_SPACE], keys[pg.K_UP], keys[pg.K_DOWN], keys[pg.K_RIGHT], keys[pg.K_LEFT])

    def MoveAndroid(self, pos):
        if (battonFIREcoord[0] + battonFIREcoord[2] > pos[0] > battonFIREcoord[0]) and (
                battonFIREcoord[1] + battonFIREcoord[3] > pos[1] > battonFIREcoord[1]):
            self.Move(1, 0, 0, 0, 0)
        elif (battonUPcoord[0] + battonUPcoord[2] > pos[0] > battonUPcoord[0]) and (
                battonUPcoord[1] + battonUPcoord[3] > pos[1] > battonUPcoord[1]):
            self.Move(0, 1, 0, 0, 0)
        elif (battonDOWNcoord[0] + battonDOWNcoord[2] > pos[0] > battonDOWNcoord[0]) and (
                battonDOWNcoord[1] + battonDOWNcoord[3] > pos[1] > battonDOWNcoord[1]):
            self.Move(0, 0, 1, 0, 0)
        elif (battonRIGHTcoord[0] + battonRIGHTcoord[2] > pos[0] > battonRIGHTcoord[0]) and (
                battonRIGHTcoord[1] + battonRIGHTcoord[3] > pos[1] > battonRIGHTcoord[1]):
            self.Move(0, 0, 0, 1, 0)
        elif (battonLEFTcoord[0] + battonLEFTcoord[2] > pos[0] > battonLEFTcoord[0]) and (
                battonLEFTcoord[1] + battonLEFTcoord[3] > pos[1] > battonLEFTcoord[1]):
            self.Move(0, 0, 0, 0, 1)




class VragTank(Tank):
    ID = 6  # Идентификатор танка игрока
    dir_to_image = 'Sprite/VragTank.png'  # Путь, название к изображению танка

    def __init__(self, map, x, y):  # Конструктор
        Tank.__init__(self, map, VragTank.dir_to_image, VragTank.ID, x, y)  # Инициализируем основные переменные

        self.pp = 60
        self.p = random.randint(0, 6)

    def MoveNew(self):
        if self.pp > 0:

            self.pp -= 1
        else:
            self.pp = 60
            self.p = random.randint(0, 6)
      #      self.p = 0

        if self.p == 0:
            self.Move(1, 0, 0, 0, 0)
        elif self.p == 1:
            self.Move(0, 1, 0, 0, 0)
        elif self.p == 2:
            self.Move(0, 0, 1, 0, 0)
        elif self.p == 3:
            self.Move(0, 0, 0, 1, 0)
        elif self.p == 4:
            self.Move(0, 0, 0, 0, 1)


class Bullet:
    def __init__(self, patron):
        #Текстура пули
        self.view_widht = pg.Surface((9, 4))
        self.view_height = pg.Surface((4, 9))
        self.view_widht.fill((120, 12, 12))
        self.view_height.fill((120, 12, 12))

        self.speed_bull = 6 #Скорость пули


        self.patron_obj = [] #Координаты объектов
        self.patron_orientation = [] #Направление движения патронов

        self.patron = patron #Сколько патронов нужно добавить


    def Add_patron(self, coord, direction):
        if self.patron > 0:
            if direction == [0, 0]: #Вверх
                self.patron_obj.append(self.view_height.get_rect(midbottom=(coord.centerx, coord.top)))
                self.patron_orientation.append(0)
            elif direction == [1, 0]: #Вниз
                self.patron_obj.append(self.view_height.get_rect(midtop=(coord.centerx, coord.bottom)))
                self.patron_orientation.append(2)
            elif direction == [1, 1]: #Вправо
                self.patron_obj.append(self.view_widht.get_rect(midleft=(coord.right, coord.centery)))
                self.patron_orientation.append(3)
            elif direction == [0, 1]: #Влево
                self.patron_obj.append(self.view_widht.get_rect(midright=(coord.left, coord.centery)))
                self.patron_orientation.append(1)

            self.patron -= 1

        else:
            print("Закончились патроны")

    def Move(self, poligon):
        global block_coll #Используем глобальную переменную
        i = 0
        while i < len(self.patron_obj):
            if self.patron_obj[i].collidelist(tank_coll) == - 1: #Пуля попала по танку?
                if self.patron_obj[i].collidelist(block_coll) == -1  \
                        and (self.patron_obj[i].y >= offset_height \
                        and self.patron_obj[i].y < max_height + offset_height \
                        and self.patron_obj[i].x < max_width + offset_width \
                        and self.patron_obj[i].x >= offset_width):
                    if self.patron_orientation[i] == 0:
                        self.patron_obj[i].y -= self.speed_bull
                    elif self.patron_orientation[i] == 2:
                        self.patron_obj[i].y += self.speed_bull
                    elif self.patron_orientation[i] == 3:
                        self.patron_obj[i].x += self.speed_bull
                    elif self.patron_orientation[i] == 1:
                        self.patron_obj[i].x -= self.speed_bull
                else:

                    block_coll = [] #Обновляем матрицу коллизий после удаления стены пулей
                    for jj in range(count_cell_height):
                        for j in range(count_cell_width):
                            if poligon[jj][j][1] != 0 and poligon[jj][j][1].colliderect(self.patron_obj[i]): #Проверяем с каким препятствием иммено столкнулась пуля
                                poligon[jj][j][0] = 0
                                poligon[jj][j][1] = 0
                            if poligon[jj][j][0] == 1:
                                block_coll.append(poligon[jj][j][1])

                    del self.patron_obj[i] #Удаляем пулю при столкновении
                    del self.patron_orientation[i]
            else:

                for j in range(len(tank_coll_ID)):
                    if tank_coll[j].colliderect(self.patron_obj[i]):
                        del tank_coll[j]
                        del listoftank[j]
                        del tank_coll_ID[j]
                        break

                del self.patron_obj[i]  # Удаляем пулю при столкновении
                del self.patron_orientation[i]
            i += 1


    def Update(self):
       for i in range(len(self.patron_obj)):
           if self.patron_orientation[i] in [0, 2]:
                display.blit(self.view_height, (self.patron_obj[i].x, self.patron_obj[i].y))  # Рисуем патрон
           else:
                display.blit(self.view_widht, (self.patron_obj[i].x, self.patron_obj[i].y))

