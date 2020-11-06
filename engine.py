import enum

class Engine:
    class PlayerType(enum.Enum):
        Human = 1
        AI = 2

    def __init__(self):
        print("Hello I'm a Game Engine")

    def flip_disc(player: PlayerType, disc_x: int, disc_y: int):
        pass