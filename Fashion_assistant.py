import random
import Catalogue


class fashion_assistant:
    def __init__(self):
        self.load_catalogue()

    def generate_outfit(self):
        pass

    def load_catalogue(self):
        self.catalogue = Catalogue.catalouge()


class random_fashion_assistant(fashion_assistant):

    def __init__(self):
        super().__init__()

    def generate_outfit(self):
        self.chosenheadwear()
        self.chosentshirt()
        self.chosenlegwear()
        self.chosenshoes()

    def chosenheadwear(self):
        pass
    # ask the catalogue for IDs and then select one, then return
    # random.choice

    def chosentshirt(self):
        pass

    def chosenlegwear():
        pass

    def chosenshoes():
        pass
