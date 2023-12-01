from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRaisedButton

import requests

class FruitApp(MDApp):
    def build(self):
        layout = MDBoxLayout(orientation='vertical')



        self.usuario = MDTextField(
            hint_text='User',
            helper_text='Enter the user name',
            helper_text_mode='on_focus'
        )
        self.password = MDTextField(
            hint_text='Password',
            helper_text='Enter the password',
            helper_text_mode='on_focus',
        )

        add_button = MDRaisedButton(
            text='Login',
            on_release=self.add_fruit
        )

        layout.add_widget(self.usuario)
        layout.add_widget(self.password)
        layout.add_widget(add_button)

        return layout

    def add_fruit(self, instance):
        user = self.usuario.text
        password = int(self.password.text)

        url = 'https://projetomodelos-6cdf6-default-rtdb.firebaseio.com/'
        requisicao = requests.get(f'{url}/adm/{user}/.json')

        dic_requisicao = requisicao.json()
        
        try:
            if password == int(dic_requisicao['senha']):
                print("Estrou caralhoooooooooo!")
            else:
                print("Errou")  
        except:
            print("Errou Try")


if __name__ == '__main__':
    FruitApp().run()
