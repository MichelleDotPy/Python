#!/bin/python3

# CodeClub Project 1-Team Chooser https://codeclubprojects.org/en-GB/python/team-chooser/
# Author: Michelle Berryman
# Date: 01/31/2019
# Associalted files: 'players.txt','teamNames.txt'

from random import choice
#create empty players & teams lists
players = []
teams = []

# open file 
#'r' means read-only
file = open('players.txt', 'r')
# read the list from the file and add to players list
players = file.read().splitlines()

#open file and add names to teams list
file = open('teamNames.txt', 'r')
teams = file.read().splitlines()

#print all player & team names
print('Available Players: ',players)
print(' ')
print('Available Team Names: ',teams)
print(' ')
print(' ')

#create empty lists for team players
teamA = []
teamB = []

#assign random playerys to each team
while len(players) > 0:
  playerA = (choice(players))
  #print(playerA)
  teamA.append(playerA)
  players.remove(playerA)
  #print('Players left', players)
  
  if players == []:
    break
  
  playerB = (choice(players))
  #print(playerB)
  teamB.append(playerB)
  players.remove(playerB)
  #print('Players left', players)

teamAName = (choice(teams))
teams.remove(teamAName)

teamBName = (choice(teams))

print('Team Names & Player Assignments:')
print(' ')
print(teamAName,": ",teamA)
print(' ')
print(teamBName,": ", teamB)
