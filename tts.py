import os
from resemble import Resemble
from gtts import gTTS


class TTS:
    language = 'en'

    def play(self, text):
        myobj = gTTS(text=text, lang=self.language, slow=False)
        myobj.save("welcome.mp3")
        os.system("mpg321 -q welcome.mp3")


def load():
    Resemble.api_key('6tIwf7cErof06FjoNeV6BAtt')

    page = 1
    page_size = 10

    response = Resemble.v2.projects.all(page, page_size)

    projects = response['items']
    # print(projects)

    response = Resemble.v2.voices.all(page, page_size)
    voices = response['items']
    print(voices)
