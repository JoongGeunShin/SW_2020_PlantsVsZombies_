__author__ = 'marble_xu'

import random
import pygame as pg
from .. import tool
from .. import constants as c
from tkinter import messagebox as msg
from tkinter import Tk

PANEL_Y_START = 87
PANEL_X_START = 22
PANEL_Y_INTERNAL = 74
PANEL_X_INTERNAL = 53
CARD_MIN = 4 # 선택해야 하는 최소 카드 개수
CARD_MAX = 8 # 선택할 수 있는 최대 카드 개수

# source/constants.py 114-131
card_name_list = [c.CARD_SUNFLOWER, c.CARD_PEASHOOTER, c.CARD_SNOWPEASHOOTER, c.CARD_WALLNUT,
                  c.CARD_CHERRYBOMB, c.CARD_THREEPEASHOOTER, c.CARD_REPEATERPEA, c.CARD_CHOMPER,
                  c.CARD_PUFFSHROOM, c.CARD_POTATOMINE, c.CARD_SQUASH, c.CARD_SPIKEWEED,
                  c.CARD_JALAPENO, c.CARD_SCAREDYSHROOM, c.CARD_SUNSHROOM, c.CARD_ICESHROOM,
                  c.CARD_HYPNOSHROOM, c.CARD_WALLNUT, c.CARD_REDWALLNUT]
# source/constants.py 72-95
plant_name_list = [c.SUNFLOWER, c.PEASHOOTER, c.SNOWPEASHOOTER, c.WALLNUT,
                   c.CHERRYBOMB, c.THREEPEASHOOTER, c.REPEATERPEA, c.CHOMPER,
                   c.PUFFSHROOM, c.POTATOMINE, c.SQUASH, c.SPIKEWEED,
                   c.JALAPENO, c.SCAREDYSHROOM, c.SUNSHROOM, c.ICESHROOM,
                   c.HYPNOSHROOM, c.WALLNUTBOWLING, c.REDWALLNUTBOWLING]
plant_sun_list = [50, 100, 175, 50, 150, 325, 200, 150, 0, 25, 50, 100, 125, 25, 25, 75, 75, 0, 0]
plant_frozen_time_list = [7500, 7500, 7500, 30000, 50000, 7500, 7500, 7500, 7500, 30000,
                          30000, 7500, 50000, 7500, 7500, 50000, 30000, 0, 0]
all_card_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def getSunValueImage(sun_value):
    font = pg.font.SysFont(None, 22)
    width = 32
    msg_image = font.render(str(sun_value), True, c.NAVYBLUE, c.LIGHTYELLOW)
    msg_rect = msg_image.get_rect()
    msg_w = msg_rect.width

    image = pg.Surface([width, 17])
    x = width - msg_w

    image.fill(c.LIGHTYELLOW)
    image.blit(msg_image, (x, 0), (0, 0, msg_rect.w, msg_rect.h))
    image.set_colorkey(c.BLACK)
    return image

#def getCardPool(data):
#    card_pool = []
#    for card in data:
#        tmp = card['name']
#        for i,name in enumerate(plant_name_list):
#            if name == tmp:
#                card_pool.append(i)
#                break
#    return card_pool

