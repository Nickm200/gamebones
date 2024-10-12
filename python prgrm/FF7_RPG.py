import time
import random
import pygame 
pygame.mixer.init()

validinput = ['run', 'fight']
validcont=['enter']
level = 5
exp = 0



#NOTE DAMAGE WILL EVENTUALLY BE DECIDED BY RANDOM VALUES (35 - 42)
#NOTE POlISH A LEVEL AND EXP SYSTEM
#NOTE ADD A HEALTH MECHANIC FOR CLOUD
#NOTE ITEM ADD AN ITEM TAB THAT CAN LINK TO BOTH HEALTH AND DAMAGE
#NOTE ADD LIMIT CHARGE AND BREAKER MECHANIC



#introduction to game
pygame.mixer.music.load('intro.wav')
pygame.mixer.music.play(-1)
time.sleep(2)
print("Stranger: you're awake! Cloud! it's been 30 years")
time.sleep(2)
print("Cloud: where am i? Who are you?")
time.sleep(2)
print("Stranger: You are in the sector 6 slums as for me.. that doesn't matter now, Tifa has been captured by shinra!")
time.sleep(2)
print("Cloud: Shinra!")
time.sleep(1)
print("Cloud: ....")
time.sleep(1)
print("Cloud: Where is shinra now im going to save Tifa")
time.sleep(2)
print("Stranger: Shinra is in sector 7 but you musn't go it is dangerous")
time.sleep(2)
print("Cloud i can handle it thanks er.. whoever you are")
print("")
print("type 'enter' to continue...")
cont = input()
if cont not in validcont:
  while cont not in validcont:
    print("Please enter the correct command")
    cont = input()
if cont == 'enter':
  pygame.mixer.music.fadeout(2000)
print("")
print("")
time.sleep(3)

#first fight
print("!!!")
pygame.mixer.music.load('battlencounter.wav')
pygame.mixer.music.play()
time.sleep(1)
print("Cloud has entered their first battle against Gun Carrier. To fight enter 'fight' to run enter 'run'")
pygame.mixer.music.load('fight.wav')
pygame.mixer.music.play(-1)
choice = input()
if choice not in validinput:
  while choice not in validinput:
    print("Please enter the correct command")
    choice = input()
if choice == 'fight':
  time.sleep(1)
  print("Cloud attacked and did 35 damage!")
  time.sleep(1)
  pygame.mixer.music.load('victory.wav')
  pygame.mixer.music.play(-1)
  print("Victory!")
  time.sleep(1)
  exp += 50      
  print("You gained " + str(exp) + " exp" )
  if exp >= 150:
    level += 1
    print("You leveled up to level " + str(level))
  print("type 'enter' to continue...")
  cont = input()
  if cont not in validcont:
    while cont not in validcont:
      print("Please enter the correct command")
      cont = input()
  if cont == 'enter':
    pygame.mixer.music.fadeout(2000)
  
    
elif choice == 'run':
  time.sleep(1)
  print("Cloud has fled")
  print("type 'enter' to continue...")
  cont = input()
  if cont not in validcont:
    while cont not in validcont:
      print("Please enter the correct command")
      cont = input()
  if cont == 'enter':
    pygame.mixer.music.fadeout(2000)      
    
print("")
print("")
time.sleep(2)


#Second fight
print("!!!")
pygame.mixer.music.load('battlencounter.wav')
pygame.mixer.music.play()
time.sleep(1)
print("Cloud has entered a battle with Death machine. To fight enter 'fight'. to run enter 'run'")
pygame.mixer.music.load('fight.wav')
pygame.mixer.music.play(-1)
choice = input()
if choice not in validinput:
  while choice not in validinput:
      print("Please enter the correct command")
      choice = input()

if choice == 'fight':
  time.sleep(1)
  print("Cloud attacked and did 39 damage!")
  time.sleep(1)
  pygame.mixer.music.load('victory.wav')
  pygame.mixer.music.play(-1)
  print("Victory!")
  time.sleep(1)
  exp += 50      
  print("You gained " + str(exp) + " exp" )
  if exp >= 150:
    level += 1
    print("You leveled up to level " + str(level))
  print("type 'enter' to continue...")
  cont = input()
  if cont not in validcont:
    while cont not in validcont:
      print("Please enter the correct command")
      cont = input()
  if cont == 'enter':
    pygame.mixer.music.fadeout(2000)
      
elif choice == 'run':
  time.sleep(1)
  print("Cloud has fled")
  print("type 'enter' to continue...")
  cont = input()
  if cont not in validcont:
    while cont not in validcont:
      print("Please enter the correct command")
      cont = input()
  if cont == 'enter':
    pygame.mixer.music.fadeout(2000)

