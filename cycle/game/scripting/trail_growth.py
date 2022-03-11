from game.scripting.action import Action

class TrailGrowth(Action):
    """
    This class handles the automatic growth of the cycles.
    
    Attributes:
        _self._grow (int): The number of segments to add.

    """
    def __init__(self) -> None:
        super().__init__()
    
    def execute(self, cast, script):
        """This function is for growing the trails increasing by 50 each time.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle_one = cast.get_first_actor("cycle_one")
        cycle_two = cast.get_first_actor("cycle_two")
        cycle_one.grow_trail(1)
        cycle_two.grow_trail(1)