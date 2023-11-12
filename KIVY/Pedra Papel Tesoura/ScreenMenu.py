from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class MenuScreen(Screen):
    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)

        layout = BoxLayout(orientation="vertical")

        self.lbl = Label(text="Bem Vindo ao Pedra Papel e Tesoura", font_size=40)

        self.button = Button(text="Jogar", font_size=30)
        self.button2 = Button(text="Sair", font_size=30)
        
        self.button.bind(on_press=self.ButtonPress)
        self.button2.bind(on_press=self.ButtonPressExit)

        layout.add_widget(self.lbl)
        layout.add_widget(self.button)
        layout.add_widget(self.button2)

        self.add_widget(layout)

    def ButtonPress(self, instance):
        self.manager.current = 'tela_game'
        
    def ButtonPressExit(self, instance):
        App.get_running_app().stop()

