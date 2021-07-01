from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity

class Action:
    def perform(self, engine: Engine, entity) -> None:
        """Perform this action with the actions needed to determine its scope
        `engine` is the scope this action is being performed in
        `entity` is object performing this action
        this action must be overriden by Action subclass
        """
        raise NotImplementedError()

class EscapeAction(Action):
    def perform(self, engine: Engine, entity) -> None:
        raise SystemExit()

class MovementAction(Action):
    def __init__(self, dx: int, dy: int):
        super().__init__()

        self.dx = dx
        self.dy = dy

    def perform(self, engine: Engine, entity) -> None:
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if not engine.game_map.in_bounds(dest_x, dest_y):
            return
        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return

        entity.move(self.dx, self.dy)