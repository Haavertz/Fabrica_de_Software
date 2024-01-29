from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button

class AlexKiddGame(FloatLayout):
    def __init__(self, **kwargs):
        super(AlexKiddGame, self).__init__(**kwargs)
        
        self.alex_kidd_image = Image(source='cenar.png', allow_stretch=True, keep_ratio=False)
        self.btn = Button(text="Jogar", font_size=30, size_hint=(None, None), size=(200, 100),
                          pos_hint={'center_x': 0.5, 'center_y': 0.33}, background_color=(215, 215, 0, 1.0),
                          color=(0, 0, 0, 1))

        self.add_widget(self.alex_kidd_image)
        self.add_widget(self.btn)

class AlexKiddApp(App):
    def build(self):
        return AlexKiddGame()

if __name__ == '__main__':
    AlexKiddApp().run()
