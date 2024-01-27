from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random

class GamePreda(App):
    def build(self):
        self.life = Label(text="❤️ ❤️ ❤️", font_name="seguiemj", font_size=20, size_hint=(1, 0.5))
        self.victory = Label(text='Vitórias: ', font_size=20)

        self.result_label = Label(text="Escolha: Pedra, Papel ou Tesoura", font_size='20sp')

        buttons_layout = BoxLayout(orientation='horizontal', spacing=10)

        main_layout = BoxLayout(orientation='vertical', spacing=10)

        main_layout.add_widget(self.life)
        main_layout.add_widget(self.victory)
        main_layout.add_widget(self.result_label)
        main_layout.add_widget(buttons_layout)

        choices = ['Pedra', 'Papel', 'Tesoura']
        for choice in choices:
            buttons_layout.add_widget(Button(text=choice, on_press=self.make_choice))

        reset_button = Button(text='Resetar Jogo', on_press=self.reset_game)
        main_layout.add_widget(reset_button)

        self.number_victory = 0
        self.number_death = 0

        return main_layout

    def make_choice(self, instance):
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
            self.number_victory += 1
            self.victory.text = " * " * self.number_victory
            if self.number_victory == 3:
                self.life.text = "Você ganhou! Parabéns!"
                self.victory.text = ' '
                self.number_victory = 0

            return "Você venceu!"
        else:
            self.number_death += 1
            self.life.text = '❤️ ' * (3 - self.number_death)
            if self.number_death == 3:
                self.life.text = "❤️ ❤️ ❤️"
                self.number_death = 0
                self.number_victory = 0
                self.victory.text = ' '
                self.result_label.text = 'Você perdeu a partida estamos resetando suas vidas e suas vitorias!'

            return 'Você perdeu uma vida!'

    def reset_game(self, instance):
        self.number_victory = 0
        self.number_death = 0
        self.life.text = "❤️ ❤️ ❤️"
        self.victory.text = ' '
        self.result_label.text = "Escolha: Pedra, Papel ou Tesoura"

if __name__ == '__main__':
    GamePreda().run()
