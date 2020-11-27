class LabirintTurtle:
    def __init__(self):
        self.karta = ""
        self.igrovoe_pole = []
        self.turtle_position = [0, 0]
        self.graf = {}
        self.lenth = 9999999
        self.pyt = []
        self.kopiya = []
        self.karta_valid = True

    def printt(self, text):
        print("\033[31m {}".format(text))

    def odno_i_to_sge(self):
        try:
            karta = self.karta.split("\n")
            koordinata = [karta[-1], karta[-2]]
            karta.pop(-1)
            karta.pop(-1)
            po_x = 0
            for i in karta:
                if len(i) > po_x:
                    po_x = len(i)
            self.igrovoe_pole = []

            for i in karta:
                self.igrovoe_pole.append(list(i))

            for i in range(len(self.igrovoe_pole)):
                if len(self.igrovoe_pole[i]) != po_x:
                    self.igrovoe_pole[i] += (po_x - len(self.igrovoe_pole[i])) * [" "]

            self.graf = {}
            for y in range(len(self.igrovoe_pole)):
                for x in range(po_x):
                    if self.igrovoe_pole[y][x] == "*":
                        continue
                    if str(x) + "," + str(y) not in self.graf:
                        self.graf[str(x) + "," + str(y)] = []

                    try:
                        if self.igrovoe_pole[y - 1][x] == " " and y - 1 >= 0:
                            new_graf = self.graf[str(x) + "," + str(y)]
                            new_graf.append(str(x) + "," + str(y - 1))
                    except:
                        pass

                    try:
                        if self.igrovoe_pole[y + 1][x] == " ":
                            new_graf = self.graf[str(x) + "," + str(y)]
                            new_graf.append(str(x) + "," + str(y + 1))
                    except:
                        pass

                    try:
                        if self.igrovoe_pole[y][x + 1] == " ":
                            new_graf = self.graf[str(x) + "," + str(y)]
                            new_graf.append(str(x + 1) + "," + str(y))
                    except:
                        pass

                    try:
                        if self.igrovoe_pole[y][x - 1] == " " and x - 1 >= 0:
                            new_graf = self.graf[str(x) + "," + str(y)]
                            new_graf.append(str(x - 1) + "," + str(y))
                    except:
                        pass

            if self.igrovoe_pole[int(koordinata[0])][int(koordinata[1])] != "*":
                pass
            else:
                print("Черепаха на месте стены")
                self.karta_valid = False
            self.pyt = []
            self.lenth = 9999999

            vihodi = []
            for i in range(len(self.igrovoe_pole[0])):
                if self.igrovoe_pole[0][i] == " ":
                    vihodi.append([i, 0])
            for i in range(len(self.igrovoe_pole[-1])):
                if self.igrovoe_pole[-1][i] == " ":
                    vihodi.append([i, len(self.igrovoe_pole) - 1])
            for i in range(len(self.igrovoe_pole)):
                if self.igrovoe_pole[i][0] == " ":
                    vihodi.append([0, i])
            for i in range(len(self.igrovoe_pole)):
                if self.igrovoe_pole[i][-1] == " ":
                    vihodi.append([len(self.igrovoe_pole[0]) - 1, i])

            def BFS_SP(graph, start, goal):
                explored = []
                queue = [[start]]
                if start == goal:
                    return []
                while queue:
                    path = queue.pop(0)
                    node = path[-1]
                    if node not in explored:
                        neighbours = graph[node]
                        for neighbour in neighbours:
                            new_path = list(path)
                            new_path.append(neighbour)
                            queue.append(new_path)
                            if neighbour == goal:
                                return new_path
                        explored.append(node)
                return False
            for i in vihodi:
                res = BFS_SP(self.graf, str(self.turtle_position[1]) + "," + str(self.turtle_position[0]),
                             str(i[0]) + "," + str(i[1]))
                if res != False:
                    if len(res) < self.lenth:
                        self.pyt = res
                        self.lenth = len(res)
            if self.pyt == [] and self.lenth == 9999999:
                print("Черепачка никак не сможет выйти")
                self.karta_valid = False

        except:
            print("Неведомая ошибка")
            self.karta_valid = False






    def load_map(self, name):
        try:
            self.__init__()
            map = open(name, "r")
            self.karta = map.read()
            gg = self.karta.split("\n")
            gg.pop(-1)
            gg.pop(-1)
            gg = "".join(gg)
            for i in gg:
                if i not in "* \n   ":
                    print("Оло карта не валидна")
                    return

            print("Карта загружена")
            karta = self.karta.split("\n")
            self.turtle_position = [karta[-1], karta[-2]]
            self.karta_valid = True
        except:
            self.__init__()
            print("Неправильное название или путь")

    def show_map(self, turtle=False):
        if self.karta_valid:
            if self.igrovoe_pole[int(self.turtle_position[0])][int(self.turtle_position[1])] != "*":
                if turtle == True:
                    self.igrovoe_pole[int(self.turtle_position[0])][int(self.turtle_position[1])] = "A"
            else:
                print("Черепаха на месте стены")

            for i in self.igrovoe_pole:
                self.printt("\t".join(i))





    def check_map(self):
        if not self.karta_valid:
            print("Оло карта не валидна")
            return
        else:
            print("С картой все ок")
        self.odno_i_to_sge()




    def exit_count_step(self):
        if not self.karta_valid:
            print("Оло карта не валидна")
            return
        self.odno_i_to_sge()
        if self.lenth != 9999999:
            print(self.lenth)

    def exit_show_step(self):
        if not self.karta_valid:
            print("Оло карта не валидна")
            return
        self.odno_i_to_sge()
        last = [[-99, -99]]
        self.kopiya = []
        for i in self.igrovoe_pole:
            self.kopiya.append(i.copy())
        for i in self.pyt:
            k = [int(i.split(",")[0]), int(i.split(",")[1])]
            if k[-2] + 1 == last[-1][1]:
                self.kopiya[k[-1]][k[-2]] = "←"
            elif k[-2] - 1 == last[-1][1]:
                self.kopiya[k[-1]][k[-2]] = "→"
            elif k[-1] - 1 == last[-1][0]:
                self.kopiya[k[-1]][k[-2]] = "↓"
            elif k[-1] + 1 == last[-1][0]:
                self.kopiya[k[-1]][k[-2]] = "↑"
            else:
                self.kopiya[k[-1]][k[-2]] = "●"
            last.append([k[-1], k[-2]])
        for i in self.kopiya:
            for p in i:
                if p not in "●↑↓→←A":
                    print(("\033[31m {}".format(p)), end="\t")

                else:
                    print("\033[34m {}".format(p), end="\t")
            print()

    def slovestnoe_opisanie(self):
        napravleniya = {"↑": 0, "→": 90, "↓": 180, "←": 270}
        if self.pyt == []:
            print("Путь не определен")
        else:
            if self.kopiya[int(self.pyt[1].split(",")[1])][int(self.pyt[1].split(",")[0])] == "↓":
                print("Разворот на 180")
            pologenie_pred = 0
            for i in self.pyt[1::]:
                if pologenie_pred - napravleniya[self.kopiya[int(i.split(",")[1])][int(i.split(",")[0])]] == 90:
                    print("Поворот налево")
                    print("Вперед")
                elif pologenie_pred - napravleniya[self.kopiya[int(i.split(",")[1])][int(i.split(",")[0])]] == -90:
                    print("Поворот направо")
                    print("Вперед")
                else:
                    print("Вперед")
                pologenie_pred = napravleniya[self.kopiya[int(i.split(",")[1])][int(i.split(",")[0])]]



h = LabirintTurtle()
h.load_map("l1.txt")
h.check_map()
h.show_map(turtle=True)
h.exit_count_step()
h.exit_show_step()
h.slovestnoe_opisanie()

h.load_map("l.txt")
h.check_map()
h.show_map(turtle=True)
h.exit_count_step()
h.exit_show_step()
h.slovestnoe_opisanie()



