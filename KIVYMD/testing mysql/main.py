from kivymd.uix.button import MDRectangleFlatButton
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from bancorest import BancoDS

class Main(MDApp):
    def build(self, **kwargs):
        super().__init__(**kwargs)
        
        layout = MDBoxLayout(orientation="vertical")
        
        self.lbl_titulo = MDLabel(text="Funcionouu!!!!!")
        self.btn_trocar = MDRectangleFlatButton(text="trocar", pos_hint={'center_x': 0.5, 'center_y': 0.5}, on_press=self.banco)
        self.btn_trocar2 = MDRectangleFlatButton(text="Conectar no Banco", pos_hint={'center_x': 0.5, 'center_y': 0.5}, on_press=self.bd)
        self.btn_trocar3 = MDRectangleFlatButton(text="Trocar Normal", pos_hint={'center_x': 0.5, 'center_y': 0.5}, on_press=self.text2)
        
        layout.add_widget(self.lbl_titulo)
        layout.add_widget(self.btn_trocar3)
        layout.add_widget(self.btn_trocar)
        layout.add_widget(self.btn_trocar2)
            
        return layout
    
    def bd(self, instace):
        self.tent = BancoDS()
        
    def banco(self, instance):
        self.tent.list_values()
        self.lbl_titulo.text = f"{self.tent.result[0]}"
        
    def text2(self, instace):
        self.lbl_titulo.text = f"Trocou normal"

if __name__ == "__main__":
    Main().run()
