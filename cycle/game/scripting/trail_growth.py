from game.scripting.action import Action


class TrailGrowth(Action):
    """
    This class handles the automatic growth of the cycles.
    
    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """
    def __init__(self) -> None:
        super().__init__()
        self._is_game_over = False  
    
    def set_is_game_over(self, is_game_over):
        """
        Stopping the trail growth when the game is over 
        
        Attributes:
            is_game_over (boolean): Whether or not the game is over
        """
        self._is_game_over = is_game_over
    
    def execute(self, cast, script):
        """This function is for growing the trails increasing by 50 each time.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if not self._is_game_over:
            cycle_one = cast.get_first_actor("cycle_one")
            cycle_two = cast.get_first_actor("cycle_two")
            cycle_one.grow_trail(1)
            cycle_two.grow_trail(1)