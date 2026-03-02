from bugemon import Bugemon
from item import Item


class Player:
    def __init__(self, team: list[Bugemon]):
        self.team = team
        self.items = []
        
    @property
    def has_lost(self):
        return all(not bugemon.is_alive for bugemon in self.team)