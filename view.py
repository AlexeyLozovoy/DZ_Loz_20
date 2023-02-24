class ConsoleView:
    def show_game(self, turn, player_score, computer_score):
        print(f"Бросков: {turn}")
        print(f"Игрок: {player_score}")
        print(f"Компьютер: {computer_score}\n")
        
    def show_winner(self, player_score, computer_score):
        if player_score > computer_score:
            print("Игрок выйграл!")
        elif player_score < computer_score:
            print("Компьютер выйграл!")
        else:
            print("Ничья!")

    def show_invalid_input(self):
        print("Не верный ввод!\n")

    def get_input(self):
        return input("ВВедите: 1 для бросков, 2 для сброса, 0 для выхода: ")
