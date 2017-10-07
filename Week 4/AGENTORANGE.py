from turtle import Turtle
import random

t = Turtle()
t.screen.bgcolor('black')
#t.color('orange')

t.fd(100)

def generateText(txt, font, color):
	t.color(randomColor)
	xpos = random.randint(-500,500)
	ypos = random.randint(-500,400)
	t.setpos(xpos, ypos)
	t.write(txt,move=True,align="center",font=(font,30,"normal"))
	
#In order for fonts to vary randomly, they must be installed in your font folder. See attached font files to download.

#
thingsToSay = ["AGENT ORANGE", "FUCK TRUMP", "WHAT HAVE WE DONE?", "FUCK DONALD TRUMP", "YOUR TIME WILL COME", "BLACK LIVES MATTER", "RESIST", "DEPLORABLE", "FUCK THE PRESIDENT", "SHAME!", "LITERALLY THE WORST", "BLOTUS", "YOURE FIRED", "IMPEACH THE PRESIDENT", "AMERICANHORRORSTORY", "TAKE A KNEE"]
colors = ["red", "orange", "green", "purple", "blue", "white", "yellow", "black", "magenta", "violet"]
fonts = ["Helvetica Bold", "Patriot", "Dancing on the Beach", "galderglynn", "Heavitas", "DELUSION", "AbandoN", "Cooper Black", "Gobold", "Friends", "Summer of Love", "Amateur Slash", "Wilmina", "Costa Rica", ]



while True:
	randomString = random.choice(thingsToSay)
	randomColor = random.choice(colors)
	randomFont = random.choice(fonts)
	generateText(randomString, randomFont, randomColor)
