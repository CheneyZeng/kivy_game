import numpy as np
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.properties import StringProperty

def get_result():
    lis = ["你赢了!","你输了!"]
    return np.random.choice(lis,1)

class GameImage(ButtonBehavior, Image):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            if App.get_running_app().flag < 3:
                opponent = get_result()
                App.get_running_app().results.append(opponent)
                App.get_running_app().flag += 1
                App.get_running_app().context = "你已经完成 %s /3 轮了，本局 %s" % (str(App.get_running_app().flag), 
                                                                         opponent[0])
                print(App.get_running_app().context)
            elif App.get_running_app().flag == 3:
                print(App.get_running_app().results.count("你赢了!"))
                App.get_running_app().flag += 1
                if App.get_running_app().results.count("你赢了!")>1:
                    App.get_running_app().context = "本轮你赢了!"
                else:
                    App.get_running_app().context = "本轮你输了!"
            else:
                App.get_running_app().context = "重启游戏"
                print(App.get_running_app().context)

class RestartImage(ButtonBehavior, Image):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            App.get_running_app().flag = 0
            App.get_running_app().context = "请开始选择你的下一轮游戏，选择剪刀，石头，布"
            App.get_running_app().results = []
                

class Game(GridLayout):
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        App.get_running_app().context = "请开始选择你的下一轮游戏，选择剪刀，石头，布"

class GameApp(App):
    context = StringProperty()
    flag = 0
    results = []

    def build(self):
        self.load_kv('kivy-game.kv')
        return Game()