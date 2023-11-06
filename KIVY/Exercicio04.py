from kivy.uix.image import Image, AsyncImage
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class Images(App):
    def build(self):
        
        self.layout = BoxLayout(orientation="vertical")

        self.image = Image(source = "Midia/images.jpg", fit_mode="fill")
        
        self.button = Button(text="Fechar")
        self.button.bind(on_press=self.abririmage)
        
        self.layout.add_widget(self.button)
        self.layout.add_widget(self.image)

        return self.layout
    
    #Aqui estou mexendo com a opacidade da image, ou seja, parece que ela n esta lá, porém ela está lá, só esta invisivel]

    def abririmage(self, instace):
        if self.image.opacity == 1:
            self.image.opacity = 0
            self.button.text = "Abrir"
        else:
            self.image.opacity = 1
            self.button.text = "Fechar"
if __name__ == "__main__":
    Images().run()


