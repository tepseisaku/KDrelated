import sys, pygame
from pygame import mixer

#pygameとmixerの初期化
pygame.init()
pygame.mixer.init()

#音楽サンプルのロード（wav形式の音楽を用意しておきます）
pygame.mixer.music.load('music1.wav')

#音楽サンプルの演奏
pygame.mixer.music.play(10)

#画面サイズ・動きの速度・色の設定
size = width, height = 500, 500
speed = [1, 1]
black = 0, 0, 0

#画面を設定
screen = pygame.display.set_mode(size)

#ハート画像のロード
ht = pygame.image.load('happy.gif')
heart = ht.get_rect()

while 1:
  for h in pygame.event.get():
    if h.type == pygame.QUIT:
      pygame.mixer.music.fadeout(2000)
      sys.exit()

  heart = heart.move(speed)

  #ハート画像が画面の左右の枠に達したら方向を変える
  if heart.left < 0 or heart.right > width:
    speed[0] = -speed[0]
  #ハート画像が画面の上下の枠に達したら方向を変える
  if heart.top < 0 or heart.bottom > height:
    speed[1] = -speed[1]

  screen.fill(black)
  screen.blit(ht, heart)
  pygame.display.flip()

  #10秒間の間隔を置く
  pygame.time.delay(10)
