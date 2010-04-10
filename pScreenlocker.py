#!/usr/bin/python
#
#       screenlocker.py
#       
#       Copyright 2009-2010 Thomas Bertani <sylar@anche.no>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.

import thread

def start():
    global state, got, panel, lines, x
    mousepos = pygame.mouse.get_pos()
    pygame.fastevent.init()
    g=0
    t_0=time.time()
    t_l=t_0
    t_c=t_0
    update_clock(screen)
    exec(plugins[panel-1]+".update(screen)")
    while 1:
	g+=1
	status=pygame.mouse.get_pressed()
	#print status
	if status[0]==1:
		pos=pygame.mouse.get_pos()
		if pos[1]>(SCREEN_SIZE[1]-160):
			state="down"
		else:
			if time.time()-t_l>=0.5:
				t_l=time.time()
				if pos[0]>(SCREEN_SIZE[0]/2):
					if panel!=len(plugins):
						panel+=1
					else:
						panel=1
				else:
					print "(old)", panel
					if panel==0:
						panel=len(plugins)
					else:
						panel-=1
					print "(new)", panel
				screen.fill((0,0,0))
				pygame.display.update(pygame.rect.Rect((0,120),(480,400)))
				exec(plugins[panel-1]+".update(screen)")
	else:
		state="up"
		got=False
	screen.fill((0,0,0))
	exec("timer="+plugins[panel-1]+".__timer")
	if time.time()-t_0>=timer:
		exec(plugins[panel-1]+".update(screen)")
		t_0=time.time()
	if time.time()-t_c>=1:
		t_c=time.time()
		update_clock(screen)
	if state=="down" or x!=0: update_locker(screen)
	tmp=pygame.fastevent.poll()
def update_locker(screen):
	global x, state, got,where
	if x<0: x=0
	if state=="up":
		if x>=330:
			x=330
			screen.fill((0,0,0))
			screen.blit(img_barra,(5,SCREEN_SIZE[1]-115))
			screen.blit(img_tasto,(x+10,SCREEN_SIZE[1]-110))
			pygame.display.update(pygame.rect.Rect((0,SCREEN_SIZE[1]-120),(SCREEN_SIZE[0],120)))
			print "ok!"
			pygame.quit()
			exit()
			return
		if x>0:
			if x>120:
				x-=15
			else:
				x-=10
			screen.fill((0,0,0))
			screen.blit(img_barra,(5,SCREEN_SIZE[1]-115))
			screen.blit(img_tasto,(x+10,SCREEN_SIZE[1]-110))
			pygame.display.update(pygame.rect.Rect((0,SCREEN_SIZE[1]-120),(SCREEN_SIZE[0],120)))
	elif state=="down":
		pos_=pygame.mouse.get_pos()
		pos[0]=pos_[0]-10
		pos[1]=pos_[1]
		if not got:
			if pos[0]>(x+120):
				#print "skipping..."
				state="up"
				got=False
				return
			else:
				#print "Agganciato!"
				got=True
				where=pos[0]-x
		if got: x=pos[0]-where
		if x<0: x=0
		if x>330: x=330
		screen.fill((0,0,0))
		screen.blit(img_barra,(5,SCREEN_SIZE[1]-115))
		screen.blit(img_tasto,(x+10,SCREEN_SIZE[1]-110))
		pygame.display.update(pygame.rect.Rect((0,SCREEN_SIZE[1]-120),(SCREEN_SIZE[0],120)))

def update_clock(screen):
	global font, panel
	dt=datetime.datetime.timetuple(datetime.datetime.today())
	hours=str(dt[3])
	minutes=str(dt[4])
	if len(minutes)==1: minutes="0"+minutes
	seconds=str(dt[5])
	if len(seconds)==1: seconds="0"+seconds
	ctime=hours+":"+minutes+"."+seconds
	fontimg1 = font.render(ctime,1,(255,255,255))
	fontimg2 = font.render(ctime,1, (50,50,50))
        screen.blit(fontimg1, (SCREEN_SIZE[0]/2-fontimg1.get_width()/2,18))#(47,18))
        screen.blit(fontimg2, (SCREEN_SIZE[0]/2-fontimg2.get_width()/2-2,18-2))#(45,16))
	pygame.display.update((45,16),(400,150))

if __name__ == '__main__':
	print ":: Loading needed plugins and vars"
	from pe import *
	print ". " + plugins.__len__().__str__() + " plugins loaded successfully!"
	print ":: Starting..."
	pos=[0,0]
        res = 'res/'
	img_barra=pygame.image.load(res+'barra.bmp')
	img_tasto=pygame.image.load(res+'tasto.bmp')
	got=False
	where=0
	x=1
	state="up"
	start()
else:
	exit(".. Cannot start this script as a module ..")
