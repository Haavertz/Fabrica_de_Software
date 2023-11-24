from kivymd.uix.button import MDRectangleFlatButton
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from bancorest import BancoDS

class Main(MDApp):
    def build(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = MDBoxLayout(orientation = "vertical")
        
        self.lbl_titulo = MDLabel(text="Funcionouu!!!!!")
        self.btn_trocar = MDRectangleFlatButton(text="trocar", pos_hint = {'center_x': 0.5, 'center_y': 0.5}, on_press = self.banco)
        
        layout.add_widget(self.lbl_titulo)
        layout.add_widget(self.btn_trocar)
        
        return layout
    
    def banco(self, instace):
        tent = BancoDS()
        tent.list_values()
        self.lbl_titulo.text = f"{tent.result[0]}"
        
        
if __name__ == "__main__":
    Main().run()