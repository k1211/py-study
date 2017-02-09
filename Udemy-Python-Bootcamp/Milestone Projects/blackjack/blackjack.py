# #Milestone Project 2 - Blackjack Game
# In this milestone project you will be creating a Complete BlackJack Card Game in Python.
#
# Here are the requirements:
#
# * You need to create a simple text-based [BlackJack](https://en.wikipedia.org/wiki/Blackjack) game
# * The game needs to have one player versus an automated dealer.
# * The player can stand or hit.
# * The player must be able to pick their betting amount.
# * You need to keep track of the players total money.
# * You need to alert the player of wins, losses, or busts, etc.

import random
J, Q, K = 10,10,10
A = 0

cards = [2,3,4,5,6,7,8,9,J,Q,K,A]

class Player():

    def __init__(self,cash):
        self.hand = []
        self.money = cash
        self.on_table = 0
        self.ans = ''

    def gamble(self, n):
        self.money -= n
        self.on_table = n

    def stand(self):
        pass

    def hit(self):
        self.hand.append(cards[random.randint(0,11)])

    def win(self):
        print "Player won!"
        self.money = self.money +  1.5*self.on_table
        print "Player's money: " , self.money

    def lose(self):
        print "Casino won!"
        self.money -= self.on_table
        print "Player's money: ", self.money

class Game(object):
    def __init__(self):
        self.turn = ''

    def cards_evaluation(self, two_cards):

        if A in two_cards:
            result = sum(two_cards) + 11
            if result > 21:
                result -= 10
        else:
            result = sum(two_cards)
        return result

cash = int(raw_input("How much money do you come with: ").strip())
baton = int(raw_input("How much money do you want to gamble: ").strip())

player = Player(cash)
game = Game()

player.gamble(baton)

hej = True
while hej:
    # turn = game.whose_turn()
    print "You have on your hand: ", player.hand

    if len(player.hand) == 2:
        eval_player = game.cards_evaluation(player.hand)

        if eval_player > 21:
            print "Player's points: ", eval_player
            player.lose()

        else:
            print "Player's points: ", eval_player
            player.win()

        break

    else:
        ans = raw_input("What do you do? [hit/stand/bust]")
        if ans == 'hit':
            player.hit()
        elif ans == 'stand':
            player.stand()
        elif ans == 'bust':
            print "Good game!"
            hej = False
        else:
            print "You inserted a wrong answer! "










