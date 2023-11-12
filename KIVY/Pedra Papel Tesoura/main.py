from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from ScreenMenu import MenuScreen
from ScreenGame import GameScreen
from PosMort import LifeDead
from PosVictoyy import VictoryGame

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
