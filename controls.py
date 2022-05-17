import sys
import pygame
from bullet import Bullet


def events(screen,gun, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                gun.kright = True
            elif event.key == pygame.K_a:
                gun.kleft = True
            elif event.key == pygame.K_w:
                gun.kup = True
            elif event.key == pygame.K_s:
                gun.kdown = True

            elif event.key == pygame.K_l:
                gun.kright2 = True
            elif event.key == pygame.K_j:
                gun.kleft2 = True
            elif event.key == pygame.K_i:
                gun.kup2 = True
            elif event.key == pygame.K_k:
                gun.kdown2 = True


                pygame.mixer.music.stop()
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
                pygame.mixer.music.load('image/45901.mp3')
                pygame.mixer.music.play(-1)


        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                gun.kright = False
            elif event.key == pygame.K_a:
                gun.kleft = False
            elif event.key == pygame.K_w:
                gun.kup = False
            elif event.key == pygame.K_s:
                gun.kdown = False

            elif event.key == pygame.K_l:
                gun.kright2 = False
            elif event.key == pygame.K_j:
                gun.kleft2 = False
            elif event.key == pygame.K_i:
                gun.kup2 = False
            elif event.key == pygame.K_k:
                gun.kdown2 = False

def update(bg_color, screen, gun, bullets):
    # screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.drawBullet()
    gun.output()
    pygame.display.flip()

def delete(bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print(len(bullets))