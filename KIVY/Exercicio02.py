from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class LoginScreen(App):
    def build(self):
        
        layout = BoxLayout(orientation="vertical")
        
        self.username = TextInput(multiline = True)
        self.password = TextInput(multiline = True, password = True)
        self.button = Button(text="Clique-me")
        self.button.bind(on_press = self.ButtonPress)
        self.lbl = Label()
        
        layout.add_widget(Label(text="User", font_size = 30))
        layout.add_widget(Label(text="Password",  font_size = 30))
        layout.add_widget(self.username)
        layout.add_widget(self.password)
        layout.add_widget(self.button)
        layout.add_widget(self.lbl)

        return layout
        
    def ButtonPress(self, instace):
        self.lbl.text = ("Bem vindo")

        
        

if __name__ == '__main__':
    LoginScreen().run()
