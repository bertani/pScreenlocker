'''
Plugins' engine :P
'''
from pygame.locals import *
import random, sys, pygame, string, datetime, time, os, re
from time import sleep
from sys import argv, path, stdout

res = 'res/'
folder="plugins/"
plugins=[]

SCREEN_SIZE = (480,640)
pygame.init()
font = pygame.font.SysFont("Arial",150)
font_ = pygame.font.SysFont("Arial",50)
font__ = pygame.font.SysFont("Arial",40)
panel=2####

path.append( folder )
ls = os.listdir( folder )
for i in ls:
	if re.match("^[A-z]*_plugin\.py$", i):	
		try:
			plugin_name = i[:len(i)-10]
			exec( "import " + plugin_name + "_plugin as " + plugin_name )
			plugins.append( plugin_name )
		except:
			print ": [ Failed to load the ", i, " plugin ]"

screen = pygame.display.set_mode(SCREEN_SIZE)#,FULLSCREEN)#0,32)
pygame.display.set_caption("Screenlocker")
#pygame.mouse.set_visible(0)
