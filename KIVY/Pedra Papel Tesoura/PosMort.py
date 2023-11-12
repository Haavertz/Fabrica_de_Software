from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from ScreenGame import GameScreen

class LifeDead(Screen):
    def __init__(self, **kw):
        super(LifeDead, self).__init__(**kw)

        layout = BoxLayout(orientation="vertical")

        self.lbl = Label(text="                                  PERDEU PÁ MAQUINA \n KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK", font_size=30, size_hint=(1,0.3))

        self.img_cat = Image(source="Midia/cat.png", fit_mode="fill")
        self.button = Button(text="Exit", size_hint=(1,0.2))
        self.button3 = Button(text="Restart to Game", size_hint=(1, 0.2))

        self.button.bind(on_press = self.Exit)
        self.button3.bind(on_press=self.Restart)

        layout.add_widget(self.lbl)
        layout.add_widget(self.img_cat)
        layout.add_widget(self.button3)
        layout.add_widget(self.button)

        self.add_widget(layout)

    def Exit(self, instace):
        App.get_running_app().stop()

    def Restart(self, instance):
        self.manager.remove_widget(self.manager.get_screen('tela_game'))
        self.manager.add_widget(GameScreen(name='tela_game'))
        self.manager.current = 'tela_game'



