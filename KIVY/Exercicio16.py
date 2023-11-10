from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from ExercicioBanco import ExercicioBanco


class MyExcluirCadastro(Screen):
    def __init__(self, **kw):
        super(MyExcluirCadastro, self).__init__(**kw)

        self.layout = BoxLayout(orientation = "horizontal")
        self.grid = GridLayout(cols = 1, size_hint = (1, 1))

        self.lbl_id = Label(text="ID:")
        self.id = TextInput()

        self.btn_confirm = Button(text="Confirmar Exclusão", font_size=20, on_press=self.procurar)
        self.btn_sair = Button(text="Sair", font_size=20, on_press=self.sair)
        
        self.grid.add_widget(self.lbl_id)
        self.grid.add_widget(self.id)
        self.grid.add_widget(self.btn_confirm)
        self.grid.add_widget(self.btn_sair)

        self.layout.add_widget(self.grid)
        self.add_widget(self.layout)
        
        
    def sair(self, instace):
        self.manager.current = 'menu'
        
    def procurar(self, instace):
        number = str(self.id.text)
        
        bd = ExercicioBanco()
        bd.exclude_values(number)
        
