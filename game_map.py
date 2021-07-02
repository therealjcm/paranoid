import numpy as np  # type: ignore
from tcod.console import Console

import tile_types


class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")

        self.visible = np.full((width, height), fill_value=False, order="F")    # currently in FOV
        self.explored = np.full((width, height), fill_value=False, order="F")   # ever in FOV

    def in_bounds(self, x: int, y: int) -> bool:
        """return true if x and y are inside of the bounds of this map"""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        """
        Renders the map
        If a tile is in the visible array then draw it with light colors
        if it is explored, but is not visible then draw it with dark colors
        otherwise default to SHROUD
        """

        console.tiles_rgb[0:self.width, 0:self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tile_types.SHROUD
        )
