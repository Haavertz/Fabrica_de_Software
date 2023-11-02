from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class HelloWorld(App):
    def build(self):
        
        layout = BoxLayout(orientation="vertical")
        tamanho = "40"
        self.label = Label(text="Hello World !!", font_size = tamanho)
        self.button = Button(text="Soy un Boton", size_hint=(1, 0.5))
        self.button.bind(on_press = self.on_button)
        layout.add_widget(self.label)
        layout.add_widget(self.button)
        
        return layout

    def on_button(self, instance):
        self.label.text = "Soy un botón du mal"

if __name__ == "__main__":
    HelloWorld().run()
