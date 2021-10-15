import names
import tweepy
import random
import emoji
import os
from dotenv import load_dotenv
from pathlib import Path


# TODO: Traduzir o script para inglês

# TODO: Criar uma função para acesso das variáveis de ambiente
load_dotenv()
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACESS_TOKEN_SECRET = os.getenv('acess_token_secret')

dotenv_path = Path('C:\\Users\\vinic\\PycharmProjects\\.env')
load_dotenv(dotenv_path=dotenv_path)


# Authenticate to Twitter
def authentication_tt():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACESS_TOKEN_SECRET)
    return tweepy.API(auth)


# Pedra papel e tesoura
def paper_stone_scisor():
    x = random.choice(['pedra', 'papel', 'tesoura'])
    return x


def rules(p_one, p_two):
    if p_one == p_two:
        return 'draw'
    elif (p_one == 'pedra' and p_two == 'tesoura') or (p_one == 'papel' and p_two == 'pedra') or (
            p_one == 'tesoura' and p_two == 'papel'):
        return 'p_one'
    else:
        return 'p_two'


def emoji_player(player):
    if player == 'pedra':
        return emoji.emojize(':fist:', use_aliases=True)
    elif player == 'papel':
        return emoji.emojize(':hand:', use_aliases=True)
    elif player == 'tesoura':
        return emoji.emojize(':v:', use_aliases=True)


if __name__ == '__main__':

    player_one = paper_stone_scisor()
    player_two = paper_stone_scisor()

    name_one = names.get_first_name()
    name_two = names.get_first_name()

    result = rules(player_one, player_two)

    if result == 'p_one':
        result = f'{name_one} is a winner'
    elif result == 'p_two':
        result = f'{name_two} is a winner'
    else:
        result = f'The players drew'

    tweet = f"{name_one} {emoji_player(player_one)} X {emoji_player(player_two)} {name_two}\n{result}"

    api = authentication_tt()

    # TODO: Refatorar o try except
    try:
        api.update_status(tweet)
    except tweepy.TweepyException as error:
        if error == 187:
            # Do something special
            print('duplicate message')
        else:
            raise error

# TODO: Refatorar o script com boas práticas 'pythonicas' e lógica
