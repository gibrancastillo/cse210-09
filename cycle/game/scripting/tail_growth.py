from game.scripting.action import Action

class TailGrowth(Action):
    """

    This class handles the automatic growth of the cycles.
    
    
    Attributes:
        _self._grow (int): The number of segments to add.

    """

    def __init__(self) -> None:
        super().__init__()
        self._grow = 0
    
    def execute(self, cast, script):
        """This function is for growing the tails increasing by 50 each time.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        self._grow += 1
        
        CycleOne = cast.get_actors("CycleOne")
        CycleTwo = cast.get_actors("CycleTwo")
        cycle1 = CycleOne[0]
        cycle2 = CycleTwo[0]
        
        if (self._grow % 30) == 0:
            cycle1.grow_tail(1)
            cycle2.grow_tail(1)