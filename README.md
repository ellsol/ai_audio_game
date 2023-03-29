# AI AUDIO GAME

## Install

    pip install -r requirements.txt

## Don't forget to freeze if new dependencies were added

    pip freeze > requirements.txt
or
    make freeze

## Environment Vars
Create a file .local.env with 

    aikey=sk-.... // OPENAI Key

## Architecture

* GameEngine - controls game, state and which scenes should be displayed
* GameState - can load and save state
* GameCharacter - is a specific character with its own voice and behaviour
* GameScene - is a setting filled with items and characters....each scene has a story to tell