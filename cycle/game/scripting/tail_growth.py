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
        
        cycle_one = cast.get_first_actor("cycle_one")
        cycle_two = cast.get_first_actor("cycle_two")
        
        if (self._grow % 1) == 0:
            cycle_one.grow_tail(1)
            cycle_two.grow_tail(1)