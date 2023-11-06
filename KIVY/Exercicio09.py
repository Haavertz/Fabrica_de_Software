import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
class firstBotao(App):
    def build(self):
        layout = BoxLayout(orientation = 'vertical')
        grid = GridLayout(cols = 1, size_hint = (1, 0.4))

        button1 = Button(text = 'Cat')
        button1.bind(on_press=self.Cat)
        
        self.imagi = Image(fit_mode="fill")
        grid.add_widget(self.imagi)
        
        grid.add_widget(button1)

        button2 = Button(text = 'Dog')
        button2.bind(on_press = self.Dog)
        grid.add_widget(button2)

        layout.add_widget(grid)

        return layout
    
    def Cat(self, nstace):
        self.imagi.source = "Midia/cat.jpg"
        
    def Dog(self, instace):
        self.imagi.source = "Midia/dog.jpg"
        
    

if __name__ == '__main__':    
    firstBotao().run()