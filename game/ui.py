import pygame

def draw_text(screen, text, color, size, position):
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(topleft = position)

    screen.blit(text_surface, text_rect)