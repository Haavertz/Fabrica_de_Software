from kivymd.uix.button import MDRectangleFlatButton
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivy.metrics import dp

class MyApp(MDApp):
    def build(self):
        layout = MDBoxLayout(orientation="vertical")

        label = MDLabel(text="Hello, KivyMD!", halign="center")
        
        text_input = MDTextField(hint_text="Digite algo", helper_text="ou toque no botão abaixo", pos_hint={"center_x": 0.5}, size_hint_x=None, width=200)
        button = MDRectangleFlatButton(text="ENVIAR!", pos_hint={"center_x": 0.5}, height=dp(40))

        layout.add_widget(label)
        layout.add_widget(text_input)
        layout.add_widget(button)

        return layout

    
if __name__ == "__main__":
    MyApp().run()
