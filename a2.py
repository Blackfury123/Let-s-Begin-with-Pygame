import pygame
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("The Penguin")
background_image = pygame.transform.scale(pygame.image.load('./background.png').convert(),(500, 500))
penguin=pygame.transform.scale(pygame.image.load('./penguin.png').convert_alpha(),(200,200))
penguin_rect=penguin.get_rect(center=(250,220))
text = pygame.font.Font(None, 36).render('Hello World ', True, pygame.Color('black'))
text_rect = text.get_rect(center=(250,360))

def game_loop():
  clock = pygame.time.Clock()
  running = True
  while running:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False

    screen.blit(background_image, (0, 0))
    screen.blit(penguin,penguin_rect)
    screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(30)
  pygame.quit()

if __name__ =='__main__':
    game_loop()