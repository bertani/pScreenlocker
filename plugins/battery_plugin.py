from pe import *

def update(screen):
	global img_battery, img_red, img_green, img_yellow, charging_step
	#img_green=img_red
	try:
		f=open("/sys/devices/platform/bq27000-battery.0/power_supply/bat/capacity","r")
		c=f.read()
		f.close()
		f=open("/sys/devices/platform/bq27000-battery.0/power_supply/bat/online","r")
		ch=f.read()
		f.close()
	except:
		c=0
		ch=0
	if int(ch)==1:
		charging=True
	else:
		charging=False
		
	#print "->",c,"<- (",charging,")"
	d=20
	if charging:
		#print "->",charging_step
		charging_step+=1
		x=3.1*int(int(c)+charging_step*d)
		if int(int(c)+charging_step*d)>=100:
			charging_step=0
			x=3.1*int(c)
			#x=3.1*int(int(c)+charging_step*d)
	try:
		if not charging: x=3.1*int(c)
		if int(c)>66:
			img_c=img_green
		elif 33<int(c)<=66:
			img_c=img_yellow
		elif int(c)<=33:
			img_c=img_red
		#else:
		#	img_c=img_red
	except:
		x=0
		img_c=img_red
	screen.fill((0,0,0))
	screen.blit(pygame.transform.scale2x(img_battery),(50,250))
	screen.blit(pygame.transform.scale(img_c,(x,155)),(83,260))
	pygame.display.update(pygame.rect.Rect((50,200),(400,300)))#(50,250),(400,150)))
	#sleep(0.5)

__timer=60
charging_step=0
img_battery=pygame.image.load(folder+res+'battery.bmp')
img_red=pygame.image.load(folder+res+'red.bmp')
img_green=pygame.image.load(folder+res+'green.bmp')
img_yellow=pygame.image.load(folder+res+'yellow.bmp')
