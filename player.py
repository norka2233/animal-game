from config import food, food_basket
from house import (
    DogCage,
    CatCage,
    GerbilCage,
    BirdCage,
    FishCage
)
import sys


class Player:

    def __init__(self, name):
        self.basket = food_basket
        self.name = name

    def enter_cage(self, cage):
        """
        player enters the room from 1 to 5, from dog - fish
        """
        self.feed(cage.animal, cage.food)

    def play_game(self):
        cages = [DogCage(), CatCage(), GerbilCage(), BirdCage(), FishCage()]

        [self.enter_cage(cage) for cage in cages]
        self.end_game('Congrats, Sobaka, You\'ve Won!')

    def feed(self, animal, appropriate_food):

        print('Available food: ', food_basket)
        print(f'You are in a {animal} cage, please, type the food to feed this animal')

        enter_food = input('> ')

        if enter_food in appropriate_food and enter_food in food_basket:
            print('Om-nom-nom')
            food_basket.remove(enter_food)


        else:
            return self.end_game('Game Over. U\'ve Lost, Sobaka!')

    def end_game(self, message):
        sys.exit(message)

if __name__ == '__main__':
    from house import GerbilCage as GC
    gerbil_cage = GC()
    # print(f'food: {gerbil_cage.food}, animal={gerbil_cage.animal}')
    p = Player('Bob')
    p.enter_cage(gerbil_cage)
