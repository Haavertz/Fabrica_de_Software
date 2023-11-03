from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class MainWindow(App):
    def build(self):

        layout = BoxLayout(orientation = "vertical")

        l = Label(text='Hello world', font_size='40px')
        
        layout.add_widget(l)

        return layout
    
if __name__ == "__main__":
    MainWindow().run()