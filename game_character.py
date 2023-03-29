import string
from abc import ABC, abstractmethod

from open_ai import OpenAIWrapper
from tts import TTS


class GameCharacter(ABC):
    tts = TTS()

    def __init__(self, open_ai: OpenAIWrapper):
        self.open_ai = open_ai

    @abstractmethod
    def ask(self, text):
        pass

    def say(self, text):
        self.tts.play(text)


class RandomGuy(GameCharacter):

    def ask(self, text: string):
        return self.open_ai.ask(text)

    def __init__(self, open_ai):
        super().__init__(open_ai)
