import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the CycleOne collides
    with the food, or the CycleOne collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast, script)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the CycleOne collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        cycle_one = cast.get_first_actor("cycle_one")
        cycle_two = cast.get_first_actor("cycle_two")

        head_one = cycle_one.get_segments()[0]
        segments_one = cycle_one.get_segments()[1:]

        head_two = cycle_two.get_segments()[0]
        segments_two = cycle_two.get_segments()[1:]
        
        for segment in segments_one:
            # Check if CyleOne's head collides with it's own trail
            if head_one.get_position().equals(segment.get_position()):
                self._is_game_over = True
            # # Check if CyleTwo's head collides with CycleOne's trail
            if head_two.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
        for segment in segments_two:
            # Check if CycleTwo's head collides with it's own trail
            if head_two.get_position().equals(segment.get_position()):
                self._is_game_over = True
            # Check if CyleOne's head collides with CycleTwo's trail
            if head_one.get_position().equals(segment.get_position()):
                self._is_game_over = True
        
    def _handle_game_over(self, cast, script):
        """Shows the 'game over' message and turns the CycleOne and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of actions.
        """
        if self._is_game_over:
            actions = script.get_actions("update")
            trail_grow = actions[2]
            trail_grow.set_is_game_over(True)

            cycle_one = cast.get_first_actor("cycle_one")
            segments_one = cycle_one.get_segments()

            cycle_two = cast.get_first_actor("cycle_two")
            segments_two = cycle_two.get_segments()

            cycle_one.set_color(constants.WHITE)
            cycle_two.set_color(constants.WHITE)

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments_one:
                segment.set_color(constants.WHITE)

            for segment in segments_two:
                segment.set_color(constants.WHITE)
            