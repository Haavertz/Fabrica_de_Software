from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class ImagePress(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")
        
        self.button = Button(text="Exibir", color=(1,1,1,1))
        self.button.bind(on_press = self.toggle_image)

        self.img = Image()   
        self.is_image_visible = True
        
        layout.add_widget(self.button)
        layout.add_widget(self.img)
        
        return layout
    
    def toggle_image(self, instance):
        if self.is_image_visible == True:
            self.img.source = "images.jpg"
            self.button.text = "Fechar"
            self.is_image_visible = False
        else:
            self.img.source = ""
            self.button.text = "Exibir"
            self.is_image_visible = True

        
if __name__ == "__main__":
    ImagePress().run()
