'''
-----------------------------------------------------------------------------
Program Name: (never put your personal name or information on the Internet)
Program Description:

-----------------------------------------------------------------------------
References:

(put a link to your reference here but also add a comment in the code below where you used the reference)

-----------------------------------------------------------------------------

Additional Libraries/Extensions:

(put a list of required extensions so that the user knows that they need to download extra features)

-----------------------------------------------------------------------------

Known bugs:

(put a list of known bugs here, if you have any)

----------------------------------------------------------------------------


Program Reflection:
I think this project deserves a level XXXXXX because ...

 Level 3 Requirements Met:
• 
•  
•  
•  
•  
• 

Features Added Beyond Level 3 Requirements:
• 
•  
•  
•  
•  
• 
-----------------------------------------------------------------------------
'''
import pygame, random

BUG_FILES=["do this later]
FONT_FILE="minecraft"
SPLAT_FILE="buzz"
W,H=1000,667; TARGET=15

pygame.init
try: pygame.mixer.init()
except: pass
screen=pygame.display.set_mode((1000,667))
clock=pygame.time.Clock()

# Safe Loaders
def img(f):
    try: return pygame.image.load(f).convert_alpha()
    except: return None
def snd(f):
    try: return pygame.mixer.Sound(f)
    except: return None

def fnt(f,s):
    try: return pygame.font.Font(f,s)
    except: return pygame.font.SysFont(None,s)

# load the images
bugs_i=[]
for x in BUG_FILES:
    i=img(x)
    if i: bugs_i.append(i)
    
font=fnt(FONT_FILE,28)
splat=snd(SPLAT_FILE)

START,PLAY,OVER="START","PLAY","OVER" # GAME STATES used to control screens
state=START; score=0

#The class
class Bug:
    def_init_(self):self.respawn()
    
    def respawn(self):
        s=random.randint(75,100)
    self.r=pygame.Rect(
        random.randint(0,W-s) # X spawn range
        random.randint(-250,-50), #change to (0,H-s) to spawn anywhere
        s,s)
    self.v=random.randint(2,6)
    self.p=pygame.transform.scale(
        random.choice(bugs_i),(s,s)) if bugs_i else None
    


