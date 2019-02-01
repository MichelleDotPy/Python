#!/bin/python3

# Code Club Project 2-Rock, Paper, Scissors https://codeclubprojects.org/en-GB/python/rock-paper-scissors/
# Author: Michell Berryman
# Date: 01/31/2019

#imports random number library
from random import randint

#define rock, paper, scissors ascii art
rock = 'O'
paper = '___'
scissors = '>8'

#player input
player = input('rock (r), paper (p), or scissors(s)?')

#convert play input to ascii art
# end=' ' tells print statement to end with a space rather than a new line
if player == 'r':
  print (rock, 'vs', end=' ')
  
elif player == 'p':
  print (paper, 'vs', end=' ') 
  
elif player == 's':
  print (scissors, 'vs', end=' ')

#assign computer's choice using random int 1-3 
chosen = randint(1,3)

# define 1= rock, 2= paper, 3 = scissors & print computer's choice using ascii art variable
if chosen == 1:
  computer = 'r'
  print(rock)
  
elif chosen ==2:
  computer = 'p'
  print(paper)
  
else:
  computer = 's'
  print(scissors)


#if player and computer's choices match, declare a draw
if player == computer:
  print('DRAW!')

#define winner
elif player == 'r' and computer == 's':
  print('Player wins!')
  
elif player == 'r' and computer == 'p':
  print('Computer wins!')
  
elif player == 'p' and computer == 'r':
  print('Player wins!')
    
elif player == 'p' and computer == 's':
  print('Computer wins!')
  
elif player == 's' and computer == 'r':
  print('Player wins!')
    
elif player == 's' and computer == 'r':
  print('Computer wins!')
    
