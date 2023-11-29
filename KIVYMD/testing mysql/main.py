from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton

import requests
import json

class FruitApp(MDApp):
    def build(self):
        layout = MDBoxLayout(orientation='vertical')

        self.inp_fruit = MDTextField(
            hint_text='Fruit',
            helper_text='Enter the fruit name',
            helper_text_mode='on_focus'
        )
        self.inp_value = MDTextField(
            hint_text='Value',
            helper_text='Enter the value of the fruit',
            helper_text_mode='on_focus',
            input_filter='float'
        )

        add_button = MDRaisedButton(
            text='Add Fruit',
            on_release=self.add_fruit
        )

        layout.add_widget(self.inp_fruit)
        layout.add_widget(self.inp_value)
        layout.add_widget(add_button)

        return layout

    def add_fruit(self, instance):
        fruit_input = self.inp_fruit.text
        value_input = self.inp_value.text

        url = 'https://modelos2-8ae7c-default-rtdb.firebaseio.com/'


        id_personalizado = 'Fruta'

        dados = {
            'Frutas':fruit_input,
            'Valores':value_input
        }

        requisicao = requests.post(f'{url}/Produtos/{id_personalizado}.json', data=json.dumps(dados))




if __name__ == '__main__':
    FruitApp().run()
