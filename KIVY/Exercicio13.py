from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from ExercicioBanco import ConectandoBanco

class MyCadastroMenu(Screen):
    def __init__(self, **kw):
        super(MyCadastroMenu, self).__init__(**kw)

        self.layout = BoxLayout(orientation="vertical")

        self.inp_cadastro = Button(text="Cadastro")
        self.inp_exit = Button(text="Sair")

        self.inp_cadastro.bind(on_press=self.ota_tela)
        self.inp_exit.bind(on_press=self.exit_close)

        self.layout.add_widget(self.inp_cadastro)
        self.layout.add_widget(self.inp_exit)

        self.add_widget(self.layout)

    def ota_tela(self, instance):
        self.manager.current = 'outra_tela'

    def exit_close(self, instance):
        App.get_running_app().stop()


class MyCadastro(Screen):
    def __init__(self, **kw):
        super(MyCadastro, self).__init__(**kw)

        self.layout = BoxLayout(orientation = "horizontal")
        self.grid = GridLayout(cols = 2, size_hint = (1, 1))

        self.lbl_nome = Label(text="Digite seu nome", font_size = 25)
        self.inp_nome = TextInput()

        self.lbl_cpf = Label(text="Digite seu CPF", font_size = 25)
        self.inp_cpf = TextInput()

        self.lbl_senha = Label(text="Digite sua Senha", font_size = 25)
        self.inp_senha = TextInput(password=True)

        self.lbl_gmail = Label(text="Digite seu GMAIL", font_size = 25)
        self.inp_gmail = TextInput()

        self.btn_confirm = Button(text="Confirmar Cadastro", font_size=20, on_press=self.ConfirmarCadastros)
        self.btn_sair = Button(text="Sair")

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
        
        
        
    def ConfirmarCadastros(self, instace):
        nome = self.inp_nome.text
        cpf = self.inp_cpf.text
        gmail = self.inp_gmail.text
        senha = self.inp_senha.text
    
        db = ConectandoBanco()
        db.insert_values(nome, cpf, senha, gmail)
    

class RunAplicationCadastro(App):
    def build(self):
        
        screen_manager = ScreenManager()
        screen_manager.add_widget(MyCadastroMenu(name='menu'))
        screen_manager.add_widget(MyCadastro(name='outra_tela'))
        return screen_manager


if __name__ == "__main__":
    RunAplicationCadastro().run()
