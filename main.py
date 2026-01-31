# Example file showing a basic pygame "game loop"
import pygame

width,height=800,800
rows, column=8,8
square_size=width//column
light=(230, 230, 232)
dark=(70, 92, 106)
# pygame setup
pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Chess")
icon=pygame.image.load('images/chess_icon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
running = True

def draw_board(win):
    for row in range(rows):
        for col in range(column):
            if (row+col)%2==0:
                color=light
            else:
                color=dark
            pygame.draw.rect(
                win,
                color,
                (col*square_size,row*square_size,
                 square_size,square_size
                )
            )
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_board(screen)
    # fill the screen with a color to wipe away anything from last frame

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()