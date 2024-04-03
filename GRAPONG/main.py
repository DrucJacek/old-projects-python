#
#
#
#
#
#
# import pygame
# from paddle import Paddle
# from ball import Ball
#
# tryb = input("Napisz k, jeśli chcesz grać z komputerem, napisz g, jeśli chcesz grać z drugą osobą: ")
#
# pygame.init()
# music = pygame.mixer.music.load('caramella_girls_caramelldansen_official_english_version_3708195094964174534.mp3')
# pygame.mixer.music.play(-1)
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
#
#
# size = (1920, 1080)
# screen = pygame.display.set_mode(size)
# pygame.display.set_caption("PONG")
#
# paddleA = Paddle(WHITE, 10, 250)
# paddleA.rect.x = 20
# paddleA.rect.y = 200
#
# paddleB = Paddle(WHITE, 10, 250)
# paddleB.rect.x = 1890
# paddleB.rect.y = 200
#
# ball = Ball(WHITE, 25, 25)
# ball.rect.x = 345
# ball.rect.y = 195
#
# all_sprites_list = pygame.sprite.Group()
#
# all_sprites_list.add(paddleA)
# all_sprites_list.add(paddleB)
# all_sprites_list.add(ball)
#
# carryOn = True
#
# clock = pygame.time.Clock()
#
#
# scoreA = 0
# scoreB = 0
#
# while carryOn:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             carryOn = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_x:
#                 carryOn = False
#
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_UP]:
#         paddleB.moveUp(5)
#     if keys[pygame.K_DOWN]:
#         paddleB.moveDown(5)
#
#     if tryb == "g":
#         if keys[pygame.K_w]:
#             paddleA.moveUp(10)
#         if keys[pygame.K_s]:
#             paddleA.moveDown(10)
#
#     if tryb == "k":
#         if ball.rect.y > paddleA.rect.y:
#             paddleA.moveDown(6)
#         if ball.rect.y < paddleA.rect.y:
#             paddleA.moveUp(6)
#         all_sprites_list.update()
#
#     if keys[pygame.K_UP]:
#         paddleB.moveUp(5)
#     if keys[pygame.K_DOWN]:
#         paddleB.moveDown(5)
#
#     if ball.rect.x >= 1920:
#         scoreA += 1
#         ball.velocity[0] = -ball.velocity[0]
#     if ball.rect.x <= 0:
#         scoreB += 1
#         ball.velocity[0] = -ball.velocity[0]
#     if ball.rect.y > 1000:
#         ball.velocity[1] = -ball.velocity[1]
#     if ball.rect.y < 0:
#         ball.velocity[1] = -ball.velocity[1]
#
#     if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
#         ball.bounce()
#
#     screen.fill(BLACK)
#     pygame.draw.line(screen, WHITE, [960, 0], [960, 1080], 5)
#
#     all_sprites_list.draw(screen)
#
#     font = pygame.font.Font(None, 80)
#     text = font.render(str(scoreA), True, WHITE)
#     screen.blit(text, (250, 10))
#     text = font.render(str(scoreB), True, WHITE)
#     screen.blit(text, (1670, 10))
#     pygame.display.flip()
#     if scoreA == 10 or scoreB == 10:
#         print("BRAWO!")
#         break
#     clock.tick(150)
# pygame.quit()

def odwrot(str1):
 if len(str1) % 4 == 0:
  return ''.join(reversed(str1))
 return str1


print(odwrot('abcd'))
print(odwrot('jacek'))









