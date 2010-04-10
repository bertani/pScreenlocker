from pe import *
from random import randint
def update(screen):
	global points, offset, drawing_area, resolution, max_speed, min_speed, color, s, s_limit, n, d_x, d_y
	screen.fill((0,0,0))
	c=0
	ch=False
	for i in directions:
		new_x=points[c][0]+i[0]
		new_y=points[c][1]+i[1]
		new_x_=new_x
		new_y_=new_y
		if new_x<=0:
			new_x_=0
			directions[c][0]=randint(min_speed,max_speed)
			ch=True
		if new_y<=0:
			new_y_=0
			directions[c][1]=randint(min_speed,max_speed)
			ch=True
		if new_x>=resolution[0]:
			new_x_=resolution[0]
			directions[c][0]=-randint(min_speed,max_speed)
			ch=True
		if new_y>=resolution[1]:
			new_y_=resolution[1]
			directions[c][1]=-randint(min_speed,max_speed)
			ch=True
		if ch:
			s+=1
			if s>=s_limit:
				color=(randint(50,255),randint(50,255),randint(50,255))
				s=0
			new_x=new_x_
			new_y=new_y_
		points[c]=(new_x,new_y)
		c+=1
	for i in range(0,n):
		d_x_=(i+1)*d_x
		d_y_=(i+1)*d_y
		points_abs=[]
		for l in points:
			points_abs.append((l[0]+offset[0]+d_x_,l[1]+offset[1]+d_y_))
		pygame.draw.polygon(screen,color,points_abs,1)
	pygame.display.update(drawing_area)
s=0
s_limit=8
max_speed=8
min_speed=5
color=[255,255,255]
points=[]#
directions=[]#
for i in range(0,3):
	points.append([5,5])
	directions.append([-1,-1])
#points=[(100,50),(50,100),(200,10),(10,10)]
#directions=[[+1,-1],[+3,-2],[+1,+1],[-1,-1]]
n=4
d_x=4
d_y=4
offset=[0,150]
resolution=[480-n*d_x-1,370-n*d_y-1]
drawing_area=pygame.rect.Rect(offset,(resolution[0]+n*d_x+1,resolution[1]+n*d_y+1))
__timer=0
