import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class firstBotao(App):
    def build(self):
        layout = BoxLayout(orientation = 'vertical')
        grid = GridLayout(cols = 1, size_hint = (1, 0.4))

        self.text_input = TextInput(text = 'Digite seu Nome')
        grid.add_widget(self.text_input)

        button1 = Button(text = 'Login')
        button1.bind(on_press=self.TroqueName)
        
        grid.add_widget(button1)

        button2 = Button(text = 'Cancelar')
        button2.bind(on_press = self.CancelText)
        grid.add_widget(button2)

        layout.add_widget(grid)

        return layout
    
    def CancelText(self, instace):
        self.text_input.text = ""
        
    def TroqueName(self, instace):
        self.text_input.text = "Mauricio"
        
    

if __name__ == '__main__':    
    firstBotao().run()