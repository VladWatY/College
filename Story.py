#vars --------------------------------------------------------------------
import time
import sys
 
string = 'Loading up .........'
for char in string:
 sys.stdout.write(char)
 sys.stdout.flush()
 time.sleep(.15)
#Name input and print --------------------------------------------------------------------
print("\nHello! What's your name?")
time.sleep(2)
 
name = input()
 
print("\nWelcome,")
print(name)
print("\n")
time.sleep(5)
#Story
print("You're in the town center and looking at two shops, one for PC Hardware and one for Food.")
time.sleep(2)
print("There exist 2 paths that you can take, it's either go to the left for the PC Hardware store, right for the Food Store")
print("right/left")
time.sleep(2)
#path1 --------------------------------------------------------------------
path = input()
if path == "right":
 print("You're considering buying PC Hardware...")
 time.sleep(2)
elif path == "left":
 print("You're considering buying food...")
 time.sleep(2)
if path == "right":
 print("Are you sure you want to spend your money on them?")
 time.sleep(2)
if path == "left":
 print("Are you sure you want to spend your money on them?")
 time.sleep(2)
elif path == "ahead":
 print("You're continuing your way and saw the shop called GAME and your mates...")
path3 = input()
#path3 --------------------------------------------------------------------
if path3 == "yes":
 print("You went and bought stuff with the money you've saved... You're walking down the road now")
 time.sleep(2)
elif path3 == "no":
 print("You decided to save the money and went along your way, nice!")
 time.sleep(3)
 print("You're continuing your way and saw the shop called GAME and your mates...")
 time.sleep(3)
print("You're really intrested in going to the GAME store but your mates are calling you.")
time.sleep(1)
print("You can either go to the shop by typing GAME, either go to your mates by typing Mates")
path2 = input()
#path2 --------------------------------------------------------------------
if path2 == "GAME":
 print("You've chosen to go and buy some stuff instead of staying with your mates and now they're mad on you")
if path2 == "Mates":
 print("You went to your mates and will come back later for the shop...")
