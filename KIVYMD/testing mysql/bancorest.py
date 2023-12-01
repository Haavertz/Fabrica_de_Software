from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen


class Tela_Principal(MDScreen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'


        layout = MDBoxLayout(orientation='vertical')
        
        color_start = [0.9529411764705882, 0.47843137254901963, 0.34901960784313724, 1.0] 
        layout.md_bg_color = color_start

        label = MDLabel(
            text="Escolha seu serviço e seu horário:",
            halign="center",
            size_hint=(None, None),
            size=(200, 100),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            line_color=(0, 0, 0, 1),
            markup=True
        )

        checkbox = MDCheckbox(
            size_hint=(None, None),
            size=(48, 48),
            pos_hint={'center_y': 0.5} 
        )


        frame = MDBoxLayout(orientation='vertical', size_hint_y=None, height=500, padding=[10, 10, 10, 10])
        frame.md_bg_color = [1.0, 1.0, 1.0, 1.0] 
        frame.radius = [20, 20, 0, 0] 
    
        frame.add_widget(checkbox)

        frame.add_widget(label)
        layout.add_widget(frame)

        self.add_widget(layout)

class Main(MDApp):
    def build(self):
        screen_manager = ScreenManager()
        
        tela_principal = Screen(name='tela_principal')
        tela_principal.add_widget(Tela_Principal())
        screen_manager.add_widget(tela_principal)

        return screen_manager

if __name__ == '__main__':
    Main().run()