class Card():
    def __init__(self, x, y, name_index, scale=0.78):
        self.loadFrame(card_name_list[name_index], scale)
        self.rect = self.orig_image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.name_index = name_index
        self.sun_cost = plant_sun_list[name_index]
        self.frozen_time = plant_frozen_time_list[name_index]
        self.frozen_timer = -self.frozen_time
        self.refresh_timer = 0
        self.select = True
        self.selectR = True

    def loadFrame(self, name, scale):
        frame = tool.GFX[name]
        rect = frame.get_rect()
        width, height = rect.w, rect.h

        self.orig_image = tool.get_image(frame, 0, 0, width, height, c.BLACK, scale)
        self.image = self.orig_image

    def checkMouseClick(self, mouse_pos):
        print('checkmouseclick')
        x, y = mouse_pos
        if(x >= self.rect.x and x <= self.rect.right and
           y >= self.rect.y and y <= self.rect.bottom):
            return True
        return False
    
    def checkMouseRight(self, rightmouse_pos):
        print('checkmouseright')
        x, y = rightmouse_pos
        if(x >= self.rect.x and x <= self.rect.right and
           y >= self.rect.y and y <= self.rect.bottom):
           return True
        return False

    def canClick(self, sun_value, current_time):
        if self.sun_cost <= sun_value and (current_time - self.frozen_timer) > self.frozen_time:
            print('canclick')
            return True
        return False

    def canSelect(self):
        print('canselect')
        return self.select
    
    def canSelectr(self):
        print('canselectr')
        return self.selectR

    def setSelect(self, can_select):
        self.select = can_select
        if can_select:
            self.image.set_alpha(255)
            print('setelect if')
        else:
            print('setselect else')
            self.image.set_alpha(128)

    def setSelectr(self, can_select):
            print('setselectr')
            self.image.set_alpha(225)

    def setFrozenTime(self, current_time):
        print('setfrozentime')
        self.frozen_timer = current_time

    def createShowImage(self, sun_value, current_time):
        '''create a card image to show cool down status
           or disable status when have not enough sun value'''
        time = current_time - self.frozen_timer
        if time < self.frozen_time: #cool down status
            image = pg.Surface([self.rect.w, self.rect.h])
            frozen_image = self.orig_image
            frozen_image.set_alpha(128)
            frozen_height = (self.frozen_time - time)/self.frozen_time * self.rect.h
            print('createshowimage if')
            image.blit(frozen_image, (0,0), (0, 0, self.rect.w, frozen_height))
            image.blit(self.orig_image, (0,frozen_height),
                       (0, frozen_height, self.rect.w, self.rect.h - frozen_height))
        elif self.sun_cost > sun_value: #disable status
            print('createshowimage else')
            image = self.orig_image
            image.set_alpha(192)
        else:
            image = self.orig_image
        return image

    def update(self, sun_value, current_time):
        if (current_time - self.refresh_timer) >= 250:
            print('update')
            self.image = self.createShowImage(sun_value, current_time)
            self.refresh_timer = current_time

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class MenuBar():
    def __init__(self, card_list, sun_value):
        self.loadFrame(c.MENUBAR_BACKGROUND)
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = 0
        
        self.sun_value = sun_value
        self.card_offset_x = 32
        self.setupCards(card_list)

    def loadFrame(self, name):
        frame = tool.GFX[name]
        rect = frame.get_rect()
        frame_rect = (rect.x, rect.y, rect.w, rect.h)

        self.image = tool.get_image(tool.GFX[name], *frame_rect, c.WHITE, 1)

    def update(self, current_time):
        self.current_time = current_time
        for card in self.card_list:
            card.update(self.sun_value, self.current_time)

    def createImage(self, x, y, num):
        if num == 1:
            return
        img = self.image
        rect = self.image.get_rect()
        width = rect.w
        height = rect.h
        self.image = pg.Surface((width * num, height)).convert()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        for i in range(num):
            x = i * width
            self.image.blit(img, (x,0))
        self.image.set_colorkey(c.BLACK)
    
    def setupCards(self, card_list):
        self.card_list = []
        x = self.card_offset_x
        y = 8
        for index in card_list:
            x += 55
            self.card_list.append(Card(x, y, index))

    def checkCardClick(self, mouse_pos):
        result = None
        for card in self.card_list:
            if card.checkMouseClick(mouse_pos):
                if card.canClick(self.sun_value, self.current_time):
                    result = (plant_name_list[card.name_index], card)
                break
        return result

    def checkcardRclick(self, rightmouse_pos):
        result2 = None
        for card in self.card_list:
            if card.checkMouseClick(rightmouse_pos):
                if card.canClick(self.sun_value, self.current_time):
                    result = (plant_name_list[card.name_index], card)
                    break
        return result2
    
    def checkMenuBarClick(self, mouse_pos):
        x, y = mouse_pos
        if(x >= self.rect.x and x <= self.rect.right and
           y >= self.rect.y and y <= self.rect.bottom):
            return True
        return False

    def decreaseSunValue(self, value):
        self.sun_value -= value

    def increaseSunValue(self, value):
        self.sun_value += value

    def setCardFrozenTime(self, plant_name):
        for card in self.card_list:
            if plant_name_list[card.name_index] == plant_name:
                card.setFrozenTime(self.current_time)
                break

    def drawSunValue(self):
        self.value_image = getSunValueImage(self.sun_value)
        self.value_rect = self.value_image.get_rect()
        self.value_rect.x = 21
        self.value_rect.y = self.rect.bottom - 21
        
        self.image.blit(self.value_image, self.value_rect)

    def draw(self, surface):
        self.drawSunValue()
        surface.blit(self.image, self.rect)
        for card in self.card_list:
            card.draw(surface)

