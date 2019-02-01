#!/bin/python3

# Code Club Project 2-Challenge- Use Fire, Logs, Water https://codeclubprojects.org/en-GB/python/rock-paper-scissors/
# Author: Michell Berryman
# Date: 01/31/2019

#imports random number library
from random import randint

#define fire, logs, water ascii art
fire = '@@@'
logs = '= = ='
water = '~ ~ ~'

#player input
player = input('fire (f), logs (l), or water (w)?')

#convert play input to ascii art & print 
# end=' ' tells print statement to end with a space rather than a new line
if player == 'f':
  print (fire, 'vs', end=' ')
  
elif player == 'l':
  print (logs, 'vs', end=' ') 
  
elif player == 'w':
  print (water, 'vs', end=' ')

#assign computer's choice using random int 1-3 
chosen = randint(1,3)

# define 1= fire, 2= logs, 3 = water & print computer's choice using ascii art variable
if chosen == 1:
  computer = 'f'
  print(fire)
  
elif chosen ==2:
  computer = 'l'
  print(logs)
  
else:
  computer = 'w'
  print(water)


#if player and computer's choices match, declare a draw
if player == computer:
  print('DRAW!')

#define winner
elif player == 'f' and computer == 'l':
  print('Player wins! Fire burns logs!')
  
elif player == 'f' and computer == 'w':
  print('Computer wins! Water puts out fire!')
  
elif player == 'l' and computer == 'w':
  print('Player wins! Logs make a bridge over water!')
    
elif player == 'l' and computer == 'f':
  print('Computer wins! Fire burns logs!')
  
elif player == 'w' and computer == 'f':
  print('Player wins! Water puts out fire!')
    
elif player == 'w' and computer == 'l':
  print('Computer wins! Logs make a bridge over water!')
    
