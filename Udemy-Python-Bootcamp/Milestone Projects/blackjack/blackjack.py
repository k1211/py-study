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

    def gamble(self, n):
        self.money -= n
        self.on_table = n

    def stand(self):
        pass

    def hit(self):
        self.hand.append(cards[random.randint(0,11)])

    def add_money(self, prize):
        self.money += prize

class Game(object):

    def win(self):
        print "Player won!"
        Player.money += +1.5*Player.on_table
        return Player.money

    def lose(self):
        print "Casino won!"
        Player.money -= Player.on_table
        return Player.money

    def cards_evaluation(self, two_cards):
        result = 0
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
casino = Player(cash=100000000)
game = Game()

hej = True
while hej:
    print "You have on your hand: ", player.hand

    if len(player.hand) == 2:
        eval = game.cards_evaluation(player.hand)
        if eval > 21:
            game.lose()
        else:
            game.win()

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