class Panel():
    def __init__(self, card_list, sun_value):
        self.loadImages(sun_value)
        self.selected_cards = []
        self.selected_num = 0
        self.setupCards(card_list)
        self.selectedr_cards = []
        self.selectedr_num = 0

    def loadFrame(self, name):
        frame = tool.GFX[name]
        rect = frame.get_rect()
        frame_rect = (rect.x, rect.y, rect.w, rect.h)

        return tool.get_image(tool.GFX[name], *frame_rect, c.WHITE, 1)

    def loadImages(self, sun_value):
        self.menu_image = self.loadFrame(c.MENUBAR_BACKGROUND)
        self.menu_rect = self.menu_image.get_rect()
        self.menu_rect.x = 0
        self.menu_rect.y = 0

        self.panel_image = self.loadFrame(c.PANEL_BACKGROUND)
        self.panel_rect = self.panel_image.get_rect()
        self.panel_rect.x = 0
        self.panel_rect.y = PANEL_Y_START

        
        self.value_image = getSunValueImage(sun_value)
        self.value_rect = self.value_image.get_rect()
        self.value_rect.x = 21
        self.value_rect.y = self.menu_rect.bottom - 21

        self.button_image =  self.loadFrame(c.START_BUTTON)
        self.button_rect = self.button_image.get_rect()
        self.button_rect.x = 155
        self.button_rect.y = 547

    def setupCards(self, card_list):
        self.card_list = []
        x = PANEL_X_START - PANEL_X_INTERNAL
        y = PANEL_Y_START + 43 - PANEL_Y_INTERNAL
        print('setupcard = panel')
        for i, index in enumerate(card_list):
            print('setupcard = pnael -> for')
            if i % 8 == 0:
                x = PANEL_X_START - PANEL_X_INTERNAL
                y += PANEL_Y_INTERNAL
                print('setupcard = panel -> if')
            x += PANEL_X_INTERNAL
            self.card_list.append(Card(x, y, index, 0.75))

    def setupRCards(self, card_list):
        self.card_rlist = []
        x = PANEL_X_START - PANEL_X_INTERNAL
        y = PANEL_Y_START + 43 - PANEL_Y_INTERNAL
        for j, index in enumerate(card_list):
            if j % 8 == 0:
                x = PANEL_X_START - PANEL_X_INTERNAL
                y += PANEL_Y_INTERNAL
            x += PANEL_X_INTERNAL
            self.card_list.append(Card(x, y, index, 0.75))

    def checkcardRclick(self,rightmouse_pos):
        for card in self.card_list:
            if card.checkMouseRight(rightmouse_pos):
                print('checkcardRclick -> panel = for if')
                if card.canSelect():
                    print('checkcardRclick -> panel = for if속if')
                break

    def checkCardClick(self, mouse_pos):
        delete_card = None
        for card in self.selected_cards:
            if delete_card: # when delete a card, move right cards to left
                card.rect.x -= 55
                print('checkcardclick -> panel = for if')
            elif card.checkMouseClick(mouse_pos):
                print('checkcardclick -> panel = elif')
                self.deleteCard(card.name_index)
                delete_card = card

        if delete_card:
            print('checkcardclick -> panel = if delete_card')
            self.selected_cards.remove(delete_card)
            self.selected_num -= 1

        if self.selected_num == CARD_MAX: 
            print('checkcardclick -> panel = if selected_nul')
            return # CARD_MAX의 개수를 넘지 않기 위해 밑의 for문 실행 전 return으로 종료

        for card in self.card_list:
            if card.checkMouseClick(mouse_pos):
                print('checkcardclick -> panel = for if 2번째문')
                if card.canSelect():
                    print('checkcardclick -> panel = for if 속 if')
                    self.addCard(card)
                break

    def addCard(self, card):
        card.setSelect(False)
        y = 8
        x = 78 + self.selected_num * 55
        self.selected_cards.append(Card(x, y, card.name_index))
        if (card.name_index == 0):
            root = Tk()
            root.withdraw()
            msg.showinfo('Sunflower(해바라기아이템정보)', '일정 시간마다 25짜리 태양 에너지를 뱉는다. 하늘에서 떨어지는 에너지로는 턱없이 부족하기 때문에 필수로 써야 하는 식물')  
        elif (card.name_index == 1):
            root = Tk()
            root.withdraw()
            msg.showinfo('Peashooter(콩슈터아이템정보)','가장 기본적인 식물. 심은 라인 끝가지 날아가는 완두콩을 발사한다.')
        elif (card.name_index ==2):
            root = Tk()
            root.withdraw()
            msg.showinfo('Snow pea(얼음완두콩아이템정보)','Peashooter와 같지만 맞은 좀비는 둔해진다. 식물을 먹는 속도도 절반이 되기 때문에 가치가 매우 높다.')
        elif(card.name_index ==3):
            root = Tk()
            root.withdraw()
            msg.showinfo('Wall-nut(호두아이템정보)','맷집이 좋은 방어용 식물. 라인 제일 앞에 세워두는 벽 역할을 하는 식물이다.')
        elif(card.name_index == 4):
            root = Tk()
            root.withdraw()
            msg.showinfo('Cherry Bomb(체리밤아이템정보)', '심은 뒤 2초뒤에 폭발하면서 심은 곳과 주변 8칸에 피해를 준다. 설치하자마자 좀비에게 짖눌리면 그냥 사라진다.')
        elif(card.name_index == 5):
            root = Tk()
            root.withdraw()
            msg.showinfo('Threepeater(삼발슈터아이템정보)','머리 하나가 각각 한 줄을 책임진다. 줄 하나당 위력은 콩슈터아이템과 같다. 맨 윗줄 밑줄에 배치할 경우, 한 줄은 무시되고 나머지 두 줄만 쏘게 된다.')
        elif(card.name_index == 6):
            root = Tk()
            root.withdraw()
            msg.showinfo('Repeater(더블슈터아이템정보)','콩슈터의 강화판. 한 번에 완두콩을 두 발 씩 날린다.')
        elif(card.name_index == 7):
            root = Tk()
            root.withdraw()
            msg.showinfo('Chomper(먹개비아이템정보)','2칸 앞까지 다가온 좀비를 잡아먹는 아이템이다. 단점은 좀비를 소화하는 시간이 길다.')
        elif(card.name_index == 8):
            root = Tk()
            root.withdraw()
            msg.showinfo('Puff-Shroom(퍼프버섯아이템정보)','포자를 쏘는 아이템이다. 심는데 태양이 들리 않고, 공격력은 콩슈터와 같지만 사정거리는 전방 3칸으로 짧은 편이다.')
        elif(card.name_index == 9):
            root = Tk()
            root.withdraw()
            msg.showinfo('Potato Mine(감자지뢰아이템정보)','심으면 텀을 두고 장전되는 아이템이다. 가격에 비해서 위력이 좋지만 올라오는데 시간이 걸리니 적어도 좀비와 4칸 이상 거리를 둬야한다.')
        elif(card.name_index == 10):
            root = Tk()
            root.withdraw()
            msg.showinfo('SQuash(스쿼시아이템정보)','앞이나 뒤에 좀비가 있으면 뛰어올라 좀비를 깔아뭉개 죽이는 아이템이다. 즉시 발동하고 점프 사정거리는 2칸이다.')
        elif(card.name_index == 11):
            root = Tk()
            root.withdraw()
            msg.showinfo('Spikeweed(스파이크위드아이템정보)','가식덩굴아이템이다. 바닥에 심으면 위를 지나는 좀비들을 찔러 공격한다. ')
        elif(card.name_index == 12):
            root = Tk()
            root.withdraw()
            msg.showinfo('Halapeno(할라페뇨아이템정보)','심으면 자폭하여 한줄을 태우는 아이템이다.')
        elif(card.name_index == 13):
            root = Tk()
            root.withdraw()
            msg.showinfo('Scaredy-shroom(겁쟁이버섯아이템정보)','콩슈터와 능력치가 같지만 가격은 콩슈터의 1/4이다. 왜냐하면 자신 주위 3X3 범위 내에 좀비가 출몰하면 숨어버려 공격을 하지 않게되기 때문이다. 그래서 주로 후방에 심는다.')
        elif(card.name_index == 14):
            root = Tk()
            root.withdraw()
            msg.showinfo('Sun-shroom(태양버섯아이템정보)','밤에 에너지를 생산할 수 있는 버섯. 밤에는 해바라기 생산력이 떨어지기 때문에 이 식물로 대체해야 한다. 성장하기전엔 생산하는 에너지량은 15지만 5개의 태양에너지를 생산한 뒤 성장하여 25짜리 에너지를 생성한다.')
        elif(card.name_index == 15 ):
            root = Tk()
            root.withdraw()
            msg.showinfo('Ice-shroom(얼음버섯아이템정보','심은 뒤 2초 후 폭발하면서 화면상의 모든 좀비들을 일정 시간 멈추게 한다. 멈춘것이 풀리면 좀비들은 느려지게된다.')
        elif(card.name_index == 16):
            root = Tk()
            root.withdraw()
            msg.showinfo('Hypno-shroom(최면버섯아이템정보)','좀비가 이 식물을 먹으면 해당 좀비는 즉시 아군이 된다.')
        self.selected_num += 1
        print('addcard')

    def deleteCard(self, index):
        print('deletecatd')
        self.card_list[index].setSelect(True)

    def checkStartButtonClick(self, mouse_pos):
        if self.selected_num < CARD_MIN:
            return False # return True는 조건에 해당됐을때 바로 실행

        # 마우스가 start 버튼안에 있는지 없는지 확인
        x, y = mouse_pos
        if (x >= self.button_rect.x and x <= self.button_rect.right and
            y >= self.button_rect.y and y <= self.button_rect.bottom):
           return True 
        return False

    def getSelectedCards(self):
        card_index_list = []
        for card in self.selected_cards:
            card_index_list.append(card.name_index)
        return card_index_list

    def draw(self, surface):
        self.menu_image.blit(self.value_image, self.value_rect)
        surface.blit(self.menu_image, self.menu_rect)
        surface.blit(self.panel_image, self.panel_rect)
        for card in self.card_list:
            card.draw(surface)
        for card in self.selected_cards:
            card.draw(surface)

        if self.selected_num >= CARD_MIN:
            surface.blit(self.button_image, self.button_rect)

