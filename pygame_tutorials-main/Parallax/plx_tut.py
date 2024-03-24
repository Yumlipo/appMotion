import pygame
import spritesheet

pygame.init()

clock = pygame.time.Clock()
FPS = 60

#create game window
SCREEN_WIDTH = 980
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

#define game variables
scroll = 0

ground_image = pygame.image.load("ground.png").convert_alpha()
ground_width = ground_image.get_width()
ground_height = ground_image.get_height()

bg_images = []
for i in range(1, 6):
  bg_image = pygame.image.load(f"plx-{i}.png").convert_alpha()
  bg_images.append(bg_image)
bg_width = bg_images[0].get_width()

def draw_bg():
  x=0
  while x < 3000:
    speed = 1
    for i in bg_images:
      screen.blit(i, ((x * bg_width) - scroll * speed, 0))
      speed += 0.2
    x += 1

def draw_ground():
  x=0
  while x < 3000:
    screen.blit(ground_image, ((x * ground_width) - scroll * 2.5, SCREEN_HEIGHT - ground_height))
    x += 1


sprite_sheet_image = pygame.image.load('car.png').convert_alpha()
sprite_sheet = spritesheet.SpriteSheet(sprite_sheet_image)

BLACK = (0, 0, 0)

animation_list = []
animation_steps = [4, 1]
action = 0

last_update = pygame.time.get_ticks()
animation_cooldown = 400
frame = 0
step_counter = 0

for animation in animation_steps:
	temp_img_list = []
	for _ in range(animation):
		temp_img_list.append(sprite_sheet.get_image(step_counter, 28, 15, 7, BLACK))
		step_counter += 1
	animation_list.append(temp_img_list)

#game loop
run = True
while run:

  clock.tick(FPS)

  #draw world
  draw_bg()

  #get keypresses
  # key = pygame.key.get_pressed()
  # if key[pygame.K_LEFT] and scroll > 0:
  #   scroll -= 5
  # if key[pygame.K_RIGHT] and scroll < 3000:
  #   scroll += 5

  # upd animation
  current_time = pygame.time.get_ticks()
  if current_time - last_update >= animation_cooldown:
    frame += 1
    last_update = current_time
    if frame >= len(animation_list[action]):
      frame = 0

  screen.blit(animation_list[action][frame], (400, 449))


  draw_ground()

  scroll += 3
  #event handlers
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN and action > 0:
        action -= 1
        frame = 0
      if event.key == pygame.K_UP and action < len(animation_list) - 1:
        action += 1
        frame = 0

  pygame.display.update()


pygame.quit()