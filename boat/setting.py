import pygame

pygame.init()

display_info= pygame.display.get_desktop_sizes()
display_width = display_info[0][0]
display_height = display_info[0][1]
print(display_width, display_height)


# text_font_size = int(display_width/1500*15)
# text_font = pygame.font.Font("EnglishTowne.ttf", text_font_size)
# title_text_font = pygame.font.Font("EnglishTowne.ttf", int(display_width/1500*125))
# big_text_font = pygame.font.Font("EnglishTowne.ttf", int(display_width/1500*25))
# small_text_font = pygame.font.Font("EnglishTowne.ttf", int(text_font_size/15*8.66))


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
BLUE = (0, 0, 200)
