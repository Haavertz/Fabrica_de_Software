from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.clock import Clock

import time
import random

class GameScreen(Screen):
    def __init__(self, **kw):
        super(GameScreen, self).__init__(**kw)

        layout = BoxLayout(orientation="vertical")
        layout_2 = BoxLayout(orientation="vertical")
        self.layout3 = BoxLayout(orientation="vertical")

        self.grid = GridLayout(cols=3, size_hint=(1, 1))
        self.grid_2 = GridLayout(cols=1, size_hint=(1, 0.2))

        self.image_pedra = Image(source="Midia/pedra.png", fit_mode="fill")
        self.image_tesoura = Image(source="Midia/tesoura.png", fit_mode="fill")
        self.image_papel = Image(source="Midia/papel.png", fit_mode="fill")

        self.image_pedra2 = Image(source="Midia/pedra.png", fit_mode="fill")
        self.image_tesoura2 = Image(source="Midia/tesoura.png", fit_mode="fill")
        self.image_papel2 = Image(source="Midia/papel.png", fit_mode="fill")

        self.lbl = Label(text=" X ", size_hint=(1, 0.5), font_size=20)
        self.vida = Label(text="❤️ ❤️ ❤️",font_name = "seguiemj", font_size=20, size_hint=(1, 0.5))
        self.victoria = Label(text="Vitorias: ", font_size=20, size_hint=(1, 0.5))

        vida_lbl_layout = BoxLayout(orientation="vertical")
        vida_lbl_layout.add_widget(self.vida)
        vida_lbl_layout.add_widget(self.lbl)
        vida_lbl_layout.add_widget(self.victoria)


        self.button = Button(text="Pedra", size_hint=(0.3, 0.3), on_press=self.pedra_point)
        self.button2 = Button(text="Tesoura", size_hint=(0.3, 0.3), on_press=self.tesoura_point)
        self.button3 = Button(text="Papel", size_hint=(0.3, 0.3), on_press=self.papel_point)
        self.button_sair = Button(text="Sair", size_hint=(1, 1), on_press=self.ButtonPress)

        self.number_random = random.randint(1, 3)

        layout_2.add_widget(self.image_pedra)
        layout_2.add_widget(self.image_tesoura)
        layout_2.add_widget(self.image_papel)

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

        Clock.schedule_once(lambda dt: self.voltarEstadoJogador(value), 0.7)
        Clock.schedule_once(lambda dt: self.voltarEstadoMaquina(value_random), 0.7)

        self.number_random = random.randint(1, 3)

    def voltarEstadoJogador(self, value):
        if value == 1:
            self.image_papel2.source = "Midia/papel.png"
            self.image_tesoura2.source = "Midia/tesoura.png"
        elif value == 2:
            self.image_papel2.source = "Midia/papel.png"
            self.image_pedra2.source = "Midia/pedra.png"
        else:
            self.image_tesoura2.source = "Midia/tesoura.png"
            self.image_pedra2.source = "Midia/pedra.png"

        self.lbl.text = " X "

    def voltarEstadoMaquina(self, value):
        if value == 1:
            self.image_papel.source = "Midia/papel.png"
            self.image_tesoura.source = "Midia/tesoura.png"
        elif value == 2:
            self.image_papel.source = "Midia/papel.png"
            self.image_pedra.source = "Midia/pedra.png"
        else:
            self.image_tesoura.source = "Midia/tesoura.png"
            self.image_pedra.source = "Midia/pedra.png"

    def Life(self, num):
        if num == 1:
            self.vida.text = "❤️ ❤️"

        elif num == 2:
            self.vida.text = "❤️"

        else:
            self.vida.text = "Você Perdeu o Jogo"
            self.numberLife = 0
            time.sleep(0.3)
            self.manager.current = 'pos_derrota'
            
    def Victory(self, num):
        try: 
            if int(num) == 3:
                time.sleep(0.3)
                self.manager.current ='pos_victory'
            if int(num):
                self.victoria.text = self.victoria.text + "*"
            else:
                self.numbervictory = ""
        except:
            print("ERROR")
        
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
        
