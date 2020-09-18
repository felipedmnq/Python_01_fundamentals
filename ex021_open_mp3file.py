#abra e reproduza um arquivo mp3.

import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
print('\033[1;31mTa escutando?\033[m')

