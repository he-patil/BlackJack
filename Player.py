from Card import Card
import random

class Player():
    def __init__(self, name, points):
        self.name = name
        self.points = points
    
    def drawCard(self, value):
        self.points +=value