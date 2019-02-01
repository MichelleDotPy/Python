#!/bin/python3

# Title: CodeClub Project 4-Colorful Creations 
# Author: Michelle Berryman
# Date: 02/01/2019
# Reference: https://codeclubprojects.org/en-GB/python/colourful-creations/

from turtle import *

#create colors dictionary using 'key : value' pairs
colors = {
  'seafoamGreen' : '#88E6B7',
  'deepPurple' : '#7F2CD2',
  'totallyTurquoise' : '#1CF1F1',
  'limeGreen' : '#20F820',
  'bubblegumPink' : '#F36BAF',
  'mauve' : '#890A49',
  'cobaltBlue' :'#0E7AE6'
  
}

#print(colors['seafoamGreen'])
#print(colors['deepPurple'])

#screen setup and background color
screen = Screen()
screen.setup(400,400)
screen.bgcolor(colors['seafoamGreen'])

#font color and styles
penup()
color(colors['deepPurple'])
style1 = ('Courier', 60, 'bold')
style2 = ('Arial', 70, 'bold')
write('HELLO', font=style1, align='center')
right(90)
forward(100)
color(colors['bubblegumPink'])
write('WORLD', font=style2, align='center')
hideturtle()
