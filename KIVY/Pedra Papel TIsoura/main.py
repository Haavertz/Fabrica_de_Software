from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

class RunAplicationCadastro(App):
    def build(self):
        
        screen_manager = ScreenManager()        
        return screen_manager


if __name__ == "__main__":
    RunAplicationCadastro().run()
