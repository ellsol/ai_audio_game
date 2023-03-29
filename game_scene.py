import string
from abc import ABC, abstractmethod

from game_character import RandomGuy
from open_ai import OpenAIWrapper


class GameScene(ABC):
    FirstRoom = "first_room"

    def __init__(self, open_ai: OpenAIWrapper):
        self.open_ai = open_ai

    @abstractmethod
    def intro_text(self) -> string:
        pass

    @abstractmethod
    def wait_for_input(self):
        pass


class FirstRoom(GameScene):

    def wait_for_input(self) -> string:
        request = input("....and you ask him:")
        answer = self.strange_man.ask(request)
        print(answer)

    def __init__(self, open_ai: OpenAIWrapper):
        super().__init__(open_ai)
        self.strange_man = RandomGuy(open_ai)

    def intro_text(self) -> string:
        return '''
        You are in a room with 12 other people. The light is dimmed and a wave of curiosity is tangible.
        It seems - like you - nobody has a clue what the meaning is behind the call for this gathering, nor
        why you or any other participant is eligible to be here. Next to you is a mountain of a man. He occasionally
        stares insecurely into your direction. You approach him!


        '''
