from abc import ABC, abstractmethod

class InkWriter(ABC):
    """ E-INK Writer abstract class.
    """

    COLORED = 1
    UNCOLORED = 0

    @abstractmethod
    def write(self, epd, frame_black, frame_red):
        pass
