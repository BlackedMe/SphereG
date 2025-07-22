import pygame
import random
from SphereG.utils.step import step
from SphereG.utils.remap import remap

def generate(screen: pygame.Surface, radius: float = 0.20) -> pygame.Surface:
    surface = pygame.Surface((screen.get_width(), screen.get_height()))

    # Divide the world into sky and earth
    for y in range(screen.get_height()):
        for x in range(screen.get_width()):
            if step(remap(y, (0, screen.get_height()), (-1, 1))):
                surface.set_at((x, y), pygame.Color("white"))
            else:
                surface.set_at((x, y), pygame.Color("black"))

    # Add turbulence around the centre at y = 0 based on radius
    radius *= screen.get_height()

    top_left = (0, screen.get_height() / 2 - radius)

    pxarray = pygame.surfarray.pixels2d(surface.subsurface(pygame.Rect(top_left, (screen.get_width(), radius * 2))))

    for row in pxarray:
        random.shuffle(row)

    return surface
