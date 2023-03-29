import os
from datetime import datetime

import yaml

from game_scene import GameScene, FirstRoom


class GameState:
    filename = "game_state.yaml"

    def __init__(self):
        self.data = dict()
        self.load()

    def current_scene(self):
        return self.data["scene"]

    def save(self):
        with open(self.filename, 'w') as f:
            documents = yaml.dump(self.data, f)

    def load(self):
        if not os.path.isfile(self.filename):
            self.create()
        with open(self.filename) as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)

    def create(self):
        self.data["startDate"] = datetime.now()
        self.data["scene"] = GameScene.FirstRoom
        self.save()

