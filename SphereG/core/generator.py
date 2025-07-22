import pygame
from SphereG.utils.step import step
from SphereG.utils.remap import remap

def generate(screen: pygame.Surface) -> pygame.Surface:
    surface = pygame.Surface((screen.get_width(), screen.get_height()))

    # Divide the world into sky and earth
    for y in range(screen.get_height()):
        for x in range(screen.get_width()):
            if step(remap(y, (0, screen.get_height()), (-1, 1))):
                surface.set_at((x, y), pygame.Color("white"))
            else:
                surface.set_at((x, y), pygame.Color("black"))

    return surface
