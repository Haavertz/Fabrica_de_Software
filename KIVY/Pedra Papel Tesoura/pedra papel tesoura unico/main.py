from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.clock import Clock
import random

class MenuScreen(Screen):
    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)

        layout = BoxLayout(orientation="vertical")

        self.lbl = Label(text="Bem Vindo ao Pedra Papel e Tesoura", font_size=40)
        self.descript = Label(text="Suas vidas serao = @@@ \n Suas vitorias serao = ***", font_size=40)

        self.button = Button(text="Jogar", font_size=30)
        self.button2 = Button(text="Sair", font_size=30)

        self.button.bind(on_press=self.ButtonPress)
        self.button2.bind(on_press=self.ButtonPressExit)

        layout.add_widget(self.lbl)
        layout.add_widget(self.descript)
        layout.add_widget(self.button)
        layout.add_widget(self.button2)

        self.add_widget(layout)

    def ButtonPress(self, instance):
        self.manager.current = 'tela_game'

    def ButtonPressExit(self, instance):
        App.get_running_app().stop()


class GameScreen(Screen):
    def __init__(self, **kw):
        super(GameScreen, self).__init__(**kw)

        layout = BoxLayout(orientation="vertical")
        layout_2 = BoxLayout(orientation="vertical")
        self.layout3 = BoxLayout(orientation="vertical")

        self.grid = GridLayout(cols=3, size_hint=(1, 1))
        self.grid_2 = GridLayout(cols=1, size_hint=(1, 0.2))

        self.image_pedra = Image(source="pedra.png", fit_mode="fill")
        self.image_tesoura = Image(source="tesoura.png", fit_mode="fill")
        self.image_papel = Image(source="papel.png", fit_mode="fill")

        self.image_pedra2 = Image(source="pedra.png", fit_mode="fill")
        self.image_tesoura2 = Image(source="tesoura.png", fit_mode="fill")
        self.image_papel2 = Image(source="papel.png", fit_mode="fill")

        self.lbl = Label(text=" X ", size_hint=(1, 0.5), font_size=20)
        self.vida = Label(text="@@@", font_size=20, size_hint=(1, 0.5))
        self.victoria = Label(text="Vitorias: ", font_size=20, size_hint=(1, 0.5))

        vida_lbl_layout = BoxLayout(orientation="vertical")
        vida_lbl_layout.add_widget(self.vida)
        vida_lbl_layout.add_widget(self.lbl)
        vida_lbl_layout.add_widget(self.victoria)

        self.button = Button(text="Pedra", size_hint=(0.3, 0.3), on_press=self.pedra_point)
        self.button2 = Button(text="Tesoura", size_hint=(0.3, 0.3), on_press=self.tesoura_point)
        self.button3 = Button(text="Papel", size_hint=(0.3, 0.3), on_press=self.papel_point)
        self.button_sair = Button(text="Exit", size_hint=(1, 1), on_press=self.ButtonPress)

        self.number_random = random.randint(1, 3)

        label_voce = Label(text="VOCÊ", size_hint=(1, 0.1), halign="center", font_size=18)
        label_maquina = Label(text="MAQUINA", size_hint=(1, 0.1), halign="center", font_size=18)

        layout_2.add_widget(label_maquina)
        layout_2.add_widget(self.image_pedra)
        layout_2.add_widget(self.image_tesoura)
        layout_2.add_widget(self.image_papel)

        self.layout3.add_widget(label_voce)
        self.layout3.add_widget(self.image_pedra2)
        self.layout3.add_widget(self.image_tesoura2)
        self.layout3.add_widget(self.image_papel2)

        self.grid.add_widget(layout_2)
        self.grid.add_widget(vida_lbl_layout)
        self.grid.add_widget(self.layout3)

        self.grid.add_widget(self.button)
        self.grid.add_widget(self.button2)
        self.grid.add_widget(self.button3)

        self.grid_2.add_widget(self.button_sair)
        layout.add_widget(self.grid)

        layout.add_widget(self.grid_2)
        self.add_widget(layout)

        self.numberLife = 0
        self.numbervictory = 0

    def ButtonPress(self, instace):
        self.manager.current = 'menu'

    def pedra_point(self, instace):
        self.cheking(1, self.number_random)
        self.image_papel2.source = ""
        self.image_tesoura2.source = ""

    def tesoura_point(self, instace):
        self.cheking(2, self.number_random)
        self.image_papel2.source = ""
        self.image_pedra2.source = ""

    def papel_point(self, instace):
        self.cheking(3, self.number_random)
        self.image_tesoura2.source = ""
        self.image_pedra2.source = ""

    def cheking(self, value, value_random):
        self.point_maquina()

        if value == value_random:
            self.lbl.text = "Empate"
        elif ((value == 1 and value_random == 2)
              or (value == 2 and value_random == 3)
              or (value == 3 and value_random == 1)):
            self.lbl.text = "Você Ganhou"
            self.numbervictory += 1
            self.Victory(self.numbervictory)
        else:
            self.lbl.text = "Você Perdeu"
            self.numberLife += 1
            self.Life(self.numberLife)

        Clock.schedule_once(lambda dt: self.voltarEstadoJogador(value), 1.8)
        Clock.schedule_once(lambda dt: self.voltarEstadoMaquina(value_random), 1.8)

        self.number_random = random.randint(1, 3)

    def voltarEstadoJogador(self, value):
        if value == 1:
            self.image_papel2.source = "papel.png"
            self.image_tesoura2.source = "tesoura.png"
        elif value == 2:
            self.image_papel2.source = "papel.png"
            self.image_pedra2.source = "pedra.png"
        else:
            self.image_tesoura2.source = "tesoura.png"
            self.image_pedra2.source = "pedra.png"

        self.lbl.text = " X "

    def voltarEstadoMaquina(self, value):
        if value == 1:
            self.image_papel.source = "papel.png"
            self.image_tesoura.source = "tesoura.png"
        elif value == 2:
            self.image_papel.source = "papel.png"
            self.image_pedra.source = "pedra.png"
        else:
            self.image_tesoura.source = "tesoura.png"
            self.image_pedra.source = "pedra.png"

    def Life(self, num):
        if num == 1:
            self.vida.text = "@@"
        elif num == 2:
            self.vida.text = "@"
        else:
            self.vida.text = "Você Perdeu o Jogo"
            self.numberLife = 0
            self.manager.current = 'pos_derrota'

    def Victory(self, num):
        if int(num) == 3:
            self.manager.current = 'pos_victory'
        if int(num):
            self.victoria.text = self.victoria.text + "*"
        else:
            self.numbervictory = ""

    def point_maquina(self):
        if self.number_random == 1:
            self.image_papel.source = ""
            self.image_tesoura.source = ""
            
        elif self.number_random == 2:
            self.image_papel.source = ""
            self.image_pedra.source = ""
            
        else:
            self.image_tesoura.source = ""
            self.image_pedra.source = ""

