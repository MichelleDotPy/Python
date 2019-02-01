#!/bin/python3

# CodeClub Project 1-Aoubt Me https://codeclubprojects.org/en-GB/python/about-me/
# Author: Michelle Berryman
# Date: 01/31/2019

#basic print statements
print ('Hello!')
print('My name is Michelle')

# multi-line print statements with ASCII art
print ('''
I live in Louisville, Ky
    __ __           __             __        
   / //_/__  ____  / /___  _______/ /____  __
  / ,< / _ \/ __ \/ __/ / / / ___/ //_/ / / /
 / /| /  __/ / / / /_/ /_/ / /__/ ,< / /_/ / 
/_/ |_\___/_/ /_/\__/\__,_/\___/_/|_|\__, /  
                                    /____/ 
''')
 
print('''
Here\'s a picture of a dog:
  __      _
o'')}____//
 `_/      )
 (_(_/-(_/
 ''')

# calculate age in year 2025
born = input('What year were you born?')
born = int(born)
ageIn2025 = (2025 - born)
print('In the year 2025 you\'ll be',ageIn2025,'years old!')
print('')

# calculate age in dog years
age = input('What is your current age?')
age = int(age)
ageInDogYears = (age * 7)
print('If you were a dog, you\'d be',ageInDogYears,'years old!')
print('')

# calculations using text
print('ha ' *4)
print('ba'+'na' *2)
print('Hello' + '!' *10)

# batman theme song using text calculations
print ('na ' *13 + 'Batman!')

# brick wall ascii pattern using text calculations
print('Here\'s a picture of a brick wall!')
print('_|'+ '___|'*10)
print('___|' *10 +'__')
print('_|'+ '___|'*10)
print('___|' *10 +'__')
print('_|'+ '___|'*10)
print('___|' *10 +'__')
