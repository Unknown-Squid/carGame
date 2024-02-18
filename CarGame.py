import sys
import pygame
import name
from pygame import mixer

pygame.init()

clock = pygame.time.Clock()
sw = 1280
sh = 720

green = (180,225,90)
blue = (10,10,225)
pink = (180,130,240)
black = (10,10,10)
red = (225, 38, 54)
white = (225,225,225)
screen = pygame.display.set_mode((sw, sh))
pygame.display.set_caption("Fast and Furious")
icon = pygame.image.load('car_icon.jpeg')
pygame.display.set_icon(icon)
mixer.music.load('Alcohol_Free.mp3')
mixer.music.play(-1)
font = pygame.font.SysFont("Arial", 62)
small_font = pygame.font.SysFont("Arial", 32)


#button
def create_button(x, y, width, height, hovercolor, defaultcolor):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed(3)

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hovercolor, (x, y, width, height))
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(screen, defaultcolor, (x, y, width, height))


#game start menu    
def start_game():
	start = pygame.image.load('start.jpg')
	exit = pygame.image.load('exit.jpg')
	while True:
		screen_bg = pygame.image.load('bg.jpg')
		screen.blit(screen_bg,(0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		
		sb = create_button(550, 250, 150, 80, pink, black)
		screen.blit(start,(550, 250))
		
		if sb:
			race_menu()
		eb = create_button (565, 450, 170, 60, pink, black)
		screen.blit(exit,(565, 450))
		if eb:
			sys.exit()
			pygame.quit()
		pygame.display.update()
		clock.tick(15)

#race menu
def race_menu():
    input_name = small_font.render("Input Your Name Here", True, white)
    input_rect = pygame.Rect(330, 300, 600, 80)
    input = pygame.image.load('input.jpg')
    next = pygame.image.load('next.png')
    back = pygame.image.load('back.png')
    touched = False
    while True:
    	screen_bg = pygame.image.load('bg.jpg')
    	screen.blit(screen_bg,(0,0))
    	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
    			pygame.quit()
    			sys.exit()
    		if event.type == pygame.MOUSEBUTTONDOWN:
    			if input_rect.collidepoint(event.pos):
    				touched = True
    				
    		if event.type == pygame.KEYDOWN:
    			if event.key == pygame.K_BACKSPACE:
    				name.text_input = name.text_input[:-1]
    			else:
    				name.text_input += event.unicode
    	pygame.draw.rect(screen, blue, input_rect)
    	screen.blit(input,(330, 300))
    	text_surface = font.render(name.text_input,  True, black)
    	screen.blit(text_surface, (input_rect
    .x + 5, input_rect.y + 5))
    	screen.blit(input_name, (480, 250))
    	nextb = create_button(830, 490, 240, 50, pink, white)
    	if touched:
    		color = white
    	else:
    		color = black
    	if nextb:
    		location()
    	backb = create_button(240, 495, 238, 60, green, red)
    	if backb:
    		start_game()
    	screen.blit(back, (200, 470))	
    	screen.blit(next, (800,470))
    	pygame.display.update()
    	clock.tick(60)

#location selection
def location():
	l = font.render("Choose Your Location below", True, blue)
	road1 = pygame.image.load('road1.jpg')
	road2 = pygame.image.load('road2.jpg')
	back = pygame.image.load('back.png')
	while True:
		screen_bg = pygame.image.load('bg.jpg')
		screen.blit(screen_bg,(0,0))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		
		road1b = create_button(250, 280, 300, 250, pink, black)
		if road1b:
			character_1()
		road1_b = pygame.Rect(250, 280, road1.get_width() + 5, road1.get_height() + 5)
		road2b = create_button(650, 280, 300, 250, pink, black)
		if road2b:
			character_2()
		backb = create_button(40, 545, 238, 60, green, red)
		if backb:
			race_menu()
		screen.blit(back, (0, 520))
		road2_b = pygame.Rect(650, 280, road2.get_width() + 5, road2.get_height() + 5)
		pygame.draw.rect(screen, black, road1_b)
		pygame.draw.rect(screen, black, road2_b)		
		screen.blit(road1,(250, 280))
		screen.blit(road2,(650, 280))
		screen.blit(l, (250, 200))
		pygame.display.update()
		clock.tick(60)

#character selection for road_1		
def character_1():
    c = font.render("Choose Your Character Below", True, blue)
    c1 = pygame.image.load('c1.png')
    c2 = pygame.image.load('c2.png')
    c3 = pygame.image.load('c3.png')
    c4 = pygame.image.load('c4.png')
    back = pygame.image.load('back.png')
    while True:
    	screen_bg = pygame.image.load('bg.jpg')
    	screen.blit(screen_bg,(0,0))
    	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
    			pygame.quit()
    			sys.exit()
    	screen.blit(c, (250,200))
    	c1b = create_button(230, 310, 75, 230, pink, black)
    	if c1b:
    		c1_game()
    	screen.blit(c1,(150,300))
    	c2b = create_button(480, 310, 75, 230, pink, black)
    	if c2b:
    		c2_game()
    	screen.blit(c2,(400,300))
    	c3b = create_button(730, 310, 75, 230, pink, black)
    	if c3b:
    		c3_game()
    	screen.blit(c3,(650,300))
    	c4b = create_button(980, 310, 75, 220, pink, black)
    	if c4b:
    		c4_game()
    	backb = create_button(40, 605, 238, 60, green, red)
    	if backb:
    		location()
    	screen.blit(back, (0, 580))
    	screen.blit(c4,(900,300))
    	pygame.display.update()
    	clock.tick(60)

#character selection for road_2
def character_2():
    c = font.render("Choose Your Character Below", True, blue)
    c1 = pygame.image.load('c1.png')
    c2 = pygame.image.load('c2.png')
    c3 = pygame.image.load('c3.png')
    c4 = pygame.image.load('c4.png')
    back = pygame.image.load('back.png')
    while True:
    	screen_bg = pygame.image.load('bg.jpg')
    	screen.blit(screen_bg,(0,0))
    	for event in pygame.event.get():
    		if event.type == pygame.QUIT:
    			pygame.quit()
    			sys.exit()
    	screen.blit(c, (250,200))
    	c1b = create_button(230, 310, 75, 230, pink, black)
    	if c1b:
    		c1_game_2()
    	screen.blit(c1,(150,300))
    	c2b = create_button(480, 310, 75, 230, pink, black)
    	if c2b:
    		c2_game_2()
    	screen.blit(c2,(400,300))
    	c3b = create_button(730, 310, 75, 230, pink, black)
    	if c3b:
    		c3_game_2()
    	screen.blit(c3,(650,300))
    	c4b = create_button(980, 310, 75, 220, pink, black)
    	if c4b:
    		c4_game_2()
    	backb = create_button(40, 605, 238, 60, green, red)
    	if backb:
    		location()
    	screen.blit(back, (0, 580))
    	screen.blit(c4,(900,300))
    	pygame.display.update()
    	clock.tick(60)    	
    	
#game loop for road_1
def c1_game():
	how_to_play = pygame.image.load('how_to_play.jpg')
	starting_line = pygame.image.load('starting_line.png')
	start_rect = starting_line.get_rect()
	win = pygame.image.load('winner.jpg')
	lose = pygame.image.load('game_over.jpg')
	s = pygame.image.load('stop.png')
	g = pygame.image.load('gas.png')
	f = pygame.image.load('finish_line.jpg')
	f_rect = f.get_rect()
	f_rect.x = 200
	f_rect.y = -7300
	r1 = pygame.image.load('road1bg.jpg')
	r1_rect = r1.get_rect()
	r1_rect.y =-7300
	c1 = pygame.image.load('c1.png')
	c1_rect = c1.get_rect()
	e1 = pygame.image.load('c4.png')
	e1_rect = e1.get_rect()		
	stop = pygame.Rect(1100, 500, 84, 125)
	gas = pygame.Rect(40, 500, 76, 125)
	enemy = pygame.Rect(40, 500, 100, 100)
	rect = pygame.Rect(500,500,500,500)
	touched = False
	touched_stop = False
	touched_gas = False
	not_touched = False
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP or pygame.K_w:
					touched_gas = True
				else:
					not_touched = True
				if event.key == pygame.K_SPACE:
					touched_stop = True
				else:
					not_touched = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				if stop.collidepoint(event.pos):
					touched_stop = True
				else:
					not_touched = True
				if gas.collidepoint(event.pos):
					touched_gas = True
				else:
					not_touched = True
				if enemy.collidepoint(event.pos):
					touched = True
			if event.type == pygame.MOUSEBUTTONUP:
				touched_gas = False
				touched_stop = False			
		if touched_stop:
			c1_rect.y += 1
			r1_rect.y -= 8
			f_rect.y -= 8
		if touched_gas: 
			c1_rect.y -= 2
			r1_rect.y += 15
			f_rect.y +=15
			start_rect.y += 50
		if touched:
			e1_rect.y -= 1.5
		if not_touched:
			c1_rect.y += 0.5
			r1_rect.y += 5
			f_rect.y += 5	
		screen.blit(r1,(r1_rect.x, r1_rect.y))
		pygame.draw.rect(screen, blue, stop)
		pygame.draw.rect(screen, blue, gas)
		screen.blit(f, (f_rect.x, f_rect.y + 550))
		screen.blit(starting_line,(start_rect.x + 200, start_rect.y + 600))
		screen.blit(c1,(c1_rect.x + 300,c1_rect.y + 500))
		text_surface = font.render(name.text_input,  True, black)
		screen.blit(text_surface, (330, c1_rect.y + 750))
		screen.blit(e1,(e1_rect.x + 700, e1_rect.y + 500))
		screen.blit(s,(1100,500))
		screen.blit(g,(40,500))
		if c1_rect.colliderect(start_rect):
			screen.blit(how_to_play,(280,150))
		if c1_rect.colliderect(f_rect):
			play_again = create_button(400, 430, 100, 100, green, blue)
			if play_again:
				c1_game()
			exit_game = create_button(800, 430, 100, 100, green, blue)
			if exit_game:
				start_game()
			screen.blit(win,(300,150))
			touched_gas = False
			touched_stop = False
			touched = False	
			not_touched = False
		else:			
			if e1_rect.colliderect(f_rect):
				play_again = create_button(400, 430, 100, 100, green, blue)
				if play_again:
					c1_game()
				exit_game = create_button(800, 430, 100, 100, green, blue)
				if exit_game:
					start_game()
				screen.blit(lose,(300,150))
				touched_gas = False
				touched_stop = False
				touched = False
				not_touched = False
		pygame.display.update()
		clock.tick(60)
		
def c2_game():
	how_to_play = pygame.image.load('how_to_play.jpg')
	starting_line = pygame.image.load('starting_line.png')
	start_rect = starting_line.get_rect()
	win = pygame.image.load('winner.jpg')
	lose = pygame.image.load('game_over.jpg')
	s = pygame.image.load('stop.png')
	g = pygame.image.load('gas.png')
	f = pygame.image.load('finish_line.jpg')
	f_rect = f.get_rect()
	f_rect.x = 200
	f_rect.y = -7300
	r1 = pygame.image.load('road1bg.jpg')
	r1_rect = r1.get_rect()
	r1_rect.y =-7300
	c2 = pygame.image.load('c2.png')
	c2_rect = c2.get_rect()
	e2 = pygame.image.load('c3.png')
	e2_rect = e2.get_rect()		
	stop = pygame.Rect(1100, 500, 84, 125)
	gas = pygame.Rect(40, 500, 76, 125)
	enemy = pygame.Rect(40, 500, 100, 100)
	rect = pygame.Rect(500,500,500,500)
	touched = False
	touched_stop = False
	touched_gas = False
	not_touched = False
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP or pygame.K_w:
					touched_gas = True
				else:
					not_touched = True
				if event.key == pygame.K_SPACE:
					touched_stop = True
				else:
					not_touched = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				if stop.collidepoint(event.pos):
					touched_stop = True
				else:
					not_touched = True
				if gas.collidepoint(event.pos):
					touched_gas = True
				else:
					not_touched = True
				if enemy.collidepoint(event.pos):
					touched = True
			if event.type == pygame.MOUSEBUTTONUP:
				touched_gas = False
				touched_stop = False			
			
		if touched_stop:
			c2_rect.y += 1
			r1_rect.y -= 8
			f_rect.y -= 8
		if touched_gas: 
			c2_rect.y -= 2
			r1_rect.y += 15
			f_rect.y +=15
			start_rect.y += 50
		if touched:
			e2_rect.y -= 1.5
		if not_touched:
			c2_rect.y += 0.5
			r1_rect.y += 5
			f_rect.y += 5
			
		screen.blit(r1,(r1_rect.x, r1_rect.y))
		pygame.draw.rect(screen, blue, stop)
		pygame.draw.rect(screen, blue, gas)
		screen.blit(f, (f_rect.x, f_rect.y + 550))
		screen.blit(starting_line,(start_rect.x + 200, start_rect.y + 600))
		screen.blit(c2,(c2_rect.x + 300,c2_rect.y + 500))
		text_surface = font.render(name.text_input,  True, black)
		screen.blit(text_surface, (330, c2_rect.y + 750))
		screen.blit(e2,(e2_rect.x + 700, e2_rect.y + 500))
		screen.blit(s,(1100,500))
		screen.blit(g,(40,500))
		if c2_rect.colliderect(start_rect):
			screen.blit(how_to_play,(280,150))
		if c2_rect.colliderect(f_rect):
			play_again = create_button(400, 430, 100, 100, green, blue)
			if play_again:
				c2_game()
			exit_game = create_button(800, 430, 100, 100, green, blue)
			if exit_game:
				start_game()
			screen.blit(win,(300,150))
			touched_gas = False
			touched_stop = False
			touched = False	
			not_touched = False
		else:			
			if e2_rect.colliderect(f_rect):
				play_again = create_button(400, 430, 100, 100, green, blue)
				if play_again:
					c2_game()
				exit_game = create_button(800, 430, 100, 100, green, blue)
				if exit_game:
					start_game()
				screen.blit(lose,(300,150))
				touched_gas = False
				touched_stop = False
				touched = False
				not_touched = False
		pygame.display.update()
		clock.tick(60)

def c3_game():
	how_to_play = pygame.image.load('how_to_play.jpg')
	starting_line = pygame.image.load('starting_line.png')
	start_rect = starting_line.get_rect()
	win = pygame.image.load('winner.jpg')
	lose = pygame.image.load('game_over.jpg')
	s = pygame.image.load('stop.png')
	g = pygame.image.load('gas.png')
	f = pygame.image.load('finish_line.jpg')
	f_rect = f.get_rect()
	f_rect.x = 200
	f_rect.y = -7300
	r1 = pygame.image.load('road1bg.jpg')
	r1_rect = r1.get_rect()
	r1_rect.y =-7300
	c3 = pygame.image.load('c3.png')
	c3_rect = c3.get_rect()
	e3 = pygame.image.load('c4.png')
	e3_rect = e3.get_rect()		
	stop = pygame.Rect(1100, 500, 84, 125)
	gas = pygame.Rect(40, 500, 76, 125)
	enemy = pygame.Rect(40, 500, 100, 100)
	rect = pygame.Rect(500,500,500,500)
	touched = False
	touched_stop = False
	touched_gas = False
	not_touched = False
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP or pygame.K_w:
					touched_gas = True
				else:
					not_touched = True
				if event.key == pygame.K_SPACE:
					touched_stop = True
				else:
					not_touched = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				if stop.collidepoint(event.pos):
					touched_stop = True
				else:
					not_touched = True
				if gas.collidepoint(event.pos):
					touched_gas = True
				else:
					not_touched = True
				if enemy.collidepoint(event.pos):
					touched = True
			if event.type == pygame.MOUSEBUTTONUP:
				touched_gas = False
				touched_stop = False			
			
		if touched_stop:
			c3_rect.y += 1
			r1_rect.y -= 8
			f_rect.y -= 8
		if touched_gas: 
			c3_rect.y -= 2
			r1_rect.y += 15
			f_rect.y +=15
			start_rect.y += 50
		if touched:
			e3_rect.y -= 1.5
		if not_touched:
			c3_rect.y += 0.5
			r1_rect.y += 5
			f_rect.y += 5
			
		screen.blit(r1,(r1_rect.x, r1_rect.y))
		pygame.draw.rect(screen, blue, stop)
		pygame.draw.rect(screen, blue, gas)
		screen.blit(f, (f_rect.x, f_rect.y + 550))
		screen.blit(starting_line,(start_rect.x + 200, start_rect.y + 600))
		screen.blit(c3,(c3_rect.x + 300,c3_rect.y + 500))
		text_surface = font.render(name.text_input,  True, black)
		screen.blit(text_surface, (330, c3_rect.y + 750))
		screen.blit(e3,(e3_rect.x + 700, e3_rect.y + 500))
		screen.blit(s,(1100,500))
		screen.blit(g,(40,500))
		if c3_rect.colliderect(start_rect):
			screen.blit(how_to_play,(280,150))
		if c3_rect.colliderect(f_rect):
			play_again = create_button(400, 430, 100, 100, green, blue)
			if play_again:
				c3_game()
			exit_game = create_button(800, 430, 100, 100, green, blue)
			if exit_game:
				start_game()
			screen.blit(win,(300,150))
			touched_gas = False
			touched_stop = False
			touched = False	
			not_touched = False
		else:			
			if e3_rect.colliderect(f_rect):
				play_again = create_button(400, 430, 100, 100, green, blue)
				if play_again:
					c3_game()
				exit_game = create_button(800, 430, 100, 100, green, blue)
				if exit_game:
					start_game()
				screen.blit(lose,(300,150))
				touched_gas = False
				touched_stop = False
				touched = False
				not_touched = False
		pygame.display.update()
		clock.tick(60)

def c4_game():
	how_to_play = pygame.image.load('how_to_play.jpg')
	starting_line = pygame.image.load('starting_line.png')
	start_rect = starting_line.get_rect()
	win = pygame.image.load('winner.jpg')
	lose = pygame.image.load('game_over.jpg')
	s = pygame.image.load('stop.png')
	g = pygame.image.load('gas.png')
	f = pygame.image.load('finish_line.jpg')
	f_rect = f.get_rect()
	f_rect.x = 200
	f_rect.y = -7300
	r1 = pygame.image.load('road1bg.jpg')
	r1_rect = r1.get_rect()
	r1_rect.y =-7300
	c4 = pygame.image.load('c4.png')
	c4_rect = c4.get_rect()
	e4 = pygame.image.load('c1.png')
	e4_rect = e4.get_rect()		
	stop = pygame.Rect(1100, 500, 84, 125)
	gas = pygame.Rect(40, 500, 76, 125)
	enemy = pygame.Rect(40, 500, 100, 100)
	rect = pygame.Rect(500,500,500,500)
	touched = False
	touched_stop = False
	touched_gas = False
	not_touched = False
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP or pygame.K_w:
					touched_gas = True
				else:
					not_touched = True
				if event.key == pygame.K_SPACE:
					touched_stop = True
				else:
					not_touched = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				if stop.collidepoint(event.pos):
					touched_stop = True
				else:
					not_touched = True
				if gas.collidepoint(event.pos):
					touched_gas = True
				else:
					not_touched = True
				if enemy.collidepoint(event.pos):
					touched = True
			if event.type == pygame.MOUSEBUTTONUP:
				touched_gas = False
				touched_stop = False			
			
		if touched_stop:
			c4_rect.y += 1
			r1_rect.y -= 8
			f_rect.y -= 8
		if touched_gas: 
			c4_rect.y -= 2
			r1_rect.y += 15
			f_rect.y +=15
			start_rect.y += 50
		if touched:
			e4_rect.y -= 1.5
		if not_touched:
			c4_rect.y += 0.5
			r1_rect.y += 5
			f_rect.y += 5
			
		screen.blit(r1,(r1_rect.x, r1_rect.y))
		pygame.draw.rect(screen, blue, stop)
		pygame.draw.rect(screen, blue, gas)
		screen.blit(f, (f_rect.x, f_rect.y + 550))
		screen.blit(starting_line,(start_rect.x + 200, start_rect.y + 600))
		screen.blit(c4,(c4_rect.x + 300,c4_rect.y + 500))
		text_surface = font.render(name.text_input,  True, black)
		screen.blit(text_surface, (330, c4_rect.y + 750))
		screen.blit(e4,(e4_rect.x + 700, e4_rect.y + 500))
		screen.blit(s,(1100,500))
		screen.blit(g,(40,500))
		if c4_rect.colliderect(start_rect):
			screen.blit(how_to_play,(280,150))
		if c4_rect.colliderect(f_rect):
			play_again = create_button(400, 430, 100, 100, green, blue)
			if play_again:
				c4_game()
			exit_game = create_button(800, 430, 100, 100, green, blue)
			if exit_game:
				start_game()
			screen.blit(win,(300,150))
			touched_gas = False
			touched_stop = False
			touched = False	
			not_touched = False
		else:			
			if e4_rect.colliderect(f_rect):
				play_again = create_button(400, 430, 100, 100, green, blue)
				if play_again:
					c4_game()
				exit_game = create_button(800, 430, 100, 100, green, blue)
				if exit_game:
					start_game()
				screen.blit(lose,(300,150))
				touched_gas = False
				touched_stop = False
				touched = False
				not_touched = False
		pygame.display.update()
		clock.tick(60)	

#game loop for road_2
def c1_game_2():
	how_to_play = pygame.image.load('how_to_play.jpg')
	starting_line = pygame.image.load('starting_line.png')
	start_rect = starting_line.get_rect()
	win = pygame.image.load('winner.jpg')
	lose = pygame.image.load('game_over.jpg')
	s = pygame.image.load('stop.png')
	g = pygame.image.load('gas.png')
	f = pygame.image.load('finish_line.jpg')
	f_rect = f.get_rect()
	f_rect.x = 200
	f_rect.y = -7300
	r1 = pygame.image.load('road2bg.jpg')
	r1_rect = r1.get_rect()
	r1_rect.y =-7300
	c1 = pygame.image.load('c1.png')
	c1_rect = c1.get_rect()
	e1 = pygame.image.load('c4.png')
	e1_rect = e1.get_rect()		
	stop = pygame.Rect(1100, 500, 84, 125)
	gas = pygame.Rect(40, 500, 76, 125)
	enemy = pygame.Rect(40, 500, 100, 100)
	rect = pygame.Rect(500,500,500,500)
	touched = False
	touched_stop = False
	touched_gas = False
	not_touched = False
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP or pygame.K_w:
					touched_gas = True
				else:
					not_touched = True
				if event.key == pygame.K_SPACE:
					touched_stop = True
				else:
					not_touched = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				if stop.collidepoint(event.pos):
					touched_stop = True
				else:
					not_touched = True
				if gas.collidepoint(event.pos):
					touched_gas = True
				else:
					not_touched = True
				if enemy.collidepoint(event.pos):
					touched = True
			if event.type == pygame.MOUSEBUTTONUP:
				touched_gas = False
				touched_stop = False			
			
		if touched_stop:
			c1_rect.y += 1
			r1_rect.y -= 8
			f_rect.y -= 8
		if touched_gas: 
			c1_rect.y -= 2
			r1_rect.y += 15
			f_rect.y +=15
			start_rect.y += 50
		if touched:
			e1_rect.y -= 1.5
		if not_touched:
			c1_rect.y += 0.5
			r1_rect.y += 5
			f_rect.y += 5
			
		screen.blit(r1,(r1_rect.x, r1_rect.y))
		pygame.draw.rect(screen, blue, stop)
		pygame.draw.rect(screen, blue, gas)
		screen.blit(f, (f_rect.x, f_rect.y + 550))
		screen.blit(starting_line,(start_rect.x + 200, start_rect.y + 600))
		screen.blit(c1,(c1_rect.x + 300,c1_rect.y + 500))
		text_surface = font.render(name.text_input,  True, black)
		screen.blit(text_surface, (330, c1_rect.y + 750))
		screen.blit(e1,(e1_rect.x + 700, e1_rect.y + 500))
		screen.blit(s,(1100,500))
		screen.blit(g,(40,500))
		if c1_rect.colliderect(start_rect):
			screen.blit(how_to_play,(280,150))
		if c1_rect.colliderect(f_rect):
			play_again = create_button(400, 430, 100, 100, green, blue)
			if play_again:
				c1_game_2()
			exit_game = create_button(800, 430, 100, 100, green, blue)
			if exit_game:
				start_game()
			screen.blit(win,(300,150))
			touched_gas = False
			touched_stop = False
			touched = False	
			not_touched = False
		else:			
			if e1_rect.colliderect(f_rect):
				play_again = create_button(400, 430, 100, 100, green, blue)
				if play_again:
					c1_game_2()
				exit_game = create_button(800, 430, 100, 100, green, blue)
				if exit_game:
					start_game()
				screen.blit(lose,(300,150))
				touched_gas = False
				touched_stop = False
				touched = False	
				not_touched = False
			
		pygame.display.update()
		clock.tick(60)
		
def c2_game_2():
	how_to_play = pygame.image.load('how_to_play.jpg')
	starting_line = pygame.image.load('starting_line.png')
	start_rect = starting_line.get_rect()
	win = pygame.image.load('winner.jpg')
	lose = pygame.image.load('game_over.jpg')
	s = pygame.image.load('stop.png')
	g = pygame.image.load('gas.png')
	f = pygame.image.load('finish_line.jpg')
	f_rect = f.get_rect()
	f_rect.x = 200
	f_rect.y = -7300
	r1 = pygame.image.load('road2bg.jpg')
	r1_rect = r1.get_rect()
	r1_rect.y =-7300
	c2 = pygame.image.load('c2.png')
	c2_rect = c2.get_rect()
	e2 = pygame.image.load('c3.png')
	e2_rect = e2.get_rect()		
	stop = pygame.Rect(1100, 500, 84, 125)
	gas = pygame.Rect(40, 500, 76, 125)
	enemy = pygame.Rect(40, 500, 100, 100)
	rect = pygame.Rect(500,500,500,500)
	touched = False
	touched_stop = False
	touched_gas = False
	not_touched = False
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP or pygame.K_w:
					touched_gas = True
				else:
					not_touched = True
				if event.key == pygame.K_SPACE:
					touched_stop = True
				else:
					not_touched = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				if stop.collidepoint(event.pos):
					touched_stop = True
				else:
					not_touched = True
				if gas.collidepoint(event.pos):
					touched_gas = True
				else:
					not_touched = True
				if enemy.collidepoint(event.pos):
					touched = True
			if event.type == pygame.MOUSEBUTTONUP:
				touched_gas = False
				touched_stop = False			
			
		if touched_stop:
			c2_rect.y += 1
			r1_rect.y -= 8
			f_rect.y -= 8
		if touched_gas: 
			c2_rect.y -= 2
			r1_rect.y += 15
			f_rect.y +=15
			start_rect.y += 50
		if touched:
			e2_rect.y -= 1.5
		if not_touched:
			c2_rect.y += 0.5
			r1_rect.y += 5
			f_rect.y += 5
			
		screen.blit(r1,(r1_rect.x, r1_rect.y))
		pygame.draw.rect(screen, blue, stop)
		pygame.draw.rect(screen, blue, gas)
		screen.blit(f, (f_rect.x, f_rect.y + 550))
		screen.blit(starting_line,(start_rect.x + 200, start_rect.y + 600))
		screen.blit(c2,(c2_rect.x + 300,c2_rect.y + 500))
		text_surface = font.render(name.text_input,  True, black)
		screen.blit(text_surface, (330, c2_rect.y + 750))
		screen.blit(e2,(e2_rect.x + 700, e2_rect.y + 500))
		screen.blit(s,(1100,500))
		screen.blit(g,(40,500))
		if c2_rect.colliderect(start_rect):
			screen.blit(how_to_play,(280,150))
		if c2_rect.colliderect(f_rect):
			play_again = create_button(400, 430, 100, 100, green, blue)
			if play_again:
				c2_game_2()
			exit_game = create_button(800, 430, 100, 100, green, blue)
			if exit_game:
				start_game()
			screen.blit(win,(300,150))
			touched_gas = False
			touched_stop = False
			touched = False	
			not_touched = False
		else:			
			if e2_rect.colliderect(f_rect):
				play_again = create_button(400, 430, 100, 100, green, blue)
				if play_again:
					c2_game_2()
				exit_game = create_button(800, 430, 100, 100, green, blue)
				if exit_game:
					start_game()
				screen.blit(lose,(300,150))
				touched_gas = False
				touched_stop = False
				touched = False
				not_touched = False
		pygame.display.update()
		clock.tick(60)

def c3_game_2():
	how_to_play = pygame.image.load('how_to_play.jpg')
	starting_line = pygame.image.load('starting_line.png')
	start_rect = starting_line.get_rect()
	win = pygame.image.load('winner.jpg')
	lose = pygame.image.load('game_over.jpg')
	s = pygame.image.load('stop.png')
	g = pygame.image.load('gas.png')
	f = pygame.image.load('finish_line.jpg')
	f_rect = f.get_rect()
	f_rect.x = 200
	f_rect.y = -7300
	r1 = pygame.image.load('road2bg.jpg')
	r1_rect = r1.get_rect()
	r1_rect.y = -7300
	c3 = pygame.image.load('c3.png')
	c3_rect = c3.get_rect()
	e3 = pygame.image.load('c4.png')
	e3_rect = e3.get_rect()	
	stop = pygame.Rect(1100, 500, 84, 125)
	gas = pygame.Rect(40, 500, 76, 125)
	enemy = pygame.Rect(40, 500, 100, 100)
	rect = pygame.Rect(500,500,500,500)
	touched = False
	touched_stop = False
	touched_gas = False
	not_touched = False
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP or pygame.K_w:
					touched_gas = True
				else:
					not_touched = True
				if event.key == pygame.K_SPACE:
					touched_stop = True
				else:
					not_touched = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				if stop.collidepoint(event.pos):
					touched_stop = True
				else:
					not_touched = True
				if gas.collidepoint(event.pos):
					touched_gas = True
				else:
					not_touched = True
				if enemy.collidepoint(event.pos):
					touched = True
			if event.type == pygame.MOUSEBUTTONUP:
				touched_gas = False
				touched_stop = False			
			
		if touched_stop:
			c3_rect.y += 1
			r1_rect.y -= 8
			f_rect.y -= 8
		if touched_gas: 
			c3_rect.y -= 2
			r1_rect.y += 15
			f_rect.y +=15
			start_rect.y += 50
		if touched:
			e3_rect.y -= 1.5
		if not_touched:
			c3_rect.y += 0.5
			r1_rect.y += 5
			f_rect.y += 5
			
		screen.blit(r1,(r1_rect.x, r1_rect.y))
		pygame.draw.rect(screen, blue, stop)
		pygame.draw.rect(screen, blue, gas)
		screen.blit(f, (f_rect.x, f_rect.y + 550))
		screen.blit(starting_line,(start_rect.x + 200, start_rect.y + 600))
		screen.blit(c3,(c3_rect.x + 300,c3_rect.y + 500))
		text_surface = font.render(name.text_input,  True, black)
		screen.blit(text_surface, (330, c3_rect.y + 750))
		screen.blit(e3,(e3_rect.x + 700, e3_rect.y + 500))
		screen.blit(s,(1100,500))
		screen.blit(g,(40,500))
		if c3_rect.colliderect(start_rect):
			screen.blit(how_to_play,(280,150))
		if c3_rect.colliderect(f_rect):
			play_again = create_button(400, 430, 100, 100, green, blue)
			if play_again:
				c3_game_2()
			exit_game = create_button(800, 430, 100, 100, green, blue)
			if exit_game:
				start_game()
			screen.blit(win,(300,150))
			touched_gas = False
			touched_stop = False
			touched = False	
			not_touched = False
		else:			
			if e3_rect.colliderect(f_rect):
				play_again = create_button(400, 430, 100, 100, green, blue)
				if play_again:
					c3_game_2()
				exit_game = create_button(800, 430, 100, 100, green, blue)
				if exit_game:
					start_game()
				screen.blit(lose,(300,150))
				touched_gas = False
				touched_stop = False
				touched = False
				not_touched = False
		pygame.display.update()
		clock.tick(60)

def c4_game_2():
	how_to_play = pygame.image.load('how_to_play.jpg')
	starting_line = pygame.image.load('starting_line.png')
	start_rect = starting_line.get_rect()
	win = pygame.image.load('winner.jpg')
	lose = pygame.image.load('game_over.jpg')
	s = pygame.image.load('stop.png')
	g = pygame.image.load('gas.png')
	f = pygame.image.load('finish_line.jpg')
	f_rect = f.get_rect()
	f_rect.x = 200
	f_rect.y = -7300
	r1 = pygame.image.load('road2bg.jpg')
	r1_rect = r1.get_rect()
	r1_rect.y =-7300
	c4 = pygame.image.load('c4.png')
	c4_rect = c4.get_rect()
	e4 = pygame.image.load('c1.png')
	e4_rect = e4.get_rect()		
	stop = pygame.Rect(1100, 500, 84, 125)
	gas = pygame.Rect(40, 500, 76, 125)
	enemy = pygame.Rect(40, 500, 100, 100)
	rect = pygame.Rect(500,500,500,500)
	touched = False
	touched_stop = False
	touched_gas = False
	not_touched = False
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP or pygame.K_w:
					touched_gas = True
				else:
					not_touched = True
				if event.key == pygame.K_SPACE:
					touched_stop = True
				else:
					not_touched = True
			if event.type == pygame.MOUSEBUTTONDOWN:
				if stop.collidepoint(event.pos):
					touched_stop = True
				else:
					not_touched = True
				if gas.collidepoint(event.pos):
					touched_gas = True
				else:
					not_touched = True
				if enemy.collidepoint(event.pos):
					touched = True
			if event.type == pygame.MOUSEBUTTONUP:
				touched_gas = False
				touched_stop = False			
			
		if touched_stop:
			c4_rect.y += 1
			r1_rect.y -= 8
			f_rect.y -= 8
		if touched_gas: 
			c4_rect.y -= 2
			r1_rect.y += 15
			f_rect.y +=15
			start_rect.y += 50
		if touched:
			e4_rect.y -= 1.5
		if not_touched:
			c4_rect.y += 0.5
			r1_rect.y += 5
			f_rect.y += 5
			
		screen.blit(r1,(r1_rect.x, r1_rect.y))
		pygame.draw.rect(screen, blue, stop)
		pygame.draw.rect(screen, blue, gas)
		screen.blit(f, (f_rect.x, f_rect.y + 550))
		screen.blit(starting_line,(start_rect.x + 200, start_rect.y + 600))
		screen.blit(c4,(c4_rect.x + 300,c4_rect.y + 500))
		text_surface = font.render(name.text_input,  True, black)
		screen.blit(text_surface, (330, c4_rect.y + 750))
		screen.blit(e4,(e4_rect.x + 700, e4_rect.y + 500))
		screen.blit(s,(1100,500))
		screen.blit(g,(40,500))
		if c4_rect.colliderect(start_rect):
			screen.blit(how_to_play,(280,150))
		if c4_rect.colliderect(f_rect):
			play_again = create_button(400, 430, 100, 100, green, blue)
			if play_again:
				c4_game_2()
			exit_game = create_button(800, 430, 100, 100, green, blue)
			if exit_game:
				start_game()
			screen.blit(win,(300,150))
			touched_gas = False
			touched_stop = False
			touched = False	
			not_touched = False
		else:			
			if e4_rect.colliderect(f_rect):
				play_again = create_button(400, 430, 100, 100, green, blue)
				if play_again:
					c4_game_2()
				exit_game = create_button(800, 430, 100, 100, green, blue)
				if exit_game:
					start_game()
				screen.blit(lose,(300,150))
				touched_gas = False
				touched_stop = False
				touched = False
				not_touched = False
		pygame.display.update()
		clock.tick(60)

		
	

running = True
while running:
    screen_bg = pygame.image.load('bg.jpg')
    screen.blit(screen_bg,(0,0))
    start_game()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(60)
        
		
