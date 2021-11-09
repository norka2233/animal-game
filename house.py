import uuid
from config import food


class Cage:

    def __init__(self, animal, food):
        self.id = uuid.uuid4()
        self.animal = animal
        self.food = food


class DogCage(Cage):

    def __init__(self):
        super().__init__('dog', food.get('dog'))


class CatCage(Cage):

    def __init__(self):
        super().__init__('cat', food.get('cat'))


class GerbilCage(Cage):

    def __init__(self):
        super().__init__('gerbil', food.get('gerbil'))


class BirdCage(Cage):

    def __init__(self):
        super().__init__('bird', food.get('bird'))


class FishCage(Cage):

    def __init__(self):
        super().__init__('fish', food.get('fish'))




if __name__ == '__main__':
    h = Cage('dog', 'meat')
    print(h.food)

    dc = DogCage()
    print(dc.food)