print("")
print("")
time.sleep(2)


# Third fight
print("!!!")
pygame.mixer.music.load('battlencounter.wav')
pygame.mixer.music.play()
time.sleep(1)
print("Cloud has entered a battle with Eagle bot. To fight enter 'fight'. to run enter 'run'")
pygame.mixer.music.load('fight.wav')
pygame.mixer.music.play(-1)
choice = input()
if choice not in validinput:
  while choice not in validinput:
      print("Please enter the correct command")
      choice = input()

if choice == 'fight':
  time.sleep(1)
  print("Cloud attacked and did 42 damage!")
  time.sleep(1)
  pygame.mixer.music.load('victory.wav')
  pygame.mixer.music.play(-1)
  print("Victory!")
  time.sleep(1)
  exp += 50      
  print("You gained " + str(exp) + " exp" )
  if exp >= 150:
    level += 1
    print("You leveled up to level " + str(level))
  print("type 'enter' to continue...")
  cont = input()
  if cont not in validcont:
    while cont not in validcont:
      print("Please enter the correct command")
      cont = input()
  if cont == 'enter':
    pygame.mixer.music.fadeout(2000)
  
      
elif choice == 'run':
  time.sleep(1)
  print("Cloud has fled")
  print("type 'enter' to continue...")
  cont = input()
  if cont not in validcont:
    while cont not in validcont:
      print("Please enter the correct command")
      cont = input()
  if cont == 'enter':
    pygame.mixer.music.fadeout(2000)

    
print("")
print("")
print("")
time.sleep(3)


#mini boss time
print("Mysterious voice: So you made it through my little bots.")
time.sleep(1)
print("Mysterious voice: You might have some promise!")
time.sleep(2)
print("Cloud: Who are you if you want to fight so be it!")
time.sleep(2)
print("")

validlimitchoice = ['cross slash', 'omnislash', 'braver']

pygame.mixer.music.load('battlencounter.wav')
pygame.mixer.music.play()
time.sleep(1)
pygame.mixer.music.load('boss.wav')
pygame.mixer.music.play(-1)
time.sleep(1)
print("Cloud has entered battle with THE FABRICATOR")
time.sleep(2)
print("Cloud's Limit Breaker is active which attack do you use? 'cross slash' , 'omnislash' or 'braver'?")
limitchoice = input()
if limitchoice not in validlimitchoice:
  while limitchoice not in validlimitchoice:
      print("Please enter the correct command")
      limitchoice = input().lower()
          
if limitchoice == 'cross slash':
  time.sleep(1)
  print("Cloud used Cross Slash! and did 107 damage!")
  time.sleep(1)
  pygame.mixer.music.load('victory.wav')
  pygame.mixer.music.play(-1)
  print("Victory!")
  exp += 100      
  print("You gained " + str(exp) + " exp" )
  if exp >= 300:
    level += 1
    print("You leveled up to level " + str(level))
  print("type 'enter' to continue...")
  cont = input()
  if cont not in validcont:
    while cont not in validcont:
      print("Please enter the correct command")
      cont = input()
  if cont == 'enter':
    pygame.mixer.music.fadeout(2000)


          
elif limitchoice == 'omnislash':
  time.sleep(1)
  print("Cloud used Omnislash! and did 162 damage!")
  time.sleep(1)
  pygame.mixer.music.load('victory.wav')
  pygame.mixer.music.play(-1)
  print("Victory!")
  exp += 100      
  print("You gained " + str(exp) + " exp" )
  if exp >= 300:
    level += 1
    print("You leveled up to level " + str(level))
  print("type 'enter' to continue...")
  cont = input()
  if cont not in validcont:
    while cont not in validcont:
      print("Please enter the correct command")
      cont = input()
  if cont == 'enter':
    pygame.mixer.music.fadeout(2000)


          
elif limitchoice == 'braver':
  time.sleep(1)
  print("Cloud used Braver! and did 92 damage!")
  time.sleep(1)
  pygame.mixer.music.load('victory.wav')
  pygame.mixer.music.play(-1)
  print("Victory!")
  exp += 100      
  print("You gained " + str(exp) + " exp" )
  if exp >= 300:
    level += 1
    print("You leveled up to level " + str(level))       
  print("type 'enter' to continue...")
  cont = input()
  if cont not in validcont:
    while cont not in validcont:
      print("Please enter the correct command")
      cont = input()
  if cont == 'enter':
    pygame.mixer.music.fadeout(2000)

print("")
print("")
print("")
time.sleep(3)     

#Temporary ending
print("Cloud found tifa in the ruble of THE FABRICATOR and saved her")
