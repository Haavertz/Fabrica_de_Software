from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.pickers import MDDatePicker

# from kivymd.uix.pickers import MDColorPicker mostra a paleta de cores
# from kivymd.uix.pickers import MDTimePicker mostra o tempo


class DataApp(MDApp):
    def build(self):
        self.show_date()
        
    def show_date(self):
        date = MDDatePicker()
        date.open()
        

if __name__ == "__main__":
    DataApp().run()