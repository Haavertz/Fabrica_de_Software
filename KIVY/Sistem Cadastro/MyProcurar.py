from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from ExercicioBanco import ExercicioBanco


class MyProcurar(Screen):
    def __init__(self, **kw):
        super(MyProcurar, self).__init__(**kw)

        self.layout = BoxLayout(orientation = "horizontal")
        self.grid = GridLayout(cols = 2, size_hint = (1, 1))

        self.lbl_id = Label(text="ID", font_size = 25)
        self.inp_id = TextInput()

        self.lbl_nome = Label(text="Nome", font_size = 25)
        self.inp_nome = TextInput()

        self.lbl_cpf = Label(text="CPF", font_size = 25)
        self.inp_cpf = TextInput(input_filter = 'int')

        self.lbl_senha = Label(text="Senha", font_size = 25)
        self.inp_senha = TextInput()

        self.lbl_gmail = Label(text="GMAIL", font_size = 25)
        self.inp_gmail = TextInput()

        self.btn_confirm = Button(text="Procurar", font_size=20, on_press=self.procurar)
        self.btn_sair = Button(text="Sair", font_size=20, on_press=self.sair)
        
        self.grid.add_widget(self.lbl_id)
        self.grid.add_widget(self.inp_id)
        self.grid.add_widget(self.lbl_nome)
        self.grid.add_widget(self.inp_nome)
        self.grid.add_widget(self.lbl_cpf)
        self.grid.add_widget(self.inp_cpf)
        self.grid.add_widget(self.lbl_gmail)
        self.grid.add_widget(self.inp_gmail)
        self.grid.add_widget(self.lbl_senha)
        self.grid.add_widget(self.inp_senha)
        self.grid.add_widget(self.btn_sair)
        self.grid.add_widget(self.btn_confirm)

        self.layout.add_widget(self.grid)
        self.add_widget(self.layout)
        
        
    def sair(self, instace):
        self.manager.current = 'menu'
        
    def procurar(self, instace):
        id_user = self.inp_id.text
        
        bd = ExercicioBanco()
        bd.select_values(id_user)
        
        try:
                                
            self.inp_nome.text = bd.resultado[1]
            self.inp_cpf.text = bd.resultado[2]
            self.inp_senha.text = bd.resultado[3]
            self.inp_gmail.text = bd.resultado[4]
        except:
            print("Não tem nada neste ID")
