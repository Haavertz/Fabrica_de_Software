from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from MyCadastro import MyCadastro
from MyCadastroMenu import MyCadastroMenu
from MyExcluirCadastro import MyExcluirCadastro 
from MyProcurar import MyProcurar

class RunAplicationCadastro(App):
    def build(self):
        
        screen_manager = ScreenManager()
        screen_manager.add_widget(MyCadastroMenu(name='menu'))
        screen_manager.add_widget(MyCadastro(name='outra_tela'))
        screen_manager.add_widget(MyExcluirCadastro(name='tela_excluir'))
        screen_manager.add_widget(MyProcurar(name='tela_procurar'))
        
        return screen_manager


if __name__ == "__main__":
    RunAplicationCadastro().run()
