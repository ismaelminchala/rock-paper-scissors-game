import random
import os

moves = ['rock', 'paper', 'scissors']


class Player:                           # The Player class is the parent class
    def __init__(self):                 # for all of the Players
        self.movements = ['rock', random.choice(moves)]
        self.ind = 0

    def move(self):                     # Same movement every time
        return 'rock'

    def learn(self, my_move, their_move):   # Learns opponents movements
        self.movements = [my_move, their_move]


class RandomPlayer(Player):             # Subclass for a player with a
    def move(self):                     # random selection strategy
        return random.choice(moves)


# Subclass for a human player: The movement is defined by the user
class HumanPlayer(Player):
    def move(self):
        while True:
            move = input('What would you like to throw? ')
            if move in moves:
                return move
            print('Enter a valid movement! \n')


class ReflectPlayer(Player):            # Subclass for a player with a
    def move(self):                     # learning strategy
        return self.movements[1]


# Subclass for a player with a cyclic selection strategy
class CyclePlayer(Player):
    def move(self):
        self.ind += 1
        return moves[self.ind % 3]


def welcome():
    print(
            """ Welcome to the rock, scissors, and paper game.
 Here are the rules:
    \t - scissors cuts paper
    \t - paper covers rock
    \t - rock crushes scissors\n"""
    )


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        while True:
            move1 = self.p1.move()
            move2 = self.p2.move()
            print(f"Player 1: {move1}   \t  Player 2: {move2}")
            if move1 != move2:
                self.p1.learn(move1, move2)
                self.p2.learn(move2, move1)
                if beats(move1, move2):
                    self.score1 += 1
                else:
                    self.score2 += 1
                return beats(move1, move2)
            print('Draw! A rematch is needed...')

    def play_game(self):
        n = 0
        while n == 0:
            games = input('Single (s) or Multiple (m) rounds? ')
            if games == 's':
                n = 1
            elif games == 'm':
                n = 5
            else:
                print("Please, choose a valid option!")
        print("Game start!")
        for round in range(n):
            print(f"Round {round+1}:")
            if self.play_round():
                print('\033[91m' + 'Player 1 wins!' + '\033[0m')
            else:
                print('\033[91m' + 'Player 2 wins!' + '\033[0m')
            print(f'Score: \t P1: {self.score1} \t vs. \t P2: {self.score2}\n')
        if self.score1 > self.score2:
            print('\33[34m' + """      ****************
      * Player 1 won *
      ****************  """ + '\033[0m')
        else:
            print('\33[34m' + """      ****************
      * Player 2 won *
      ****************  """ + '\033[0m')
        print('\33[34m' + "     -   Game over   -    " + '\033[0m')


if __name__ == '__main__':
    os.system('clear')
    welcome()
    cont = 0
    while cont == 0:
        mode = input(""" Who would you like to play with?
 Please enter "random", "reflect", "repeat", or "cycle"\n""")
        if mode == 'random':
            game = Game(HumanPlayer(), RandomPlayer())
            cont = 1
        elif mode == 'reflect':
            game = Game(HumanPlayer(), ReflectPlayer())
            cont = 1
        elif mode == 'repeat':
            game = Game(HumanPlayer(), Player())
            cont = 1
        elif mode == 'cycle':
            game = Game(HumanPlayer(), CyclePlayer())
            cont = 1
        else:
            print('Please enter a correct game mode: \n')
    game.play_game()
