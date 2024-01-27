from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random

class GamePreda(App):
    def build(self):
        self.life = Label(text="❤️ ❤️ ❤️",font_name = "seguiemj", font_size=20, size_hint=(1, 0.5))
        self.victory = Label(text='Vitorias: ', font_size=20)
        
        self.result_label = Label(text="Escolha: Pedra, Papel ou Tesoura")
        self.result_label.font_size = '20sp'

        buttons_layout = BoxLayout(orientation='horizontal', spacing=10, size=(100,100))

        main_layout = BoxLayout(orientation='vertical', spacing=10)

        main_layout.add_widget(self.life)
        main_layout.add_widget(self.result_label)
        main_layout.add_widget(buttons_layout)
        buttons_layout.add_widget(Button(text='Pedra', on_press=self.make_choice))
        buttons_layout.add_widget(Button(text='Papel', on_press=self.make_choice))
        buttons_layout.add_widget(Button(text='Tesoura', on_press=self.make_choice))

        return main_layout

    def make_choice(self, instance):
        self.number_death = 0
        self.number_victory = 0
        user_choice = instance.text
        choices = ['Pedra', 'Papel', 'Tesoura']
        computer_choice = random.choice(choices)

        result = self.determine_winner(user_choice, computer_choice)
        self.result_label.text = f"Você escolheu: {user_choice}\nComputador escolheu: {computer_choice}\n{result}"

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "Empate!"
        elif (
            (user_choice == 'Pedra' and computer_choice == 'Tesoura') or
            (user_choice == 'Papel' and computer_choice == 'Pedra') or
            (user_choice == 'Tesoura' and computer_choice == 'Papel')
        ):
            if self.number_victory == 0:
                self.life.text += " * "
                self.number_victory += 1
            elif self.number_victory == 1:
                self.life.text
        else:
            if self.number_death == 0:
                self.life.text = '❤️ ❤️'
                self.number_death += 1
            elif self.number_death == 1:
                self.life.text = '❤️'
                self.number_death += 1
            else:
                self.life.text= 'MORREU!'

if __name__ == '__main__':
    GamePreda().run()
