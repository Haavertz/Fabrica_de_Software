from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.selectioncontrol import MDCheckbox
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
            size_hint=(None,None),
            size=(250, 100),
            pos_hint={'center_x':0.5,'center_y': 0.5},
            padding = [0,0,0,0]
        )

        checkbox = MDCheckbox(
            size_hint=(None, None),
            size=(48, 48),
            halign="center",
            pos_hint={'center_y': 0.5},
            padding = [0,0,0,0],
            active = False
        
        )

        box_layout = MDBoxLayout(orientation='horizontal', padding=[0, 0, 0, 0], 
                                 line_color=(0,0,0,1), size_hint=(None, None), 
                                 size=(300, 100), pos_hint={'center_x':0.5,'center_y': -0.5})

        box_layout.add_widget(label)
        box_layout.add_widget(checkbox)

        frame = MDBoxLayout(orientation='vertical', size_hint_y=None, height=500)



        frame.md_bg_color = [1.0, 1.0, 1.0, 1.0] 
        frame.radius = [20, 20, 0, 0] 

        frame.add_widget(box_layout)

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