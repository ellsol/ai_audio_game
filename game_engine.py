from game_scene import GameScene, FirstRoom
from game_state import GameState
from open_ai import OpenAIWrapper
from tts import TTS


class GameEngine:
    def __init__(self):
        self.state = GameState()
        self.tts = TTS()
        self.open_ai = OpenAIWrapper()
        self.currentScene = self.get_current_scene(self.state.current_scene())

    def get_current_scene(self, id):
        if id == GameScene.FirstRoom:
            return FirstRoom(self.open_ai)
        else:
            return FirstRoom(self.open_ai)

    def round(self):
        self.show_introduction()
        self.currentScene.wait_for_input()

    def show_introduction(self):
        msg = self.currentScene.intro_text()
        print(msg)
        #self.tts.play(msg)