class MoveCard():
    def __init__(self, x, y, card_name, plant_name, scale=0.78):
        self.loadFrame(card_name, scale)
        self.rect = self.orig_image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.w = 1
        self.image = self.createShowImage()

        self.card_name = card_name
        self.plant_name = plant_name
        self.move_timer = 0
        self.select = True

    def loadFrame(self, name, scale):
        frame = tool.GFX[name]
        rect = frame.get_rect()
        width, height = rect.w, rect.h

        self.orig_image = tool.get_image(frame, 0, 0, width, height, c.BLACK, scale)
        self.orig_rect = self.orig_image.get_rect()
        self.image = self.orig_image

    def checkMouseClick(self, mouse_pos):
        x, y = mouse_pos
        if(x >= self.rect.x and x <= self.rect.right and
           y >= self.rect.y and y <= self.rect.bottom):
            return True
        return False

    def createShowImage(self):
        '''create a part card image when card appears from left'''
        if self.rect.w < self.orig_rect.w: #create a part card image
            image = pg.Surface([self.rect.w, self.rect.h])
            image.blit(self.orig_image, (0, 0), (0, 0, self.rect.w, self.rect.h))
            self.rect.w += 1
        else:
            image = self.orig_image
        return image

    def update(self, left_x, current_time):
        if self.move_timer == 0:
            self.move_timer = current_time
        elif (current_time - self.move_timer) >= c.CARD_MOVE_TIME:
            if self.rect.x > left_x:
                self.rect.x -= 1
                self.image = self.createShowImage()
            self.move_timer += c.CARD_MOVE_TIME

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class MoveBar():
    def __init__(self, card_pool):
        self.loadFrame(c.MOVEBAR_BACKGROUND)
        self.rect = self.image.get_rect()
        self.rect.x = 90
        self.rect.y = 0
        
        self.card_start_x = self.rect.x + 8
        self.card_end_x = self.rect.right - 5
        self.card_pool = card_pool
        self.card_list = []
        self.create_timer = -c.MOVEBAR_CARD_FRESH_TIME

    def loadFrame(self, name):
        frame = tool.GFX[name]
        rect = frame.get_rect()
        frame_rect = (rect.x, rect.y, rect.w, rect.h)

        self.image = tool.get_image(tool.GFX[name], *frame_rect, c.WHITE, 1)

    def createCard(self):
        if len(self.card_list) > 0 and self.card_list[-1].rect.right > self.card_end_x:
            return False
        x = self.card_end_x
        y = 6
        index = random.randint(0, len(self.card_pool) - 1)
        card_index = self.card_pool[index]
        card_name = card_name_list[card_index] + '_move'
        plant_name = plant_name_list[card_index]
        self.card_list.append(MoveCard(x, y, card_name, plant_name))
        return True

    def update(self, current_time):
        self.current_time = current_time
        left_x = self.card_start_x
        for card in self.card_list:
            card.update(left_x, self.current_time)
            left_x = card.rect.right + 1

        if(self.current_time - self.create_timer) > c.MOVEBAR_CARD_FRESH_TIME:
            if self.createCard():
                self.create_timer = self.current_time

    def checkCardClick(self, mouse_pos):
        result = None
        for index, card in enumerate(self.card_list):
            if card.checkMouseClick(mouse_pos):
                result = (card.plant_name, card)
                break
        return result
    
    def checkMenuBarClick(self, mouse_pos):
        x, y = mouse_pos
        if(x >= self.rect.x and x <= self.rect.right and
           y >= self.rect.y and y <= self.rect.bottom):
            return True
        return False

    def deleateCard(self, card):
        self.card_list.remove(card)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        for card in self.card_list:
            card.draw(surface)