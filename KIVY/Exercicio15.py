from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.app import App


class MyCadastroMenu(Screen):
    def __init__(self, **kw):
        super(MyCadastroMenu, self).__init__(**kw)

        self.layout = BoxLayout(orientation="vertical")

        self.inp_cadastro = Button(text="Cadastro")
        self.btn_excluir = Button(text="Excluir")
        self.btn_procurar = Button(text="Procurar")
        self.inp_exit = Button(text="Sair")

        self.btn_excluir.bind(on_press=self.ota_tela_excluir)
        self.inp_cadastro.bind(on_press=self.ota_tela)
        self.inp_exit.bind(on_press=self.exit_close)
        self.btn_procurar.bind(on_press=self.tela_procurar)
        
        self.layout.add_widget(self.inp_cadastro)
        self.layout.add_widget(self.btn_procurar)
        self.layout.add_widget(self.btn_excluir)
        self.layout.add_widget(self.inp_exit)

        self.add_widget(self.layout)
        
    def ota_tela_excluir(self, instace):
        self.manager.current = 'tela_excluir'

    def ota_tela(self, instance):
        self.manager.current = 'outra_tela'
    
    def tela_procurar(self, instace):
        self.manager.current = 'tela_procurar'
    
    
    def exit_close(self, instance):
        App.get_running_app().stop()

  