class LifeDead(Screen):
    def __init__(self, **kw):
        super(LifeDead, self).__init__(**kw)

        layout = BoxLayout(orientation="vertical")

        self.lbl = Label(text="Você perdeu!", font_size=30, size_hint=(1, 0.3))
        self.lbl2 = Label(text="KKKKKKKKKKKKKKKKKKKKKKKKK", font_size=15, size_hint=(1, 0.3))
        self.img_cat = Image(source="cat.png", fit_mode="fill")
        self.button3 = Button(text="Resetar o jogo", on_press=self.Restart)
        self.button = Button(text="Sair", on_press=self.Exit)

        layout.add_widget(self.lbl)
        layout.add_widget(self.lbl2)
        layout.add_widget(self.img_cat)
        layout.add_widget(self.button3)
        layout.add_widget(self.button)

        self.add_widget(layout)

    def Exit(self, instance):
        App.get_running_app().stop()

    def Restart(self, instance):
        self.manager.remove_widget(self.manager.get_screen('tela_game'))
        self.manager.add_widget(GameScreen(name='tela_game'))
        self.manager.current = 'tela_game'

class VictoryGame(Screen):
    def __init__(self, **kw):
        super(VictoryGame, self).__init__(**kw)

        layout = BoxLayout(orientation="vertical")

        self.lbl = Label(text="Você ganhou", font_size=30, size_hint=(1, 0.3))
        self.lbl2 = Label(text="Tá esperto ein malandro", font_size=15, size_hint=(1, 0.3))
        self.img_cat = Image(source="cat_victory.jpg", fit_mode="fill")
        self.button = Button(text="Sair", size_hint=(1, 0.2))
        self.button2 = Button(text="Resetar o jogo", size_hint=(1, 0.2))

        self.button2.bind(on_press=self.Restart)
        self.button.bind(on_press=self.Exit)

        layout.add_widget(self.lbl)
        layout.add_widget(self.lbl2)
        layout.add_widget(self.img_cat)
        layout.add_widget(self.button2)
        layout.add_widget(self.button)
        self.add_widget(layout)

    def Exit(self, instance):
        App.get_running_app().stop()

    def Restart(self, instance):
        self.manager.remove_widget(self.manager.get_screen('tela_game'))
        self.manager.add_widget(GameScreen(name='tela_game'))
        self.manager.current = 'tela_game'

class RunAplicationCadastro(App):
    def build(self):

        screen_manager = ScreenManager()
        screen_manager.add_widget(MenuScreen(name='menu'))
        screen_manager.add_widget(GameScreen(name='tela_game'))
        screen_manager.add_widget(LifeDead(name='pos_derrota'))
        screen_manager.add_widget(VictoryGame(name='pos_victory'))

        return screen_manager

if __name__ == "__main__":
    RunAplicationCadastro().run()
