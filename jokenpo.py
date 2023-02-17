import names
import random
import emoji


class Player:
    def __init__(self):
        self.__name = names.get_first_name()
        self.__jokenpo_move, self.__emoji_result = self.__move()

    @property
    def name(self):
        return self.__name

    @property
    def jokenpo_move(self):
        return self.__jokenpo_move

    @property
    def emoji_result(self):
        return self.__emoji_result

    @staticmethod
    def __move():
        play = random.choice(['rock', 'paper', 'scissor'])

        if play == 'rock':
            emoji_result = emoji.emojize(':fist:', language='alias')
            return play, emoji_result
        elif play == 'paper':
            emoji_result = emoji.emojize(':hand:', language='alias')
            return play, emoji_result
        elif play == 'scissor':
            emoji_result = emoji.emojize(':v:', language='alias')
            return play, emoji_result


class Jokenpo:
    def __init__(self):
        self.__player1 = Player()
        self.__player2 = Player()
        self.__result_text = self.__result()

    @property
    def result_text(self):
        return self.__result_text

    def __rules(self):
        if self.__player1.jokenpo_move == self.__player2.jokenpo_move:
            return 'Draw'
        elif (self.__player1.jokenpo_move == 'rock' and self.__player2.jokenpo_move == 'scissor') or \
                (self.__player1.jokenpo_move == 'paper' and self.__player2.jokenpo_move == 'rock') \
                or (self.__player1.jokenpo_move == 'scissor' and self.__player2.jokenpo_move == 'paper'):
            return 'p_one'
        else:
            return 'p_two'

    def __result(self):
        if self.__rules() == 'p_one':
            result = f'{self.__player1.name} is a winner'
        elif self.__rules() == 'p_two':
            result = f'{self.__player2.name} is a winner'
        else:
            result = 'The players drew'

        return f"{self.__player1.name} {self.__player1.emoji_result} X {self.__player2.emoji_result} " \
               f"{self.__player2.name}\n" \
               f"{result}"


# TODO: Develop menu to play on terminal and vs human
def menu():
    pass


if __name__ == '__main__':
    menu()

    jokenpo = Jokenpo()
    print(jokenpo.result_text)
